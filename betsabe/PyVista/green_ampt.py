from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QSlider, QLineEdit,QLabel
from sys import argv, exit, path
from math import *

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

    def rain_infiltration(self,h,p,t,theta_i):
        # variáveis fornecidas pelo usuario
        p = int(self.line_edit_precipitation.text())
        t = int(self.slider_hours.value())

        # variáveis obtidas da função runAnalysis (necessario defini-las como variaveis globais)
        # theta_i = self.theta_i
        # h = self.h

        # variáveis obtidas da função define_material (que cria um objeto)
        theta_r = self.material_theta_r 
        theta_s = self.material_theta_s 
        alpha = self.material_vg_alpha 
        m = self.material_vg_n 
        n = self.material_vg_m 
        k_day = self.material_vg_k

        # cálculos com essas variáveis
        k = k_day/4
        theta_e = (theta_i-theta_r)/(theta_s-theta_r)
        psi = ((1 - theta_e^(1/m))/(alpha^n*theta_e^(1/m)))^(1/n)
        a = abs(psi) * (theta_s - theta_i)
        tp = k*abs(psi)*(theta_s-theta_i)/(p*(p-k))
        hwp = p*tp
        hw0 = k*(t-tp) + hwp
        hw = hw0 + a*log((hw0 + a)/(hwp + a))*((hw0 + a)/hw0)

        # possibilidades
        if isnan(hw): # se hw não tiver valor
            hw = 0
        elif hw<0: # se hw for negativo
            hw = 0
        elif hw>h: # se hw for maior que o h
            hw = h

        self.line_edit_hw.setText(str(hw))
        return 
    
    def time_update(self):
        self.line_edit_hw.setText(str(self.slider_hours.value()))
        return 
    


app = QApplication(argv)
UIWindow =  Popup_rain()
exit(app.exec_())