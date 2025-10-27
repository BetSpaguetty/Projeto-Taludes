from _views.mainWindow import TaludesWindow
from _controllers.ambienteController import AmbienteController
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
import os
from config import *
import webbrowser
from _views.mapPreview import windowMapSelector
from _models.defaultMaps import * 

class TaludesApp :

    def __init__(self):
        self.window = TaludesWindow()
        self.ambientes = []

        self._association()
        self._initialization()
        

    def _association(self) :
        self.window.tecgrafbutton.clicked.connect(lambda : self.openTecgraf())

        self.buttonAddFile = self.window.topBar.addButton('Add File')
        self.buttonAddFile.clicked.connect(self.createNewAmbient)

        self.buttonGetMap = self.window.topBar.addButton('Get Map')
        self.buttonGetMap.clicked.connect(lambda : self.functionButtonGetMap())


    def _initialization(self) :
        self.addAmbient('DATA/mapa1.tif')


    def openTecgraf(self) :
        url = TECGRAF_LINK
        webbrowser.open(url)





    # FUNCIONALIDADES ----------------------------------------------------------------------------- >>>

    def functionButtonGetMap(self) : 
        getMaps()
        self.mapSelector = windowMapSelector([{'name':'Rio De Janeiro 25/10/2024', 'size': 2.4}, {'name':'São Paulo', 'size': 1.4}, {'name':'Gavea 25/10/2024', 'size': 1.2}])
        self.mapSelector.show()





    # CRIANDO AMBIENTE ---------------------------------------------------------------------------- >>>

    def createNewAmbient(self) :
        filepath = self.getFileTif()
        if filepath :
            self.addAmbient(filepath)

    def getFileTif(self) :
        caminho, _ = QFileDialog.getOpenFileName( None, "Selecionar Arquivo", "", "Arquivos de dados (*.tif)" )
        if caminho : return caminho
        return None

    def addAmbient(self, filepath) :
        name = os.path.basename(filepath)
        ambient = AmbienteController(filepath)
        self.window.addAmbient(ambient.view, name)
        self.ambientes.append(ambient)



