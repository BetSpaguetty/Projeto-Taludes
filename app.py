from _views.mainWindow import TaludesWindow
from _controllers.ambienteController import AmbienteController
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
import os
from config import *
import webbrowser

class TaludesApp :

    def __init__(self):
        self.window = TaludesWindow()
        self.ambientes = []

        self._configuration()
        self._initialization()
        

    def _configuration(self) :
        self.buttonAddFile = self.window.topBar.addButton('Add File')
        self.buttonAddFile.clicked.connect(self.createNewAmbient)
        self.window.tecgrafbutton.clicked.connect(lambda : self.openTecgraf())


    def _initialization(self) :
        self.addAmbient('DATA/mapa1.tif')


    def openTecgraf(self) :
        url = TECGRAF_LINK
        webbrowser.open(url)

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



