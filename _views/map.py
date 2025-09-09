from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.base import *
from pyvistaqt import QtInteractor
import rasterio
import numpy as np
import pyvista as pv
import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets
import warnings
from rasterio.errors import NotGeoreferencedWarning

import pyqtgraph as pg
import pyqtgraph.opengl as gl

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
        self._mapWindow()
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

        self.button3D = self.addButton('3D', checkable=True)
        self.button2D = self.addButton('2D', checkable=True)

        self.buttonConfig = QPushButton('config')
        self.buttonConfig.setObjectName('visualButton')

        self.mapBarLayout.addWidget(self.button2D)
        self.mapBarLayout.addWidget(self.button3D)
        self.mapBarLayout.addStretch()
        self.mapBarLayout.addWidget(self.buttonConfig)


    def _mapWindowPyqtgraph(self) :
        self.w = gl.GLViewWidget()
        self.mainBoxLayout.addWidget(self.w)


    def _mapWindow(self) :
        self.plotter = QtInteractor()
        self.plotter.setObjectName('plotter')
        self.plotter.set_background("black")
        self.mainBoxLayout.addWidget(self.plotter)

    def addButton(self, title:str, checkable:False) :
        button = QPushButton(title)
        button.setCheckable(checkable)
        button.setObjectName('visualButton')
        return button


    def renderGL(self, matriz,  mLinhas, mColunas) :
        p3d = gl.GLSurfacePlotItem(x=mLinhas[0], y=mColunas[:,0], z=matriz, shader='heightColor', smooth=False)
        self.w.addItem(p3d)


    def renderMap3D(self, matriz, mLinhas, mColunas, layer=None, scale = 25) :
        self.plotter.clear() 
        mLinhas = scale * mLinhas
        mColunas = scale * mColunas
        grid = pv.StructuredGrid(mLinhas, mColunas, matriz)
        if layer  is not None: grid["FOS"] = layer.ravel(order='F').astype(np.float32)
        else : grid["elevation"] = matriz.ravel(order="F").astype(np.float32)
        self.plotter.add_mesh(
            grid, 
            scalar_bar_args={
                'vertical': True, 
                'position_x': 0.85, 
                'position_y': 0.25,
                "color": "white",   
                })
        self.plotter.enable_lightkit()
        self.plotter.render()


    def renderMap2D(self, matriz, mLinhas, mColunas, layer=None, isosurfaces= 30):
        self.plotter.clear() 
        grid = pv.StructuredGrid(mLinhas, mColunas, np.zeros(matriz.shape))
        if layer is not None : 
            grid["FOS"] = layer.ravel(order='F').astype(np.float32)
            scalar = 'FOS'
        else : 
            grid["elevation"] = matriz.ravel(order="F").astype(np.float32)
            scalar = 'elevation'
        contours = grid.contour(isosurfaces=isosurfaces, scalars=scalar)
        self.plotter.add_mesh(
            contours,
            scalar_bar_args={
                'vertical': True,
                'position_x': 0.85,
                'position_y': 0.25,
                "color": "white",
            }
        )
        self.plotter.enable_lightkit()
        self.plotter.render()







    

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






