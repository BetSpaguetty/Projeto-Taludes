from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from __DDCores.base import *
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import pyqtgraph.opengl as gl
from matplotlib import cm, colors
import pyqtgraph as pg
from dataclasses import dataclass
from pyqtgraph.opengl import shaders
from __DDCores.windowBars import QSS_HORIZONTAL
from PIL import Image
import numpy as np
import numpy as np
from matplotlib import image as mpimg
from pyqtgraph.opengl import MeshData
class MapView(DDWidget) :

    def __init__(self):
        super().__init__()
        self._properties()
        self._view()
        self._matrixViewers()
        self._initialization()

    def _initialization(self) :
        self.viewsModes = { 
            '2D' : {'function': self.renderMatrix2D, 'viewer': 0 },
            '3D' : {'function': self.renderMatrix3D, 'viewer': 1 }
            }



    def _properties(self) : 
        self.matrixFilter = None 
        self.matrixElevation = None 
        self.vectorX = None 
        self.vectorY = None 
        self.viewMode = '3D'
        self.transparency = 1.0
        self.colorMap = 'terrain'
        self.listColors = None 
        self.listBounds = None 
        self.layer = None 
        self.ploted = False
        self.renderFunction = self.renderMatrix3D
        self.hasLayer = True

        

    def _view(self) :
        # BODY
        self.setMinimumWidth(300)
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setContentsMargins(5,1,5,5)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBox.setObjectName('viewer')

        # FILTERS BAR --------------------------- >>>
        self.filtersSpace = QWidget()
        self.filtersSpace.setObjectName('filtersSpace')
        self.filtersSpace.setFixedHeight(35)
        self.filtersSpaceLayout = QHBoxLayout()
        self.filtersSpaceLayout.setSpacing(5)
        self.filtersSpaceLayout.setContentsMargins(0,5,0,5)
        self.filtersSpaceLayout.setAlignment(Qt.AlignLeft)
        self.filtersSpace.setLayout(self.filtersSpaceLayout)
        self.mainBoxLayout.addWidget(self.filtersSpace)

        # GRUPOS
        self.groupFilterButtons = QButtonGroup()
        self.groupFilterButtons.setExclusive(True)
        self.groupModeButtons = QButtonGroup()
        self.groupModeButtons.setExclusive(True)

        # CONFIG BAR ---------------------------- >>>
        self.configSpace = QWidget()
        self.configSpace.setObjectName('configSpace')
        self.configSpace.setFixedHeight(35)
        self.configSpaceLayout = QHBoxLayout()
        self.configSpaceLayout.setSpacing(5)
        self.configSpaceLayout.setContentsMargins(0, 5, 0, 5)
        self.configSpaceLayout.setAlignment(Qt.AlignLeft)
        self.configSpace.setLayout(self.configSpaceLayout)
        self.mainBoxLayout.addWidget(self.configSpace)

        self.button3D = self.addModeButton('3D')
        self.button2D = self.addModeButton('2D')




        self.setStyleSheet(QSS)




    def addFilterButton(self, title, icon:str=None, checkable:bool=True) : 
        button = QPushButton(title)
        if icon : 
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(25, 25))
            button.setObjectName('iconButton')
        else :
            button.setObjectName('filterButton')
        button.setCheckable(checkable)
        self.filtersSpaceLayout.addWidget(button)
        self.groupFilterButtons.addButton(button)
        return button


    def addModeButton(self, title, icon:str=None, checkable:bool=True) : 
        button = QPushButton(title)
        if icon : 
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(25, 25))
            button.setObjectName('iconButton')
        else :
            button.setObjectName('modeButton')
        button.setCheckable(checkable)
        self.configSpaceLayout.addWidget(button)
        self.groupModeButtons.addButton(button)
        return button


    def addConfigButton(self, title, icon:str=None, checkable:bool=True) : 
        button = QPushButton(title)
        if icon : 
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(25, 25))
            button.setObjectName('iconButton')
        else :
            button.setObjectName('filterButton')
        button.setCheckable(checkable)
        self.configSpaceLayout.addWidget(button)
        return button

    
    def addItemConfig(self, item) :
        self.configSpaceLayout.addWidget(item, alignment=Qt.AlignLeft)


    def addComboBox(self) : 
        comboBox = QComboBox()
        comboBox.setObjectName('comboBox')
        self.configSpaceLayout.addWidget(comboBox, alignment=Qt.AlignLeft)
        return comboBox


    # VIEWERS ------------------------------------------------------------------------------------- >>>

    def _matrixViewers(self) :
        #2D MAP
        self.ViewWidget2D = pg.GraphicsLayoutWidget()
        self.viewBox2D = self.ViewWidget2D.addViewBox()
        self.viewBox2D.setAspectLocked(True)
        self.matrixItem2D = pg.ImageItem()
        self.viewBox2D.addItem(self.matrixItem2D)

        #3D MAP
        self.viewWidget3D = gl.GLViewWidget()
        self.viewWidget3D.setCameraPosition(distance=3000)
        custom_shader = shaders.ShaderProgram(vertex=vertex_shader, fragment=fragment_shader)
        self.matrixItem3D = gl.GLSurfacePlotItem(x=None, y=None, z=None, colors=None, 
                                                 shader=custom_shader, 
                                                 smooth=False, 
                                                 computeNormals=True, 
                                                 glOptions='opaque', 
                                                 drawFaces=True, drawEdges=False)
        
        self.matrixItem3D.setGLOptions('translucent')
        self.viewWidget3D.addItem(self.matrixItem3D)

        # STACK
        self.mainBoxLayout.addWidget(self.ViewWidget2D)
        self.mainBoxLayout.addWidget(self.viewWidget3D)




 


    # MATRIX FILTER ------------------------------------------------------------------------------- >>>

    def saveMatrix(self,  matrixFilter:np.ndarray, matrixElevation:np.ndarray=None, vX:np.ndarray=None, vY:np.ndarray=None) :
        self.matrixFilter = matrixFilter
        self.matrixElevation = matrixElevation
        if vX is not None : self.vectorX = vX 
        if vY is not None : self.vectorY = vY


    def renderMatrix(self, matrixFilter, *args) : 
        self.ploted = True
        self.saveMatrix(matrixFilter, *args)
        self.renderFunction(matrixFilter, *args)


    def autoRender(self) :
        if self.ploted :  
            self.renderMatrix(self.matrixFilter, self.matrixElevation, self.vectorX, self.vectorY)


    def renderMatrix3D(self, matrixFilter, matrixElevation=None, vectorX=None, vectorY=None) :
        colors = self.getColorMap(matrixFilter, TO1D=True)
        self.matrixItem3D.setData(x=vectorY, y=vectorX, z=matrixElevation, colors=colors)
 


    def renderMatrix2D(self, matrixFilter, *args) :
        colors = self.getColorMap(matrixFilter)
        self.matrixItem2D.setImage(colors)



    def imageToMatrix(self, img:str, TO1D = False) : 
        image = Image.open(img).convert("RGBA") 
        matriz = np.array(image, dtype=np.float32)
        if TO1D : matriz = matriz.reshape(-1, 4)
        return matriz



    def getColorMap(self, matrix:np.ndarray, TO1D = False) :
        if TO1D : matrix = matrix.flatten()
        # Color map
        if self.listColors is None : cmap = cm.get_cmap(self.colorMap)
        else : cmap = mcolors.ListedColormap(self.listColors)
        # Normalização
        if self.listBounds is None : norm = mcolors.Normalize(vmin=np.min(matrix), vmax=np.max(matrix))
        else : norm = mcolors.BoundaryNorm(boundaries=self.listBounds, ncolors=cmap.N)
        # Cores
        colorMap = cmap(norm(matrix))

        colorMap[..., -1] = self.transparency 
        return colorMap


    def cleanViewer3D(self) :
        for item in self.viewWidget3D.items :
            self.viewWidget3D.removeItem(item)


    def addImage(self) : 
        pass


    # MATRIX CONFIG ------------------------------------------------------------------------------- >>>

    def setMatrixShader(self, shader:str) : 
        if shader == 'None' : shader = None
        self.matrixItem3D.setShader(shader)


    def setMatrixSmooth(self, smooth:bool) : 
        self.matrixItem3D.opts['smooth'] = smooth
        self.autoRender()

    def setMatrixDrawEdges(self, a0:bool) : 
        self.matrixItem3D.opts['drawEdges'] = a0
        self.autoRender()

    def setMatrixDrawFaces(self, a0:bool) : 
        self.matrixItem3D.opts['drawFaces'] = a0
        self.autoRender()


    def setViewer2D(self) :
        self.viewMode = '2D'
        self.ViewWidget2D.setVisible(True)
        self.viewWidget3D.setVisible(False) 
        self.renderFunction = self.renderMatrix2D
        self.autoRender()


    def setViewer3D(self) :
        self.viewMode = '3D'
        self.ViewWidget2D.setVisible(False)
        self.viewWidget3D.setVisible(True)
        self.renderFunction = self.renderMatrix3D
        self.autoRender()





    def setColorMap(self, colorMap, listColors:list[str] = None, listBounds:list[float] = None ) :
        self.colorMap   = colorMap
        self.listColors = listColors
        self.listBounds = listBounds
        self.autoRender()



    def setOpacity(self, opacity:float=1.0) : 
        self.transparency = opacity
        self.autoRender()

    
    def setLayer(self, img:str) :
        pass


    def setModelTransformations(self, vX:np.ndarray, vY:np.ndarray) :
        self.vectorX = vX 
        self.vectorY = vY 
        self.autoRender()



    def criar_slider_rotulado(self, titulo: str, minimo: int, maximo: int, valor_inicial: int = None) -> QWidget:
       
        slider = QSlider(Qt.Horizontal)
        slider.setObjectName("slider")
        slider.setMinimum(minimo)
        slider.setMaximum(maximo)
        slider.setValue(valor_inicial if valor_inicial is not None else minimo)

        label_titulo = QLabel(titulo)
        label_titulo.setStyleSheet("color: white; font-size: 11px;")

        widget = QWidget()

        widgetLayout = QHBoxLayout()
        widgetLayout.setContentsMargins(0,0,0,0)
        widgetLayout.setSpacing(5)
        widget.setLayout(widgetLayout)


        label_min = QLabel(str(minimo))
        label_min.setStyleSheet("color: white; font-size: 11px;")
        label_max = QLabel(str(maximo))
        label_max.setStyleSheet("color: white; font-size: 11px;")




        layoutSlider = QVBoxLayout()
        layoutSlider.setContentsMargins(0,0,0,0)
        layoutSlider.setSpacing(0)

        layoutSlider.addWidget(label_titulo, alignment=Qt.AlignCenter)
        layoutSlider.addWidget(slider)


        widgetLayout.addWidget(label_min, alignment=Qt.AlignBottom)
        widgetLayout.addLayout(layoutSlider)
        widgetLayout.addWidget(label_max, alignment=Qt.AlignBottom)



        self.configSpaceLayout.addWidget(widget, alignment=Qt.AlignLeft)

        return slider

