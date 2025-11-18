from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from __DDCores.base  import *





class BasicSlider(DDWidget) : 

    def __init__(self, name:str, min:int, max:int):
        super().__init__()
        self.name = name 
        self.min = min 
        self.max = max 
        self.view()


    def view(self) : 
        # Elements
        self.labelname = QLabel(self.name)
        self.labelMin = QLabel(str(self.min))
        self.labelMax = QLabel(str(self.max))
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(self.min)
        self.slider.setMaximum(self.max)
        self.slider.setSizePolicy(self.slider.sizePolicy().Expanding, self.slider.sizePolicy().Fixed)
        self.visor = QLineEdit()
        self.visor.setReadOnly(True)
        self.slider.valueChanged.connect(lambda v: self.visor.setText(str(v)))
        self.slider.setValue(50)

        # Layout
        self.mainBoxLayout = DDVBoxLayout()
        self.mainBox.setLayout(self.mainBoxLayout)

        # Up Layout
        upLayout = DDHBoxLayout(5, (5, 0, 5, 0))
        self.mainBoxLayout.addLayout(upLayout)
        upLayout.addWidget(self.labelname)
        upLayout.addStretch()
        upLayout.addWidget(self.visor)

        # Bottom Layout
        btLayout = DDHBoxLayout(5, (5, 0, 5, 0))
        self.mainBoxLayout.addLayout(btLayout)
        btLayout.addWidget(self.labelMin)
        btLayout.addWidget(self.slider)
        btLayout.addWidget(self.labelMax)

        self.setFixedHeight(60)
        self.setStyleSheet(QSS_BASIC_SLIDER)


    def getValue(self) : 
        return self.slider.value()







QSS_BASIC_SLIDER = """

QLabel {

    color: white; 
    font-size: 13px;

}








"""







