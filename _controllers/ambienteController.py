from Taludes.taludes import *
from _models.mapa import Mapa
from _views.ambienteView import AmbienteView
from _views.toolsbar import *
import os
from app_config import *
from Taludes.presets import *
from app_types import *
from _views.soil import  *
from _views.rain import  *
from _views.mapOptionsView import  *
from Taludes.rain import *

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
        self.renderElevation()

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
        self.view.mapaView.renderMap(matrixFos, matrixElevation, vX, vY)


    def renderElevation(self) :
        self.filterType = GraphFilters.ELEVATION
        matrixElevation = self.mapa.getElevationMatrix()
        vX, vY = self.mapa.getXYScaleVector()
        self.view.mapaView.renderMap(matrixElevation, matrixElevation, vX, vY)



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


    def configFilterButton(self, dictButton:DictButton) :
        button = self.view.mapaView.addButtonMode(dictButton.TITLE, checkable=True) 
        button.clicked.connect(lambda : dictButton.FUNCTION())
        dictButton.BUTTON = button





    def functionButtonConfiguration(self) :
        caixinha = MinhaCaixinha() 
        caixinha.exec_() 


    def functionSliderTempo(self) :
        self.calculateHW()
        self.parameterChanged()



    # ASSOCIATIONS -------------------------------------------------------------------------------- >>>


    def _association(self) :
        self.associateHeader()
        self.associateParameters()
        self.associateGraphModes()
        self.associateGraphFilters()
        self._associateRainComponent()
        self._associateSoilComponent()
        self._associateGraphConfigs()


    def associateHeader(self) :
        pass

    # MAP --------------------------------------- >>>

    def _associateGraphConfigs(self) :
        self.buttonConfiguration = self.view.mapaView.addButtonConfig(icon='public/configIcon.png')
        self.buttonConfiguration.clicked.connect(lambda : self.functionButtonConfiguration())


    def associateGraphFilters(self) :
        self.buttonFilterElevation = self.view.mapaView.addButtonFilter(GraphFilters.ELEVATION.value, checkable=True)
        self.mapGraphFilters[GraphFilters.ELEVATION] = self.buttonFilterElevation
        self.buttonFilterElevation.clicked.connect(lambda : self.renderElevation())
        self.buttonFilterFos = self.view.mapaView.addButtonFilter(GraphFilters.FOS.value, checkable=True)
        self.mapGraphFilters[GraphFilters.FOS] = self.buttonFilterFos
        self.buttonFilterFos.clicked.connect(lambda : self.renderFos())
        
   
    def associateGraphModes(self) :
        self.buttonMode2D = self.view.mapaView.addButtonMode(GraphModes.D2.value, checkable=True)
        self.mapGraphModes[GraphModes.D2] = self.buttonMode2D
        self.buttonMode2D.clicked.connect(lambda : self.setGraphMode2D())
        self.buttonMode3D = self.view.mapaView.addButtonMode(GraphModes.D3.value, checkable=True)
        self.mapGraphModes[GraphModes.D3] = self.buttonMode3D
        self.buttonMode3D.clicked.connect(lambda : self.setGraphMode3D())
        self.view.mapaView.addSeparatorButtonsBarr()





    # TOOLSBAR ---------------------------------- >>>

    def associateParameters(self) :
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



    def _associateSoilComponent(self) :
        boxSoilView = self.view.toolsbar.addBox('Soil')
        self.soilView = SoilView()
        boxSoilView.addSubWidget(self.soilView)
        self.soilView.setClay(INITIAL_CLAY)
        self.soilView.setSand(INITIAL_SAND)
        self.soilView.setSilt(INITIAL_SILT)
        self.soilView.editClay.valueChanged.connect(lambda : self.defineSoil())
        self.soilView.editSand.valueChanged.connect(lambda : self.defineSoil())















