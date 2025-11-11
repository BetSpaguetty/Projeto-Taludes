from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from __DDCores.base import *
from __DDCores.base import *
from Filtros.Taludes.presets import *




class ConfigurationMatrixViewer(DDWidget) : 


    def __init__(self):
        super().__init__()

        self._view()


    def _view(self) : 
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setContentsMargins(20,10,20,10)
        self.mainBoxLayout.setSpacing(10)
        self.mainBoxLayout.setAlignment(Qt.AlignTop)
        self.mainBox.setLayout(self.mainBoxLayout)

        self.dbShader = self.addDropBox('Shaders')
        self.btSmooth = self.addButton('Smooth')
        self.btDrawFaces = self.addButton('Draw Faces')
        self.btDrawEdges = self.addButton('Draw Edges')

        self.setStyleSheet(QSS)


    def addDropBox(self, title) -> QComboBox : 
        comboBox = QComboBox()
        labelTitle = QLabel(title)
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(5)
        layout.addWidget(labelTitle)
        layout.addWidget(comboBox)
        self.mainBoxLayout.addLayout(layout)
        return comboBox

    
    def addButton(self, title) -> QPushButton : 
        button = QPushButton()
        button.setText(title)
        button.setCheckable(True)
        button.setChecked(False)
        self.mainBoxLayout.addWidget(button)
        return button




QSS = """

#comboBoxConfig { 


}

#buttonConfig { 


}




"""


