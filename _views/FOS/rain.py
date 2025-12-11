from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from __DDCores.base import *

from PyQt5.QtWidgets import QWidget, QGridLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import MaxNLocator

from Filtros.FOS.rain import *

class RainView(DDWidget) :

    def __init__(self):
        super().__init__()
        

        self.mainBoxLayout = DDVBoxLayout()
        self.mainBox.setLayout(self.mainBoxLayout)
        self.tabs = QTabWidget()
        self.mainBoxLayout.addWidget(self.tabs)
        self._view()

        self.arquivo = None
        self.setStyleSheet(QSS)



    def _view(self) : 
        self.rainManual = RainManual()
        self.rainFile = RainFile()

        self.tabs.addTab(self.rainManual, 'Manual')
        self.tabs.addTab(self.rainFile, 'File')
        self.rainManual.sliderTempo.valueChanged.connect(self.atualizarTempo)







        

    def atualizarTempo(self, t) :
        self.rainManual.lineEditTempo.setText(f'{t}')

    def getPreciptacao(self) :
        return self.rainManual.spinBoxPreciptacao.value()

    def getTempo(self) :
        return self.rainManual.sliderTempo.value()





class RainManual(DDWidget) : 


    def __init__(self):
        super().__init__()


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
        self.layoutSliderTempo.addWidget(self.labelMinTempo, )
        self.layoutSliderTempo.addWidget(self.sliderTempo,  )
        self.layoutSliderTempo.addWidget(self.labelMaxTempo,  )

        self.mainBoxLayout.addWidget(self.labelTempo, 3, 0, 1, 2, alignment=Qt.AlignBottom)
        self.mainBoxLayout.addWidget(self.lineEditTempo, 4, 0, 1, 1,  alignment=Qt.AlignTop)
        self.mainBoxLayout.addLayout(self.layoutSliderTempo, 4, 1, 1, 1,  alignment=Qt.AlignTop)





class RainFile(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout principal
        self.layout = QVBoxLayout(self)

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

        # Armazena dados do arquivo
        self.period = []
        self.precipitation = []
        self.dict_rain = {}
        self.isOpen = False


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
        caminho, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar Arquivo",
            "",
            "Arquivos XLSX (*.xlsx);;Arquivos CSV (*.csv)"
        )
        if caminho:
            return caminho
        return None

    # BOTÃO → LER ARQUIVO → PROCESSAR → MOSTRAR HISTOGRAMA
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
        if caminho.endswith(".csv"):
            df = pd.read_csv(caminho)
        else:
            df = pd.read_excel(caminho)

        # Pega as duas colunas
        self.period = df.iloc[:, 0].to_list()
        self.precipitation = df.iloc[:, 1].to_list()
        self.dict_rain = dict(zip(self.period, self.precipitation))




    def calc_hw(self, p_mm, t_h, theta_i=0.3):
        # conversão
        p = p_mm / 1000.0  # mm/h -> m/h
        h = 3  # m

        # médium soil
        theta_r = 0.01
        theta_s = 0.392
        alpha = 2.49  # m^-1
        n = 1.1689
        m = 0.1445
        k_day = 0.12  # m/dia

        try:
            k = k_day / 24.0
            theta_e = (theta_i - theta_r) / (theta_s - theta_r)
            psi = ((1 - (theta_e ** (1 / m))) / ((alpha**n) * (theta_e ** (1 / m)))) ** (1 / n)
            a = abs(psi) * (theta_s - theta_i)

            tp = k * abs(psi) * (theta_s - theta_i) / (p * (p - k))
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
    def get_hw_list(self):
        lista_hw = []

        for t in self.period:
            p = self.dict_rain[t]
            hw = self.calc_hw(p, t, 0.3)
            lista_hw.append(hw)
        
        return lista_hw

    # Retorna o HW acumulado até certo período
    def get_total_hw(self, t_final):
        lista_hw = self.get_hw_list()

        if t_final > len(lista_hw):
            t_final = len(lista_hw)

        total = sum(lista_hw[:t_final])

        # Limites físicos
        if total < 0:
            total = 0
        if total > 3:  # limite de h = 3m
            total = 3
        
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



















