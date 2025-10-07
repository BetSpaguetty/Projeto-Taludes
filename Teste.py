from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.base import *
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import pyqtgraph.opengl as gl
from matplotlib import cm, colors
import pyqtgraph as pg


class MapView(DDWidget) :



    def __init__(self):
        super().__init__()
        
        self.setMinimumWidth(300)
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setContentsMargins(5,1,5,5)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBox.setObjectName('map')
        self._initialization()
        self.setStyleSheet(QSS)


    def _properties(self) :
        self.mapType : str = None
        self.Z = None 
        self.vX = None 
        self.vY = None 
        self.layer = None 

    
    def _view(self) :
        self._toolsBar()
        self._mapWindowPyqtgraph()



    def _toolsBar(self) :
        self.mapBar = QWidget()
        self.mapBar.setObjectName('mapBar')
        self.mapBar.setFixedHeight(30)
        self.mainBoxLayout.addWidget(self.mapBar)
        self.mapBarLayout = QHBoxLayout()
        self.mapBarLayout.setSpacing(5)
        self.mapBarLayout.setContentsMargins(0,0,0,0)
        self.mapBarLayout.setAlignment(Qt.AlignLeft)
        self.mapBar.setLayout(self.mapBarLayout)



    def _mapWindowPyqtgraph(self) :
        self.mapViewer2D = pg.ImageView()
        self.mapViewer3D = gl.GLViewWidget()
        self.mapViewer3D.setCameraPosition(distance=3000)
        self.mainBoxLayout.addWidget(self.mapViewer2D)
        self.mainBoxLayout.addWidget(self.mapViewer3D)




    def _initialization(self) :
        self.setMap3D()


    def setMap3D(self) :
        self.mapType = '3D'
        self.mapViewer2D.setVisible(False)
        self.mapViewer3D.setVisible(True)
        if self.Z is not None:
            self.render3D(self.Z, self.vX, self.vY, self.layer)


    def setMap2D(self) :
        self.mapType = '2D'
        self.mapViewer3D.setVisible(False)
        self.mapViewer2D.setVisible(True)
        if self.Z is not None : 
            self.render2D(self.Z, self.layer)


    def addButton(self, title:str, checkable:False) -> QPushButton :
        button = QPushButton(title)
        button.setCheckable(checkable)
        button.setObjectName('visualButton')
        self.mapBarLayout.addWidget(button)
        return button




    def renderGL(self, Z:np.ndarray,  vX:np.ndarray, vY:np.ndarray, layer=None) :
        self.Z = Z
        self.vX = vX
        self.vY = vY 
        self.layer = layer
        if   self.mapType == '2D' : self.render2D(Z, layer)
        elif self.mapType == '3D' : self.render3D(Z, vX, vY, layer)


    def render2D(self, Z:np.ndarray, layer=None) :
        if layer is None : colors = self.getColorSpectre2D(Z)
        else : colors = self.getColorSpectre2D(layer)
        self.mapViewer2D.setImage(colors)

    
    def render3D(self, Z:np.ndarray,  vX:np.ndarray, vY:np.ndarray, layer=None) :
        if layer is None : colors = self.getColorSpectre(Z)
        else : colors = self.getColorSpectre(layer)
        self.cleanGraph()       
        p3d = gl.GLSurfacePlotItem(x=vY, y=vX, z=Z, colors=colors, shader='shaded', smooth=False)
        self.mapViewer3D.addItem(p3d)


    def getColorSpectre2D(self, matrix:np.ndarray) :
        norm = mcolors.Normalize(vmin=np.min(matrix), vmax=np.max(matrix))
        cmap = cm.get_cmap('viridis')
        colors = cmap(norm(matrix))  

        return colors

    def getColorSpectre(self, matrix:np.ndarray) :
        norm = mcolors.Normalize(vmin=np.min(matrix), vmax=np.max(matrix))
        cmap = cm.get_cmap('viridis')
        colors = cmap(norm(matrix.flatten()))  
        return colors


    def cleanGraph(self) :
        for item in self.mapViewer3D.items :
            self.mapViewer3D.removeItem(item)



    

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






