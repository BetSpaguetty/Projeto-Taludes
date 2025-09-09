from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.base import *
from Taludes.presets import *
from decimal import Decimal, getcontext
getcontext().prec = 10  

# BARRA DE FERRAMENTAS PRINCIPAL
class ToolsBar(QWidget) :

    def __init__(self):
        super().__init__()
        self.setFixedWidth(250)
        self.LAYOUT = QHBoxLayout()
        self.setLayout(self.LAYOUT)
        self.LAYOUT.setSpacing(0)
        self.LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.boxMain = QWidget()
        self.boxMainLayout = QVBoxLayout()
        self.boxMainLayout.setContentsMargins(5,5,5,5)
        self.boxMainLayout.setSpacing(5)
        self.boxMainLayout.setAlignment(Qt.AlignTop)
        self.boxMain.setLayout(self.boxMainLayout)
        self.boxMain.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.boxMain.setObjectName('boxMain')
        self.LAYOUT.addWidget(self.boxMain)

        self.setStyleSheet(QSS_TOOLSBAR)
    

    def putOnToolsBar(self, widget: QWidget) :
        self.boxMainLayout.addWidget(widget)
    

    def addBox(self, title) :
        box = OptionToolsBar(title)
        self.putOnToolsBar(box)
        return box

    def addButton(self, title) :
        box = QWidget()
        box.setObjectName('boxButtonToolsBar')
        boxLayout = QHBoxLayout()
        boxLayout.setSpacing(0)
        boxLayout.setContentsMargins(0,0,0,0)
        box.setLayout(boxLayout)
        button = QPushButton(title)
        button.setObjectName('buttonToolsBar')
        boxLayout.addWidget(button)
        button.setFixedHeight(32)
        button.setCursor(Qt.PointingHandCursor)

        self.putOnToolsBar(box)
        return button




class OptionToolsBar(QWidget) :

    def __init__(self, titulo:str):
        super().__init__()
        self.titulo = titulo
        self.LAYOUT = QVBoxLayout(self)
        self.LAYOUT.setSpacing(0)
        self.LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.LAYOUT)
        self.mainBox = QWidget()
        self.mainBox.setObjectName('option')
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.LAYOUT.addWidget(self.mainBox)

        self.icon_open   = QIcon("DDCores/icons/down-arrow_white.png")
        self.icon_closed = QIcon("DDCores/icons/right-arrow_white.png")
        self.botaoOpcao = QPushButton(f' {titulo}')
        self.botaoOpcao.setFixedHeight(32)
        self.botaoOpcao.setObjectName('boxOption')
        self.botaoOpcao.setCheckable(True)
        self.botaoOpcao.setChecked(False)
        self.botaoOpcao.setIcon(self.icon_closed)
        self.botaoOpcao.setIconSize(QSize(10, 10))

        # Área Oculta
        self.areaOculta = QWidget()
        self.areaOculta.setObjectName('hiddenArea')
        self.areaOcultaLayout = QVBoxLayout(self.areaOculta)
        self.areaOcultaLayout.setSpacing(5)
        self.areaOcultaLayout.setContentsMargins(10, 0, 10, 10)
        self.areaOculta.setVisible(False)
        self.mainBoxLayout.addWidget(self.botaoOpcao)
        self.mainBoxLayout.addWidget(self.areaOculta)
        self.botaoOpcao.setCursor(QCursor(Qt.PointingHandCursor))
        self.botaoOpcao.toggled.connect(self.toggle_icon)


    def click(self) :
        self.botaoOpcao.click()
        

    def toggle_icon(self, checked):
        if checked: 
            self.botaoOpcao.setIcon(self.icon_open)
            self.areaOculta.setVisible(True)
        else: 
            self.botaoOpcao.setIcon(self.icon_closed)
            self.areaOculta.setVisible(False)


    def putOnOcultArea(self, elemento) :
        self.areaOcultaLayout.addWidget(elemento)


    def addSubButton(self, title) :
        sub = SubButton(title)
        self.putOnOcultArea(sub)
        return sub

    def addSubWidget(self, widget) :
        self.putOnOcultArea(widget)
        return widget





