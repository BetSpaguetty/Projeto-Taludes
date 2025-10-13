from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.base import *



class RainView(DDWidget) :

    def __init__(self):
        super().__init__()
        
        self._view()
        self.setStyleSheet(QSS)


    def _view(self) :
        self.mainBoxLayout = QGridLayout()
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBox.setObjectName('rain')

        # HW ================ >>
        self.labelHW = QLabel('HW')
        self.labelHW.setObjectName('HWLabel')
        self.lineEditHW = QLineEdit()
        self.lineEditHW.setReadOnly(True)
        self.lineEditHW.setAlignment(Qt.AlignCenter)
        self.lineEditHW.setObjectName('HWLineEdit')
        self.lineEditHW.setFixedWidth(80)
        self.layoutHW = QHBoxLayout()
        self.layoutHW.addStretch()
        self.layoutHW.addWidget(self.labelHW)
        self.layoutHW.addWidget(self.lineEditHW)
        self.layoutHW.addStretch()
        self.mainBoxLayout.addLayout(self.layoutHW, 0, 0, 1, 2 , alignment=Qt.AlignCenter)


        # Preciptação ======= >>
        self.labelPreciptacao = QLabel('Preciptação')
        self.spinBoxPreciptacao = QSpinBox()
        self.spinBoxPreciptacao.setMinimum(0)
        self.spinBoxPreciptacao.setMaximum(500)
        self.spinBoxPreciptacao.setValue(100)
        self.spinBoxPreciptacao.setObjectName('PLineEdit')
        self.mainBoxLayout.addWidget(self.labelPreciptacao, 1, 0, 1, 2, alignment=Qt.AlignBottom)
        self.mainBoxLayout.addWidget(self.spinBoxPreciptacao, 2, 0, 1, 2, alignment=Qt.AlignLeft)

        # Tempo ============= >>
        self.labelTempo = QLabel("Tempo (h)")
        self.lineEditTempo = QLineEdit()
        self.lineEditTempo.setText('0')
        self.lineEditTempo.setReadOnly(True)
        self.lineEditTempo.setObjectName('TempoLineEdit')
        self.lineEditTempo.setFixedWidth(80)

        self.layoutSliderTempo = QHBoxLayout()
        self.labelMinTempo = QLabel('0')
        self.labelMaxTempo = QLabel('48')
        self.sliderTempo = QSlider(Qt.Horizontal)
        self.sliderTempo.setMinimum(0)
        self.sliderTempo.setMaximum(48)
        self.sliderTempo.setTickInterval(1)
        self.sliderTempo.setValue(0)
        self.sliderTempo.valueChanged.connect(self.atualizarTempo)
        self.layoutSliderTempo.addWidget(self.labelMinTempo, )
        self.layoutSliderTempo.addWidget(self.sliderTempo,  )
        self.layoutSliderTempo.addWidget(self.labelMaxTempo,  )


        self.mainBoxLayout.addWidget(self.labelTempo, 3, 0, 1, 2, alignment=Qt.AlignBottom)
        self.mainBoxLayout.addWidget(self.lineEditTempo, 4, 0, 1, 1,  alignment=Qt.AlignTop)
        self.mainBoxLayout.addLayout(self.layoutSliderTempo, 4, 1, 1, 1,  alignment=Qt.AlignTop)
        

    def atualizarTempo(self, t) :
        self.lineEditTempo.setText(f'{t}')

    def getPreciptacao(self) :
        return self.spinBoxPreciptacao.value()

    def getTempo(self) :
        return self.sliderTempo.value()


QSS = """


QLabel {
    color: white;
    font-size: 14px;

}
QLineEdit {
    border-radius: 5px;
    border: 1px solid black;
    padding: 4px;
    text-align: center;

}

#TempoLineEdit {
    border-radius: 5px;
    border: 1px solid black;
    background-color: #d1d1d1;
    padding: 4px;
    text-align: center;

}

#rain {
    border: 1px solid #606060;
    border-radius: 5px;
}


#labelMaterial {

    color: white;

}



#HWLabel {
    color: white;
    font-size: 16px;
    font-weight: 400;

}

#HWLineEdit {
    text-align: center;
    border-radius: 5px;
    border: 2px solid #055796;
    background-color: #d1d1d1;

    padding: 6px;

}



"""

