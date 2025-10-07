from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

from _views.ambienteView import *
from DDCores.base import *




class Workspace(DDWidget) :

    def __init__(self, ):
        super().__init__()
        self._configuration()

    def _configuration(self) :
        self.setObjectName('workspace')
        self.tabBox = QTabWidget()
        self.tabBox.setObjectName('tabBox')
        self.mainBoxLayout = QHBoxLayout()
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setContentsMargins(0,0,0,0)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBoxLayout.addWidget(self.tabBox)


        self.setStyleSheet(QSS_WORKSPACE)


    def addAmbient(self, ambient, name = 'Ambiente') :
        self.tabBox.addTab(ambient, name)











QSS_WORKSPACE = """
#workspace {
    background-color: pink ; 

}

#tabBox::pane {
    background-color: #101010 ; 

    }



QTabWidget::pane {
    border: 0px solid #404040;
    background: #f0f0f0;
}

QTabBar::tab {
    background: #404040;
    height: 20px;
    width: 80px;
    color: white;
    padding: 6px 12px;
    margin-right: 1px;
}

QTabBar::tab:selected {
    background: #101010 ;
    color: white;
}

QTabBar::tab:hover {
    background: #151515;

}




"""



