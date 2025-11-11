import os
from config import *
from configMatrix import *
from Filtros.FOS.taludes import *
from Filtros.FOS.presets import *
from Filtros.FOS.types import *
from _models.mapa import Mapa
from _views.ambienteView import AmbienteView
from _views.toolbar import *
from _views.matrixOptionsView import  *
from Filtros.FOS.filterFOS import *
from Filtros.Inclination.filterInclination import *
from Filtros.FlowAccumulation.filterFlowAccumulation import *


class AmbienteController :

    def __init__(self, filepath):
        self.view  = AmbienteView()
        self.mapa : Mapa = Mapa(filepath)
        self.filepath : str = filepath
        self._properties()
        self._association()
        self._initialization()

 
    def _properties(self) :
        self.filterType : GraphFilters = GraphFilters.ELEVATION
        self.mapParametersViews : dict[Parameters,     SubEditor] = {}
        self.mapGraphFilters    : dict[GraphFilters, QPushButton] = {}
        self.mapGraphModes      : dict[GraphModes,   QPushButton] = {}
        self.actualToolbar = None
        self.filters = {}
        self.filtersBars = {}
        

    def _initialization(self) :
        self.view.header.labelTitle.setText(os.path.basename(self.filepath))
        self.view.header.labelDimensions.setText(f'{self.mapa.getElevationMatrix().shape}')
        self.buttonMode3D.click()
        self.buttonFilterElevation.click()
        self.dropboxColorMaps.setCurrentIndex(2)
        self.dropBoxShaders.setCurrentIndex(1)

    # --------------------------------------------------------------------------------------------- >>>
    
    # GRAPH MODES ------------------------------- >>>

    def setGraphMode2D(self) :
        self.view.matrixViewer.setViewer2D()

    def setGraphMode3D(self) :
        self.view.matrixViewer.setViewer3D()


    
    def removeToolbar(self) : 
        if self.actualToolbar is not None : 
            self.view.corpoLayout.takeAt(0)
            self.actualToolbar.setParent(None)
        self.actualToolbar = None

    def insertToolbar(self, toolbar) : 
        if self.actualToolbar is not None : 
            self.view.corpoLayout.takeAt(0)
            self.actualToolbar.setParent(None)
        self.view.corpoLayout.insertWidget(0, toolbar)
        self.actualToolbar = toolbar

    # GRAPH FILTERS ----------------------------- >>>

    def renderMatrix(self, matrix) : 
        matrixElevation = self.mapa.getElevationMatrix()
        vX, vY = self.mapa.getXYScaleVector()
        self.view.matrixViewer.renderMatrix(matrix, matrixElevation, vX, vY)



    # OBJECTS FUNCTIONS --------------------------------------------------------------------------- >>>


    def functionButtonConfiguration(self) :
        caixinha = MinhaCaixinha() 
        caixinha.exec_() 


    def functionChangeColorMap(self, id) :
        if id == -1 : return
        colorMap = self.dropboxColorMaps.itemText(id)
        if colorMap in self.mapColorMaps : self.view.matrixViewer.setColorMap('custom', self.mapColorMaps[colorMap][0], self.mapColorMaps[colorMap][1])
        else : self.view.matrixViewer.setColorMap(colorMap)


    def functionSliderTransparency(self, opacity) :
        self.view.matrixViewer.setOpacity(opacity/100)


    def functionDropBoxSahder(self, id) : 
        shader = self.dropBoxShaders.itemText(id)
        self.view.matrixViewer.setMatrixShader(shader)


    def functionButtonConfig(self) : 
        return







    # ASSOCIATIONS -------------------------------------------------------------------------------- >>>

    def _association(self) :
        self._associateGraphModes()
        self._associateGraphConfigs()
        self._associateFilters()


    # MAP --------------------------------------- >>>

    def _associateGraphConfigs(self) :
        # CONFIG -------------------------------- >>>
        self.buttonConfig = self.view.header.addButton('CONFIG')
        self.buttonConfig.clicked.connect(lambda : self.functionButtonConfig())

        # COLOR MAP ----------------------------- >>>
        self.mapColorMaps = {}
        self.dropboxColorMaps = self.view.matrixViewer.addComboBox()
        for colorMap in COLORMAPS :
            if   isinstance(colorMap,   str) :
                self.dropboxColorMaps.addItem(colorMap)
            elif isinstance(colorMap, tuple) : 
                self.mapColorMaps[colorMap[0]] = (colorMap[1], colorMap[2])
                self.dropboxColorMaps.addItem(colorMap[0])
        self.dropboxColorMaps.currentIndexChanged.connect(self.functionChangeColorMap)

        # OPACIDADE ----------------------------- >>>
        self.sliderOpacity = self.view.matrixViewer.criar_slider_rotulado('Opacidade', 0, 100, 100)
        self.sliderOpacity.valueChanged.connect(self.functionSliderTransparency)

        # SHADERS ------------------------------- >>>
        self.dropBoxShaders = self.view.matrixViewer.addComboBox()
        for shader in SHADERS : 
            self.dropBoxShaders.addItem(shader)
        self.dropBoxShaders.currentIndexChanged.connect(self.functionDropBoxSahder)


    def _associateGraphModes(self) :
        self.buttonMode2D = self.view.matrixViewer.button2D
        self.mapGraphModes[GraphModes._2D] = self.buttonMode2D
        self.buttonMode2D.clicked.connect(lambda : self.setGraphMode2D())

        self.buttonMode3D = self.view.matrixViewer.button3D
        self.mapGraphModes[GraphModes._3D] = self.buttonMode3D
        self.buttonMode3D.clicked.connect(lambda : self.setGraphMode3D())


    # FILTERS ------------------------------------------------------------------------------------- >>>


    def _associateFilters(self) : 
        # ELEVATION 
        self.buttonFilterElevation = self.view.matrixViewer.addFilterButton(GraphFilters.ELEVATION.value, checkable=True)
        self.buttonFilterElevation.clicked.connect(lambda : self.functionButtonElevation())

        self.addFilter('FOS', FilterFOS())
        self.addFilter('Flow', FilterFlow())
        self.addFilter('Inclination', FilterInclination())


    def functionButtonElevation(self) : 
        self.removeToolbar()
        self.renderMatrix(self.mapa.getElevationMatrix())




    def addFilter(self, filterName:str, filter:Filter) : 
        matrixElevation = self.mapa.getElevationMatrix()
        filter.setElevationMatrix(matrixElevation)
        filter.setScale(self.mapa.getScale())
        filter.connectReceptor(self.renderMatrix)

        toolbar = self.createFilterBar(filterName, filter)

        button = self.view.matrixViewer.addFilterButton(filterName, checkable=True)
        button.clicked.connect(lambda : self.functionFilter(filter, toolbar))

        self.filters[filterName] = filter
        self.filtersBars[filterName] = toolbar


    def functionFilter(self, filter:Filter, filterBar) :
        matrix = filter.calculateMatrix()
        self.insertToolbar(filterBar)
        self.renderMatrix(matrix)


    def createFilterBar(self, filterName, filter:Filter) -> ToolBar:
        toolbar = ToolBar(filterName)
        for name, views in filter.views.items() : 
            box = toolbar.addBox(name)
            for view in views : 
                box.addSubWidget(view)
        return toolbar










