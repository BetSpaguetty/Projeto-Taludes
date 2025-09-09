from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.windowBars import *

 
class CoresWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        self._base()
        self._topBar()
        self._central()
  
    def _base(self) : 
        self.setWindowTitle("CORES")
        self.setMinimumSize(500, 500)
        self.resize(1200, 600)
        self.widgetCentral = QWidget()
        self.setCentralWidget(self.widgetCentral)
        self.layoutCentral = QVBoxLayout()
        self.layoutCentral.setSpacing(0)
        self.layoutCentral.setContentsMargins(0, 0, 0, 0)
        self.widgetCentral.setLayout(self.layoutCentral)
        self.setStyleSheet(QSS_MAIN_WINDOW)

 
    def _topBar(self) :
        self.topBar = HorizontalBar()
        self.layoutCentral.addWidget(self.topBar)

    
    def _central(self) :
        self.horizontalLayout = QHBoxLayout()
        self.layoutCentral.addLayout(self.horizontalLayout)

        self.leftBar = VerticalBar()
        self.mainSpace = QWidget()
        self.mainSpace.setObjectName('mainSpace')

        self.horizontalLayout.addWidget(self.leftBar)
        self.horizontalLayout.addWidget(self.mainSpace)

        



QSS_MAIN_WINDOW = """

QMainWindow { 
    background-color: black;  
    border: 1px solid transparent; 
    } 



#mainSpace {
    background-color: #202020;
}


"""




