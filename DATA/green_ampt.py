from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog, QSlider, QLineEdit,QLabel
from sys import argv, exit, path
from math import *

# from green_ampt_histogram import Popup_histogram

class Popup_rain(QDialog): 
    def __init__(self):
        super().__init__()
        uic.loadUi("rain.ui", self)

        self.slider_hours = self.findChild(QSlider,"slider_hours")
        self.line_edit_hw = self.findChild(QLineEdit,"line_edit_hw")
        self.line_edit_precipitation = self.findChild(QLineEdit,"line_edit_precipitation")
        self.label_time = self.findChild(QLabel,"label_time")
        
        self.show()
        
    def show_histogram(self):
        
        return
    
    def check_slider(self):
        if self.line_edit_precipitation.text() == "":
            self.slider_hours.setEnabled(False)
        else:
            self.slider_hours.setEnabled(True)
        return
    
    def rain_infiltration(self):
        # variáveis fornecidas pelo usuario
        p = int(self.line_edit_precipitation.text()) # mm
        p = p/1000 # mm/h -> m/h
        t = int(self.slider_hours.value()) # h

        # variáveis obtidas da função runAnalysis (necessario defini-las como variaveis globais)
        self.theta_i = 0.3
        self.h = 3 # m
        theta_i = self.theta_i
        h = self.h

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
UIWindow =  Popup_rain()
exit(app.exec_())