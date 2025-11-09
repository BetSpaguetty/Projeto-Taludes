import os
from config import *
from configMatrix import *
from Filtros.Taludes.taludes import *
from Filtros.Taludes.presets import *
from _models.mapa import Mapa
from _views.ambienteView import AmbienteView
from _views.toolbar import *
from _views.matrixOptionsView import  *
from _views.configView import ConfigurationMatrixViewer
from _views.FOS.toolbarFOS import ToolBarFOS
from Filtros.Taludes.filterTaludes import *
from Filtros.Rugosidade.filterRugosidade import *
from Filtros.subFilters.subFilters import *


class AmbienteController :

    def __init__(self, filepath):
        self.view  = AmbienteView()
        self.mapa : Mapa = Mapa(filepath)
        self.filepath : str = filepath
        self.toolbarFOS = ToolBarFOS()
        self._properties()
        self._association()
        self._initialization()

 
    def _properties(self) :
        self.filterType : GraphFilters = GraphFilters.ELEVATION
        self.mapParametersViews : dict[Parameters,     SubEditor] = {}
        self.mapGraphFilters    : dict[GraphFilters, QPushButton] = {}
        self.mapGraphModes      : dict[GraphModes,   QPushButton] = {}
        self.actualToolbar = None
        

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
        self._associateGraphFilters()
        self._associateGraphConfigs()
        self._associateTaludes()
        self._associateRugosidade()


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

    # BUTTONS =================================== >>>
    def _associateGraphFilters(self) :
        self.buttonFilterElevation = self.view.matrixViewer.addFilterButton(GraphFilters.ELEVATION.value, checkable=True)
        self.buttonFilterElevation.clicked.connect(lambda : self.functionButtonElevation())

        self.buttonFilterFos = self.view.matrixViewer.addFilterButton(GraphFilters.FOS.value, checkable=True)
        self.buttonFilterFos.clicked.connect(lambda : self.functionButtonFOS())
        
        self.buttonFilterRugosidade = self.view.matrixViewer.addFilterButton(GraphFilters.RUGOSITY.value, checkable=True)
        self.buttonFilterRugosidade.clicked.connect(lambda : self.functionButtonRugosidade())


    # BUTTONS FUNCTIONS ========================= >>>

    def functionButtonElevation(self) : 
        self.filterType = GraphFilters.ELEVATION 
        self.removeToolbar()
        self.renderMatrix(self.mapa.getElevationMatrix())


    def functionButtonFOS(self) : 
        self.filterType = GraphFilters.FOS 
        self.insertToolbar(self.toolbarFOS)
        self.filterTaludes.sendMatrix()
    

    def functionButtonRugosidade(self) : 
        self.filterType = GraphFilters.RUGOSITY 
        self.removeToolbar()
        self.filterRugosidade.sendMatrix()

    # FUNCTIONS ================================= >>>


    def _associateTaludes(self) : 
        matrixElevation = self.mapa.getElevationMatrix()
        self.filterTaludes = FiltroTaludes(matrixElevation)
        self.filterTaludes.setScale(25)
        self.filterTaludes.connectReceptor(self.renderMatrix)
        for name, views in self.filterTaludes.views.items() : 
            box = self.toolbarFOS.addBox(name)
            for view in views : 
                box.addSubWidget(view)


    def _associateRugosidade(self) : 
        matrixElevation = self.mapa.getElevationMatrix()
        self.filterRugosidade = FiltroRugosidade(matrixElevation)
        self.filterRugosidade.setScale(25)
        self.filterRugosidade.connectReceptor(self.renderMatrix)













