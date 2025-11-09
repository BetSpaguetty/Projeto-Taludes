from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from __DDCores.base  import *
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import pyqtgraph.opengl as gl
import pyqtgraph as pg
from PIL import Image

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt
import numpy as np
import sys

class MatrixGLWidget(DDWidget) :

    def __init__(self):
        super().__init__()
        self._properties()
        self._view()
        self._buttons()
        self._matrixViewers()
        self._initialization()

    def _initialization(self) :
        pass


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
        self.buttonGroups : dict[QButtonGroup] = {}
        self.buttonGroupsWidgets : dict[QButtonGroup] = {}


    def _view(self) :
        # BODY
        self.setMinimumWidth(300)
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setContentsMargins(5,1,5,5)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBox.setObjectName('viewer')

        # FILTERS BAR --------------------------- >>>
        self.topSpace = QWidget()
        self.topSpace.setObjectName('filtersSpace')
        self.topSpace.setFixedHeight(35)
        self.filtersSpaceLayout = QHBoxLayout()
        self.filtersSpaceLayout.setSpacing(5)
        self.filtersSpaceLayout.setContentsMargins(0,5,0,5)
        self.filtersSpaceLayout.setAlignment(Qt.AlignLeft)
        self.topSpace.setLayout(self.filtersSpaceLayout)
        self.mainBoxLayout.addWidget(self.topSpace)


        # CONFIG BAR ---------------------------- >>>
        self.bottomSpace = QWidget()
        self.bottomSpace.setObjectName('configSpace')
        self.bottomSpace.setFixedHeight(35)
        self.configSpaceLayout = QHBoxLayout()
        self.configSpaceLayout.setSpacing(5)
        self.configSpaceLayout.setContentsMargins(0, 5, 0, 5)
        self.configSpaceLayout.setAlignment(Qt.AlignLeft)
        self.bottomSpace.setLayout(self.configSpaceLayout)
        self.mainBoxLayout.addWidget(self.bottomSpace)


        self.setStyleSheet(QSS)



    def addButtonBottom(self, title, icon) : 
        pass



    def addGroupButtonBottom(self, title, icon, groupName:str, exclusive:bool=True) : 
        if groupName not in self.buttonGroups : 
            group = QButtonGroup()
            if exclusive : group.setExclusive(True)
            self.buttonGroups[groupName] = group
            widgetGroupButton = QWidget()

        button = QPushButton(title)
        if icon : 
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(25, 25))
            button.setObjectName('iconButton')
        else :
            button.setObjectName('modeButton')
        button.setCheckable(True)
        self.configSpaceLayout.addWidget(button)
        group.addButton(button)
        return button











    def _buttons(self) : 
        self.groupFilterButtons = QButtonGroup()
        self.groupFilterButtons.setExclusive(True)
        self.groupModeButtons = QButtonGroup()
        self.groupModeButtons.setExclusive(True)

        self.button3D = self.addGroupButtonBottom('3D', self.groupModeButtons)
        self.button2D = self.addGroupButtonBottom('2D', self.groupModeButtons)






    # PARTE ALTA ---------------------------------------------------------------------------------- >>>
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


    # PARTE BAIXA --------------------------------------------------------------------------------- >>>
    def addGroupButtonBottom(self, title, group:QButtonGroup, icon:str=None, checkable:bool=True) : 
        button = QPushButton(title)
        if icon : 
            button.setIcon(QIcon(icon))
            button.setIconSize(QSize(25, 25))
            button.setObjectName('iconButton')
        else :
            button.setObjectName('modeButton')
        button.setCheckable(checkable)
        self.configSpaceLayout.addWidget(button)
        group.addButton(button)
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
        self.matrixItem3D = gl.GLSurfacePlotItem(
            x=None, y=None, z=None, colors=None, 
            shader='shaded', 
            smooth=False, 
            computeNormals=True, 
            glOptions='opaque', 
            drawFaces=True, drawEdges=False)
        
        self.matrixItem3D.setGLOptions('translucent')
        self.viewWidget3D.addItem(self.matrixItem3D)

        # COLOR BAR 
        self.colorbar = ColorBar()

        # STACK
        self.viewersLayout = QHBoxLayout()
        self.mainBoxLayout.addLayout(self.viewersLayout)
        self.viewersLayout.addWidget(self.ViewWidget2D)
        self.viewersLayout.addWidget(self.viewWidget3D)
        self.viewersLayout.addWidget(self.colorbar)


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




class ColorBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(100)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)

        # Define fundo preto no QWidget
        self.setStyleSheet("background-color: black; color: white;")

        # Cria a figura do matplotlib
        self.fig, self.ax = plt.subplots(figsize=(1, 4))
        self.fig.subplots_adjust(left=0.1, right=0.5)

        # Define fundo preto na figura e no eixo
        self.fig.patch.set_facecolor('black')
        self.ax.set_facecolor('black')

        # Cria o canvas para exibir no PyQt
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)

    def setColorMap(self, cmap, norm):
        """Atualiza a barra de cores dinamicamente."""
        self.ax.clear()  # limpa o eixo anterior

        # Define fundo preto novamente (clear apaga)
        self.ax.set_facecolor('black')

        # Cria a nova colorbar
        cb = self.fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), cax=self.ax)
        cb.ax.yaxis.set_tick_params(color='white')
        for label in cb.ax.get_yticklabels():
            label.set_color('white')

        # Redesenha o canvas
        self.canvas.draw()


QSS_COLOBAR = """


"""



 
QSS = """

#groupButton {
    border: ;

}


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
    background-color: transparent;
    font-size: 12px;
    color: white;
    min-width: 35px;
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