# =================================================================================================================================================== |||

vertex_shader = """
#version 120
attribute vec3 vertex;
attribute vec3 normal;
uniform mat4 modelViewMatrix;
uniform mat4 projectionMatrix;
varying vec3 vNormal;
void main() {
    vNormal = normal;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(vertex, 1.0);
}
"""

fragment_shader = """
#version 120
varying vec3 vNormal;
void main() {
    float light = dot(normalize(vNormal), vec3(0.0, 0.0, 1.0));
    gl_FragColor = vec4(0.5 + 0.5 * light, 0.2, 0.8, 1.0);
}
"""


NEW_QSS = """



"""


 
QSS = """


#slider::groove:horizontal {
    border: 1px solid #bbb;
    background: #e0e0e0;
    height: 4px;
    border-radius: 3px;
}
#slider::sub-page:horizontal {
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #2196F3, stop:1 #42A5F5
    );
    border-radius: 3px;
}
#slider::add-page:horizontal {
    background: #ccc;
    border-radius: 3px;
}
#slider::handle:horizontal {
    background: white;
    border: 2px solid #2196F3;
    width: 14px;
    height: 10px;
    margin: -5px 0;
    border-radius: 7px;
}
#slider::handle:horizontal:hover {
    background: #E3F2FD;
    border: 2px solid #1976D2;
}



#comboBox { 
    background-color: white;
    border: 1px solid gray;
    border-radius: 6px;
    padding: 4px;
    color: white;
    background-color: #101010;

}

#comboBox:hover {
    border: 1px solid #0078d7;
}
#comboBox::drop-down {
    border: 0px;
}



#viewer {
    background-color: #202020;
    border-radius: 5px;

    }

#filtersSpace {
    border-bottom: 1px solid #505050;

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







"""






