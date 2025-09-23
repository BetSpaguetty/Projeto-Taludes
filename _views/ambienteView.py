from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.base import *
from _views.toolsbar import ToolsBar
from _views.map  import MapView
from _views.rain import RainView
from _views.soil import SoilView

class AmbienteView(DDWidget) :

    def __init__(self):
        super().__init__()
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setSpacing(10)
        self.mainBoxLayout.setContentsMargins(10,10,10,10)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBox.setObjectName('ambiente')

        # HEADER -------------------------------- >>>

        self.header = AmbienteHeader()
        self.mainBoxLayout.addWidget(self.header)

        # CORPO --------------------------------- >>>
        corpo = QWidget()
        corpoLayout = QHBoxLayout()
        corpoLayout.setSpacing(10)
        corpoLayout.setContentsMargins(0,0,0,0)
        corpo.setLayout(corpoLayout)
        self.mainBoxLayout.addWidget(corpo)

        # TOOLSBAR ------------------------------ >>>
        self.toolsbar = ToolsBar()
        corpoLayout.addWidget(self.toolsbar)

        # MAP ----------------------------------- >>>
        self.map = MapView()
        corpoLayout.addWidget(self.map, stretch=1)

        # VIEWS --------------------------------- >>>
        self.componentsSpace = AmbienteComponentsSpace()
        corpoLayout.addWidget(self.componentsSpace)

        self.setStyleSheet(QSS)
        self._upElements()    


    def _upElements(self) :
        self.soil = self.componentsSpace.soil
        self.rain = self.componentsSpace.rain
    



class AmbienteHeader(DDWidget) :

    def __init__(self, title='unk map'):
        super().__init__()
        self.mainBox.setObjectName('header')
        self.setFixedHeight(80) 

        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setContentsMargins(5,0,5,0)
        self.mainBoxLayout.setSpacing(0)
        self.mainBox.setLayout(self.mainBoxLayout)


        # SUPERIOR ------------------------------ >>>
        self.boxSuperior = QWidget()
        self.boxSuperior.setObjectName('bSuperior')
        self.boxSuperior.setFixedHeight(40)
        self.boxSuperiorLayout = QHBoxLayout()
        self.boxSuperiorLayout.setSpacing(10)
        self.boxSuperiorLayout.setContentsMargins(10,5,10,5)
        self.boxSuperiorLayout.setAlignment(Qt.AlignLeft)
        self.boxSuperior.setLayout(self.boxSuperiorLayout)
        self.mainBoxLayout.addWidget(self.boxSuperior)

        
        # INFERIOR ------------------------------ >>>
        self.boxInferior = QWidget()
        self.boxInferior.setObjectName('bInferior')
        self.boxInferiorLayout = QHBoxLayout()
        self.boxInferiorLayout.setSpacing(10)
        self.boxInferiorLayout.setContentsMargins(5,5,10,5)
        self.boxInferiorLayout.setAlignment(Qt.AlignLeft)
        self.boxInferior.setLayout(self.boxInferiorLayout)
        self.mainBoxLayout.addWidget(self.boxInferior, stretch=1)


        self.labelTitle = self.addTitle(title)
        self.labelType  = self.addInformation('Tipo: ')
        self.labelDimensions = self.addInformation('Dimensões: ')
         

        self.boxSuperiorLayout.addStretch()
        self.closeButton = QLabel('X')
        self.closeButton.setObjectName('closeButton')
        self.boxSuperiorLayout.addWidget(self.closeButton)

       

    def addInformation(self, title) :
        labelInfo = QLabel(title)
        labelInfo.setObjectName('labelInfo')
        self.boxSuperiorLayout.addWidget(labelInfo)
        self.boxSuperiorLayout.addWidget(VerticalLine("#404040"))
        return labelInfo

    def addTitle(self, title) :
        labelTitle = QLabel(title)
        labelTitle.setObjectName('labelTitle')
        self.boxSuperiorLayout.addWidget(labelTitle)
        self.boxSuperiorLayout.addWidget(VerticalLine("#606060"))
        return labelTitle
        

    def addButton(self, title) -> QPushButton:
        button = QPushButton(title)
        button.setObjectName('buttonHeader')
        self.boxInferiorLayout.addWidget(button)
        return button



class AmbienteComponentsSpace(DDWidget) :

    def __init__(self):
        super().__init__()
        self.mainBox.setObjectName('componentsSpace')
        self.setFixedWidth(300)
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setAlignment(Qt.AlignTop)
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setContentsMargins(0,0,0,0)
        self.mainBox.setLayout(self.mainBoxLayout)

        self.scrollArea = QScrollArea()
        self.scrollArea.setObjectName('scroll')
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mainBoxLayout.addWidget(self.scrollArea)

        self.scrollWidget = QWidget()
        self.scrollWidget.setObjectName('scrollWidget')

        self.scrollLayout = QVBoxLayout()
        self.scrollLayout.setAlignment(Qt.AlignTop)
        self.scrollLayout.setSpacing(10)
        self.scrollLayout.setContentsMargins(5,5,5,5)
        self.scrollWidget.setLayout(self.scrollLayout)

        self.scrollArea.setWidget(self.scrollWidget)

        # Triangulo 
        self.soil = SoilView()
        self.scrollLayout.addWidget(self.soil)

        # Chuva
        self.rain = RainView()
        self.scrollLayout.addWidget(self.rain)

        self.setStyleSheet(SCROLL_QSS)

 


SCROLL_QSS = """
QScrollArea {
    background-color: transparent;
    border: none;
}

QScrollBar:vertical {
    background: #202020;
    width: 0px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: #303030;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background: #404040;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
    background: none;
    border: none;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: none;
}

#scrollWidget {

    background-color: transparent;
}

#scroll {
    background-color: transparent;

}

"""


QSS = """

#ambiente {

    }


#header {
    border-radius: 5px;
    background-color: #202020;

}

#bSuperior {
    border-bottom: 1px solid #606060;

}

#labelTitle {
    font-size: 15px;
    color: white;
    font-weight: 500;
    font-family: Segoe UI;

}


#bInferior {

}

#labelInfo {
    color: #909090;

}

#buttonHeader {
    border-radius: 5px;
    background-color: #404040;
    color: white;
    width: 80px;
    height: 25px;

}


#componentsSpace {
    background-color: #202020;
    border-radius: 5px;

}

#closeButton {
    color: #e65550;
    font-size: 14px;
    font-weight: 500;

}

"""





