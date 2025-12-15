from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from __DDCores.base import *
from Filtros.FOS.taludes import *
from Filtros.FOS.presets import *
from Filtros.FOS.types import *
from PyQt5.QtWidgets import QWidget, QGridLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import MaxNLocator
from _views.Componentes.sliders import *
from Filtros.FOS.rain import *

class RainView(DDWidget) :

    def __init__(self):
        super().__init__()
        self.mainBoxLayout = DDVBoxLayout()
        self.mainBox.setLayout(self.mainBoxLayout)
        self.tabWidget = QTabWidget()
        self.mainBoxLayout.addWidget(self.tabWidget)
        self._UI()


        self.arquivo = None
        self.callbackfunction = None
        self.pagetab = 0
        self.setStyleSheet(QSS)

    def _UI(self) : 
        self.rainManual = RainManual()
        self.rainFile   = RainFile()
        self.tabWidget.addTab(self.rainManual, 'Manual')
        self.tabWidget.addTab(self.rainFile, 'File')
        self.tabWidget.currentChanged.connect(self.changeTab)



    def onChange(self, function) : 
        self.callbackfunction = function
        self.rainFile.callbackfunction = function
        self.rainManual.callbackfunction = function

    

    def changeTab(self, index) : 
        self.pagetab = index
        if self.callbackfunction : self.callbackfunction()

    



class RainManual(DDWidget) : 


    def __init__(self):
        super().__init__()
        self.callbackfunction = None

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

     
        self.sliderTempo = BasicSlider('Tempo', 1, 48)
        
        self.sliderTempo.slider.valueChanged.connect(self.updateTempo)

        self.mainBoxLayout.addWidget(self.sliderTempo, 4, 1, 1, 1,  alignment=Qt.AlignTop)


    def updateTempo(self) : 
        if self.callbackfunction : self.callbackfunction()


    def getHW(self, h:float, thetai:float, solo:Soils) :
        p = self.getPreciptacao()
        t = self.getTempo()
        hw = Taludes.calculateHW(p, t, thetai, h, solo)
        self.lineEditHW.setText(f'{hw:.3f}')
        return hw


    def getPreciptacao(self) :
        return self.spinBoxPreciptacao.value()

    def getTempo(self) :
        return self.sliderTempo.getValue()



class RainFile(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.callbackfunction = None
        # Layout principal
        self.layout = QVBoxLayout(self)



        self.lineEditHW = QLineEdit()
        self.lineEditHW.setReadOnly(True)
        self.lineEditHW.setAlignment(Qt.AlignCenter)
        self.lineEditHW.setObjectName('HWLineEdit')
        self.lineEditHW.setFixedWidth(80)
        self.layout.addWidget(self.lineEditHW)


        # Botão para abrir arquivo
        self.button_open = QPushButton("Selecionar Arquivo de Chuva")
        self.button_open.clicked.connect(self.on_open_file)
        self.layout.addWidget(self.button_open)

        self.button_send = QPushButton("Enviar")
        self.layout.addWidget(self.button_send)

        # Área do gráfico
        self.graph_layout = QGridLayout()
        self.layout.addLayout(self.graph_layout)

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.graph_layout.addWidget(self.canvas)

        self.sliderTempo = BasicSlider('Tempo', 1, 48)
        self.layout.addWidget(self.sliderTempo)
        self.sliderTempo.slider.valueChanged.connect(self.updateTempo)

        # Armazena dados do arquivo
        self.period = []
        self.precipitation = []
        self.dict_rain = {}
        self.isOpen = False


    def updateTempo(self) : 
        if self.callbackfunction : self.callbackfunction()


    # FUNÇÃO PARA ATUALIZAR GRÁFICO
    def update_graph(self, period, precipitation):
        self.fig.clear()
        ax = self.fig.add_subplot(111)

        ax.bar(period, precipitation, edgecolor="black")
        ax.set_xlabel("Time (h)")
        ax.set_ylabel("Precipitation (mm)")
        ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=10))

        self.canvas.draw()

    # SELECIONA O ARQUIVO
    def getFileRain(self):
        caminho, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo", "", "Arquivos XLSX (*.xlsx);;Arquivos CSV (*.csv)" )
        if caminho: return caminho
        return None

    # BOTÃO -> LER ARQUIVO → PROCESSAR → MOSTRAR HISTOGRAMA
    def on_open_file(self):
        caminho = self.getFileRain()
        if not caminho:
            return  
        self.isOpen = True
        self.read_rain_file(caminho)
        self.update_graph(self.period, self.precipitation)

    # LEITURA DO ARQUIVO + TRANSFORMAÇÃO
    def read_rain_file(self, caminho):
        # Lê XLSX ou CSV
        if caminho.endswith(".csv"): df = pd.read_csv(caminho)
        else : df = pd.read_excel(caminho)

        # Pega as duas colunas
        self.period = df.iloc[:, 0].to_list()
        self.precipitation = df.iloc[:, 1].to_list()
        self.dict_rain = dict(zip(self.period, self.precipitation))




    def calc_hw(self, p_mm, t_h, h, theta_i, solo:Soils) :
        # conversão
        p = p_mm / 1000.0  # mm/h -> m/h

        SOIL = SOIL_MATERIALS[solo]
        thetaR = SOIL.THETA_R
        thetaS = SOIL.THETA_S
        alpha = SOIL.VG_ALPHA
        n = SOIL.VG_N
        m = SOIL.VG_M
        kDay = SOIL.VG_K

        try:
            k = kDay / 24.0
            theta_e = (theta_i - thetaR) / (thetaS - thetaR)
            psi = ((1 - (theta_e ** (1 / m))) / ((alpha**n) * (theta_e ** (1 / m)))) ** (1 / n)
            a = abs(psi) * (thetaS - theta_i)

            tp = k * abs(psi) * (thetaS - theta_i) / (p * (p - k))
            hwp = p * tp
            hw0 = k * (t_h - tp) + hwp

            hw = hw0 + a * log((hw0 + a) / (hwp + a)) * ((hw0 + a) / hw0)

            if isnan(hw) or hw < 0:
                return 0
            if hw > h:
                return h
        except:
            return 0
        
        return hw

    # Retorna lista de HW para todos os períodos do arquivo
    def get_hw_list(self, h, thetai, solo):
        lista_hw = []
        for t in self.period:
            p = self.dict_rain[t]
            hw = self.calc_hw(p, t, h, thetai, solo)
            lista_hw.append(hw)
        
        return lista_hw

    # Retorna o HW acumulado até certo período
    def get_total_hw(self, h, thetai, solo):

        t_final = self.sliderTempo.getValue()

        lista_hw = self.get_hw_list(h, thetai, solo)

        if t_final > len(lista_hw) : t_final = len(lista_hw)
        total = sum(lista_hw[:t_final])

        if total < 0: total = 0
        if total > h: total = h
        
        return total







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




#tabBox::pane {
    background-color: #202020 ; 

    }



QTabWidget::pane {
    border: 0px solid #404040;
    background:black;
}

QTabBar::tab {
    background: #101010;
    height: 20px;
    width: 80px;
    color: white;
    padding: 6px 12px;
    margin-right: 1px;
}

QTabBar::tab:selected {
    background: #202020 ;
    color: white;
}

QTabBar::tab:hover {
    background: #151515;

}




"""



















