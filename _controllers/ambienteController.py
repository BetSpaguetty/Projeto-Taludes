from Taludes.taludes import *

from _models.ambiente import Ambiente
from _views.ambienteView import AmbienteView
from _views.toolsbar import *
import os

from config import *


class AmbienteController :

    def __init__(self, filepath, type='file'):
        self.model = Ambiente()
        self.view = AmbienteView()

        self.file : str = filepath
        self.solo : Materiais = Materiais.COARSE
        self.type = 'file'
        self.parametersViews : list[SubEditor] = []
        self.parametersViewsMap : dict[Parameters, SubEditor] = {}
        self.renderFunction = self.render3D

        self._association()
        self._configuration()
        self._initialization()


    def _configuration(self) :
        self.render3DParams = {'scale': 25 }
        self.render2DParams = {'isosurfaces': 30}

        self.renders = {
            '3D' : self.render3DParams,
            '2D' : self.render2DParams,
            }

        self.model.uploadFile(self.file)
        self.defineSoil()
        self.view.header.labelTitle.setText(os.path.basename(self.file))
        self.view.header.labelDimensions.setText(f'{self.model.nLinhas}x{self.model.nColunas}')
        self.view.header.labelType.setText(f'{self.type}')
        

    def _initialization(self) :
        self.view.map.button3D.click()
        self.boxParameters.click()
        


    # RENDERIZAÇÂO -------------------------------------------------------------------------------- >>>


    def render3D(self, layer=None) :
        self.renderFunction = self.render3D
        self.view.map.button2D.setChecked(False)
        self.view.map.renderMap3D(self.model.matriz, self.model.mLinhas, self.model.mColunas, layer)


    def render2D(self, layer=None) :
        self.renderFunction = self.render2D
        self.view.map.button3D.setChecked(False)
        self.view.map.renderMap2D(self.model.matriz, self.model.mLinhas, self.model.mColunas, layer)



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

    def runFos(self) : 
        h, hw, phi, c, thetai = self.getParameters()
        fos  = self.model.calculateFos(h, hw, c, phi, thetai, SOIL_FUNCTIONS[self.solo])
        self.renderFunction(fos)


    def getParameters(self) :
        h      = self.parametersViewsMap[Parameters.H].getValue()
        hw     = self.parametersViewsMap[Parameters.HW].getValue()
        phi    = self.parametersViewsMap[Parameters.PHI].getValue()
        c      = self.parametersViewsMap[Parameters.C].getValue()
        thetai = self.parametersViewsMap[Parameters.THETAI].getValue()

        """ TODO
        p = self.view.rain.editP.text()
        t = self.view.rain.editT.text()
        h = self.view.rain.editH.text()
        hw  = self.model.calculateHW(self.solo, p, t, h, thetai)
        """
        return h, hw, phi, c, thetai

        
    # ASSOCIAÇÃO ---------------------------------------------------------------------------------- >>>


    def _association(self) :
        self._associateHeader()
        self._associateToolsbar()
        self._associateComponents()
        self._associateMap()

    def _associateHeader(self) :
        self.buttonSaveMap = self.view.header.addButton('Save Map')
        self.buttonCurMap = self.view.header.addButton('Cut Map')


    def _associateToolsbar(self) :
        self.buttonRun = self.view.toolsbar.addButton('Run Fos')
        self.boxParameters = self.view.toolsbar.addBox('Parameters')
        for K, P in FIX_PARAMETERS.items() :
            widget = SubEditor(P['char'], P['param'].min, P['param'].max )
            self.boxParameters.addSubWidget(widget)
            self.parametersViews.append(widget)
            self.parametersViewsMap[K] = widget
        self.widgetThetai = SubEditor(THETAI[Parameters.THETAI]['char'], SOIL_THETAI[self.solo].min, SOIL_THETAI[self.solo].max )
        self.boxParameters.addSubWidget(self.widgetThetai)
        self.parametersViews.append(self.widgetThetai)
        self.parametersViewsMap[Parameters.THETAI] = self.widgetThetai
        self.buttonRun.clicked.connect(lambda : self.runFos())


    def _associateComponents(self) :
        self.view.soil.editClay.setValue(INITIAL_CLAY)
        self.view.soil.editSand.setValue(INITIAL_SAND)
        self.view.soil.editSilt.setValue(INITIAL_SILT)
        self.view.soil.editClay.valueChanged.connect(lambda : self.defineSoil())
        self.view.soil.editSand.valueChanged.connect(lambda : self.defineSoil())

    
    def _associateMap(self) :
        self.view.map.button3D.clicked.connect(lambda : self.render3D(self.model.fos))
        self.view.map.button2D.clicked.connect(lambda : self.render2D(self.model.fos))



