from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QSlider, QLineEdit,QLabel, QGridLayout, QFileDialog
from sys import argv, exit, path
from math import *

from matplotlib.backends.backend_qt5agg  import FigureCanvasQTAgg as FigureCanvas
from matplotlib.ticker import MaxNLocator
from matplotlib.figure import Figure

import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class Popup_histogram(QDialog): 
    def __init__(self):
        super().__init__()
        uic.loadUi("histogram.ui", self)

        self.line_edit_hw = self.findChild(QLineEdit,"line_edit_hw")
        self.slider_precipitation = self.findChild(QSlider,"slider_precipitation")
        self.slider_period = self.findChild(QSlider,"slider_period")
        self.label_file_name = self.findChild(QLabel,"label_file_name")
        self.layout_histogram = self.findChild(QGridLayout,"layout_histogram")

        # Adicionar o canvas ao layout
        self.figura = Figure()
        self.canvas = FigureCanvas(self.figura)
        self.layout_histogram.addWidget(self.canvas)

        self.show()

    def show_error_popup(self, error_message):
        # Cria a caixa de mensagem de erro
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)  # Define o ícone como erro
        msg.setWindowTitle("Erro")  # Define o título da janela
        msg.setText(error_message)  # Define o texto da mensagem
        msg.setStandardButtons(QMessageBox.Ok)  # Adiciona o botão OK
        msg.exec_()  # Exibe a mensagem

    def read_file(self):
        self.file, filtro = QFileDialog.getOpenFileName(None, "Selecione um arquivo", "", "Arquivos XLSX (*.xlsx);;Arquivos CSV (*.csv)")
        if self.file == "":
            self.show_error_popup("Arquivo não selecionado.")
            print(self.file)
        else:
            self.create_graph()
            self.info_graph()
            self.slider_period.setEnabled(True)
            self.slider_precipitation.setEnabled(True)
            self.label_file_name.setText(f" File: {self.file}")
            print(self.file)
        return
    
    def info_graph(self):
        df = pd.read_excel(self.file) # Ler o arquivo Excel
        precipitation = df['precipitacao (mm)']
        period = df['tempo (h)']

        self.slider_precipitation.setRange(min(precipitation),max(precipitation))
        self.slider_period.setRange(min(period), max(period))
        return
    
    def create_graph(self):
        df = pd.read_excel(self.file) # Ler o arquivo Excel
        precipitation = df['precipitacao (mm)']
        period = df['tempo (h)']

        histogram = self.figura.add_subplot(111)
        self.figura.subplots_adjust(left=0.2, bottom=0.2)
        histogram.bar(period, precipitation, color='blue', edgecolor='black')
        histogram.set_ylabel('precipitation (mm)', fontsize=9)
        histogram.set_xlabel('time (h)', fontsize=9)
        histogram.tick_params(labelsize=9)
        histogram.xaxis.set_major_locator(MaxNLocator(nbins=10))
        histogram.yaxis.set_major_locator(MaxNLocator(nbins=10))

        self.canvas.draw()
        return
    
    def rain_infiltration(self):
        p = int(self.slider_precipitation.value()) # h
        p = p/1000 # mm/h -> m/h
        t = int(self.slider_period.value()) # h

        # variáveis obtidas da função runAnalysis
        theta_i = 0.3
        h = 3
        # médium
        theta_r = 0.01
        theta_s = 0.392
        alpha = 2.49 # m^(-1)
        n = 1.1689
        m = 0.1445
        k_day = 0.12 # m/dia

        # Cálculos
        if p == 0:
            self.line_edit_hw.setText(f'{0:.7f}')
        else:
            try:
                # cálculos com essas variáveis
                k = k_day/24 # m/h
                theta_e = (theta_i-theta_r)/(theta_s-theta_r)
                psi = ((1 - (theta_e**(1/m)))/((alpha**n)*(theta_e**(1/m))))**(1/n)
                a = abs(psi) * (theta_s - theta_i)
                tp = k*abs(psi)*(theta_s-theta_i)/(p*(p-k))
                hwp = p*tp # m
                hw0 = k*(t-tp) + hwp
                hw = hw0 + a*log((hw0 + a)/(hwp + a))*((hw0 + a)/hw0)

                # Possibilidades
                if isnan(hw): # se hw não tiver valor
                    hw = 0
                elif hw<0: # se hw for negativo
                    hw = 0
                elif hw>h: # se hw for maior que o h
                    hw = h
                self.line_edit_hw.setText(f'{hw:.7f}')
            except (ZeroDivisionError, ValueError) as e:
                self.line_edit_hw.setText(f'{0:.7f}')
        return

app = QApplication(argv)
UIWindow = Popup_histogram()
exit(app.exec_())