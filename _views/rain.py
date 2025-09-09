from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.base import *



class RainView(DDWidget) :

    def __init__(self):
        super().__init__()
        self.setFixedHeight(300)
        self.mainBox.setObjectName('rain')
        self.mainBoxLayout = QVBoxLayout()
        self.mainBox.setLayout(self.mainBoxLayout)
        self._elements()
        self.setStyleSheet(QSS)



    def _elements(self) :
        self.title = QLabel('Rain')
        self.title.setObjectName('labelMaterial')
        self.mainBoxLayout.addWidget(self.title, alignment=Qt.AlignCenter)
        self.editP = self.addEditor('P(cm/h) preciptação: ')
        self.editT = self.addEditor('t(h) tempo: ')
        self.editH = self.addEditor('hw(m) profundidade:  ')


        

    def addEditor(self, title, readOnly=False) -> QLineEdit :
        box = QWidget()
        layout = QHBoxLayout()
        box.setLayout(layout)
        label = QLabel(title)
        label.setObjectName('labelMaterial')
        lineEdit = QLineEdit()
        lineEdit.setObjectName('lineEditMaterial')
        lineEdit.setReadOnly(readOnly)
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(lineEdit)
        self.mainBoxLayout.addWidget(box)
        return lineEdit
 







QSS = """


#rain {
    border: 1px solid #606060;
    border-radius: 5px;
}


#labelMaterial {

    color: white;

}






"""
