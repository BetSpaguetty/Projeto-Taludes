from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.base import *
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import pyqtgraph.opengl as gl
from matplotlib import cm, colors



class MapView(DDWidget) :

    def __init__(self):
        super().__init__()
        self.setMinimumWidth(300)
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setContentsMargins(5,1,5,5)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBox.setObjectName('map')
        self._mapBar()
        self._mapWindowPyqtgraph()
        self.setStyleSheet(QSS)


    def _mapBar(self) :
        self.mapBar = QWidget()
        self.mapBar.setObjectName('mapBar')
        self.mapBar.setFixedHeight(30)
        self.mainBoxLayout.addWidget(self.mapBar)
        self.mapBarLayout = QHBoxLayout()
        self.mapBarLayout.setSpacing(5)
        self.mapBarLayout.setContentsMargins(0,0,0,0)
        self.mapBarLayout.setAlignment(Qt.AlignLeft)
        self.mapBar.setLayout(self.mapBarLayout)

        self.grupo = QButtonGroup()

        self.buttonElevation = self.addButton('Elevation', checkable=True)
        self.buttonFos = self.addButton('Fos', checkable=True)

        self.buttonConfig = QPushButton('config')
        self.buttonConfig.setObjectName('visualButton')

        self.mapBarLayout.addWidget(self.buttonElevation)
        self.mapBarLayout.addWidget(self.buttonFos)
        self.mapBarLayout.addStretch()
        self.mapBarLayout.addWidget(self.buttonConfig)



    def _mapWindowPyqtgraph(self) :
        self.mapWindow = gl.GLViewWidget()
        self.mapWindow.setCameraPosition(distance=3000)
        self.mainBoxLayout.addWidget(self.mapWindow)



    def addButton(self, title:str, checkable:False) :
        button = QPushButton(title)
        button.setCheckable(checkable)
        button.setObjectName('visualButton')
        return button


    def renderGL(self, Z:np.ndarray,  vX:np.ndarray, vY:np.ndarray, layer=None) :
        if layer is None : colors = self.getColorSpectre(Z)
        else : colors = self.getColorSpectre(layer)
        
        self.cleanGraph()
       
        p3d = gl.GLSurfacePlotItem(x=vY, y=vX, z=Z, colors=colors, shader='shaded', smooth=False)
        self.mapWindow.addItem(p3d)



    def getColorSpectre(self, matrix:np.ndarray) :
        norm = mcolors.Normalize(vmin=np.min(matrix), vmax=np.max(matrix))
        cmap = cm.get_cmap('viridis')
        colors = cmap(norm(matrix.flatten()))  
        return colors



    def cleanGraph(self) :
        for item in self.mapWindow.items :
            self.mapWindow.removeItem(item)



    

QSS = """
#map {

    background-color: #202020;
    border-radius: 5px;

}

#mapBar {

}
#visualButton {
    border-radius: 3px;
    background-color: #404040;
    color: white;
    width: 50px;
    height: 20px;

    }
#visualButton:hover {
    background-color: #606060;


    }

#visualButton:checked {
    background-color: #198de6;


    }

#plotter {

}



"""






