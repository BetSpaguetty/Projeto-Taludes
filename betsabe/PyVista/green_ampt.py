from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QSlider, QLineEdit,QLabel, QGraphicsView, QGraphicsScene
from sys import argv, exit, path
from math import *

from matplotlib.backends.backend_qt5agg  import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

# funcao de green ampt 
class Popup_rain(QDialog): 
    def __init__(self):
        super().__init__()
        uic.loadUi("Projeto-Taludes\\betsabe\\PyVista\\rain.ui", self)
        
        self.slider_hours = self.findChild(QSlider,"slider_hours")
        self.line_edit_hw = self.findChild(QLineEdit,"line_edit_hw")
        self.line_edit_precipitation = self.findChild(QLineEdit,"line_edit_precipitation")
        self.label_time = self.findChild(QLabel,"label_time")
        
        self.show()
        
    # def rain_infiltration(self,h,p,t,theta_i):
    def rain_infiltration(self):

        # variáveis fornecidas pelo usuario
        p = int(self.line_edit_precipitation.text()) # mm
        p = p/1000 # mm/h -> m/h
        print("precipitação (m/h)=",p) 
        t = int(self.slider_hours.value()) # h
        print("horas=",t) 

        # variáveis obtidas da função runAnalysis (necessario defini-las como variaveis globais)
        self.theta_i = 0.3
        self.h = 3 # m

        theta_i = self.theta_i
        h = self.h

        # variáveis obtidas da função define_material (que cria um objeto)
        # self.material_theta_r = 0.025
        # self.material_theta_500 = 0.046
        # self.material_theta_s = 0.366
        # self.material_vg_alpha = 4.3
        # self.material_vg_n = 1.5206
        # self.material_vg_m = 0.3424
        # self.material_vg_k = 0.7

        # theta_r = self.material_theta_r
        # theta_s = self.material_theta_s
        # alpha = self.material_vg_alpha # m^(-1)
        # n = self.material_vg_n
        # m = self.material_vg_m 
        # k_day = self.material_vg_k # m/dia

        # médium
        theta_r = 0.01
        theta_s = 0.392
        alpha = 2.49 # m^(-1)
        n = 1.1689
        m = 0.1445
        k_day = 0.12 # m/dia

        # cálculos com essas variáveis
        k = k_day/24 # m/h
        theta_e = (theta_i-theta_r)/(theta_s-theta_r)
        psi = ((1 - (theta_e**(1/m)))/((alpha**n)*(theta_e**(1/m))))**(1/n)
        a = abs(psi) * (theta_s - theta_i)
        tp = k*abs(psi)*(theta_s-theta_i)/(p*(p-k))
        hwp = p*tp # m
        hw0 = k*(t-tp) + hwp
        hw = hw0 + a*log((hw0 + a)/(hwp + a))*((hw0 + a)/hw0)
        
        # possibilidades
        if isnan(hw): # se hw não tiver valor
            hw = 0
        elif hw<0: # se hw for negativo
            hw = 0
        elif hw>h: # se hw for maior que o h
            hw = h

        self.line_edit_hw.setText(f'{hw:.7f}')
        print("hw (m) =",hw)
        print("------------------------------------------------------------")
        return 
    
app = QApplication(argv)
UIWindow =  Popup_rain()
exit(app.exec_())