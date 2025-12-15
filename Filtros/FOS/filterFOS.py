import os
from config import *
from configMatrix import *
from Filtros.FOS.taludes import *
from Filtros.FOS.presets import *
from Filtros.FOS.types import *
from _views.toolbar import *
from _views.matrixOptionsView import  *
from Filtros.filtro import *
from _views.Componentes.sliders import *

class FilterFOS(Filter) : 

    def __init__(self):
        super().__init__()
        self.propertiesTaludes()
        self.viewsFOS()
        self.soilView.comboBoxSoil.setCurrentIndex(0)
        self.defineSoil()


    def propertiesTaludes(self) : 
        self.mapParametersViews = {}
        self.solo = None


    def viewsFOS(self) : 

        # Parameters
        self.viewsParameters = DDWidget()
        self.playout = DDVBoxLayout()
        self.viewsParameters.mainBox.setLayout(self.playout)
        for K, P in PARAMETERS.items() :
            widget = SubEditor(K.value, P.min, P.max)
            widget.slider.valueChanged.connect(self.sendMatrixToReceptor)
            self.mapParametersViews[K] = widget
            self.playout.addWidget(widget)
        self.views['Parameters'] = self.viewsParameters

        # Rain
        self.rainView = RainView()
        self.rainView.onChange(self.sendMatrixToReceptor)
        self.views['Rain'] = self.rainView

        # Soll
        self.soilView = SoilView()
        self.soilView.onChange(self.defineSoil)
        self.views['Soil'] = self.soilView

        # Scale 
        self.scaleSlider = BasicSlider('Scale', 1, 100)
        self.scaleSlider.slider.setValue(25)
        self.views['Scale'] = self.scaleSlider


        


    def defineSoil(self) :
        if self.solo == self.soilView.getSoil() : return
        self.solo = self.soilView.getSoil()        
        self.mapParametersViews[Parameters.THETAI].setMinMax(SOIL_THETAI[self.solo].min, SOIL_THETAI[self.solo].max)


    def calculateMatrix(self) :
        if self.matrixElevation is None : return
        return self.calculateFos()
 

    def calculateFos(self) : 
        h, hw, c, phi, thetai = self.getParameters()
        matrix = self.getElevationMatrix()
        solo = self.solo
        scale = self.scaleSlider.getValue()
        fos  = Taludes.calculateTaludes(matrix, solo , h, hw, c, phi, thetai, scale)
        return fos


    def calculateHW(self) :
    
        h = self.mapParametersViews[Parameters.H].getValue()
        thetai = self.mapParametersViews[Parameters.THETAI].getValue()
        solo = self.soilView.getSoil()

        if   self.rainView.pagetab == 0 : 
            hw = self.rainView.rainManual.getHW(h, thetai, solo)
        elif self.rainView.pagetab == 1 and self.rainView.rainFile.isOpen == True : 
            hw = self.rainView.rainFile.get_total_hw(h, thetai, solo)

        return hw


    def getParameters(self) :
        h      = self.mapParametersViews[Parameters.H].getValue()
        hw     = self.calculateHW()
        c      = self.mapParametersViews[Parameters.C].getValue()
        phi    = self.mapParametersViews[Parameters.PHI].getValue()
        thetai = self.mapParametersViews[Parameters.THETAI].getValue()
        return h, hw, c, phi, thetai    
    


    def functionSliderTempo(self) :
        self.sendMatrixToReceptor()