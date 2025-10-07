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
        self.view.header.labelDimensions.setText(f'{self.mapa.getMainMatrix().shape}')
        self.button3D.click()
        self.buttonElevation.click()


    # --------------------------------------------------------------------------------------------- >>>
    
    # GRAPH MODES ------------------------------- >>>
    def set2DGraphMode(self) :
        self.setGraphMode(GraphModes.D2)
        self.view.map.setViewer2D()


    def set3DGraphMode(self) :
        self.setGraphMode(GraphModes.D3)
        self.view.map.setViewer3D()


    def setGraphMode(self, mode:GraphModes) :
        for graphMode, button in self.mapGraphModes.items() :
            if graphMode != mode : button.setChecked(False)
            else : button.setChecked(True)


    # GRAPH FILTERS ----------------------------- >>>

    def setFilterFos(self) :
        self.setFilter(GraphFilters.FOS)
        self.filterType = GraphFilters.FOS
        self.fos = self.calculateFos()
        self.view.map.renderMap(self.mapa.getMainMatrix(), self.fos, self.mapa.getXScaleVector(), self.mapa.getYScaleVector(),)


    def setFilterElevation(self) :
        self.setFilter(GraphFilters.ELEVATION)
        self.filterType = GraphFilters.ELEVATION
        self.view.map.renderMap(self.mapa.getMainMatrix(), vX=self.mapa.getXScaleVector(), vY=self.mapa.getYScaleVector())


    def setFilter(self, filter) :
        for graphFilter, button in self.mapGraphFilters.items() :
            if graphFilter != filter : button.setChecked(False)
            else : button.setChecked(True)




    def parameterChanged(self) :
        if self.filterType == GraphFilters.FOS :
            self.setFilterFos()



    def getParameters(self) :
        h      = self.mapParametersViews[Parameters.H].getValue()
        hw     = self.mapParametersViews[Parameters.HW].getValue()
        c      = self.mapParametersViews[Parameters.C].getValue()
        phi    = self.mapParametersViews[Parameters.PHI].getValue()
        thetai = self.mapParametersViews[Parameters.THETAI].getValue()
        return h, hw, c, phi, thetai    
    

    def calculateFos(self) : 
        h, hw, c, phi, thetai = self.getParameters()
        Z = self.mapa.getMainMatrix()
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
        button = self.view.map.addButton(dictButton.TITLE, checkable=True) 
        button.clicked.connect(lambda : dictButton.FUNCTION())
        dictButton.BUTTON = button



    # ASSOCIATIONS -------------------------------------------------------------------------------- >>>


    def _association(self) :
        self.associateHeader()
        self.associateParameters()
        self.associateGraphModes()
        self.associateGraphFilters()
        self._associateRainComponent()
        self._associateSoilComponent()


    def associateHeader(self) :
        self.buttonSaveMap = self.view.header.addButton('Save Map')
        self.buttonCurMap = self.view.header.addButton('Cut Map')

    # MAP --------------------------------------- >>>


    def associateGraphFilters(self) :
        self.buttonElevation = self.view.map.addButton(GraphFilters.ELEVATION.value, checkable=True)
        self.buttonFos = self.view.map.addButton(GraphFilters.FOS.value, checkable=True)
        self.mapGraphFilters[GraphFilters.ELEVATION] = self.buttonElevation
        self.mapGraphFilters[GraphFilters.FOS] = self.buttonFos
        self.buttonElevation.clicked.connect(lambda: self.setFilterElevation())
        self.buttonFos.clicked.connect(lambda: self.setFilterFos())

        
   
    def associateGraphModes(self) :
        self.button2D = self.view.map.addButton(GraphModes.D2.value, checkable=True)
        self.button3D = self.view.map.addButton(GraphModes.D3.value, checkable=True)
        self.mapGraphModes[GraphModes.D2] = self.button2D
        self.mapGraphModes[GraphModes.D3] = self.button3D
        self.button2D.clicked.connect(lambda: self.set2DGraphMode())
        self.button3D.clicked.connect(lambda: self.set3DGraphMode())





    # TOOLSBAR ---------------------------------- >>>

    def associateParameters(self) :
        self.boxParameters = self.view.toolsbar.addBox('Parameters')
        for K, P in PARAMETERS.items() :
            widget = SubEditor(K.value, P.min, P.max)
            widget.slider.valueChanged.connect(self.parameterChanged)
            self.boxParameters.addSubWidget(widget)
            self.mapParametersViews[K] = widget




    def _associateRainComponent(self) :
        rainv = self.view.toolsbar.addBox('Rain')
        self.rain = RainView()
        rainv.addSubWidget(self.rain)



    def _associateSoilComponent(self) :
        soilOption = self.view.toolsbar.addBox('Soil')
        self.soilView = SoilView()
        soilOption.addSubWidget(self.soilView)
        self.soilView.setClay(INITIAL_CLAY)
        self.soilView.setSand(INITIAL_SAND)
        self.soilView.setSilt(INITIAL_SILT)
        self.soilView.editClay.valueChanged.connect(lambda : self.defineSoil())
        self.soilView.editSand.valueChanged.connect(lambda : self.defineSoil())






