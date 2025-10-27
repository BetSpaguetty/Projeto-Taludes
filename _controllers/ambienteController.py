from Taludes.taludes import *
from _models.mapa import Mapa
from _views.ambienteView import AmbienteView
from _views.toolsbar import *
import os
from config import *
from Taludes.presets import *
from _views.soil import  *
from _views.rain import  *
from _views.mapOptionsView import  *
from Taludes.rain import *
from _views.configView import ConfigurationMatrixViewer

class AmbienteController :

    def __init__(self, filepath):
        self.view  = AmbienteView()
        self.mapa : Mapa = Mapa(filepath)
        self.filepath : str = filepath
        self._properties()
        self._association()
        self._initialization()

 
    def _properties(self) :
        self.filterType : GraphFilters = None
        self.solo : Materiais = None
        self.mapParametersViews : dict[Parameters,   SubEditor]   = {}
        self.mapGraphFilters    : dict[GraphFilters, QPushButton] = {}
        self.mapGraphModes      : dict[GraphModes,   QPushButton] = {}
        

    def _initialization(self) :
        self.defineSoil()
        self.view.header.labelTitle.setText(os.path.basename(self.filepath))
        self.view.header.labelDimensions.setText(f'{self.mapa.getElevationMatrix().shape}')
        self.buttonMode3D.click()
        self.buttonFilterElevation.click()
        self.dropboxColorMaps.setCurrentIndex(1)
        self.dropBoxShaders.setCurrentIndex(1)

    # --------------------------------------------------------------------------------------------- >>>
    
    # GRAPH MODES ------------------------------- >>>

    def setGraphMode2D(self) :
        self.view.mapaView.setViewer2D()


    def setGraphMode3D(self) :
        self.view.mapaView.setViewer3D()


    # GRAPH FILTERS ----------------------------- >>>

    def renderFos(self) :
        self.filterType = GraphFilters.FOS 
        matrixFos = self.calculateFos()
        matrixElevation = self.mapa.getElevationMatrix()
        vX, vY = self.mapa.getXYScaleVector()
        self.view.mapaView.renderMatrix(matrixFos, matrixElevation, vX, vY)


    def renderElevation(self) :
        self.filterType = GraphFilters.ELEVATION
        matrixElevation = self.mapa.getElevationMatrix()
        vX, vY = self.mapa.getXYScaleVector()
        self.view.mapaView.renderMatrix(matrixElevation, matrixElevation, vX, vY)



    def parameterChanged(self) :
        if self.filterType == GraphFilters.FOS :
            self.renderFos()



    def calculateHW(self) :
        p = self.rainView.getPreciptacao()
        t = self.rainView.getTempo()
        thetai = self.mapParametersViews[Parameters.THETAI].getValue()
        hw = calculo_hw(p, t, thetai)
        self.rainView.lineEditHW.setText(f'{hw:.5f}')
        return hw


    def getParameters(self) :
        h      = self.mapParametersViews[Parameters.H].getValue()
        hw     = self.calculateHW()
        c      = self.mapParametersViews[Parameters.C].getValue()
        phi    = self.mapParametersViews[Parameters.PHI].getValue()
        thetai = self.mapParametersViews[Parameters.THETAI].getValue()
        return h, hw, c, phi, thetai    
    

    def calculateFos(self) : 
        h, hw, c, phi, thetai = self.getParameters()
        Z = self.mapa.getElevationMatrix()
        lenI = Z.shape[0]
        lenJ = Z.shape[1]
        fos  = calculateFos(Z, lenI, lenJ, h, hw, c, phi, thetai, self.mapa.scale, self.solo)
        return fos
    


    # FOS --------------------------------------------------------------------------------------------- >>>

    def defineSoil(self) :
        clay = self.soilView.getClay()
        sand = self.soilView.getSand()
        silt = self.soilView.getSilt()
        for KEY, SOIL in SOIL_FUNCTIONS.items() :
            if SOIL(clay, sand, silt) : 
                if self.solo == KEY : break
                self.solo = KEY
                self.soilChanged()
                break
        


    def soilChanged(self) :
        self.mapParametersViews[Parameters.THETAI].setMinMax(SOIL_THETAI[self.solo].min, SOIL_THETAI[self.solo].max)
        self.soilView.setSoilLabel(self.solo.value)



    # OBJECTS FUNCTIONS --------------------------------------------------------------------------- >>>


    def functionButtonConfiguration(self) :
        caixinha = MinhaCaixinha() 
        caixinha.exec_() 


    def functionSliderTempo(self) :
        self.calculateHW()
        self.parameterChanged()

   

    def functionChangeColorMap(self, id) :
        if id == -1 : return
        colorMap = self.dropboxColorMaps.itemText(id)
        if colorMap in self.mapColorMaps : self.view.mapaView.setColorMap('aaa', self.mapColorMaps[colorMap][0], self.mapColorMaps[colorMap][1])
        else : self.view.mapaView.setColorMap(colorMap)


    def functionSliderTransparency(self, opacity) :
        self.view.mapaView.setOpacity(opacity/100)

    def functionDropBoxSahder(self, id) : 
        shader = self.dropBoxShaders.itemText(id)
        self.view.mapaView.setMatrixShader(shader)

    def functionButtonConfig(self) : 
        self.configWindow = ConfigurationMatrixViewer()
        self.configWindow.btDrawFaces.setChecked(True)
        self.configWindow.btSmooth.clicked.connect(lambda : self.view.mapaView.setMatrixSmooth(self.configWindow.btSmooth.isChecked()))
        self.configWindow.btDrawFaces.clicked.connect(lambda : self.view.mapaView.setMatrixDrawFaces(self.configWindow.btDrawFaces.isChecked()))
        self.configWindow.btDrawEdges.clicked.connect(lambda : self.view.mapaView.setMatrixDrawEdges(self.configWindow.btDrawEdges.isChecked()))


        self.configWindow.show()


    # ASSOCIATIONS -------------------------------------------------------------------------------- >>>


    def _association(self) :
        self._associateParameters()
        self._associateGraphModes()
        self._associateGraphFilters()
        self._associateRainComponent()
        self._associateSoilComponent()
        self._associateGraphConfigs()


    # MAP --------------------------------------- >>>

    def _associateGraphConfigs(self) :

        self.buttonConfig = self.view.header.addButton('CONFIG')
        self.buttonConfig.clicked.connect(lambda : self.functionButtonConfig())

        # COLOR MAP ----------------------------- >>>
        self.mapColorMaps = {}
        self.dropboxColorMaps = self.view.mapaView.addComboBox()
        for colorMap in COLORMAPS :
            if   isinstance(colorMap,   str) :
                self.dropboxColorMaps.addItem(colorMap)
            elif isinstance(colorMap, tuple) : 
                self.mapColorMaps[colorMap[0]] = (colorMap[1], colorMap[2])
                self.dropboxColorMaps.addItem(colorMap[0])
        self.dropboxColorMaps.currentIndexChanged.connect(self.functionChangeColorMap)


        self.sliderOpacity = self.view.mapaView.criar_slider_rotulado('Opacidade', 0, 100, 100)
        self.sliderOpacity.valueChanged.connect(self.functionSliderTransparency)

        self.dropBoxShaders = self.view.mapaView.addComboBox()
        for shader in SHADERS : 
            self.dropBoxShaders.addItem(shader)
        self.dropBoxShaders.currentIndexChanged.connect(self.functionDropBoxSahder)


        

 
    # Botões filtros graficos
    def _associateGraphFilters(self) :
        self.buttonFilterElevation = self.view.mapaView.addFilterButton(GraphFilters.ELEVATION.value, checkable=True)
        self.mapGraphFilters[GraphFilters.ELEVATION] = self.buttonFilterElevation
        self.buttonFilterElevation.clicked.connect(lambda : self.renderElevation())
        self.buttonFilterFos = self.view.mapaView.addFilterButton(GraphFilters.FOS.value, checkable=True)
        self.mapGraphFilters[GraphFilters.FOS] = self.buttonFilterFos
        self.buttonFilterFos.clicked.connect(lambda : self.renderFos())
        
    
    # Botões modos graficos
    def _associateGraphModes(self) :
        self.buttonMode2D = self.view.mapaView.button2D
        self.mapGraphModes[GraphModes.D2] = self.buttonMode2D
        self.buttonMode2D.clicked.connect(lambda : self.setGraphMode2D())
        self.buttonMode3D = self.view.mapaView.button3D
        self.mapGraphModes[GraphModes.D3] = self.buttonMode3D
        self.buttonMode3D.clicked.connect(lambda : self.setGraphMode3D())



    # TOOLSBAR ------------------------------------------------------------------------------------ >>>

    def _associateParameters(self) :
        self.boxParameters = self.view.toolsbar.addBox('Parameters')
        for K, P in PARAMETERS.items() :
            widget = SubEditor(K.value, P.min, P.max)
            widget.slider.valueChanged.connect(self.parameterChanged)
            self.boxParameters.addSubWidget(widget)
            self.mapParametersViews[K] = widget


    def _associateRainComponent(self) :
        boxRainView = self.view.toolsbar.addBox('Rain')
        self.rainView = RainView()
        boxRainView.addSubWidget(self.rainView)
        self.rainView.sliderTempo.valueChanged.connect(lambda : self.functionSliderTempo())
        self.rainView.spinBoxPreciptacao.valueChanged.connect(lambda : self.functionSliderTempo())


    def _associateSoilComponent(self) :
        boxSoilView = self.view.toolsbar.addBox('Soil')
        self.soilView = SoilView()
        boxSoilView.addSubWidget(self.soilView)
        self.soilView.setClay(INITIAL_CLAY)
        self.soilView.setSand(INITIAL_SAND)
        self.soilView.setSilt(INITIAL_SILT)
        self.soilView.editClay.valueChanged.connect(lambda : self.defineSoil())
        self.soilView.editSand.valueChanged.connect(lambda : self.defineSoil())















