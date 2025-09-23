from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.window import CoresWindow
from _views.workspace import Workspace
import webbrowser
from config import *

 
class TaludesWindow(CoresWindow) :

    def __init__(self) :
        super().__init__()
        self._configuration()


    def _configuration(self) :
        self.mainSpaceLayout = QHBoxLayout()
        self.mainSpaceLayout.setSpacing(0)
        self.mainSpaceLayout.setContentsMargins(0,0,0,0)
        self.mainSpace.setLayout(self.mainSpaceLayout)
        self.workspace = Workspace()
        self.mainSpaceLayout.addWidget(self.workspace)
        self.tecgrafbutton = self.leftBar.addItem('public/tecgrafLogo', 30)


    def addAmbient(self, ambiente, name='amebiente') :
        self.workspace.addAmbient(ambiente, name)


    def removeAmbient(self, ambient) :
        raise NotImplementedError()


QSS = """

QMainWindow { 
    background-color: #202020;  
    border: 0px solid transparent; 
    } 

QMainWindow::separator { 
    width: 2px; 
    height: 0px; 
    background-color: #404040; 
    margin: 5px;
    } 


"""



