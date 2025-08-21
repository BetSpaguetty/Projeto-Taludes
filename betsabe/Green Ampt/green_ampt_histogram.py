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

        self.line_edit_pre = self.findChild(QLineEdit,"line_edit_pre")
        self.line_edit_hw = self.findChild(QLineEdit,"line_edit_hw")
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
            self.figura.clear()       # limpa os eixos
            self.canvas.draw()
            self.info_graph()
            self.create_graph()
            self.line_edit_pre.setEnabled(False)
            self.slider_period.setEnabled(True)
            # self.slider_precipitation.setEnabled(True)
            self.label_file_name.setText(f" File: {self.file}")
            print(self.file)
        return
    
    def info_graph(self):
        df = pd.read_excel(self.file) # Ler o arquivo Excel
        self.precipitation = df.iloc[:,1] # Pega todas as linhas ":" da coluna 1
        self.period = df.iloc[:,0] # Pega todas as linhas ":" da coluna 0

        self.slider_period.setRange(min(self.period), max(self.period))
        return
    
    # Ao mudar o valor da precipitação, muda automaticamente o período
    def change_period(self):
        if self.line_edit_pre.isEnabled() == False:
            dicionary_period_precipitation = dict(zip(self.period, self.precipitation))
            value = dicionary_period_precipitation[self.slider_period.value()]
            self.line_edit_pre.setText(str(value))
        else:
            self.slider_period.setRange(0,48)
        return
    
    # Permite que o usuário insira ao invés de utilizar informações do gráfico
    def insert_mode(self):
        self.line_edit_pre.setEnabled(True)
        if self.figura:
            self.label_file_name.setText(f" File: ")
            self.figura.clear()       # limpa os eixos
            self.canvas.draw()    # redesenha o canvas vazio

        return

    # Cria o gráfico (histograma)
    def create_graph(self):
        histogram = self.figura.add_subplot(111)
        self.figura.subplots_adjust(left=0.2, bottom=0.2)
        histogram.bar(self.period, self.precipitation, color='blue', edgecolor='black')
        histogram.set_ylabel('precipitation (mm)', fontsize=9)
        histogram.set_xlabel('time (h)', fontsize=9)
        histogram.tick_params(labelsize=9)
        histogram.xaxis.set_major_locator(MaxNLocator(nbins=10))
        histogram.yaxis.set_major_locator(MaxNLocator(nbins=10))

        self.canvas.draw()
        return
    
    # Faz o cálculo do hw 
    def rain_infiltration(self):
        p = float(self.line_edit_pre.text()) # h
        p = p/1000 # mm/h -> m/h
        t = float(self.slider_period.value()) # h

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
        # if p == 0:
        #     self.line_edit_hw.setText(f'{0:.7f}')
        # else:
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
            self.line_edit_hw.setText(f'{0:.7f}erro')
            # erro

            # Quando o hw for menor que 0, o hw sera o último positivo
        return
    
    # Cria uma lista de hws daquele arquivo específico, com a intenção de identificar o último hw positivo.
    def lista_hw(self):
        
        return

app = QApplication(argv)
UIWindow = Popup_histogram()
exit(app.exec_())