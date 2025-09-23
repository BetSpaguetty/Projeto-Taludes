from Taludes.taludes import *

from _models.ambienteModel import AmbienteModel
from _views.ambienteView import AmbienteView
from _views.toolsbar import *
import os
from ddmapa import Mapa
from config import *


class AmbienteController :

    def __init__(self, filepath):
        self.model = AmbienteModel()
        self.view  = AmbienteView()
        self.filepath : str = filepath
        self.mapa     : Mapa = Mapa(filepath)

        self._properties()
        self._association()
        self._configuration()
        self._initialization()


    def _properties(self) :
        self.renderType = 'elevation'
        self.solo : Materiais = Materiais.COARSE
        self.fos  : np.ndarray = None
        self.parametersViews : list[SubEditor] = []
        self.mapParametersViews : dict[Parameters, SubEditor] = {}


    def _configuration(self) :
        self.defineSoil()
        self.view.header.labelTitle.setText(os.path.basename(self.filepath))
        self.view.header.labelDimensions.setText(f'{self.mapa.getMainMatrix().shape}')
        

    def _initialization(self) :
        self.boxParameters.click()
        self.view.map.buttonElevation.click()
        


    # RENDERIZAÇÂO -------------------------------------------------------------------------------- >>>


    def parameterChanged(self) :
        if self.renderType == 'fos' :
            self.renderFos()


    def renderFos(self) :
        self.renderType = 'fos'
        self.view.map.buttonElevation.setChecked(False)
        self.fos = self.getFos()
        self.view.map.renderGL(self.mapa.getMainMatrix(), self.mapa.getXScaleVector(), self.mapa.getYScaleVector(), self.fos)


    def renderElevation(self) :
        self.renderType = 'elevation'
        self.view.map.buttonFos.setChecked(False)
        self.view.map.renderGL(self.mapa.getMainMatrix(), self.mapa.getXScaleVector(), self.mapa.getYScaleVector())





    # DEFINIÇÃO DO SOLO --------------------------------------------------------------------------- >>>


    def defineSoil(self) :
        clay = self.view.soil.getClay()
        sand = self.view.soil.getSand()
        silt = self.view.soil.getSilt()
        for KEY, SOIL in SOIL_TYPES.items() :
            if SOIL['function'](clay, sand, silt) : 
                self.solo = KEY
                break
        self.changeSoil()



    def changeSoil(self) :
        self.widgetThetai.setMinMax(SOIL_THETAI[self.solo].min, SOIL_THETAI[self.solo].max)
        self.view.soil.labelSoil.setText(self.solo.value)

    # FOS APLICATION

    def getFos(self) : 
        h, hw, c, phi, thetai = self.getParameters()
        Z = self.mapa.getMainMatrix()
        lenI = Z.shape[0]
        lenJ = Z.shape[1]
        fos  = calculateFos(Z, lenI, lenJ, h, hw, c, phi, thetai, self.mapa.scale, self.solo)
        return fos


    def getParameters(self) :
        h      = self.mapParametersViews[Parameters.H].getValue()
        hw     = self.mapParametersViews[Parameters.HW].getValue()
        c      = self.mapParametersViews[Parameters.C].getValue()
        phi    = self.mapParametersViews[Parameters.PHI].getValue()
        thetai = self.mapParametersViews[Parameters.THETAI].getValue()
        return h, hw, c, phi, thetai

        
    # ASSOCIAÇÃO ==================================================================================================================================== >>>


    def _association(self) :
        self._associateHeader()
        self._associateToolsbar()
        self._associateComponents()
        self._associateMap()

    def _associateHeader(self) :
        self.buttonSaveMap = self.view.header.addButton('Save Map')
        self.buttonCurMap = self.view.header.addButton('Cut Map')


    def _associateToolsbar(self) :
        self.boxParameters = self.view.toolsbar.addBox('Parameters')
        for K, P in FIX_PARAMETERS.items() :
            widget = SubEditor(P['char'], P['param'].min, P['param'].max )
            widget.slider.valueChanged.connect(self.parameterChanged)
            self.boxParameters.addSubWidget(widget)
            self.parametersViews.append(widget)
            self.mapParametersViews[K] = widget
        self.widgetThetai = SubEditor(THETAI[Parameters.THETAI]['char'], SOIL_THETAI[self.solo].min, SOIL_THETAI[self.solo].max )
        self.widgetThetai.slider.valueChanged.connect(self.parameterChanged)

        self.boxParameters.addSubWidget(self.widgetThetai)
        self.parametersViews.append(self.widgetThetai)
        self.mapParametersViews[Parameters.THETAI] = self.widgetThetai


    def _associateComponents(self) :
        self.view.soil.editClay.setValue(INITIAL_CLAY)
        self.view.soil.editSand.setValue(INITIAL_SAND)
        self.view.soil.editSilt.setValue(INITIAL_SILT)
        self.view.soil.editClay.valueChanged.connect(lambda : self.defineSoil())
        self.view.soil.editSand.valueChanged.connect(lambda : self.defineSoil())

    
    def _associateMap(self) :
        self.view.map.buttonElevation.clicked.connect(lambda : self.renderElevation())
        self.view.map.buttonFos.clicked.connect(lambda : self.renderFos())