class SubButton(QPushButton) :

    def __init__(self, titulo, descricao=None, icon=None) :
        super().__init__(titulo)
        layoutMain = QHBoxLayout()
        self.setObjectName('basicSubButton')
        self.setLayout(layoutMain)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        if icon :
            self.setIcon(icon)
        if descricao :
            layoutMain.addStretch()
            labelDescricao = QLabel(descricao)
            layoutMain.addWidget(labelDescricao)
            labelDescricao.setObjectName('subButtonLabel')


class SubEditor(DDWidget) :
    
    def __init__(self, title, min, max):
        super().__init__()
        #self.identificador = identificador
        self.realMin = min
        self.realMax = max
        self.internMin, self.internMax, self.multiplicador = encontrarMultiplicador(min, max)

        # Create main frame
        self.mainBoxLayout = QHBoxLayout()
        self.mainBoxLayout.setSpacing(5)
        self.mainBoxLayout.setContentsMargins(0,0,0,0)
        self.mainBox.setLayout(self.mainBoxLayout)

        # Label Lateral
        widgetLabel = QWidget()
        widgetLabel.setObjectName('widgetLabel')
        widgetLabel.setFixedWidth(50)
        layoutLabel = QHBoxLayout()
        layoutLabel.setSpacing(0)
        layoutLabel.setContentsMargins(0,0,0,0)
        widgetLabel.setLayout(layoutLabel)
        labelLateral = self.createLabelLateral(title)
        self.mainBoxLayout.addWidget(widgetLabel)
        layoutLabel.addWidget(labelLateral)

        # layout funcional
        layoutFuncional = self.createBasicVBoxLayout()
        self.mainBoxLayout.addLayout(layoutFuncional)

        # SpinBox layout
        spinBoxlayout = self.createBasicHBoxLayout()
        layoutFuncional.addLayout(spinBoxlayout)

        # Label min
        self.labelMin = self.createLabelMinMax(self.realMin)
        spinBoxlayout.addWidget(self.labelMin)

        # SpinBox 
        self.spinboxCoeficiente = self.createSpinBox()
        spinBoxlayout.addWidget(self.spinboxCoeficiente)

        # Label max
        self.labelMax = self.createLabelMinMax(self.realMax)
        spinBoxlayout.addWidget(self.labelMax)

        # Slider
        self.slider = self.createSlider(int(self.internMin), int(self.internMax))
        layoutFuncional.addWidget(self.slider)

        self.changeSlider()
        self.slider.valueChanged.connect(self.changeSlider)

        self.setStyleSheet(QSS)

    def changeSlider(self) :
        valor = self.getValue()
        self.spinboxCoeficiente.setValue(valor)

    def changeSpin(self, value) :
        pass
    

    def setMinMax(self, min, max) :
        self.realMin = min
        self.realMax = max
        self.internMin, self.internMax, self.multiplicador = encontrarMultiplicador(min, max)
        self.labelMin.setText(f'{self.realMin}')
        self.labelMax.setText(f'{self.realMax}')
        self.slider.setMinimum(self.internMin)
        self.slider.setMaximum(self.internMax)
        self.slider.setValue(int((self.internMin + self.internMax) / 2))


    def getValue(self) :
        return self.slider.value() / self.multiplicador
    

    def createSpinBox(self) :
        spinboxCoeficiente = QDoubleSpinBox()
        spinboxCoeficiente.setAlignment(Qt.AlignCenter)
        spinboxCoeficiente.setObjectName("spinboxCoeficiente")
        return spinboxCoeficiente

    def createSlider(self, min, max):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min)
        slider.setMaximum(max)
        slider.setValue(int((max + min) / 2))
        slider.setObjectName("sliderCoeficiente")
        return slider

    def createLabelLateral(self, texto):
        label = QLabel(texto)
        label.setAlignment(Qt.AlignCenter)
        label.setWordWrap(True)
        label.setObjectName("labelLateral")
        return label

    def createLabelMinMax(self, txt):
        label = QLabel(str(txt))
        label.setObjectName("labelMinMax")
        return label
    
    def createBasicHBoxLayout(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        return layout

    def createBasicVBoxLayout(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        return layout



def encontrarMultiplicador(num1, num2):
    # Ajusta a precisão (quanto maior, menos risco de erro)
    
    num1 = Decimal(str(num1))
    num2 = Decimal(str(num2))
    multiplicador = 1
    
    while not (num1 == num1.to_integral_value() and num2 == num2.to_integral_value()):
        num1 *= 10
        num2 *= 10
        multiplicador *= 10
    
    return int(num1), int(num2), multiplicador

# QSS ----------------------------------------------------------------------------------------------------------------------------------------------- >>>




QSS_TOOLSBAR = """

#option {
    background-color: #303030;
    border-radius: 5px;
}

#titleArea {
    background-color: #151515;

    }

#titleAreaLabel {
    padding: 15px 15px 15px 5px;
    font-size: 15px; 
    font-weight: 500;
    font-family: Segoe UI;

    color: white; 

    }

#boxMain {
    color: white;
    background-color: #202020 ;
    border-radius: 5px;

    }


#boxOption {
    background-color: #202020;
    color: white;
    text-align: left;
    font-size: 13px;
    font-family: verdana;
    font-weight: 400;
    border-radius: 4px;
    padding: 5px 10px 5px 10px;

    }
    

#boxOption:hover  {
    background-color: #303030;
    }

#boxOption:checked  {
    background-color: #303030;

    }
    
#subOption {

    }

#subButtonLabel {
    font-size: 15px;

    }


#hiddenArea {
    border-radius:  5px ; 
    }


    
#basicSubButton {
    width: 100%;
    height: 30px ;
    background-color: #707070 ;
    color: white;
    border: 0px solid black ;
    border-radius: 5px;
    }

#basicSubButton:hover {
    background-color: #909090 ;


    }

    
#boxButtonToolsBar {
    border-radius: 5px;
}

#buttonToolsBar {
    border-radius: 5px;
    background-color: #b0b0b0;

    color: black;


}
#buttonToolsBar:hover {
    background-color: #d0d0d0;


}


"""


QSS = f"""
QFrame#coefFrame {{
    background-color: #2b2b2b;
    color: #e0e0e0;
    border-radius: 2px;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
}}

QLabel#labelMinMax {{
    color : white;
    padding: 2px 4px;
    qproperty-alignment: AlignCenter;
}}

QLabel#labelLateral {{
    color: white;
    font-weight: bold;
    font-size: 13px;
    padding: 2px 4px;
    qproperty-alignment: AlignCenter;
    font-family: Segoe UI;
}}

#widgetLabel {{
    background-color: #454545;
    border-radius: 5px;



}}

QDoubleSpinBox#spinboxCoeficiente {{
    background-color: #3c3f41;
    border: 1px solid #5c5f61;
    border-radius: 4px;
    padding: 4px 6px;
    color: #ffffff;
    selection-background-color: transparent;
}}

QDoubleSpinBox#spinboxCoeficiente:focus {{
    border: 1px solid #007acc;
    background-color: #2f2f2f;
}}

QSlider#sliderCoeficiente::groove:horizontal {{
    height: 5px;
    background: #5a5a5a;
    border-radius: 3px;
}}

QSlider#sliderCoeficiente::handle:horizontal {{
    background: #007acc;
    border: 1px solid #007acc;
    width: 12px;
    height: 12px;
    margin: -4px 0;
    border-radius: 6px;
}}

QSlider#sliderCoeficiente::sub-page:horizontal {{
    background: #007acc;
    border-radius: 3px;
}}


"""
