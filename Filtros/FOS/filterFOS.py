import os
from config import *
from configMatrix import *
from Filtros.FOS.taludes import *
from Filtros.FOS.presets import *
from Filtros.FOS.types import *
from _views.toolbar import *
from _views.matrixOptionsView import  *
from Filtros.filtro import *


class FilterFOS(Filter) : 

    def __init__(self):
        super().__init__()
        self.propertiesTaludes()
        self.viewsTaludes()


    def propertiesTaludes(self) : 
        self.mapParametersViews = {}

    def viewsTaludes(self) : 
        # Parameters
        self.viewsParameters = []
        for K, P in PARAMETERS.items() :
            widget = SubEditor(K.value, P.min, P.max)
            widget.slider.valueChanged.connect(self.sendMatrix)
            self.mapParametersViews[K] = widget
            self.viewsParameters.append(widget)
        self.views['Parameters'] = self.viewsParameters

        # Rain
        self.viewsRain = []
        self.rainView = RainView()
        self.viewsRain.append(self.rainView)
        self.views['Rain'] = self.viewsRain

        # Soll
        self.viewsSoil = []
        self.soilView = SoilView()
        self.soilView.setClay(INITIAL_CLAY)
        self.soilView.setSand(INITIAL_SAND)
        self.soilView.setSilt(INITIAL_SILT)
        self.viewsSoil.append(self.soilView)
        self.soilView.comboSoil.setCurrentIndex(0)
        self.views['Soil'] = self.viewsSoil


        self.rainView.sliderTempo.valueChanged.connect(lambda : self.functionSliderTempo())
        self.rainView.spinBoxPreciptacao.valueChanged.connect(lambda : self.functionSliderTempo())
        self.soilView.editClay.valueChanged.connect(lambda : self.defineSoil())
        self.soilView.editSand.valueChanged.connect(lambda : self.defineSoil())
        self.soilView.comboSoil.currentIndexChanged.connect(lambda : self.defineSoil())


    def defineSoil(self) :
        self.solo = self.soilView.getSolo()        
        self.soilChanged()

    def soilChanged(self) :
        self.mapParametersViews[Parameters.THETAI].setMinMax(SOIL_THETAI[self.solo].min, SOIL_THETAI[self.solo].max)



    def sendMatrix(self) : 
        if self.matrixElevation is None : return
        matrixFos = self.calculateFos()
        self.sendCallback(matrixFos)


    def calculateMatrix(self):
        if self.matrixElevation is None : return
        return self.calculateFos()
 

    def calculateFos(self) : 
        h, hw, c, phi, thetai = self.getParameters()
        Z = self.getElevationMatrix()
        solo = self.soilView.getSolo()
        fos  = Taludes.calculateTaludes(Z, solo , h, hw, c, phi, thetai, self.scale)
        self.setFilterMatrix(fos)
        return fos


    def calculateHW(self) :
        p = self.rainView.getPreciptacao()
        t = self.rainView.getTempo()
        h      = self.mapParametersViews[Parameters.H].getValue()
        solo = self.soilView.getSolo()

        thetai = self.mapParametersViews[Parameters.THETAI].getValue()
        hw = Taludes.calculateHW(p, t, thetai, h, solo)
        self.rainView.lineEditHW.setText(f'{hw:.5f}')
        return hw


    def getParameters(self) :
        h      = self.mapParametersViews[Parameters.H].getValue()
        hw     = self.calculateHW()
        c      = self.mapParametersViews[Parameters.C].getValue()
        phi    = self.mapParametersViews[Parameters.PHI].getValue()
        thetai = self.mapParametersViews[Parameters.THETAI].getValue()
        return h, hw, c, phi, thetai    
    



    def functionSliderTempo(self) :
        self.sendMatrix()