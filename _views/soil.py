from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.base import *



class SoilView(DDWidget) :

    def __init__(self):
        super().__init__()
        self.setFixedHeight(300)
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setContentsMargins(2,2,2,2)
        self.mainBoxLayout.setSpacing(5)
        self.mainBoxLayout.setAlignment(Qt.AlignTop)
        self.mainBox.setObjectName('soil')
        self.mainBox.setLayout(self.mainBoxLayout)

        self._base()
        self.logic()
        self.setStyleSheet(QSS)

 
    def _base(self) :
        self.labelTitle = QLabel('Soil')
        self.labelTitle.setObjectName('labelTitle')
        self.mainBoxLayout.addWidget(self.labelTitle, alignment=Qt.AlignCenter)
        self.spinsLayout = QHBoxLayout()
        self.spinsLayout.setContentsMargins(0,0,0,0)
        self.spinsLayout.setSpacing(0)
        self.mainBoxLayout.addLayout(self.spinsLayout)
        self.editClay = self.addSpin('Clay')
        self.editSand = self.addSpin('Sand')
        self.editSilt = self.addSpin('Silt', readOnly=True)
      
        self.labelSoil = QLineEdit()
        self.labelSoil.setReadOnly(True)
        self.labelSoil.setObjectName('lineSoil')
        self.labelSoil.setAlignment(Qt.AlignCenter)
        self.mainBoxLayout.addWidget(self.labelSoil, alignment=Qt.AlignHCenter)


    def addSpin(self, title, readOnly=False) -> QSpinBox :
        box = QWidget()
        layout = QVBoxLayout()
        box.setLayout(layout)
        label = QLabel(title)
        label.setObjectName('labelSoil')
        spinBox = QSpinBox()
        spinBox.lineEdit().setReadOnly(readOnly)
        spinBox.setMinimum(0)
        spinBox.setMaximum(100)
        spinBox.setObjectName('spinSoil')
        spinBox.setMinimumWidth(50)
        spinBox.setReadOnly(readOnly)
        layout.addWidget(label)
        layout.addWidget(spinBox)
        self.spinsLayout.addWidget(box)
        return spinBox
    

    def getSilt(self) : return self.editSilt.value()
    def getSand(self) : return self.editSand.value()
    def getClay(self) : return self.editClay.value()


    def logic(self) :
        self.editClay.valueChanged.connect( lambda : self.update('CLAY'))
        self.editSand.valueChanged.connect( lambda : self.update('SAND'))

    # premissa : o minimo e maximo valores dos spins são 0 e 100
    def update(self, editor) :
        self.editClay.blockSignals(True)
        self.editSand.blockSignals(True)
        self.editSilt.blockSignals(True)
        if editor == 'CLAY' : 
            second = self.editSand
        if editor == 'SAND' : 
            second = self.editClay
        total = self.editClay.value() + self.editSand.value() + self.editSilt.value()
        sobra = total - 100
        silt = self.editSilt.value()
        silt += sobra * -1        
        soil = second.value()
        if silt < 0 :
            soil += silt 
            silt = 0
        if silt > 100 :
            soil += (silt - 100) * -1
            silt = 100
        second.setValue(soil)
        self.editSilt.setValue(silt)
        self.editClay.blockSignals(False)
        self.editSand.blockSignals(False)
        self.editSilt.blockSignals(False)







QSS = """


#soil {
    border: 1px solid #606060;
    border-radius: 5px;

}


#labelMaterial {
    color: white;

}

#lineEditMaterial {

}

QSpinBox {
    selection-background-color: #808080;
    }



QSpinBox:focus {
    border: 1px solid #007acc;
    background-color: black;
    color: white;
    }


#labelSoil {
    color:white;

}

#lineSoil {
    height: 20px;
    text-align: center;
    font-size: 14px;
    font-weight: 500;
    border-radius: 10px;
    padding: 5px;

}

"""
