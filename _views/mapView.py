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



class MapView(DDWidget) :

    def __init__(self):
        super().__init__()
        self._properties()
        self._view()
        self.groupModeButtons = QButtonGroup()
        self.groupModeButtons.setExclusive(True)
        self.groupFilterButtons = QButtonGroup()
        self.groupFilterButtons.setExclusive(True)
        self._mapViewers()
        self._initialization()
  

    def _initialization(self) :
        pass


    def _properties(self) : 
        self.renderFunction = self.renderMap3D
        self.mapViewers : dict = {}
        self.matrixFilter : np.ndarray = None
        self.matrixElevation : np.ndarray = None
        self.vX : np.ndarray = None
        self.vY : np.ndarray = None
        self.colorType : str = 'viridis'
        self.colorOpacity : int = 1.0
        self.layers = []
        self.viewer : str = None
        
    def _view(self) :
        # BODY
        self.setMinimumWidth(300)
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setContentsMargins(5,1,5,5)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBox.setObjectName('map')
        # BUTTONS BAR
        self.topBarr = QWidget()
        self.topBarr.setObjectName('mapBar')
        self.topBarr.setFixedHeight(40)
        self.topBarrLayout = QHBoxLayout()
        self.topBarrLayout.setSpacing(5)
        self.topBarrLayout.setContentsMargins(0,3,0,3)
        self.topBarrLayout.setAlignment(Qt.AlignLeft)
        self.topBarr.setLayout(self.topBarrLayout)
        self.mainBoxLayout.addWidget(self.topBarr)


        self.buttonsBarrLeftLayout  = QHBoxLayout()
        self.buttonsBarrLeftLayout.setSpacing(5)
        self.buttonsBarrRightLayout = QHBoxLayout()
        self.buttonsBarrRightLayout.setSpacing(5)
        self.buttonsBarrRightLayout.addStretch()

        self.topBarrLayout.addLayout(self.buttonsBarrLeftLayout)
        self.topBarrLayout.addLayout(self.buttonsBarrRightLayout)



        self.setStyleSheet(QSS)


  


    def _mapViewers(self) :
        #2D MAP
        self.mapViewer2D = pg.GraphicsLayoutWidget()
        self.vb = self.mapViewer2D.addViewBox()
        self.vb.setAspectLocked(True)
        #3D MAP
        self.mapViewer3D = gl.GLViewWidget()
        self.mapViewer3D.setCameraPosition(distance=3000)
        self.mainBoxLayout.addWidget(self.mapViewer2D)
        self.mainBoxLayout.addWidget(self.mapViewer3D)
        

    def addSeparatorButtonsBarr(self) :
        linhaVertical = VerticalLine('#808080')
        self.buttonsBarrLeftLayout.addWidget(linhaVertical)


    def addButtonMode(self, title:str, checkable:False, icon:str = None) -> QPushButton :
        button = QPushButton(title)
        button.setCheckable(checkable)
        if icon : 
            button.setIcon(QIcon(icon))
            button.setObjectName('iconButton')
            button.setIconSize(QSize(25, 25))
        else :
            button.setObjectName('modeButton')
        self.buttonsBarrLeftLayout.addWidget(button)
        self.groupModeButtons.addButton(button)
        return button


    def addButtonFilter(self, title:str, checkable:False, icon:str = None) :
        button = QPushButton(title)
        if icon : 
            button.setIcon(QIcon(icon))
            button.setObjectName('iconButton')
        else :
            button.setObjectName('filterButton')
        button.setCheckable(checkable)
        self.buttonsBarrLeftLayout.addWidget(button)
        self.groupFilterButtons.addButton(button)
        button.setIconSize(QSize(25, 25))
        return button



    def addButtonConfig(self, title:str='', checkable:bool=False, icon:str = None) :
        button = QPushButton(title)
        if icon : 
            button.setObjectName('iconButton')
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(25, 25))
        else :
            button.setObjectName('visualButton')
        button.setCheckable(checkable)
        self.buttonsBarrRightLayout.addWidget(button)
        return button


    # ------------------------------------------- >>>

    def saveInformations(self,  matrixFilter:np.ndarray, matrixElevation:np.ndarray, vX:np.ndarray, vY:np.ndarray) :
        self.matrixFilter = matrixFilter
        self.matrixElevation = matrixElevation
        if vX is not None : self.vX = vX 
        if vY is not None : self.vY = vY


    def renderMap(self, matrixFilter, matrixElevation:np.ndarray=None, vX:np.ndarray=None, vY:np.ndarray=None) :
        self.saveInformations(matrixFilter, matrixElevation, vX, vY)
        self.renderFunction(matrixFilter, matrixElevation, vX, vY)



    def renderMap2D(self, matrixFilter, *args) :
        self.vb.clear()
        colors = self.getColorSpectre2D(matrixFilter)
        colors = (colors * 255).astype(np.uint8) 
        img_item = pg.ImageItem(colors)
        self.vb.addItem(img_item)

    
    def renderMap3D(self, matrixFilter, MatrixElevation, vX, vY) :
        self.cleanGraph()       
        colors = self.getColorSpectre3D(matrixFilter)
        p3d = gl.GLSurfacePlotItem(x=vY, y=vX, z=MatrixElevation, colors=colors, shader='shaded', smooth=False)
        p3d.setGLOptions('translucent')
        self.mapViewer3D.addItem(p3d)


    def getColorSpectre2D(self, matrix:np.ndarray) :
        norm = mcolors.Normalize(vmin=np.min(matrix), vmax=np.max(matrix))
        cmap = cm.get_cmap(self.colorType)
        colors = cmap(norm(matrix))  
        colors[..., -1] = self.colorOpacity
        return colors


    def getColorSpectre3D(self, matrix:np.ndarray) :
        norm = mcolors.Normalize(vmin=np.min(matrix), vmax=np.max(matrix))
        cmap = cm.get_cmap(self.colorType)
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
        self.renderFunction = self.renderMap2D
        if self.matrixFilter is not None: self.renderMap(self.matrixFilter, self.matrixElevation)


    def setViewer3D(self) :
        self.viewer = '3D'
        self.mapViewer3D.setVisible(True)
        self.mapViewer2D.setVisible(False)
        self.renderFunction = self.renderMap3D
        if self.matrixFilter is not None : self.renderMap(self.matrixFilter, self.matrixElevation, self.vX, self.vY)




# =================================================================================================================================================== |||



QSS = """
#map {

    background-color: #202020;
    border-radius: 5px;

}

#mapBar {



}

#iconButton {
    background-color: transparent;
    border-radius: 3px;


    }

#iconButton:hover {
    background-color: #303030;

}

#modeButton {
    border-radius: 3px;
    background-color: #404040;
    font-size: 12px;
    color: white;
    min-width: 50px;
    height: 30px;

    }
#modeButton:hover {
    background-color: #606060;


    }

#modeButton:checked {
    background-color: #1175c2;


    }


#filterButton {
    border-radius: 3px;
    background-color: #404040;
    font-size: 12px;
    color: white;
    min-width: 50px;
    padding: 0px 5px 0px 5px;
    height: 30px;
}


#filterButton:hover {
    background-color: #606060;


    }

#filterButton:checked {
    background-color: #c40e66;


    }



#plotter {


}




"""






