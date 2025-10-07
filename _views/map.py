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
from dataclasses import dataclass

from PIL import Image


class MapView(DDWidget) :

    def __init__(self):
        super().__init__()
        self._properties()
        self._view()
        self._mapViewers()
        self._initialization()
  

    def _initialization(self) :
        pass


    def _properties(self) : 
        self.renderFunction = self.render3D
        self.viewer : str = None
        self.mapViewers : dict = {}
        self.mainMapMatrix : np.ndarray = None
        self.mainMapFilter : np.ndarray = None
        self.vX : np.ndarray = None
        self.vY : np.ndarray = None
        self.colorType : str = 'viridis'
        self.colorOpacity : int = 1.0
        self.layers = []
        

    def _view(self) :
        # BODY
        self.setMinimumWidth(300)
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setContentsMargins(5,1,5,5)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBox.setObjectName('map')
        # BUTTONS BAR
        self.mapBar = QWidget()
        self.mapBar.setObjectName('mapBar')
        self.mapBar.setFixedHeight(30)
        self.mainBoxLayout.addWidget(self.mapBar)
        self.mapBarLayout = QHBoxLayout()
        self.mapBarLayout.setSpacing(5)
        self.mapBarLayout.setContentsMargins(0,0,0,0)
        self.mapBarLayout.setAlignment(Qt.AlignLeft)
        self.mapBar.setLayout(self.mapBarLayout)


    def _mapViewers(self) :
        self.mapViewer2D = pg.ImageView()
        self.mapViewer2D = pg.GraphicsLayoutWidget()
        self.vb = self.mapViewer2D.addViewBox()
        self.vb.setAspectLocked(True)

        self.mapViewer3D = gl.GLViewWidget()
        self.mapViewer3D.setCameraPosition(distance=3000)
        self.mainBoxLayout.addWidget(self.mapViewer2D)
        self.mainBoxLayout.addWidget(self.mapViewer3D)
        


    def addButton(self, title:str, checkable:False) -> QPushButton :
        button = QPushButton(title)
        button.setCheckable(checkable)
        button.setObjectName('visualButton')
        self.mapBarLayout.addWidget(button)
        return button

    # ------------------------------------------- >>>

    def setInfos(self,  Z:np.ndarray, filter:np.ndarray, vX:np.ndarray, vY:np.ndarray) :
        self.mainMapMatrix = Z
        if filter is not None : self.mainMapFilter = filter
        if vX is not None : self.vX = vX 
        if vY is not None : self.vY = vY


    def renderMap(self,  Z:np.ndarray, filter:np.ndarray=None, vX:np.ndarray=None, vY:np.ndarray=None) :
        self.setInfos(Z, filter, vX, vY)
        self.renderFunction(Z, filter, vX, vY)


    def render2D(self, Z, filter, *args) :
        self.vb.clear()
        colors = self.getColorSpectre2D(Z) if filter is None else self.getColorSpectre2D(filter)
        #colors = pg.ImageItem(colors)
        colors = (colors * 255).astype(np.uint8)  # converte para 0–255
        img_item = pg.ImageItem(colors)
        #self.vb.addItem(pg.ImageItem(np.array(Image.open("DATA/img1.jpg").convert("RGBA"))))
        self.vb.addItem(img_item)
        #self.layers.append(img_item)
        #self.mapViewer2D.setImage(colors)

    
    def render3D(self, Z, filter, vX, vY) :
        self.cleanGraph()       
        colors = self.getColorSpectre3D(Z) if filter is None else self.getColorSpectre3D(filter)
        p3d = gl.GLSurfacePlotItem(x=vY, y=vX, z=Z, colors=colors, shader='shaded', smooth=False)
        p3d.setGLOptions('translucent')
        self.mapViewer3D.addItem(p3d)


    def getColorSpectre2D(self, matrix:np.ndarray) :
        norm = mcolors.Normalize(vmin=np.min(matrix), vmax=np.max(matrix))
        cmap = cm.get_cmap('viridis')
        colors = cmap(norm(matrix))  
        colors[..., -1] = self.colorOpacity
        return colors

    def getColorSpectre3D(self, matrix:np.ndarray) :
        norm = mcolors.Normalize(vmin=np.min(matrix), vmax=np.max(matrix))
        cmap = cm.get_cmap('viridis')
        colors = cmap(norm(matrix.flatten()))  
        colors[:, -1] = self.colorOpacity  
        return colors

    
    def cleanGraph(self) :
        for item in self.mapViewer3D.items :
            self.mapViewer3D.removeItem(item)
    

    def setViewer2D(self) :
        self.viewer = '2D'
        self.mapViewer2D.setVisible(True)
        self.mapViewer3D.setVisible(False)
        self.renderFunction = self.render2D
        if self.mainMapMatrix is not None: self.renderMap(self.mainMapMatrix, self.mainMapFilter)


    def setViewer3D(self) :
        self.viewer = '3D'
        self.mapViewer3D.setVisible(True)
        self.mapViewer2D.setVisible(False)
        self.renderFunction = self.render3D
        if self.mainMapMatrix is not None : self.renderMap(self.mainMapMatrix, self.mainMapFilter, self.vX, self.vY)




# =================================================================================================================================================== |||

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






