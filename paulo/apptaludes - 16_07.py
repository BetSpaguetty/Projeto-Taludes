# This Python file uses the following encoding: utf-8

# pip install pyvista
# pip install pyvistaqt
# pip install PyQt5
# pip install scipy
# pip install mpltern
# pip install rasterio

import sys
from sys import argv, exit, path
# from PySide2 import QtWidgets

import os
os.environ["PYOPENGL_PLATFORM"] = "osmesa"
import pyvistaqt
#print(pyvistaqt.__file__)

#from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QPushButton, QSizePolicy, QToolBar, QToolButton, QMainWindow, QLabel, QDialog, QLineEdit, QMessageBox, QGraphicsView, QStackedWidget
#from PySide2.QtGui import QPixmap
from PyQt5 import uic
#from PySide2.QtCore import Qt, QEvent

# from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QPushButton, QSizePolicy, QToolBar, QToolButton, QMainWindow, QLabel, QDialog, QLineEdit, QMessageBox, QGraphicsView
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt, QEvent


import scipy as sp
import numpy as np
from PIL import Image

import matplotlib as mpl
mpl.use('Qt5Agg')
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import mpltern
from mpltern.datasets import get_triangular_grid
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
from matplotlib.colors import Normalize

# from pyvistaqt import QtInteractor
import pyvista as pv
import rasterio

from random import randint
from math import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar

from PyQt5 import uic
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QAction, QToolBar, QStackedWidget, QWidget, QVBoxLayout, QDialog, QMessageBox, QApplication, QMainWindow, QGraphicsScene, QFileDialog, QPushButton, QGraphicsView, QLineEdit, QLabel, QGridLayout, QSizePolicy, QToolButton, QSlider
from PyQt5.QtGui import QPixmap
from pyvistaqt import QtInteractor, BackgroundPlotter

# #python -m pip install scipy (No terminal)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
#
# Needs to run
# python -m pip install -U mpltern
# to install mpltern

#      pyside2-uic form.ui -o ui_form.py
#      pyside2-uic form2.ui -o ui_form2.py
#      pyside2-uic popup_LatLon.ui -o ui_popup_LatLon.py
#      pyside2-uic add_info.ui -o ui_add_info.py

#from ui_form import Ui_AppTaludes
#from ui_form2 import Ui_Form2
# from ui_form3 import Ui_Form
#from ui_popup_LatLon import Ui_Dialog
#from ui_add_info import Ui_Dialog as Ui_Dialog2

class AppTaludes(QWidget):
    global wind2
    wind2 = 0
    global wind3
    wind3 = 0
    global wind4
    wind4 = 0
    global selected_map
    selected_map = 0

    def __init__(self, parent=None):
        #super().__init__(parent)
        super(AppTaludes, self).__init__()
        uic.loadUi("c:\\Users\\paulobaccar\\Documents\\AppTaludes\\form.ui", self)
        #self = AppTaludes()
        #self.setupUi(self)

        global selfx
        selfx = self

        # uic.loadUi("untitled.ui",self)

        # self.window1 = Form2()
        # self.window1.hide()

        self.tabs.tabCloseRequested.connect(self.tabs.removeTab)
        self.tabs_2.tabCloseRequested.connect(self.tabs_2.removeTab)
        self.tabs_3.tabCloseRequested.connect(self.tabs_3.removeTab)

        #self.tabs_2.setMinimumSize(int(self.width()*1/10), int(self.height()*3/4))
        #self.tabs_3.setMinimumSize(int(self.width()*2/3), 500) #int(self.height()*3/20)

        toolbar = QToolBar(parent=self)

        toolbar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        toolbar.setMinimumSize(1500,15)

        self.toolButton = QToolButton()
        self.toolButton.setText(" File")
        toolbar.addWidget(self.toolButton)
        toolbar.addSeparator()

        self.toolButton4 = QToolButton()
        self.toolButton4.setText("Maps")
        toolbar.addWidget(self.toolButton4)
        toolbar.addSeparator()

        self.toolButton2 = QToolButton()
        self.toolButton2.setText("Soil")
        toolbar.addWidget(self.toolButton2)
        toolbar.addSeparator()

        self.toolButton3 = QToolButton()
        self.toolButton3.setText("Properties")
        toolbar.addWidget(self.toolButton3)
        toolbar.addSeparator()

        self.toolButton5 = QToolButton()
        self.toolButton5.setText("Save")
        toolbar.addWidget(self.toolButton5)
        toolbar.addSeparator()

        self.toolButton6 = QToolButton()
        self.toolButton6.setText("Rain")
        toolbar.addWidget(self.toolButton6)
        toolbar.addSeparator()

        self.toolButton7 = QToolButton()
        self.toolButton7.setText("Convert")
        toolbar.addWidget(self.toolButton7)
        toolbar.addSeparator()

        self.toolButton8 = QToolButton()
        self.toolButton8.setText("View")
        toolbar.addWidget(self.toolButton8)
        toolbar.addSeparator()

        self.horizontalSlider_C.valueChanged.connect(self.number_changed)             #c
        self.horizontalSlider_Phi.valueChanged.connect(self.number_changed)           #phi
        self.horizontalSlider_H.valueChanged.connect(self.number_changed)             #h
        self.horizontalSlider_Hw.valueChanged.connect(self.number_changed)            #hw
        self.horizontalSlider_Theta.valueChanged.connect(self.number_changed)         #theta
        self.horizontalSlider_t.valueChanged.connect(self.number_changed)             #t

        self.lineEdit_areia.textChanged.connect(self.number_changed_2)       #Areia
        self.lineEdit_argila.textChanged.connect(self.number_changed_2)      #Argila

        self.material_type = 'GRANULAR FINE'
        self.lineEdit_areia.textChanged.connect(self.define_material)       #Areia
        self.lineEdit_argila.textChanged.connect(self.define_material)      #Argila

        self.plineEdit.textChanged.connect(self.define_chuva)
        self.horizontalSlider_t.valueChanged.connect(self.define_chuva)
        self.horizontalSlider_H.valueChanged.connect(self.define_chuva)
        self.horizontalSlider_Theta.valueChanged.connect(self.define_chuva)

        self.x1label.setVisible(False)
        self.x2label.setVisible(False)
        self.y1label.setVisible(False)
        self.y2label.setVisible(False)
        self.label.setVisible(False)
        self.limits.setVisible(False)
        self.imgname.setVisible(False)
        self.imgsizex.setVisible(False)
        self.imgsizey.setVisible(False)
        self.label_shape.setVisible(False)
        self.frame_exibicao_elevacao.setVisible(False)
        self.stacked_elevacao.setVisible(False)

        self.x1lineEdit.setVisible(False)
        self.x2lineEdit.setVisible(False)
        self.y1lineEdit.setVisible(False)
        self.y2lineEdit.setVisible(False)
        self.Adjust.setVisible(False)

        self.AnalysisBtn.setVisible(False)
        self.tabs.setVisible(False)
        self.tabs_2.setVisible(False)
        self.tabs_3.setVisible(False)
        self.tabs_4.setVisible(False)

        self.lineEdit_areia.setVisible(False)
        self.lineEdit_argila.setVisible(False)
        self.label_areia.setVisible(False)
        self.label_argila.setVisible(False)
        self.label_silte.setVisible(False)
        self.label_silte2.setVisible(False)
        self.label_material.setVisible(False)

        self.hLbl.setVisible(False)
        self.hlineEdit.setVisible(False)
        self.horizontalSlider_H.setVisible(False)
        self.hwLbl.setVisible(False)
        self.hwlineEdit.setVisible(False)
        self.horizontalSlider_Hw.setVisible(False)
        self.cLbl.setVisible(False)
        self.ClineEdit.setVisible(False)
        self.horizontalSlider_C.setVisible(False)
        self.oLbl.setVisible(False)
        self.philineEdit.setVisible(False)
        self.horizontalSlider_Phi.setVisible(False)
        self.thetaLbl.setVisible(False)
        self.thetalineEdit.setVisible(False)
        self.horizontalSlider_Theta.setVisible(False)
        self.tLbl.setVisible(False)
        self.tlineEdit.setVisible(False)
        self.horizontalSlider_t.setVisible(False)
        self.pLbl.setVisible(False)
        self.plineEdit.setVisible(False)
        self.ClearBtn.setVisible(False)
        self.mapaRio_Button.setVisible(False)
        self.corteArquivo_label.setVisible(False)
        self.corteArquivo_label.setMaximumSize(170,15)
        self.nome_arquivo_corte.setVisible(False)
        self.recortar_Button.setVisible(False)
        self.browse.setVisible(False)
        self.prop_Button.setVisible(False)
        self.topButton.setVisible(False)
        self.sideButton.setVisible(False)
        self.frontButton.setVisible(False)

        self.n_tabs = 0
        self.inclina_tabs = 0
        self.number_analysis = 0
        self.number_of_adjusts = 0

        self.horizontalSlider_H.setSingleStep(1)

        self.figure = plt.figure()

        self.AnalysisBtn.clicked.connect(self.analysisClick)
        self.AnalysisBtn.clicked.connect(self.runAnalysis)
        self.Adjust.clicked.connect(self.figureAdjust)
        self.ClearBtn.clicked.connect(self.clearCanvas)
        self.hidden = 0
        self.toolButton3.clicked.connect(self.showProp)
        self.toolButton.clicked.connect(self.getfile)
        self.toolButton2.clicked.connect(self.mostra_solo)
        self.toolButton4.clicked.connect(self.mostra_lista)

        self.toolButton7.clicked.connect(self.mostra_conversor)
        self.toolButton8.clicked.connect(self.mostra_vistas)

        self.topButton.clicked.connect(self.view_top)
        self.sideButton.clicked.connect(self.view_side)
        self.frontButton.clicked.connect(self.view_front)

        global wind2
        wind2 = 0
        global wind3
        wind3 = 0
        global selected_map
        selected_map = 0
        global azim
        azim = 30
        global elev
        elev = 30
        global roll
        roll = 0

        if selected_map == 1 and wind2 == 0:
            self.elev_incl(fname)
            selected_map = 0

        # self.toolButton4.clicked.connect(self.window1.show())
        self.toolButton5.clicked.connect(self.mostra_recortar)
        self.toolButton6.clicked.connect(self.mostra_chuva)

        # Bairros RJ
        # self.botao_regiao1 = self.findChild(QPushButton,"botao_regiao1")
        # self.botao_regiao2 = self.findChild(QPushButton,"botao_regiao2")
        # self.botao_regiao3 = self.findChild(QPushButton,"botao_regiao3")
        # self.botao_regiao4 = self.findChild(QPushButton,"botao_regiao4")
        # self.botao_regiao5 = self.findChild(QPushButton,"botao_regiao5")
        # self.botao_regiao6 = self.findChild(QPushButton,"botao_regiao6")
        # self.botao_regiao7 = self.findChild(QPushButton,"botao_regiao7")
        # self.botao_regiao8 = self.findChild(QPushButton,"botao_regiao8")
        # self.botao_regiao9 = self.findChild(QPushButton,"botao_regiao9")
        # self.botao_regiao10 = self.findChild(QPushButton,"botao_regiao10")
        # self.botao_regiao11 = self.findChild(QPushButton,"botao_regiao11")
        # self.botao_regiao12 = self.findChild(QPushButton,"botao_regiao12")
        # self.botao_regiao13 = self.findChild(QPushButton,"botao_regiao13")
        # self.botao_regiao14 = self.findChild(QPushButton,"botao_regiao14")
        # self.botao_regiao15 = self.findChild(QPushButton,"botao_regiao15")
        # self.botao_regiao16 = self.findChild(QPushButton,"botao_regiao16")
        # self.botao_regiao17 = self.findChild(QPushButton,"botao_regiao17")
        # self.botao_regiao18 = self.findChild(QPushButton,"botao_regiao18")
        # self.botao_regiao19 = self.findChild(QPushButton,"botao_regiao19")
        # self.botao_regiao20 = self.findChild(QPushButton,"botao_regiao20")

        # Tornando os botões invisiveis e coloridos ao passar o mouse em cima
        #self.botao_regiao1.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao2.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao3.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao4.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao5.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao6.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao7.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao8.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao9.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao10.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao11.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao12.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao13.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao14.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao15.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao16.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao17.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao18.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao19.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        #self.botao_regiao20.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
        #                                QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")

        # Botões começam invisíveis
        self.label_mapa_rio.setVisible(False)
        self.botao_regiao1.setVisible(False)
        self.botao_regiao2.setVisible(False)
        self.botao_regiao3.setVisible(False)
        self.botao_regiao4.setVisible(False)
        self.botao_regiao5.setVisible(False)
        self.botao_regiao6.setVisible(False)
        self.botao_regiao7.setVisible(False)
        self.botao_regiao8.setVisible(False)
        self.botao_regiao9.setVisible(False)
        self.botao_regiao10.setVisible(False)
        self.botao_regiao11.setVisible(False)
        self.botao_regiao12.setVisible(False)
        self.botao_regiao13.setVisible(False)
        self.botao_regiao14.setVisible(False)
        self.botao_regiao15.setVisible(False)
        self.botao_regiao16.setVisible(False)
        self.botao_regiao17.setVisible(False)
        self.botao_regiao18.setVisible(False)
        self.botao_regiao19.setVisible(False)
        self.botao_regiao20.setVisible(False)

        pixmap = QPixmap("c:\\Users\\paulobaccar\\Downloads\\mapa-rio-de-janeiro.jpg")
        self.label_mapa_rio.setPixmap(pixmap)

        self.setMinimumSize(1600,550)

        self.tri = 0
        self.material_definido = 0
        self.plots = []


        plt.close()
    #

    def showProp(self):
        #if self.hidden == 0:
        #    self.hLbl.setVisible(False)
        #    self.hlineEdit.setVisible(False)
        #    self.horizontalSlider_H.setVisible(False)
        #    self.hwLbl.setVisible(False)
        #    self.hwlineEdit.setVisible(False)
        #    self.horizontalSlider_Hw.setVisible(False)
        #    self.cLbl.setVisible(False)
        #    self.ClineEdit.setVisible(False)
        #    self.horizontalSlider_C.setVisible(False)
        #    self.oLbl.setVisible(False)
        #    self.philineEdit.setVisible(False)
        #    self.horizontalSlider_Phi.setVisible(False)
        #    self.thetaLbl.setVisible(False)
        #    self.thetalineEdit.setVisible(False)
        #    self.horizontalSlider_Theta.setVisible(False)
        #    self.ClearBtn.setVisible(False)
        #    self.hidden = 1
        #else:
        #    self.hLbl.setVisible(True)
        #    self.hlineEdit.setVisible(True)
        #    self.horizontalSlider_H.setVisible(True)
        #    self.hwLbl.setVisible(True)
        #    self.hwlineEdit.setVisible(True)
        #    self.horizontalSlider_Hw.setVisible(True)
        #    self.cLbl.setVisible(True)
        #    self.ClineEdit.setVisible(True)
        #    self.horizontalSlider_C.setVisible(True)
        #    self.oLbl.setVisible(True)
        #    self.philineEdit.setVisible(True)
        #    self.horizontalSlider_Phi.setVisible(True)
        #    self.thetaLbl.setVisible(True)
        #    self.thetalineEdit.setVisible(True)
        #    self.horizontalSlider_Theta.setVisible(True)
        #    self.ClearBtn.setVisible(True)
        #    self.hidden = 0
        #self.lineEdit_areia.setVisible(not self.lineEdit_areia.isVisible())
        #self.lineEdit_argila.setVisible(not self.lineEdit_argila.isVisible())
        #self.label_areia.setVisible(not self.label_areia.isVisible())
        #self.label_argila.setVisible(not self.label_argila.isVisible())
        #self.label_silte.setVisible(not self.label_silte.isVisible())
        #self.label_silte2.setVisible(not self.label_silte2.isVisible())
        #self.label_material.setVisible(not self.label_material.isVisible())

        self.hLbl.setVisible(not self.hLbl.isVisible())
        self.hlineEdit.setVisible(not self.hlineEdit.isVisible())
        self.horizontalSlider_H.setVisible(not self.horizontalSlider_H.isVisible())
        self.hwLbl.setVisible(not self.hwLbl.isVisible())
        self.hwlineEdit.setVisible(not self.hwlineEdit.isVisible())
        self.horizontalSlider_Hw.setVisible(not self.horizontalSlider_Hw.isVisible())
        self.cLbl.setVisible(not self.cLbl.isVisible())
        self.ClineEdit.setVisible(not self.ClineEdit.isVisible())
        self.horizontalSlider_C.setVisible(not self.horizontalSlider_C.isVisible())
        self.oLbl.setVisible(not self.oLbl.isVisible())
        self.philineEdit.setVisible(not self.philineEdit.isVisible())
        self.horizontalSlider_Phi.setVisible(not self.horizontalSlider_Phi.isVisible())
        self.thetaLbl.setVisible(not self.thetaLbl.isVisible())
        self.thetalineEdit.setVisible(not self.thetalineEdit.isVisible())
        self.horizontalSlider_Theta.setVisible(not self.horizontalSlider_Theta.isVisible())
        self.ClearBtn.setVisible(not self.ClearBtn.isVisible())

        if self.plineEdit.isVisible() == True:
            self.horizontalSlider_Hw.setVisible(False)
        elif self.ClearBtn.isVisible() == True:
            self.horizontalSlider_Hw.setVisible(True)
    #

    def define_material(self):
        #if self.material_definido >=1 :
        #    self.canvasT.setParent(None)

        clay = self.valueArgila;
        sand = self.valueAreia;
        silt = self.valueSilte;

        if (clay + silt + sand) != 100:
            self.material_type = 'A soma não da 100%'
        elif clay <= 18 and sand >= 65:
            self.material_type = 'COARSE';
            self.material_theta_r = 0.025;
            self.material_theta_500 = 0.046;
            self.material_theta_s = 0.366;
            self.material_vg_alpha = 4.30; #%[m^-1]
            self.material_vg_n = 1.5206;
            self.material_vg_m = 0.3424;
            self.material_vg_k = 0.70;     #%{m/dia}
        elif clay<=18 and sand >= 15 and sand <= 65:
            self.material_type = 'GRANULAR MEDIUM';
            self.material_theta_r = 0.010;
            self.material_theta_500 = 0.179;
            self.material_theta_s = 0.392;
            self.material_vg_alpha = 2.49;
            self.material_vg_n = 1.1689;
            self.material_vg_m = 0.1445;
            self.material_vg_k = 0.12;
        elif clay<=18 and sand <=15:
            self.material_type = 'GRANULAR FINE';
            self.material_theta_r = 0.010;
            self.material_theta_500 = 0.188;
            self.material_theta_s = 0.412;
            self.material_vg_alpha = 0.82;
            self.material_vg_n = 1.2179;
            self.material_vg_m = 0.1789;
            self.material_vg_k = 0.04;
        elif clay>=18 and clay <= 35 and sand >= 15: #or clay<=18 and sand >= 15 and sand <= 65:
            self.material_type = 'MEDIUM';
            self.material_theta_r = 0.010;
            self.material_theta_500 = 0.179;
            self.material_theta_s = 0.392;
            self.material_vg_alpha = 2.49;
            self.material_vg_n = 1.1689;
            self.material_vg_m = 0.1445;
            self.material_vg_k = 0.12;
        elif clay>=18 and clay<=35  and sand <= 15:
            self.material_type = 'MEDIUM FINE';
            self.material_theta_r = 0.010;
            self.material_theta_500 = 0.188;
            self.material_theta_s = 0.412;
            self.material_vg_alpha = 0.82;
            self.material_vg_n = 1.2179;
            self.material_vg_m = 0.1789;
            self.material_vg_k = 0.04;
        elif clay>=35 and clay <= 60:
            self.material_type = 'FINE';
            self.material_theta_r = 0.010;
            self.material_theta_500 = 0.327;
            self.material_theta_s = 0.481;
            self.material_vg_alpha = 1.98;
            self.material_vg_n = 1.0861;
            self.material_vg_m = 0.0793;
            self.material_vg_k = 0.09;
        elif clay > 60:
            self.material_type = 'VERY FINE';
            self.material_theta_r = 0.010;        # Linha 65
            self.material_theta_500 = 0.392;
            self.material_theta_s = 0.538;
            self.material_vg_alpha = 1.68;
            self.material_vg_n = 1.0730;
            self.material_vg_m = 0.068;
            self.material_vg_k = 0.08;
        #

        if clay <= 18:
            self.horizontalSlider_C.setMaximum(0)
            self.horizontalSlider_C.setMinimum(0)
            print("Solo 0")
        else:
            self.horizontalSlider_C.setMaximum(20)
            self.horizontalSlider_C.setMinimum(0)

        self.horizontalSlider_Theta.setMaximum(int(self.material_theta_s * 1000))
        self.horizontalSlider_Theta.setMinimum(int(self.material_theta_500 * 1000))
        self.horizontalSlider_Theta.setSliderPosition(int(self.material_theta_500 * 1000))
        self.horizontalSlider_Theta.setSingleStep(int((self.material_theta_s - self.material_theta_500) * 100))
        self.horizontalSlider_Theta.setPageStep(int((self.material_theta_s - self.material_theta_500) * 100))
        self.horizontalSlider_Theta.setTickInterval(int((self.material_theta_s - self.material_theta_500)/100))

        self.label_material.setText(str(self.material_type))

        fig = plt.figure()
        # fig.set_figwidth(4.5)
        # fig.set_figheight(3.9)

        ax = plt.subplot(111,projection="ternary")

        ax.taxis.set_major_locator(MultipleLocator(0.2))
        ax.laxis.set_major_locator(MultipleLocator(0.2))
        ax.raxis.set_major_locator(MultipleLocator(0.2))

        #ax.set_tlabel("Cl")
        #ax.set_llabel("Sd")
        #ax.set_rlabel("S")
        ax.tick_params(labelrotation="axis")
        ax.grid(which='major') #which="both")

        t = [0.6, 0.6, 0.35, 0.35]
        l = [0.4, 0, 0, 0.65]
        r = [0, 0.4, 0.65, 0]
        ax.fill(t, l, r, color="b") #Trapézio azul

        t = [1, 0.6, 0.6]
        l = [0, 0.4, 0]
        r = [0, 0 , 0.4]
        ax.fill(t, l, r, color="m") #Triângulo roxo

        t = [0.35, 0.35, 0.18, 0.18]
        l = [0.65, 0.15, 0.15, 0.82]
        r = [0, 0.5, 0.67, 0]
        ax.fill(t, l, r, color="y") #Trapézio amarelo

        t = [0.35, 0.35, 0.18, 0.18]
        l = [0.15, 0, 0, 0.15]
        r = [0.5, 0.65, 0.82, 0.67]
        ax.fill(t, l, r, color="lime") #Paralelogramo verde claro

        t = [0.18, 0.18, 0, 0]
        l = [0.15, 0, 0, 0.15]
        r = [0.67, 0.82, 1, 0.85]
        ax.fill(t, l, r, color="g") #Paralelogramo verde escuro

        t = [0.18, 0.18, 0, 0]
        l = [0.65, 0.15, 0.15, 0.65]
        r = [0.17, 0.67, 0.82, 0.35]
        ax.fill(t, l, r, color="orange") #Paralelogramo laranja

        t = [0.18, 0.18, 0, 0]
        l = [0.82, 0.65, 0.65, 1]
        r = [0, 0.17, 0.35, 0]
        ax.fill(t, l, r, color="r") #Trapézio vermelho

        ax.scatter((clay/100),(sand/100),(silt/100), color="black")

        ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
        labels = ["Sl", "0.2", "0.4", "0.6", "0.8", "1"]
        ax.taxis.set_ticks(ticks, labels=labels)
        labels = ["Cl", "0.2", "0.4", "0.6", "0.8", "1"]
        ax.laxis.set_ticks(ticks, labels=labels)
        labels = ["Sd", "0.2", "0.4", "0.6", "0.8", "1"]
        ax.raxis.set_ticks(ticks, labels=labels)

        self.tri+=1

        fig.tight_layout
        self.canvasT = FigureCanvas(fig)
        self.canvasT.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.canvasT.setMaximumSize(315,300)           #(390,345)

        #plt.close('all')

        #for i in reversed(range(self.verticalLayout_6.count())):
        #    self.verticalLayout_6.itemAt(i).widget().setParent(None)
        
        #if self.material_definido >=1 :
        #    self.verticalLayout_6.itemAt(0).widget().setParent(None)
        
        # self.verticalLayout_6.itemAt(0).widget().setParent(None)
        
        #if self.tabs_3.count() > 1:
        #    self.tabs_3.removeTab(0)
        
        self.tabMat = QWidget()
        self.tabMat_layout = QVBoxLayout()
        self.tabMat_layout.addWidget(self.canvasT)
        self.tabMat.setLayout(self.tabMat_layout)

        self.tab_name = "Solo"
        self.tabs_4.addTab(self.tabMat, self.tab_name)

        if self.tabs_4.count() >= 2:
            self.tabs_4.removeTab(0)

        self.tabs_4.setVisible(True)
        
        #self.verticalLayout_6.addWidget(self.canvasT)

        valueC = str(self.horizontalSlider_C.value())
        self.ClineEdit.setText(valueC)

        valuePhi = str(self.horizontalSlider_Phi.value())
        self.philineEdit.setText(valuePhi)

        valueH = str(self.horizontalSlider_H.value()/10)
        self.hlineEdit.setText(valueH)

        valueHw = str(self.horizontalSlider_Hw.value() * self.horizontalSlider_H.value()/1000)
        self.hwlineEdit.setText(valueHw)

        valueTheta = str(self.horizontalSlider_Theta.value()/1000)
        self.thetalineEdit.setText(valueTheta)

        self.stacked_elevacao.resize
        #size = self.tabs_3.size()
        #self.plotter.resize(size)

        #self.plotter.update()
        #self.plotter.resize(self.tabs_3.size())
        #print("¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢")

        print("Muda solo")
        self.material_definido+=1
    #

    def define_chuva(self):
        # variáveis fornecidas pelo usuario
        p = int(self.plineEdit.text()) # mm
        p = p/1000 # mm/h -> m/h
        #print("precipitação (m/h)=",p) 
        t = int(self.horizontalSlider_t.value()) # h
        #print("horas=",t) 

        # variáveis obtidas da função runAnalysis (necessario defini-las como variaveis globais)
        self.theta_i = self.horizontalSlider_Theta.value();   # 0.3
        self.h = self.horizontalSlider_H.value()/10;    # 3 # m

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
        theta_r = self.material_theta_r       # 0.01
        theta_s = self.material_theta_s       # 0.392
        alpha = self.material_vg_alpha        # 2.49 # m^(-1)
        n = self.material_vg_n                # 1.1689
        m = self.material_vg_m                # 0.1445
        k_day = self.material_vg_k            # 0.12 # m/dia

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

        self.hwlineEdit.setText(f'{hw:.7f}')
        #print("hw (m) =", hw)
        #print("------------------------------------------------------------")
        return
    #

    def number_changed(self):
        valueC = str(self.horizontalSlider_C.value()/10)
        self.ClineEdit.setText(valueC)

        valuePhi = str(self.horizontalSlider_Phi.value())
        self.philineEdit.setText(valuePhi)

        valueH = str(self.horizontalSlider_H.value()/10)
        self.hlineEdit.setText(valueH)

        valueHw = str(self.horizontalSlider_Hw.value() * self.horizontalSlider_H.value()/1000)
        self.hwlineEdit.setText(valueHw)

        valueTheta = str(self.horizontalSlider_Theta.value()/1000)
        self.thetalineEdit.setText(valueTheta)

        print("number_changed")

        self.runAnalysis()
    #

    def number_changed_2(self):
        self.valueAreia = int(self.lineEdit_areia.text())
        valueAreia = self.lineEdit_areia.text()

        self.valueArgila = int(self.lineEdit_argila.text())
        valueArgila = self.lineEdit_argila.text()

        self.valueSilte = 100 - self.valueArgila - self.valueAreia
        valueSilte = str(self.valueSilte)
        self.label_silte2.setText(valueSilte)

        # print(self.lineEdit_areia.text())
        # print(self.lineEdit_argila.text())

        print("number_changed_2")
    #

    def analysisClick(self):
        self.n_tabs += 1
    #

    def runAnalysis(self):
        global fname
        global azim
        global elev
        global roll
        fname = self.imgname.text()
        imgx = Image.open(fname)

        # self.fname = self.imgname.text()
        # imgx = Image.open(self.fname)

        # self.tabs.setVisible(True)
        self.tabAtual = self.tabs_2.currentIndex()
        self.tabs_2.setVisible(True)

        X1 = int(self.x1lineEdit.text())
        X2 = int(self.x2lineEdit.text())
        y1 = int(self.y1lineEdit.text())
        y2 = int(self.y2lineEdit.text())

        h_value = self.horizontalSlider_H.value()/10;
        hw_value = self.horizontalSlider_Hw.value();
        c_value = self.horizontalSlider_C.value()/10;
        phi_value = self.horizontalSlider_Phi.value();
        theta_value = self.horizontalSlider_Theta.value();

        c = c_value
        h = h_value
        phi = phi_value
        hw = h_value * hw_value/100
        theta_i = theta_value/1000
        self.fos_array = np.ones((imgx.size[0], imgx.size[1]))  #((imgx.size[0]+1,imgx.size[1]+1))   #[x1:x2, y1:y2]

        if self.tabs_2.count() == 1:
            self.tabs_2.removeTab(0)
        #

        # Creating figure
        self.fos_array = self.fos_array.transpose()

        if self.number_of_adjusts >= 1:
            self.fos_array = self.fos_array[y1-1:y2, X1-1:X2]
            self.fos_array2 = self.fos_array

            sizey = X2-X1
            sizex = y2-y1

            for i in range(0, sizex):
                for j in range(0, sizey):
                    alpha = self.g_max[y1+i,X1+j]   #[x1+j,y1+i]
                    if self.material_type == 'COARSE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.046;
                        theta_i_max = 0.365;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min)

                        self.fos_array2[i-1,j-1] = (6788110953151657*(x1**2)*(x2**2)*x5)/18014398509481984 + (1355958164086877*(x1**2)*x3*(x4**2)*x5)/9007199254740992 - (8873610522459485*(x1**2)*(x4**2)*x5)/72057594037927936 - (1692657047651061*(x1**2))/18014398509481984 - (3851498880822799*x1*(x2**2)*x3)/1125899906842624 + (2526110258615389*x1*x2*(x3**2))/1125899906842624 + (2706917046260173*x1*x2)/9007199254740992 - (3556745139181571*x1*(x3**3)*x4)/9007199254740992 - (579938420281673*x1*(x3**2))/1125899906842624 + (8180563435756073*x1*x3*x4)/36028797018963968 + (3114137794295375*x1*x3)/9007199254740992 - (8586273326384709*x1*x5)/144115188075855872 + (3545170951606327*(x2**2)*(x3**2))/4503599627370496 + (8665832770244175*(x2**2)*x3)/4503599627370496 - (7818372289906591*(x2**2)*x5)/4503599627370496 + (2684009153708421*(x2**2))/2251799813685248 - (4201502816181941*x2*(x3**2))/2251799813685248 - (3562767927008791*x2*x3*x4)/36028797018963968 + (2328059298502727*x2*x3*x5)/9007199254740992 + (8830399494179771*x2*x4*(x5**2))/72057594037927936 + (5482565565501159*x2*x5)/4503599627370496 - (2681827153050867*x2)/2251799813685248 + (8730627984475617*(x3**2)*x4)/72057594037927936 + (1323618450977937*(x3**2))/2251799813685248 - (5618799156698347*x3*x5)/36028797018963968 - (4911690079918821*x3)/4503599627370496 - (7212846679305375*(x4**2))/36028797018963968 - (2144834721434649*x4*x5)/288230376151711744 + (6420485161231939*x4)/9007199254740992 - (6209185403811853*x5)/36028797018963968 + 981468462750861/4503599627370496
                        self.fos_array2[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'GRANULAR MEDIUM':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.179;
                        theta_i_max = 0.392;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[i-1,j-1] = (2395554010573903*(x1**3)*x5)/9007199254740992 - (1584791230571555*(x1**2)*x2*x3)/1125899906842624 - (8675059321513597*(x1**2))/36028797018963968 + (2712053627057047*x1*x2*x3)/1125899906842624 - (436588234554137*x1*x3*x5)/562949953421312 + (8696742236362029*x1*x3)/18014398509481984 + (84167422866237*x1*x4)/1125899906842624 + (5038972167706281*(x2**3)*x5)/1125899906842624 - (2769339911649845*(x2**3))/562949953421312 - (5816346030793635*(x2**2)*(x4**2))/18014398509481984 - (2296851704845541*(x2**2)*x5)/281474976710656 + (4711729450227555*(x2**2))/562949953421312 + (4526012208234625*x2*x3*x5)/2251799813685248 - (1438367102275171*x2*x3)/562949953421312 + (3235555885457197*x2*(x4**3))/18014398509481984 - (6984536435614461*x2*(x5**3))/18014398509481984 + (4734726859996689*x2*x5)/1125899906842624 - (8887739276337299*x2)/2251799813685248 + (7909776872928529*(x3**2))/36028797018963968 + (4825069300825317*x3*x4)/144115188075855872 + (1932527580330421*x3*(x5**2))/2251799813685248 - (7088385317352909*x3*x5)/4503599627370496 - (6028859269012785*x3)/36028797018963968 - (4457058916701155*(x4**2))/18014398509481984 + (205865104591035*x4)/281474976710656 - (1093234104604003*x5)/2251799813685248 + 4657821803862761/9007199254740992;
                        self.fos_array2[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'GRANULAR FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.188;
                        theta_i_max = 0.412;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[i-1,j-1] = (5997468984231391*x4)/9007199254740992 - (5850653107015129*x2)/2251799813685248 - (2903074490076611*x1)/4503599627370496 - (4978764466261023*x5)/18014398509481984 + (2497394100991123*x1*x2)/1125899906842624 + (1094809215253921*x1*x3)/1125899906842624 + (7011891843826591*x1*x4)/36028797018963968 - (137137518003759*x2*x3)/35184372088832 + (6916471811591635*x1*x5)/18014398509481984 - (5185975094203355*x2*x4)/576460752303423488 + (6973754261875579*x2*x5)/9007199254740992 - (6728904517417159*x3*x5)/9007199254740992 - (5049272361606063*x1*(x2**2))/2251799813685248 + (8151483504101627*x1*(x3**2))/18014398509481984 + (7836140676118751*(x2**2)*x3)/2251799813685248 - (103490230972707*(x1**3)*x4)/562949953421312 - (2508927668464753*(x2**3)*x3)/2251799813685248 + (1751145175163683*(x2**2))/562949953421312 - (2910103121418035*(x4**2))/18014398509481984 - (4149956958460727*(x1**2)*x2*x3)/4503599627370496 - (2909406058924355*x1*(x2**2)*x5)/1125899906842624 + (4267265215922321*(x1**3)*x2*x5)/4503599627370496 + (5734832464949375*x1*x3*(x5**3))/18014398509481984 - (4082556226690241*(x1**2)*(x3**2)*x4)/36028797018963968 - (883679796825111*x1*x3*x5)/562949953421312 + (3185546221473745*x2*x3*x5)/1125899906842624 + 1119623049971351/2251799813685248;
                        self.fos_array2[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'MEDIUM':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.179;
                        theta_i_max = 0.392;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[i-1,j-1] = - (7605402998259809*(x1**3)*x6)/9007199254740992 + (5433101380788941*(x1**2)*(x6**2))/9007199254740992 + (5438216367263101*(x1**2)*x6)/4503599627370496 + (6933674839011865*x1*x2)/18014398509481984 - (3183093811021595*x1*x3)/18014398509481984 - (6604577520812421*x1*x4*x5)/36028797018963968 - (6677569571403873*x1*x4*x6)/18014398509481984 + (5492449447091975*x1*x5*x6)/144115188075855872 + (5423482706553025*x1*x5)/18014398509481984 - (690523320510537*x1*x6)/562949953421312 - (3321581480764011*(x2**3)*(x6**2))/2251799813685248 + (4144557554361693*(x2**2))/4503599627370496 - (5247773900528281*x2*x3)/18014398509481984 + (912731872269751*x2*(x4**2))/4503599627370496 - (4408639353815769*x2*x5)/36028797018963968 + (8395993053582923*x2*x6)/4503599627370496 - (8532874373358735*x2)/4503599627370496 + (4503753517663555*(x3**2))/9007199254740992 + (5623770062789117*x3*x4*x5)/18014398509481984 - (4581567852841661*x3*(x5**2))/18014398509481984 + (6873632408613219*x3*(x6**3))/18014398509481984 - (2940490725035801*x3*x6)/4503599627370496 - (2371501908453915*x3)/4503599627370496 - (947262250475269*(x4**2))/2251799813685248 + (7492475340553871*x4*(x5**2)*x6)/576460752303423488 - (4920950276662705*x4*x5)/18014398509481984 + (1219489943909891*x4*x6)/9007199254740992 + (8174395509123883*x4)/9007199254740992 + (1206779442258227*(x5**2))/18014398509481984 + (3236337280494743*x5)/9007199254740992 - (2948601616754633*(x6**2))/9007199254740992 + 8820801393289007/18014398509481984;
                        self.fos_array2[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'MEDIUM FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.188;
                        theta_i_max = 0.412;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[i-1,j-1] =  (3886190004610709*x4)/4503599627370496 - (5729276149747483*x3)/9007199254740992 - (6788231717529895*x2)/2251799813685248 + (479426134057027*x5)/1125899906842624 - (2555014444031809*x6)/4503599627370496 + (8284280323761517*x1*x3)/36028797018963968 - (5766260012425305*x1*x4)/9007199254740992 - (525466186966067*x2*x3)/562949953421312 + (3559543339455779*x1*x5)/18014398509481984 + (3044854372294711*x2*x4)/2251799813685248 + (2604085627039555*x2*x6)/1125899906842624 + (7021469540150699*x3*x5)/288230376151711744 - (231180365885025*x3*x6)/562949953421312 - (2434138700745953*x4*x5)/9007199254740992 - (2798606821472435*(x2**2)*x4)/1125899906842624 - (4787498997851079*(x2**2)*x6)/2251799813685248 + (6336213524232577*(x2**2))/2251799813685248 + (8898687912479801*(x3**2))/18014398509481984 - (6956481687155787*(x4**2))/18014398509481984 - (6059931181255597*(x5**2))/144115188075855872 + (3017676058392109*x1*x2*(x4**2))/9007199254740992 - (424322724646621*(x2**2)*x3*x4)/9007199254740992 + (8194181095609791*x1*(x3**2)*(x6**2))/72057594037927936 + (4040226326314105*x1*x2*x4)/4503599627370496 + (6767925566021999*x1*x2*x6)/36028797018963968 + (4332927401162267*x2*x3*x4)/9007199254740992 - (6054326828217865*x1*x3*x6)/9007199254740992 - (1182428728719139*x2*x3*x5)/4503599627370496 - (3671852565176795*x1*x4*x6)/36028797018963968 + (5352375486130983*x2*x3*x6)/4503599627370496 + (3079416316199729*x3*x4*x6)/9007199254740992 - (5765496138098037*x2*x3*x4*x6)/9007199254740992 + 3442293244771261/4503599627370496;
                        self.fos_array2[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.327;
                        theta_i_max = 0.481;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[i-1,j-1] = (8711105383099221*(x1**2))/72057594037927936 + (4480937614520491*x1*x2*x3*x6)/4503599627370496 + (6445291833574493*x1*x2*x4*(x6**2))/576460752303423488 - (281440029914825*x1*(x3**2)*x6)/562949953421312 - (6629445291354447*x1*x3*x4)/18014398509481984 + (849190321960673*x1*x3*x5)/2251799813685248 - (6187137339255229*x1*x4*x6)/18014398509481984 - (4624215388296035*x1*x6)/18014398509481984 - (1587486474559393*(x2**3)*x6)/1125899906842624 - (4900095579043665*(x2**2)*x4)/4503599627370496 + (1169434422300945*(x2**2))/562949953421312 - (7554405290076481*x2*x3*x4*x5*x6)/72057594037927936 - (7246543431362679*x2*x3*x5)/36028797018963968 - (721288367741207*x2*x3)/1125899906842624 + (8836698625396407*x2*x4*(x5**2))/144115188075855872 + (4781016702927063*x2*x4)/4503599627370496 + (4010700648742253*x2*x6)/2251799813685248 - (2883657241266265*x2)/1125899906842624 - (6577851316887483*(x3**3))/18014398509481984 + (2688469612731583*(x3**2))/2251799813685248 + (6653205645687021*x3*(x4**2)*(x6**2))/18014398509481984 - (2099413330989821*x3*(x4**2))/4503599627370496 + (6161799069262313*x3*x4)/9007199254740992 + (1857306243852377*x3*x5*x6)/9007199254740992 - (2865566660442267*x3*x5)/9007199254740992 - (4614774789911059*x3*x6)/9007199254740992 - (1937328245404209*x3)/2251799813685248 - (7930907804563573*(x4**2))/36028797018963968 - (4754832626658037*x4*x5)/18014398509481984 + (171256162149423*x4)/281474976710656 - (8578558619551665*(x5**2)*x6)/288230376151711744 + (8704230461968029*x5)/18014398509481984 - (3382315052029319*(x6**3))/1152921504606846976 - (6812374621577823*x6)/18014398509481984 + 6174808073279873/9007199254740992;
                        self.fos_array2[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'VERY FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.392;
                        theta_i_max = 0.538;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[i-1,j-1] = (3443522597856495*x4)/4503599627370496 - (2348315328800215*x2)/1125899906842624 - (8559581679713667*x1)/36028797018963968 + (8018106863502985*x5)/18014398509481984 - (4230345748317103*x6)/9007199254740992 - (1544138636456145*(x4**2)*(x6**2))/18014398509481984 + (902528602503447*x1*x2)/1125899906842624 - (7043808527068311*x2*x3)/4503599627370496 - (7246008324732221*x1*x6)/18014398509481984 + (1747413719569329*x2*x6)/1125899906842624 - (2597399368633979*x3*x6)/4503599627370496 - (2391652988631193*x4*x5)/4503599627370496 + (6181389039177289*x1*(x3**2))/9007199254740992 - (5186363803500845*x1*(x5**2))/36028797018963968 - (2321574606811609*x2*(x5**2))/72057594037927936 - (2543509902109129*x3*(x4**2))/9007199254740992 + (2780023057880475*(x1**2)*x6)/9007199254740992 + (3526997481352009*(x2**2))/4503599627370496 - (7277171475332687*(x4**3))/72057594037927936 + (5569296935854231*x1*x4*(x5**2))/18014398509481984 + (5469000151567747*(x3**2)*x4*x5)/18014398509481984 + (651427578412907*x1*x2*x5)/1125899906842624 - (3056278760769427*x1*x3*x4)/4503599627370496 - (2474169676151269*x1*x3*x5)/18014398509481984 + (5800416867896625*x2*x3*x4)/4503599627370496 - (6838031967161513*x1*x3*x6)/9007199254740992 - (2410625286488745*x2*x3*x5)/9007199254740992 + (5260456502000859*x2*x3*x6)/4503599627370496 + (2296168764961959*x1*x5*x6)/4503599627370496 + (8412632997477619*x3*x4*x6)/18014398509481984 - (8539609750453113*x1*x2*x5*x6)/9007199254740992 - (5748018464844461*x1*(x2**2)*x4*x6)/4503599627370496 + 6230592657726943/9007199254740992;
                        self.fos_array2[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]

                    # self.fos_array[i,j] = (1605074512383065*(alpha**2)*(c**2)*(h**2)*phi)/151115727451828646838272 - (1414963042633059*(alpha**2)*(c**2)*h*phi)/18889465931478580854784 - (2774717211173289*(alpha**2)*(c**2)*hw*phi)/604462909807314587353088 + (2835477809945801*(alpha**2)*(c**2)*phi)/37778931862957161709568 + (6731555515546295*(alpha**2)*c)/73786976294838206464 + (5516753565726847*(alpha**2)*phi)/147573952589676412928 + (5653461066590515*alpha*(c**2)*h)/590295810358705651712 + (3025671568382675*alpha*(c**2)*phi)/590295810358705651712 - (2098110323770171*alpha*(c**2))/36893488147419103232 - (3002978305542275*alpha*c*(h**2))/4611686018427387904 + (2687741203999111*alpha*c*h)/576460752303423488 + (6472386681360727*alpha*c*hw*phi)/590295810358705651712 - (2982096583892561*alpha*c*(phi**2))/2361183241434822606848 - (4627184841729915*alpha*c)/288230376151711744 - (5688086807612743*alpha*(phi**2))/590295810358705651712 - (4311146912769217*alpha*phi)/1152921504606846976 - (4976341265194569*(c**2)*(h**2)*phi)/147573952589676412928 + (2283034929082703*(c**2)*h*phi)/9223372036854775808 + (1342385546936077*(c**2)*hw*phi)/147573952589676412928 - (1295331185150365*(c**2)*phi)/2305843009213693952 + (2592141320026855*c*(h**2))/72057594037927936 - (4971891995221437*c*h)/18014398509481984 - (4809409727287499*c*hw*phi)/9223372036854775808 + (2265715759669333*c*(phi**2))/36893488147419103232 + (3352624142374595*c)/4503599627370496 + (20768301037335*(h**2)*(hw**2)*phi)/2305843009213693952 - (1324783938325601*hw)/36028797018963968 + (3497832476657703*(phi**2))/4611686018427387904 + (6865366199800263*phi)/72057594037927936 + 1489595912300695/9007199254740992;
            #

            # print(self.fos_array2)
            z = np.array(imgx)[y1-1:y2, X1-1:X2]
            self.fos_array3 = self.fos_array2.copy()

            for i in range(0, sizex):
                for j in range(0, sizey):
                    if self.fos_array2[i-1,j-1] > 2:
                        self.fos_array2[i-1,j-1] = 2 #float("NaN")
                        self.fos_array3[i-1,j-1] = float("NaN")
                        z[i-1,j-1] = float("NaN")
            #
            for i in range(0, sizex):
                for j in range(0, sizey):
                    if self.fos_array2[i-1,j-1] < 1:
                        self.fos_array2[i-1,j-1] = 1
                        self.fos_array3[i-1,j-1] = 1


            # print(self.fos_array3.shape[0])
            # fig_fos, ax = plt.subplots(1,1,figsize=(12,10))

            # cmap = plt.get_cmap('rainbow_r')

            # plt.imshow(self.fos_array2.transpose(), cmap)
            # im_fos = ax.imshow(self.fos_array2.transpose(), cmap)

            # ax.set_yticks([0, 0.2*sizey, 0.4*sizey, 0.6*sizey, 0.8*sizey, sizey], labels=[0, 5*sizey, 10*sizey, 15*sizey, 20*sizey, 25*sizey])
            # ax.set_xticks([0, 0.2*sizex, 0.4*sizex, 0.6*sizex, 0.8*sizex, sizex], labels=[0, 5*sizex, 10*sizex, 15*sizex, 20*sizex, 25*sizex])

            # plt.colorbar(im_fos,ax=ax)
            # plt.axis([0, sizex-1, 0, sizey-1])
            # ax.invert_yaxis()

            lin_x = np.linspace(0,1,self.fos_array.shape[0]+2,endpoint=False)
            lin_y = np.linspace(0,1,self.fos_array.shape[1]+2,endpoint=False)
            y,x = np.meshgrid(lin_y,lin_x)
            ##############  z = np.array(imgx)

            # self.fos_array2 = self.fos_array2.transpose()
            x2 = self.fos_array2.shape[0]
            y2 = self.fos_array2.shape[1]

            self.fos_array2 = np.fliplr(self.fos_array2)
            z = np.fliplr(z)
            self.fos_array2 = np.flipud(self.fos_array2)
            z = np.flipud(z)
            # self.fos_array2 = self.fos_array2.transpose()
            # z = z.transpose()

            fig_fos, ax = plt.subplots(subplot_kw=dict(projection="3d"), constrained_layout=1, figsize=(12, 10))
            norm1 = plt.Normalize(vmin= self.fos_array2.min().min(), vmax= self.fos_array2.max().max())

            ax.plot_surface(x[2:x2, 2:y2], y[2:x2, 2:y2], z[2:x2+2, 2:y2+2], facecolors= plt.cm.rainbow_r(norm1(self.fos_array2[2:x2+2, 2:y2+2])), antialiased=False, shade=False) #[0:x2-1, 0:y2-1]
            m = mpl.cm.ScalarMappable(cmap= plt.cm.rainbow_r, norm= norm1)
            m.set_array(self.fos_array2.transpose()) #[0:x2-1, 0:y2-1])
            plt.colorbar(m, ax= ax, location= "right")
            plt.axis([np.nanmin(x), np.nanmax(x)-0.01, np.nanmin(y), np.nanmax(y)-0.01, np.nanmin(z), np.nanmax(z)])

            plt.xticks([])
            plt.yticks([])

            ax.invert_yaxis()

            ##################################################
            ax.view_init(elev= elev, azim= azim, roll= roll)
            ##################################################

            self.canvas_fos = FigureCanvas(fig_fos)
            self.toolb_fos = NavigationToolbar(self.canvas_fos, self)

            self.tabInc = QWidget()
            self.tabInc_layout = QVBoxLayout()
            self.tabInc_layout.addWidget(self.canvas_fos)
            self.tabInc_layout.addWidget(self.toolb_fos)
            self.tabInc.setLayout(self.tabInc_layout)

            self.tab_name = "Segurança (3D) " + str(self.inclina_tabs)
            self.tabs_2.addTab(self.tabInc,self.tab_name)

            plt.close('all')

            ############################################################################################################

            self.fos_array3 = self.fos_array3.transpose()
            # self.fos_array3 = np.flipud(self.fos_array3)

            fig_fos2, ax2 = plt.subplots(1,1,figsize=(12,10))
            cmap = plt.get_cmap('rainbow_r')

            # x3 = self.fos_array3.shape[0]
            # y3 = self.fos_array3.shape[1]
            # plt.imshow(self.fos_array3[0:x3-10, 0:y3-10], cmap)
            # im_fos = ax2.imshow(self.fos_array3[0:x3-10, 0:y3-10], cmap)
            plt.imshow(self.fos_array3, cmap)
            im_fos = ax2.imshow(self.fos_array3, cmap)

            ax2.set_yticks([0, 0.2*(sizey-2), 0.4*(sizey-2), 0.6*(sizey-2), 0.8*(sizey-2), (sizey-2)], labels=[0, 5*sizey, 10*sizey, 15*sizey, 20*sizey, 25*sizey])
            ax2.set_xticks([0, 0.2*(sizex-2), 0.4*(sizex-2), 0.6*(sizex-2), 0.8*(sizex-2), (sizex-2)], labels=[0, 5*sizex, 10*sizex, 15*sizex, 20*sizex, 25*sizex])

            plt.colorbar(im_fos,ax=ax2)
            plt.axis([0, sizex-2, 0, sizey-2])

            ax2.invert_yaxis()

            self.canvas_fos2 = FigureCanvas(fig_fos2)
            self.toolb_fos2 = NavigationToolbar(self.canvas_fos2, self)

            self.tabInc2 = QWidget()
            self.tabInc_layout2 = QVBoxLayout()
            self.tabInc_layout2.addWidget(self.canvas_fos2)
            self.tabInc_layout2.addWidget(self.toolb_fos2)
            self.tabInc2.setLayout(self.tabInc_layout2)

            self.tab_name2 = "Segurança (2D) " + str(self.inclina_tabs)
            self.tabs_2.addTab(self.tabInc2,self.tab_name2)

            def on_click(event):
                global azim
                global elev
                azim, elev = ax.azim, ax.elev

            cid = fig_fos.canvas.mpl_connect('button_release_event', on_click)

            # ax.grid(False)
            # plt.axis('off')


        else:
            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))
            fig_fos2, ax2 = plt.subplots(1,1,figsize=(12,10))
            self.fos_array2 = self.fos_array

            for i in range(1,imgx.size[0]-1):
                for j in range(1,imgx.size[1]-1):
                    alpha = self.g_max[i-1,j-1]
                    if self.material_type == 'COARSE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.046;
                        theta_i_max = 0.365;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min)

                        self.fos_array2[j-1,i-1] = (6788110953151657*(x1**2)*(x2**2)*x5)/18014398509481984 + (1355958164086877*(x1**2)*x3*(x4**2)*x5)/9007199254740992 - (8873610522459485*(x1**2)*(x4**2)*x5)/72057594037927936 - (1692657047651061*(x1**2))/18014398509481984 - (3851498880822799*x1*(x2**2)*x3)/1125899906842624 + (2526110258615389*x1*x2*(x3**2))/1125899906842624 + (2706917046260173*x1*x2)/9007199254740992 - (3556745139181571*x1*(x3**3)*x4)/9007199254740992 - (579938420281673*x1*(x3**2))/1125899906842624 + (8180563435756073*x1*x3*x4)/36028797018963968 + (3114137794295375*x1*x3)/9007199254740992 - (8586273326384709*x1*x5)/144115188075855872 + (3545170951606327*(x2**2)*(x3**2))/4503599627370496 + (8665832770244175*(x2**2)*x3)/4503599627370496 - (7818372289906591*(x2**2)*x5)/4503599627370496 + (2684009153708421*(x2**2))/2251799813685248 - (4201502816181941*x2*(x3**2))/2251799813685248 - (3562767927008791*x2*x3*x4)/36028797018963968 + (2328059298502727*x2*x3*x5)/9007199254740992 + (8830399494179771*x2*x4*(x5**2))/72057594037927936 + (5482565565501159*x2*x5)/4503599627370496 - (2681827153050867*x2)/2251799813685248 + (8730627984475617*(x3**2)*x4)/72057594037927936 + (1323618450977937*(x3**2))/2251799813685248 - (5618799156698347*x3*x5)/36028797018963968 - (4911690079918821*x3)/4503599627370496 - (7212846679305375*(x4**2))/36028797018963968 - (2144834721434649*x4*x5)/288230376151711744 + (6420485161231939*x4)/9007199254740992 - (6209185403811853*x5)/36028797018963968 + 981468462750861/4503599627370496
                        self.fos_array2[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'GRANULAR MEDIUM':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.179;
                        theta_i_max = 0.392;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[j-1,i-1] = (2395554010573903*(x1**3)*x5)/9007199254740992 - (1584791230571555*(x1**2)*x2*x3)/1125899906842624 - (8675059321513597*(x1**2))/36028797018963968 + (2712053627057047*x1*x2*x3)/1125899906842624 - (436588234554137*x1*x3*x5)/562949953421312 + (8696742236362029*x1*x3)/18014398509481984 + (84167422866237*x1*x4)/1125899906842624 + (5038972167706281*(x2**3)*x5)/1125899906842624 - (2769339911649845*(x2**3))/562949953421312 - (5816346030793635*(x2**2)*(x4**2))/18014398509481984 - (2296851704845541*(x2**2)*x5)/281474976710656 + (4711729450227555*(x2**2))/562949953421312 + (4526012208234625*x2*x3*x5)/2251799813685248 - (1438367102275171*x2*x3)/562949953421312 + (3235555885457197*x2*(x4**3))/18014398509481984 - (6984536435614461*x2*(x5**3))/18014398509481984 + (4734726859996689*x2*x5)/1125899906842624 - (8887739276337299*x2)/2251799813685248 + (7909776872928529*(x3**2))/36028797018963968 + (4825069300825317*x3*x4)/144115188075855872 + (1932527580330421*x3*(x5**2))/2251799813685248 - (7088385317352909*x3*x5)/4503599627370496 - (6028859269012785*x3)/36028797018963968 - (4457058916701155*(x4**2))/18014398509481984 + (205865104591035*x4)/281474976710656 - (1093234104604003*x5)/2251799813685248 + 4657821803862761/9007199254740992;
                        self.fos_array2[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'GRANULAR FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.188;
                        theta_i_max = 0.412;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[j-1,i-1] = (5997468984231391*x4)/9007199254740992 - (5850653107015129*x2)/2251799813685248 - (2903074490076611*x1)/4503599627370496 - (4978764466261023*x5)/18014398509481984 + (2497394100991123*x1*x2)/1125899906842624 + (1094809215253921*x1*x3)/1125899906842624 + (7011891843826591*x1*x4)/36028797018963968 - (137137518003759*x2*x3)/35184372088832 + (6916471811591635*x1*x5)/18014398509481984 - (5185975094203355*x2*x4)/576460752303423488 + (6973754261875579*x2*x5)/9007199254740992 - (6728904517417159*x3*x5)/9007199254740992 - (5049272361606063*x1*(x2**2))/2251799813685248 + (8151483504101627*x1*(x3**2))/18014398509481984 + (7836140676118751*(x2**2)*x3)/2251799813685248 - (103490230972707*(x1**3)*x4)/562949953421312 - (2508927668464753*(x2**3)*x3)/2251799813685248 + (1751145175163683*(x2**2))/562949953421312 - (2910103121418035*(x4**2))/18014398509481984 - (4149956958460727*(x1**2)*x2*x3)/4503599627370496 - (2909406058924355*x1*(x2**2)*x5)/1125899906842624 + (4267265215922321*(x1**3)*x2*x5)/4503599627370496 + (5734832464949375*x1*x3*(x5**3))/18014398509481984 - (4082556226690241*(x1**2)*(x3**2)*x4)/36028797018963968 - (883679796825111*x1*x3*x5)/562949953421312 + (3185546221473745*x2*x3*x5)/1125899906842624 + 1119623049971351/2251799813685248;
                        self.fos_array2[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'MEDIUM':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.179;
                        theta_i_max = 0.392;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[j-1,i-1] = - (7605402998259809*(x1**3)*x6)/9007199254740992 + (5433101380788941*(x1**2)*(x6**2))/9007199254740992 + (5438216367263101*(x1**2)*x6)/4503599627370496 + (6933674839011865*x1*x2)/18014398509481984 - (3183093811021595*x1*x3)/18014398509481984 - (6604577520812421*x1*x4*x5)/36028797018963968 - (6677569571403873*x1*x4*x6)/18014398509481984 + (5492449447091975*x1*x5*x6)/144115188075855872 + (5423482706553025*x1*x5)/18014398509481984 - (690523320510537*x1*x6)/562949953421312 - (3321581480764011*(x2**3)*(x6**2))/2251799813685248 + (4144557554361693*(x2**2))/4503599627370496 - (5247773900528281*x2*x3)/18014398509481984 + (912731872269751*x2*(x4**2))/4503599627370496 - (4408639353815769*x2*x5)/36028797018963968 + (8395993053582923*x2*x6)/4503599627370496 - (8532874373358735*x2)/4503599627370496 + (4503753517663555*(x3**2))/9007199254740992 + (5623770062789117*x3*x4*x5)/18014398509481984 - (4581567852841661*x3*(x5**2))/18014398509481984 + (6873632408613219*x3*(x6**3))/18014398509481984 - (2940490725035801*x3*x6)/4503599627370496 - (2371501908453915*x3)/4503599627370496 - (947262250475269*(x4**2))/2251799813685248 + (7492475340553871*x4*(x5**2)*x6)/576460752303423488 - (4920950276662705*x4*x5)/18014398509481984 + (1219489943909891*x4*x6)/9007199254740992 + (8174395509123883*x4)/9007199254740992 + (1206779442258227*(x5**2))/18014398509481984 + (3236337280494743*x5)/9007199254740992 - (2948601616754633*(x6**2))/9007199254740992 + 8820801393289007/18014398509481984;
                        self.fos_array2[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'MEDIUM FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.188;
                        theta_i_max = 0.412;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[j-1,i-1] =  (3886190004610709*x4)/4503599627370496 - (5729276149747483*x3)/9007199254740992 - (6788231717529895*x2)/2251799813685248 + (479426134057027*x5)/1125899906842624 - (2555014444031809*x6)/4503599627370496 + (8284280323761517*x1*x3)/36028797018963968 - (5766260012425305*x1*x4)/9007199254740992 - (525466186966067*x2*x3)/562949953421312 + (3559543339455779*x1*x5)/18014398509481984 + (3044854372294711*x2*x4)/2251799813685248 + (2604085627039555*x2*x6)/1125899906842624 + (7021469540150699*x3*x5)/288230376151711744 - (231180365885025*x3*x6)/562949953421312 - (2434138700745953*x4*x5)/9007199254740992 - (2798606821472435*(x2**2)*x4)/1125899906842624 - (4787498997851079*(x2**2)*x6)/2251799813685248 + (6336213524232577*(x2**2))/2251799813685248 + (8898687912479801*(x3**2))/18014398509481984 - (6956481687155787*(x4**2))/18014398509481984 - (6059931181255597*(x5**2))/144115188075855872 + (3017676058392109*x1*x2*(x4**2))/9007199254740992 - (424322724646621*(x2**2)*x3*x4)/9007199254740992 + (8194181095609791*x1*(x3**2)*(x6**2))/72057594037927936 + (4040226326314105*x1*x2*x4)/4503599627370496 + (6767925566021999*x1*x2*x6)/36028797018963968 + (4332927401162267*x2*x3*x4)/9007199254740992 - (6054326828217865*x1*x3*x6)/9007199254740992 - (1182428728719139*x2*x3*x5)/4503599627370496 - (3671852565176795*x1*x4*x6)/36028797018963968 + (5352375486130983*x2*x3*x6)/4503599627370496 + (3079416316199729*x3*x4*x6)/9007199254740992 - (5765496138098037*x2*x3*x4*x6)/9007199254740992 + 3442293244771261/4503599627370496;
                        self.fos_array2[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.327;
                        theta_i_max = 0.481;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[j-1,i-1] = (8711105383099221*(x1**2))/72057594037927936 + (4480937614520491*x1*x2*x3*x6)/4503599627370496 + (6445291833574493*x1*x2*x4*(x6**2))/576460752303423488 - (281440029914825*x1*(x3**2)*x6)/562949953421312 - (6629445291354447*x1*x3*x4)/18014398509481984 + (849190321960673*x1*x3*x5)/2251799813685248 - (6187137339255229*x1*x4*x6)/18014398509481984 - (4624215388296035*x1*x6)/18014398509481984 - (1587486474559393*(x2**3)*x6)/1125899906842624 - (4900095579043665*(x2**2)*x4)/4503599627370496 + (1169434422300945*(x2**2))/562949953421312 - (7554405290076481*x2*x3*x4*x5*x6)/72057594037927936 - (7246543431362679*x2*x3*x5)/36028797018963968 - (721288367741207*x2*x3)/1125899906842624 + (8836698625396407*x2*x4*(x5**2))/144115188075855872 + (4781016702927063*x2*x4)/4503599627370496 + (4010700648742253*x2*x6)/2251799813685248 - (2883657241266265*x2)/1125899906842624 - (6577851316887483*(x3**3))/18014398509481984 + (2688469612731583*(x3**2))/2251799813685248 + (6653205645687021*x3*(x4**2)*(x6**2))/18014398509481984 - (2099413330989821*x3*(x4**2))/4503599627370496 + (6161799069262313*x3*x4)/9007199254740992 + (1857306243852377*x3*x5*x6)/9007199254740992 - (2865566660442267*x3*x5)/9007199254740992 - (4614774789911059*x3*x6)/9007199254740992 - (1937328245404209*x3)/2251799813685248 - (7930907804563573*(x4**2))/36028797018963968 - (4754832626658037*x4*x5)/18014398509481984 + (171256162149423*x4)/281474976710656 - (8578558619551665*(x5**2)*x6)/288230376151711744 + (8704230461968029*x5)/18014398509481984 - (3382315052029319*(x6**3))/1152921504606846976 - (6812374621577823*x6)/18014398509481984 + 6174808073279873/9007199254740992;
                        self.fos_array2[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'VERY FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.392;
                        theta_i_max = 0.538;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array2[j-1,i-1] = (3443522597856495*x4)/4503599627370496 - (2348315328800215*x2)/1125899906842624 - (8559581679713667*x1)/36028797018963968 + (8018106863502985*x5)/18014398509481984 - (4230345748317103*x6)/9007199254740992 - (1544138636456145*(x4**2)*(x6**2))/18014398509481984 + (902528602503447*x1*x2)/1125899906842624 - (7043808527068311*x2*x3)/4503599627370496 - (7246008324732221*x1*x6)/18014398509481984 + (1747413719569329*x2*x6)/1125899906842624 - (2597399368633979*x3*x6)/4503599627370496 - (2391652988631193*x4*x5)/4503599627370496 + (6181389039177289*x1*(x3**2))/9007199254740992 - (5186363803500845*x1*(x5**2))/36028797018963968 - (2321574606811609*x2*(x5**2))/72057594037927936 - (2543509902109129*x3*(x4**2))/9007199254740992 + (2780023057880475*(x1**2)*x6)/9007199254740992 + (3526997481352009*(x2**2))/4503599627370496 - (7277171475332687*(x4**3))/72057594037927936 + (5569296935854231*x1*x4*(x5**2))/18014398509481984 + (5469000151567747*(x3**2)*x4*x5)/18014398509481984 + (651427578412907*x1*x2*x5)/1125899906842624 - (3056278760769427*x1*x3*x4)/4503599627370496 - (2474169676151269*x1*x3*x5)/18014398509481984 + (5800416867896625*x2*x3*x4)/4503599627370496 - (6838031967161513*x1*x3*x6)/9007199254740992 - (2410625286488745*x2*x3*x5)/9007199254740992 + (5260456502000859*x2*x3*x6)/4503599627370496 + (2296168764961959*x1*x5*x6)/4503599627370496 + (8412632997477619*x3*x4*x6)/18014398509481984 - (8539609750453113*x1*x2*x5*x6)/9007199254740992 - (5748018464844461*x1*(x2**2)*x4*x6)/4503599627370496 + 6230592657726943/9007199254740992;
                        self.fos_array2[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]

                    # self.fos_array[j,i] = (1605074512383065*(alpha**2)*(c**2)*(h**2)*phi)/151115727451828646838272 - (1414963042633059*(alpha**2)*(c**2)*h*phi)/18889465931478580854784 - (2774717211173289*(alpha**2)*(c**2)*hw*phi)/604462909807314587353088 + (2835477809945801*(alpha**2)*(c**2)*phi)/37778931862957161709568 + (6731555515546295*(alpha**2)*c)/73786976294838206464 + (5516753565726847*(alpha**2)*phi)/147573952589676412928 + (5653461066590515*alpha*(c**2)*h)/590295810358705651712 + (3025671568382675*alpha*(c**2)*phi)/590295810358705651712 - (2098110323770171*alpha*(c**2))/36893488147419103232 - (3002978305542275*alpha*c*(h**2))/4611686018427387904 + (2687741203999111*alpha*c*h)/576460752303423488 + (6472386681360727*alpha*c*hw*phi)/590295810358705651712 - (2982096583892561*alpha*c*(phi**2))/2361183241434822606848 - (4627184841729915*alpha*c)/288230376151711744 - (5688086807612743*alpha*(phi**2))/590295810358705651712 - (4311146912769217*alpha*phi)/1152921504606846976 - (4976341265194569*(c**2)*(h**2)*phi)/147573952589676412928 + (2283034929082703*(c**2)*h*phi)/9223372036854775808 + (1342385546936077*(c**2)*hw*phi)/147573952589676412928 - (1295331185150365*(c**2)*phi)/2305843009213693952 + (2592141320026855*c*(h**2))/72057594037927936 - (4971891995221437*c*h)/18014398509481984 - (4809409727287499*c*hw*phi)/9223372036854775808 + (2265715759669333*c*(phi**2))/36893488147419103232 + (3352624142374595*c)/4503599627370496 + (20768301037335*(h**2)*(hw**2)*phi)/2305843009213693952 - (1324783938325601*hw)/36028797018963968 + (3497832476657703*(phi**2))/4611686018427387904 + (6865366199800263*phi)/72057594037927936 + 1489595912300695/9007199254740992;

            z = np.array(imgx)
            self.fos_array3 = self.fos_array2.copy()
            for i in range(1,imgx.size[0]-1):
                for j in range(1,imgx.size[1]):
                    if self.fos_array2[j-1,i-1] > 2:
                        self.fos_array3[j-1,i-1] = float("NaN")
                        self.fos_array2[j-1,i-1] = 2 #float("NaN")
                        # self.fos_array3[j-1,i-1] = float("NaN")
                        z[j-1,i-1] = float("NaN")
            for i in range(1,imgx.size[0]-1):
                for j in range(1,imgx.size[1]):
                    if self.fos_array2[j-1,i-1] < 1:
                        self.fos_array2[j-1,i-1] = 1
                        self.fos_array3[j-1,i-1] = 1

            x2 = self.fos_array2.shape[0]
            y2 = self.fos_array2.shape[1]

            lin_x = np.linspace(0,1,self.fos_array.shape[0],endpoint=False)
            lin_y = np.linspace(0,1,self.fos_array.shape[1],endpoint=False)
            y,x = np.meshgrid(lin_y,lin_x)
            ##############  z = np.array(imgx)

            fig_fos, ax = plt.subplots(subplot_kw=dict(projection="3d"), constrained_layout=1, figsize=(12, 10))#(6, 5)
            norm1 = plt.Normalize(vmin= self.fos_array2.min().min(), vmax= self.fos_array2.max().max())

            # z = np.flipud(z)
            # self.fos_array2 = np.flipud(self.fos_array2)

            xA = np.flipud(x.transpose()[2:x2-2, 2:y2-2])
            yA = np.flipud(y.transpose()[2:x2-2, 2:y2-2])
            zA = np.flipud(z.transpose()[2:x2-2, 2:y2-2])
            self.fos_array2A = np.flipud(self.fos_array2.transpose()[2:x2-2, 2:y2-2])

            z = np.flipud(z)
            self.fos_array2 = np.flipud(self.fos_array2)

            #print("X size: ", x.shape)
            #print("Y size: ", y.shape)
            #print("Z size: ", z.shape)
            #print("Fos size: ", self.fos_array2.shape)
            #print("X2: ", x2)
            #print("Y2: ", y2)


            #ax.plot_surface(x.transpose()[0:x2, 5:y2], y.transpose()[0:x2, 5:y2], z.transpose()[0:x2, 2:y2], facecolors= plt.cm.rainbow_r(norm1(self.fos_array2.transpose()[0:x2, 2:y2])), antialiased=False, shade=False)
            ax.plot_surface(x.transpose()[2:y2-2, 2:x2], y.transpose()[2:y2-2, 2:x2], z.transpose()[2:y2-2, 2:x2], facecolors= plt.cm.rainbow_r(norm1(self.fos_array2.transpose()[2:y2-2, 2:x2])), antialiased=False, shade=False)
            
            
            #(x.transpose()[0:x2+1, 0:y2], y.transpose()[0:x2+1, 0:y2], z.transpose()[0:x2+1, 0:y2], facecolors= plt.cm.rainbow_r(norm1(self.fos_array2.transpose()[0:x2+1, 0:y2])), antialiased=False, shade=False)
            #x[2:x2-2, 2:y2-2], y[2:x2-2, 2:y2-2], z[2:x2-2, 2:y2-2], facecolors= plt.cm.rainbow_r(norm1(self.fos_array2[2:x2-2, 2:y2-2])), antialiased=False, shade=False) 
            # #np.flipud(x.transpose()[2:x2-2, 2:y2-2]), np.flipud(y.transpose()[2:x2-2, 2:y2-2]), np.flipud(z.transpose()[2:x2-2, 2:y2-2]), facecolors= plt.cm.rainbow_r(norm1(np.flipud(self.fos_array2.transpose()[2:x2-2, 2:y2-2]))), antialiased=False, shade=False)
            m = mpl.cm.ScalarMappable(cmap= plt.cm.rainbow_r, norm= norm1)
            m.set_array(self.fos_array2.transpose())
            plt.colorbar(m, ax= ax, location= "right")

            plt.xticks([])
            plt.yticks([])
            # ax.grid(False)
            # plt.axis('off')

            self.canvas_fos = FigureCanvas(fig_fos)
            self.toolb_fos = NavigationToolbar(self.canvas_fos, self)

            self.tabInc = QWidget()
            self.tabInc_layout = QVBoxLayout()
            self.tabInc_layout.addWidget(self.canvas_fos)
            self.tabInc_layout.addWidget(self.toolb_fos)
            self.tabInc.setLayout(self.tabInc_layout)

            #self.tabInc.setMaximumSize(int(self.width()/2), int(self.height()))

            self.tab_name = "Segurança (3D) " + str(self.inclina_tabs)
            self.tabs_2.addTab(self.tabInc,self.tab_name)

            plt.close('all')

            ############################################################################################################

            cmap = plt.get_cmap('rainbow_r')

            self.fos_array3 = np.flipud(self.fos_array3)

            plt.imshow(np.flipud(self.fos_array3), cmap)
            im_fos = ax2.imshow(np.flipud(self.fos_array3), cmap)

            ax2.set_yticks([0, 0.2*(imgx.size[1]-2), 0.4*(imgx.size[1]-2), 0.6*(imgx.size[1]-2), 0.8*(imgx.size[1]-2), (imgx.size[1]-2)], labels=[0, 5*(imgx.size[1]), 10*(imgx.size[1]), 15*(imgx.size[1]), 20*(imgx.size[1]), 25*(imgx.size[1])])
            ax2.set_xticks([0, 0.2*(imgx.size[0]-2), 0.4*(imgx.size[0]-2), 0.6*(imgx.size[0]-2), 0.8*(imgx.size[0]-2), (imgx.size[0]-2)], labels=[0, 5*(imgx.size[0]), 10*(imgx.size[0]), 15*(imgx.size[0]), 20*(imgx.size[0]), 25*(imgx.size[0])])

            ax2.set_xlim(0, (imgx.size[0]-2))
            ax2.set_ylim(0, (imgx.size[1]-2))

            # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            # print(imgx.size[0])
            # print(imgx.size[1])

            plt.colorbar(im_fos,ax=ax2)
            plt.axis([0, (imgx.size[0]-2), 0, (imgx.size[1]-2)])
            # ax2.invert_yaxis()

            ##################################################
            ax.view_init(elev= elev, azim= azim, roll= roll)
            ##################################################

            self.canvas_fos2 = FigureCanvas(fig_fos2)
            self.toolb_fos2 = NavigationToolbar(self.canvas_fos2, self)

            self.tabInc2 = QWidget()
            self.tabInc_layout2 = QVBoxLayout()

            #print(int(self.height()))
            #w = int(str(self.width()))
            #h = int(str(self.height()))
            #self.tabInc_layout2.SetMaximumSize(1500/2, 800/2) #int(self.width())/2, int(self.height())/2)

            self.tabInc_layout2.addWidget(self.canvas_fos2)
            self.tabInc_layout2.addWidget(self.toolb_fos2)
            self.tabInc2.setLayout(self.tabInc_layout2)

            self.tab_name2 = "Segurança (2D) " + str(self.inclina_tabs)
            self.tabs_2.addTab(self.tabInc2,self.tab_name2)

            def on_click(event):
                global azim
                global elev
                azim, elev = ax.azim, ax.elev

            cid = fig_fos.canvas.mpl_connect('button_release_event', on_click)

            ################################## NÃO DELETAR #######################################

            # cmap = plt.get_cmap('rainbow_r')

            # plt.imshow(self.fos_array2, cmap)
            # im_fos = ax.imshow(self.fos_array2, cmap)

            # ax.set_yticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1], imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])
            # ax.set_xticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0], imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])

            # plt.colorbar(im_fos,ax=ax)
            # plt.axis([0, imgx.size[0], 0, imgx.size[1]])
            # ax.invert_yaxis()


            #######################################################################################################################################################

            #self.tabInc2.setMaximumSize(int(self.width()/2), int(self.height()))
            self.tabs_2.setMinimumSize(int(self.width()/2), int(self.height()/2))

        # #

        if self.tabs_2.count() >= 3:
            self.tabs_2.removeTab(0)
            self.tabs_2.removeTab(0)
        #

        self.tabs_2.setCurrentIndex(self.tabAtual)

        plt.close('all')

        print("runAnalysis")
        # self.runAnalysis2()
    #

    def runAnalysis2(self):
        self.tabs_2.removeTab(-1)

        global fname
        global azim
        global elev
        global roll

        fname = self.imgname.text()     ###
        imgx = Image.open(fname)           ###

        self.tabAtual = self.tabs_2.currentIndex()
        # self.tabs.setVisible(True)
        self.tabs_2.setVisible(True)

        X1 = int(self.x1lineEdit.text())
        X2 = int(self.x2lineEdit.text())
        y1 = int(self.y1lineEdit.text())
        y2 = int(self.y2lineEdit.text())

        h_value = self.horizontalSlider_H.value()/10;
        hw_value = self.horizontalSlider_Hw.value();
        c_value = self.horizontalSlider_C.value()/10;
        phi_value = self.horizontalSlider_Phi.value();
        theta_value = self.horizontalSlider_Theta.value();

        c = c_value
        h = h_value
        phi = phi_value
        hw = h_value * hw_value/100
        theta_i = theta_value/1000
        #self.fos_array = np.ones((imgx.size[1],imgx.size[0]))   #[x1:x2, y1:y2]
        self.fos_array = np.ones((imgx.size[0],imgx.size[1]))

        # Creating figure
        self.fos_array = self.fos_array.transpose()

        if self.number_of_adjusts >= 1:
            self.fos_array = self.fos_array.transpose()
            self.fos_array = self.fos_array[y1-1:y2, X1-1:X2]

            sizey = X2-X1
            sizex = y2-y1

            for i in range(0, sizex):
                for j in range(0, sizey):
                    alpha = self.g_max[y1+i,X1+j]   #[x1+j,y1+i]

                    if self.material_type == 'COARSE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.046;
                        theta_i_max = 0.365;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min)

                        self.fos_array[i-1,j-1] = (6788110953151657*(x1**2)*(x2**2)*x5)/18014398509481984 + (1355958164086877*(x1**2)*x3*(x4**2)*x5)/9007199254740992 - (8873610522459485*(x1**2)*(x4**2)*x5)/72057594037927936 - (1692657047651061*(x1**2))/18014398509481984 - (3851498880822799*x1*(x2**2)*x3)/1125899906842624 + (2526110258615389*x1*x2*(x3**2))/1125899906842624 + (2706917046260173*x1*x2)/9007199254740992 - (3556745139181571*x1*(x3**3)*x4)/9007199254740992 - (579938420281673*x1*(x3**2))/1125899906842624 + (8180563435756073*x1*x3*x4)/36028797018963968 + (3114137794295375*x1*x3)/9007199254740992 - (8586273326384709*x1*x5)/144115188075855872 + (3545170951606327*(x2**2)*(x3**2))/4503599627370496 + (8665832770244175*(x2**2)*x3)/4503599627370496 - (7818372289906591*(x2**2)*x5)/4503599627370496 + (2684009153708421*(x2**2))/2251799813685248 - (4201502816181941*x2*(x3**2))/2251799813685248 - (3562767927008791*x2*x3*x4)/36028797018963968 + (2328059298502727*x2*x3*x5)/9007199254740992 + (8830399494179771*x2*x4*(x5**2))/72057594037927936 + (5482565565501159*x2*x5)/4503599627370496 - (2681827153050867*x2)/2251799813685248 + (8730627984475617*(x3**2)*x4)/72057594037927936 + (1323618450977937*(x3**2))/2251799813685248 - (5618799156698347*x3*x5)/36028797018963968 - (4911690079918821*x3)/4503599627370496 - (7212846679305375*(x4**2))/36028797018963968 - (2144834721434649*x4*x5)/288230376151711744 + (6420485161231939*x4)/9007199254740992 - (6209185403811853*x5)/36028797018963968 + 981468462750861/4503599627370496
                        self.fos_array[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'GRANULAR MEDIUM':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.179;
                        theta_i_max = 0.392;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[i-1,j-1] = (2395554010573903*(x1**3)*x5)/9007199254740992 - (1584791230571555*(x1**2)*x2*x3)/1125899906842624 - (8675059321513597*(x1**2))/36028797018963968 + (2712053627057047*x1*x2*x3)/1125899906842624 - (436588234554137*x1*x3*x5)/562949953421312 + (8696742236362029*x1*x3)/18014398509481984 + (84167422866237*x1*x4)/1125899906842624 + (5038972167706281*(x2**3)*x5)/1125899906842624 - (2769339911649845*(x2**3))/562949953421312 - (5816346030793635*(x2**2)*(x4**2))/18014398509481984 - (2296851704845541*(x2**2)*x5)/281474976710656 + (4711729450227555*(x2**2))/562949953421312 + (4526012208234625*x2*x3*x5)/2251799813685248 - (1438367102275171*x2*x3)/562949953421312 + (3235555885457197*x2*(x4**3))/18014398509481984 - (6984536435614461*x2*(x5**3))/18014398509481984 + (4734726859996689*x2*x5)/1125899906842624 - (8887739276337299*x2)/2251799813685248 + (7909776872928529*(x3**2))/36028797018963968 + (4825069300825317*x3*x4)/144115188075855872 + (1932527580330421*x3*(x5**2))/2251799813685248 - (7088385317352909*x3*x5)/4503599627370496 - (6028859269012785*x3)/36028797018963968 - (4457058916701155*(x4**2))/18014398509481984 + (205865104591035*x4)/281474976710656 - (1093234104604003*x5)/2251799813685248 + 4657821803862761/9007199254740992;
                        self.fos_array[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'GRANULAR FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.188;
                        theta_i_max = 0.412;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[i-1,j-1] = (5997468984231391*x4)/9007199254740992 - (5850653107015129*x2)/2251799813685248 - (2903074490076611*x1)/4503599627370496 - (4978764466261023*x5)/18014398509481984 + (2497394100991123*x1*x2)/1125899906842624 + (1094809215253921*x1*x3)/1125899906842624 + (7011891843826591*x1*x4)/36028797018963968 - (137137518003759*x2*x3)/35184372088832 + (6916471811591635*x1*x5)/18014398509481984 - (5185975094203355*x2*x4)/576460752303423488 + (6973754261875579*x2*x5)/9007199254740992 - (6728904517417159*x3*x5)/9007199254740992 - (5049272361606063*x1*(x2**2))/2251799813685248 + (8151483504101627*x1*(x3**2))/18014398509481984 + (7836140676118751*(x2**2)*x3)/2251799813685248 - (103490230972707*(x1**3)*x4)/562949953421312 - (2508927668464753*(x2**3)*x3)/2251799813685248 + (1751145175163683*(x2**2))/562949953421312 - (2910103121418035*(x4**2))/18014398509481984 - (4149956958460727*(x1**2)*x2*x3)/4503599627370496 - (2909406058924355*x1*(x2**2)*x5)/1125899906842624 + (4267265215922321*(x1**3)*x2*x5)/4503599627370496 + (5734832464949375*x1*x3*(x5**3))/18014398509481984 - (4082556226690241*(x1**2)*(x3**2)*x4)/36028797018963968 - (883679796825111*x1*x3*x5)/562949953421312 + (3185546221473745*x2*x3*x5)/1125899906842624 + 1119623049971351/2251799813685248;
                        self.fos_array[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'MEDIUM':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.179;
                        theta_i_max = 0.392;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[i-1,j-1] = - (7605402998259809*(x1**3)*x6)/9007199254740992 + (5433101380788941*(x1**2)*(x6**2))/9007199254740992 + (5438216367263101*(x1**2)*x6)/4503599627370496 + (6933674839011865*x1*x2)/18014398509481984 - (3183093811021595*x1*x3)/18014398509481984 - (6604577520812421*x1*x4*x5)/36028797018963968 - (6677569571403873*x1*x4*x6)/18014398509481984 + (5492449447091975*x1*x5*x6)/144115188075855872 + (5423482706553025*x1*x5)/18014398509481984 - (690523320510537*x1*x6)/562949953421312 - (3321581480764011*(x2**3)*(x6**2))/2251799813685248 + (4144557554361693*(x2**2))/4503599627370496 - (5247773900528281*x2*x3)/18014398509481984 + (912731872269751*x2*(x4**2))/4503599627370496 - (4408639353815769*x2*x5)/36028797018963968 + (8395993053582923*x2*x6)/4503599627370496 - (8532874373358735*x2)/4503599627370496 + (4503753517663555*(x3**2))/9007199254740992 + (5623770062789117*x3*x4*x5)/18014398509481984 - (4581567852841661*x3*(x5**2))/18014398509481984 + (6873632408613219*x3*(x6**3))/18014398509481984 - (2940490725035801*x3*x6)/4503599627370496 - (2371501908453915*x3)/4503599627370496 - (947262250475269*(x4**2))/2251799813685248 + (7492475340553871*x4*(x5**2)*x6)/576460752303423488 - (4920950276662705*x4*x5)/18014398509481984 + (1219489943909891*x4*x6)/9007199254740992 + (8174395509123883*x4)/9007199254740992 + (1206779442258227*(x5**2))/18014398509481984 + (3236337280494743*x5)/9007199254740992 - (2948601616754633*(x6**2))/9007199254740992 + 8820801393289007/18014398509481984;
                        self.fos_array[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'MEDIUM FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.188;
                        theta_i_max = 0.412;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[i-1,j-1] =  (3886190004610709*x4)/4503599627370496 - (5729276149747483*x3)/9007199254740992 - (6788231717529895*x2)/2251799813685248 + (479426134057027*x5)/1125899906842624 - (2555014444031809*x6)/4503599627370496 + (8284280323761517*x1*x3)/36028797018963968 - (5766260012425305*x1*x4)/9007199254740992 - (525466186966067*x2*x3)/562949953421312 + (3559543339455779*x1*x5)/18014398509481984 + (3044854372294711*x2*x4)/2251799813685248 + (2604085627039555*x2*x6)/1125899906842624 + (7021469540150699*x3*x5)/288230376151711744 - (231180365885025*x3*x6)/562949953421312 - (2434138700745953*x4*x5)/9007199254740992 - (2798606821472435*(x2**2)*x4)/1125899906842624 - (4787498997851079*(x2**2)*x6)/2251799813685248 + (6336213524232577*(x2**2))/2251799813685248 + (8898687912479801*(x3**2))/18014398509481984 - (6956481687155787*(x4**2))/18014398509481984 - (6059931181255597*(x5**2))/144115188075855872 + (3017676058392109*x1*x2*(x4**2))/9007199254740992 - (424322724646621*(x2**2)*x3*x4)/9007199254740992 + (8194181095609791*x1*(x3**2)*(x6**2))/72057594037927936 + (4040226326314105*x1*x2*x4)/4503599627370496 + (6767925566021999*x1*x2*x6)/36028797018963968 + (4332927401162267*x2*x3*x4)/9007199254740992 - (6054326828217865*x1*x3*x6)/9007199254740992 - (1182428728719139*x2*x3*x5)/4503599627370496 - (3671852565176795*x1*x4*x6)/36028797018963968 + (5352375486130983*x2*x3*x6)/4503599627370496 + (3079416316199729*x3*x4*x6)/9007199254740992 - (5765496138098037*x2*x3*x4*x6)/9007199254740992 + 3442293244771261/4503599627370496;
                        self.fos_array[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.327;
                        theta_i_max = 0.481;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[i-1,j-1] = (8711105383099221*(x1**2))/72057594037927936 + (4480937614520491*x1*x2*x3*x6)/4503599627370496 + (6445291833574493*x1*x2*x4*(x6**2))/576460752303423488 - (281440029914825*x1*(x3**2)*x6)/562949953421312 - (6629445291354447*x1*x3*x4)/18014398509481984 + (849190321960673*x1*x3*x5)/2251799813685248 - (6187137339255229*x1*x4*x6)/18014398509481984 - (4624215388296035*x1*x6)/18014398509481984 - (1587486474559393*(x2**3)*x6)/1125899906842624 - (4900095579043665*(x2**2)*x4)/4503599627370496 + (1169434422300945*(x2**2))/562949953421312 - (7554405290076481*x2*x3*x4*x5*x6)/72057594037927936 - (7246543431362679*x2*x3*x5)/36028797018963968 - (721288367741207*x2*x3)/1125899906842624 + (8836698625396407*x2*x4*(x5**2))/144115188075855872 + (4781016702927063*x2*x4)/4503599627370496 + (4010700648742253*x2*x6)/2251799813685248 - (2883657241266265*x2)/1125899906842624 - (6577851316887483*(x3**3))/18014398509481984 + (2688469612731583*(x3**2))/2251799813685248 + (6653205645687021*x3*(x4**2)*(x6**2))/18014398509481984 - (2099413330989821*x3*(x4**2))/4503599627370496 + (6161799069262313*x3*x4)/9007199254740992 + (1857306243852377*x3*x5*x6)/9007199254740992 - (2865566660442267*x3*x5)/9007199254740992 - (4614774789911059*x3*x6)/9007199254740992 - (1937328245404209*x3)/2251799813685248 - (7930907804563573*(x4**2))/36028797018963968 - (4754832626658037*x4*x5)/18014398509481984 + (171256162149423*x4)/281474976710656 - (8578558619551665*(x5**2)*x6)/288230376151711744 + (8704230461968029*x5)/18014398509481984 - (3382315052029319*(x6**3))/1152921504606846976 - (6812374621577823*x6)/18014398509481984 + 6174808073279873/9007199254740992;
                        self.fos_array[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]
                    elif self.material_type == 'VERY FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.392;
                        theta_i_max = 0.538;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[i-1,j-1] = (3443522597856495*x4)/4503599627370496 - (2348315328800215*x2)/1125899906842624 - (8559581679713667*x1)/36028797018963968 + (8018106863502985*x5)/18014398509481984 - (4230345748317103*x6)/9007199254740992 - (1544138636456145*(x4**2)*(x6**2))/18014398509481984 + (902528602503447*x1*x2)/1125899906842624 - (7043808527068311*x2*x3)/4503599627370496 - (7246008324732221*x1*x6)/18014398509481984 + (1747413719569329*x2*x6)/1125899906842624 - (2597399368633979*x3*x6)/4503599627370496 - (2391652988631193*x4*x5)/4503599627370496 + (6181389039177289*x1*(x3**2))/9007199254740992 - (5186363803500845*x1*(x5**2))/36028797018963968 - (2321574606811609*x2*(x5**2))/72057594037927936 - (2543509902109129*x3*(x4**2))/9007199254740992 + (2780023057880475*(x1**2)*x6)/9007199254740992 + (3526997481352009*(x2**2))/4503599627370496 - (7277171475332687*(x4**3))/72057594037927936 + (5569296935854231*x1*x4*(x5**2))/18014398509481984 + (5469000151567747*(x3**2)*x4*x5)/18014398509481984 + (651427578412907*x1*x2*x5)/1125899906842624 - (3056278760769427*x1*x3*x4)/4503599627370496 - (2474169676151269*x1*x3*x5)/18014398509481984 + (5800416867896625*x2*x3*x4)/4503599627370496 - (6838031967161513*x1*x3*x6)/9007199254740992 - (2410625286488745*x2*x3*x5)/9007199254740992 + (5260456502000859*x2*x3*x6)/4503599627370496 + (2296168764961959*x1*x5*x6)/4503599627370496 + (8412632997477619*x3*x4*x6)/18014398509481984 - (8539609750453113*x1*x2*x5*x6)/9007199254740992 - (5748018464844461*x1*(x2**2)*x4*x6)/4503599627370496 + 6230592657726943/9007199254740992;
                        self.fos_array[i-1,j-1] = 10 ** self.fos_array[i-1,j-1]

                    # self.fos_array[i,j] = (1605074512383065*(alpha**2)*(c**2)*(h**2)*phi)/151115727451828646838272 - (1414963042633059*(alpha**2)*(c**2)*h*phi)/18889465931478580854784 - (2774717211173289*(alpha**2)*(c**2)*hw*phi)/604462909807314587353088 + (2835477809945801*(alpha**2)*(c**2)*phi)/37778931862957161709568 + (6731555515546295*(alpha**2)*c)/73786976294838206464 + (5516753565726847*(alpha**2)*phi)/147573952589676412928 + (5653461066590515*alpha*(c**2)*h)/590295810358705651712 + (3025671568382675*alpha*(c**2)*phi)/590295810358705651712 - (2098110323770171*alpha*(c**2))/36893488147419103232 - (3002978305542275*alpha*c*(h**2))/4611686018427387904 + (2687741203999111*alpha*c*h)/576460752303423488 + (6472386681360727*alpha*c*hw*phi)/590295810358705651712 - (2982096583892561*alpha*c*(phi**2))/2361183241434822606848 - (4627184841729915*alpha*c)/288230376151711744 - (5688086807612743*alpha*(phi**2))/590295810358705651712 - (4311146912769217*alpha*phi)/1152921504606846976 - (4976341265194569*(c**2)*(h**2)*phi)/147573952589676412928 + (2283034929082703*(c**2)*h*phi)/9223372036854775808 + (1342385546936077*(c**2)*hw*phi)/147573952589676412928 - (1295331185150365*(c**2)*phi)/2305843009213693952 + (2592141320026855*c*(h**2))/72057594037927936 - (4971891995221437*c*h)/18014398509481984 - (4809409727287499*c*hw*phi)/9223372036854775808 + (2265715759669333*c*(phi**2))/36893488147419103232 + (3352624142374595*c)/4503599627370496 + (20768301037335*(h**2)*(hw**2)*phi)/2305843009213693952 - (1324783938325601*hw)/36028797018963968 + (3497832476657703*(phi**2))/4611686018427387904 + (6865366199800263*phi)/72057594037927936 + 1489595912300695/9007199254740992;

            z = np.array(imgx)[y1-1:y2, X1-1:X2]
            self.fos_array2 = self.fos_array.copy()
            for i in range(0, sizex):
                for j in range(0, sizey):
                    if self.fos_array[i-1,j-1] > 2:
                        self.fos_array[i-1,j-1] = 2 #float("NaN")
                        self.fos_array2[i-1,j-1] = float("NaN")
                        z[i-1,j-1] = float("NaN")
            for i in range(0, sizex):
                for j in range(0, sizey):
                    if self.fos_array[i-1,j-1] < 1:
                        self.fos_array[i-1,j-1] = 1
                        self.fos_array2[i-1,j-1] = 1

            #####################                    #########################                  #########################

            lin_x = np.linspace(0,1,self.fos_array.shape[0],endpoint=False)
            lin_y = np.linspace(0,1,self.fos_array.shape[1],endpoint=False)
            y,x = np.meshgrid(lin_y,lin_x)

            x3 = self.fos_array2.shape[0]
            y3 = self.fos_array2.shape[1]

            self.fos_array2 = np.fliplr(self.fos_array2)
            z = np.fliplr(z)
            # self.fos_array2 = self.fos_array2.transpose()
            # x = x.transpose()
            # y = y.transpose()
            # z = z.transpose()
            self.fos_array2 = np.flipud(self.fos_array2)
            self.fos_array2 = np.fliplr(self.fos_array2)
            self.fos_array = np.fliplr(self.fos_array)

            self.fos_array = np.flipud(self.fos_array)
            z = np.flipud(z)
            # self.fos_array = self.fos_array.transpose()
            # z = z.transpose()
            # self.fos_array = np.fliplr(self.fos_array)
            # x = np.fliplr(x)

            # print(x3)
            # print(y3)
            # print(sizex)
            # print(sizey)

            fig_fos, ax = plt.subplots(subplot_kw=dict(projection="3d"), constrained_layout=1, figsize=(12, 10))
            norm1 = plt.Normalize(vmin= self.fos_array.min().min(), vmax= self.fos_array.max().max())

            ax.plot_surface(x.transpose()[2:sizey, 2:sizex], y.transpose()[2:sizey, 2:sizex], z.transpose()[2:sizey, 2:sizex], facecolors= plt.cm.rainbow_r(norm1(self.fos_array.transpose()[2:sizey, 2:sizex])), antialiased=False, shade=False)

            #ax.plot_surface(x.transpose()[2:sizey-1, 2:sizex-1], y.transpose()[2:sizey-1, 2:sizex-1], z.transpose()[2:sizey-1, 2:sizex-1], facecolors= plt.cm.rainbow_r(norm1(self.fos_array.transpose()[2:sizey-1, 2:sizex-1])), antialiased=False, shade=False)
            
            m = mpl.cm.ScalarMappable(cmap= plt.cm.rainbow_r, norm= norm1)
            m.set_array(self.fos_array) #[0:x2-1, 0:y2-1])
            plt.colorbar(m, ax= ax, location= "right")
            # plt.axis([np.nanmin(x), np.nanmax(x)-0.02, np.nanmin(y), np.nanmax(y)-0.02, np.nanmin(z), np.nanmax(z)])

            # plt.axis([0, (sizex-2)/40, 0, (sizey-2)/30, np.nanmin(z), np.nanmax(z)])

            # plt.axis([0, sizex/100, 0, sizey/100, np.nanmin(z), np.nanmax(z)])

            plt.xticks([])
            plt.yticks([])

            ax.invert_yaxis()

            ##################################################
            ax.view_init(elev= elev, azim= azim, roll= roll)
            ##################################################

            self.canvas_fos = FigureCanvas(fig_fos)
            self.toolb_fos = NavigationToolbar(self.canvas_fos, self)

            self.tabInc = QWidget()
            self.tabInc_layout = QVBoxLayout()
            self.tabInc_layout.addWidget(self.canvas_fos)
            self.tabInc_layout.addWidget(self.toolb_fos)
            self.tabInc.setLayout(self.tabInc_layout)

            self.tab_name = "Segurança (3D) " + str(self.inclina_tabs)
            self.tabs_2.addTab(self.tabInc,self.tab_name)

            plt.close('all')

            self.fos_array2 = np.flipud(self.fos_array2)
            # self.fos_array2 = np.fliplr(self.fos_array2)

            ############################################################################################################

            self.fos_array2 = self.fos_array2.transpose()
            # self.fos_array = np.flipud(self.fos_array)

            fig_fos2, ax2 = plt.subplots(1,1,figsize=(12,10))
            cmap = plt.get_cmap('rainbow_r')

            # x3 = self.fos_array3.shape[0]
            # y3 = self.fos_array3.shape[1]
            # plt.imshow(self.fos_array3[0:x3-10, 0:y3-10], cmap)
            # im_fos = ax2.imshow(self.fos_array3[0:x3-10, 0:y3-10], cmap)
            plt.imshow(self.fos_array2, cmap)
            im_fos = ax2.imshow(self.fos_array2, cmap)

            ax2.set_yticks([0, 0.2*(sizey-2), 0.4*(sizey-2), 0.6*(sizey-2), 0.8*(sizey-2), (sizey-2)], labels=[0, 5*sizey, 10*sizey, 15*sizey, 20*sizey, 25*sizey])
            ax2.set_xticks([0, 0.2*(sizex-2), 0.4*(sizex-2), 0.6*(sizex-2), 0.8*(sizex-2), (sizex-2)], labels=[0, 5*sizex, 10*sizex, 15*sizex, 20*sizex, 25*sizex])

            plt.colorbar(im_fos,ax=ax2)
            plt.axis([0, sizex-2, 0, sizey-2])

            ax2.invert_yaxis()

            self.canvas_fos2 = FigureCanvas(fig_fos2)
            self.toolb_fos2 = NavigationToolbar(self.canvas_fos2, self)

            self.tabInc2 = QWidget()
            self.tabInc_layout2 = QVBoxLayout()
            self.tabInc_layout2.addWidget(self.canvas_fos2)
            self.tabInc_layout2.addWidget(self.toolb_fos2)
            self.tabInc2.setLayout(self.tabInc_layout2)

            self.tab_name2 = "Segurança (2D) " + str(self.inclina_tabs)
            self.tabs_2.addTab(self.tabInc2,self.tab_name2)

            def on_click(event):
                global azim
                global elev
                azim, elev = ax.azim, ax.elev

            cid = fig_fos.canvas.mpl_connect('button_release_event', on_click)

            #######################################################################################################################################################

        else:
            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))
            fig_fos2, ax2 = plt.subplots(1,1,figsize=(12,10))

            # self.fos_array3 = self.fos_array.copy()
            #self.fos_array = self.fos_array.transpose()
            print(self.fos_array.shape)

            for i in range(1,imgx.size[0]):
                for j in range(1,imgx.size[1]):
                    alpha = self.g_max[i,j]

                    if self.material_type == 'COARSE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.046;
                        theta_i_max = 0.365;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min)

                        self.fos_array[j-1,i-1] = (6788110953151657*(x1**2)*(x2**2)*x5)/18014398509481984 + (1355958164086877*(x1**2)*x3*(x4**2)*x5)/9007199254740992 - (8873610522459485*(x1**2)*(x4**2)*x5)/72057594037927936 - (1692657047651061*(x1**2))/18014398509481984 - (3851498880822799*x1*(x2**2)*x3)/1125899906842624 + (2526110258615389*x1*x2*(x3**2))/1125899906842624 + (2706917046260173*x1*x2)/9007199254740992 - (3556745139181571*x1*(x3**3)*x4)/9007199254740992 - (579938420281673*x1*(x3**2))/1125899906842624 + (8180563435756073*x1*x3*x4)/36028797018963968 + (3114137794295375*x1*x3)/9007199254740992 - (8586273326384709*x1*x5)/144115188075855872 + (3545170951606327*(x2**2)*(x3**2))/4503599627370496 + (8665832770244175*(x2**2)*x3)/4503599627370496 - (7818372289906591*(x2**2)*x5)/4503599627370496 + (2684009153708421*(x2**2))/2251799813685248 - (4201502816181941*x2*(x3**2))/2251799813685248 - (3562767927008791*x2*x3*x4)/36028797018963968 + (2328059298502727*x2*x3*x5)/9007199254740992 + (8830399494179771*x2*x4*(x5**2))/72057594037927936 + (5482565565501159*x2*x5)/4503599627370496 - (2681827153050867*x2)/2251799813685248 + (8730627984475617*(x3**2)*x4)/72057594037927936 + (1323618450977937*(x3**2))/2251799813685248 - (5618799156698347*x3*x5)/36028797018963968 - (4911690079918821*x3)/4503599627370496 - (7212846679305375*(x4**2))/36028797018963968 - (2144834721434649*x4*x5)/288230376151711744 + (6420485161231939*x4)/9007199254740992 - (6209185403811853*x5)/36028797018963968 + 981468462750861/4503599627370496
                        self.fos_array[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'GRANULAR MEDIUM':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.179;
                        theta_i_max = 0.392;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[j-1,i-1] = (2395554010573903*(x1**3)*x5)/9007199254740992 - (1584791230571555*(x1**2)*x2*x3)/1125899906842624 - (8675059321513597*(x1**2))/36028797018963968 + (2712053627057047*x1*x2*x3)/1125899906842624 - (436588234554137*x1*x3*x5)/562949953421312 + (8696742236362029*x1*x3)/18014398509481984 + (84167422866237*x1*x4)/1125899906842624 + (5038972167706281*(x2**3)*x5)/1125899906842624 - (2769339911649845*(x2**3))/562949953421312 - (5816346030793635*(x2**2)*(x4**2))/18014398509481984 - (2296851704845541*(x2**2)*x5)/281474976710656 + (4711729450227555*(x2**2))/562949953421312 + (4526012208234625*x2*x3*x5)/2251799813685248 - (1438367102275171*x2*x3)/562949953421312 + (3235555885457197*x2*(x4**3))/18014398509481984 - (6984536435614461*x2*(x5**3))/18014398509481984 + (4734726859996689*x2*x5)/1125899906842624 - (8887739276337299*x2)/2251799813685248 + (7909776872928529*(x3**2))/36028797018963968 + (4825069300825317*x3*x4)/144115188075855872 + (1932527580330421*x3*(x5**2))/2251799813685248 - (7088385317352909*x3*x5)/4503599627370496 - (6028859269012785*x3)/36028797018963968 - (4457058916701155*(x4**2))/18014398509481984 + (205865104591035*x4)/281474976710656 - (1093234104604003*x5)/2251799813685248 + 4657821803862761/9007199254740992;
                        self.fos_array[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'GRANULAR FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        phi_min = 15;
                        phi_max = 45;
                        x4 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.188;
                        theta_i_max = 0.412;
                        x5 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[j-1,i-1] = (5997468984231391*x4)/9007199254740992 - (5850653107015129*x2)/2251799813685248 - (2903074490076611*x1)/4503599627370496 - (4978764466261023*x5)/18014398509481984 + (2497394100991123*x1*x2)/1125899906842624 + (1094809215253921*x1*x3)/1125899906842624 + (7011891843826591*x1*x4)/36028797018963968 - (137137518003759*x2*x3)/35184372088832 + (6916471811591635*x1*x5)/18014398509481984 - (5185975094203355*x2*x4)/576460752303423488 + (6973754261875579*x2*x5)/9007199254740992 - (6728904517417159*x3*x5)/9007199254740992 - (5049272361606063*x1*(x2**2))/2251799813685248 + (8151483504101627*x1*(x3**2))/18014398509481984 + (7836140676118751*(x2**2)*x3)/2251799813685248 - (103490230972707*(x1**3)*x4)/562949953421312 - (2508927668464753*(x2**3)*x3)/2251799813685248 + (1751145175163683*(x2**2))/562949953421312 - (2910103121418035*(x4**2))/18014398509481984 - (4149956958460727*(x1**2)*x2*x3)/4503599627370496 - (2909406058924355*x1*(x2**2)*x5)/1125899906842624 + (4267265215922321*(x1**3)*x2*x5)/4503599627370496 + (5734832464949375*x1*x3*(x5**3))/18014398509481984 - (4082556226690241*(x1**2)*(x3**2)*x4)/36028797018963968 - (883679796825111*x1*x3*x5)/562949953421312 + (3185546221473745*x2*x3*x5)/1125899906842624 + 1119623049971351/2251799813685248;
                        self.fos_array[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]

                        # self.fos_array = self.fos_array.transpose()
                    elif self.material_type == 'MEDIUM':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.179;
                        theta_i_max = 0.392;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[j-1,i-1] = - (7605402998259809*(x1**3)*x6)/9007199254740992 + (5433101380788941*(x1**2)*(x6**2))/9007199254740992 + (5438216367263101*(x1**2)*x6)/4503599627370496 + (6933674839011865*x1*x2)/18014398509481984 - (3183093811021595*x1*x3)/18014398509481984 - (6604577520812421*x1*x4*x5)/36028797018963968 - (6677569571403873*x1*x4*x6)/18014398509481984 + (5492449447091975*x1*x5*x6)/144115188075855872 + (5423482706553025*x1*x5)/18014398509481984 - (690523320510537*x1*x6)/562949953421312 - (3321581480764011*(x2**3)*(x6**2))/2251799813685248 + (4144557554361693*(x2**2))/4503599627370496 - (5247773900528281*x2*x3)/18014398509481984 + (912731872269751*x2*(x4**2))/4503599627370496 - (4408639353815769*x2*x5)/36028797018963968 + (8395993053582923*x2*x6)/4503599627370496 - (8532874373358735*x2)/4503599627370496 + (4503753517663555*(x3**2))/9007199254740992 + (5623770062789117*x3*x4*x5)/18014398509481984 - (4581567852841661*x3*(x5**2))/18014398509481984 + (6873632408613219*x3*(x6**3))/18014398509481984 - (2940490725035801*x3*x6)/4503599627370496 - (2371501908453915*x3)/4503599627370496 - (947262250475269*(x4**2))/2251799813685248 + (7492475340553871*x4*(x5**2)*x6)/576460752303423488 - (4920950276662705*x4*x5)/18014398509481984 + (1219489943909891*x4*x6)/9007199254740992 + (8174395509123883*x4)/9007199254740992 + (1206779442258227*(x5**2))/18014398509481984 + (3236337280494743*x5)/9007199254740992 - (2948601616754633*(x6**2))/9007199254740992 + 8820801393289007/18014398509481984;
                        self.fos_array[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'MEDIUM FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.188;
                        theta_i_max = 0.412;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[j-1,i-1] =  (3886190004610709*x4)/4503599627370496 - (5729276149747483*x3)/9007199254740992 - (6788231717529895*x2)/2251799813685248 + (479426134057027*x5)/1125899906842624 - (2555014444031809*x6)/4503599627370496 + (8284280323761517*x1*x3)/36028797018963968 - (5766260012425305*x1*x4)/9007199254740992 - (525466186966067*x2*x3)/562949953421312 + (3559543339455779*x1*x5)/18014398509481984 + (3044854372294711*x2*x4)/2251799813685248 + (2604085627039555*x2*x6)/1125899906842624 + (7021469540150699*x3*x5)/288230376151711744 - (231180365885025*x3*x6)/562949953421312 - (2434138700745953*x4*x5)/9007199254740992 - (2798606821472435*(x2**2)*x4)/1125899906842624 - (4787498997851079*(x2**2)*x6)/2251799813685248 + (6336213524232577*(x2**2))/2251799813685248 + (8898687912479801*(x3**2))/18014398509481984 - (6956481687155787*(x4**2))/18014398509481984 - (6059931181255597*(x5**2))/144115188075855872 + (3017676058392109*x1*x2*(x4**2))/9007199254740992 - (424322724646621*(x2**2)*x3*x4)/9007199254740992 + (8194181095609791*x1*(x3**2)*(x6**2))/72057594037927936 + (4040226326314105*x1*x2*x4)/4503599627370496 + (6767925566021999*x1*x2*x6)/36028797018963968 + (4332927401162267*x2*x3*x4)/9007199254740992 - (6054326828217865*x1*x3*x6)/9007199254740992 - (1182428728719139*x2*x3*x5)/4503599627370496 - (3671852565176795*x1*x4*x6)/36028797018963968 + (5352375486130983*x2*x3*x6)/4503599627370496 + (3079416316199729*x3*x4*x6)/9007199254740992 - (5765496138098037*x2*x3*x4*x6)/9007199254740992 + 3442293244771261/4503599627370496;
                        self.fos_array[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.327;
                        theta_i_max = 0.481;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[j-1,i-1] = (8711105383099221*(x1**2))/72057594037927936 + (4480937614520491*x1*x2*x3*x6)/4503599627370496 + (6445291833574493*x1*x2*x4*(x6**2))/576460752303423488 - (281440029914825*x1*(x3**2)*x6)/562949953421312 - (6629445291354447*x1*x3*x4)/18014398509481984 + (849190321960673*x1*x3*x5)/2251799813685248 - (6187137339255229*x1*x4*x6)/18014398509481984 - (4624215388296035*x1*x6)/18014398509481984 - (1587486474559393*(x2**3)*x6)/1125899906842624 - (4900095579043665*(x2**2)*x4)/4503599627370496 + (1169434422300945*(x2**2))/562949953421312 - (7554405290076481*x2*x3*x4*x5*x6)/72057594037927936 - (7246543431362679*x2*x3*x5)/36028797018963968 - (721288367741207*x2*x3)/1125899906842624 + (8836698625396407*x2*x4*(x5**2))/144115188075855872 + (4781016702927063*x2*x4)/4503599627370496 + (4010700648742253*x2*x6)/2251799813685248 - (2883657241266265*x2)/1125899906842624 - (6577851316887483*(x3**3))/18014398509481984 + (2688469612731583*(x3**2))/2251799813685248 + (6653205645687021*x3*(x4**2)*(x6**2))/18014398509481984 - (2099413330989821*x3*(x4**2))/4503599627370496 + (6161799069262313*x3*x4)/9007199254740992 + (1857306243852377*x3*x5*x6)/9007199254740992 - (2865566660442267*x3*x5)/9007199254740992 - (4614774789911059*x3*x6)/9007199254740992 - (1937328245404209*x3)/2251799813685248 - (7930907804563573*(x4**2))/36028797018963968 - (4754832626658037*x4*x5)/18014398509481984 + (171256162149423*x4)/281474976710656 - (8578558619551665*(x5**2)*x6)/288230376151711744 + (8704230461968029*x5)/18014398509481984 - (3382315052029319*(x6**3))/1152921504606846976 - (6812374621577823*x6)/18014398509481984 + 6174808073279873/9007199254740992;
                        self.fos_array[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]
                    elif self.material_type == 'VERY FINE':
                        h_min = 1;
                        h_max = 5;
                        x1 = (h - h_min)/(h_max-h_min);

                        hw_min = 0;
                        hw_max = 5;
                        x2 = (hw - hw_min)/(hw_max-hw_min);

                        alpha_min = 15;
                        alpha_max = 60;
                        x3 = (alpha - alpha_min)/(alpha_max-alpha_min);

                        c_min = 0;
                        c_max = 20;
                        x4 = (c - c_min)/(c_max-c_min);

                        phi_min = 15;
                        phi_max = 45;
                        x5 = (phi - phi_min)/(phi_max-phi_min);

                        theta_i_min = 0.392;
                        theta_i_max = 0.538;
                        x6 = (theta_i - theta_i_min)/(theta_i_max-theta_i_min);

                        self.fos_array[j-1,i-1] = (3443522597856495*x4)/4503599627370496 - (2348315328800215*x2)/1125899906842624 - (8559581679713667*x1)/36028797018963968 + (8018106863502985*x5)/18014398509481984 - (4230345748317103*x6)/9007199254740992 - (1544138636456145*(x4**2)*(x6**2))/18014398509481984 + (902528602503447*x1*x2)/1125899906842624 - (7043808527068311*x2*x3)/4503599627370496 - (7246008324732221*x1*x6)/18014398509481984 + (1747413719569329*x2*x6)/1125899906842624 - (2597399368633979*x3*x6)/4503599627370496 - (2391652988631193*x4*x5)/4503599627370496 + (6181389039177289*x1*(x3**2))/9007199254740992 - (5186363803500845*x1*(x5**2))/36028797018963968 - (2321574606811609*x2*(x5**2))/72057594037927936 - (2543509902109129*x3*(x4**2))/9007199254740992 + (2780023057880475*(x1**2)*x6)/9007199254740992 + (3526997481352009*(x2**2))/4503599627370496 - (7277171475332687*(x4**3))/72057594037927936 + (5569296935854231*x1*x4*(x5**2))/18014398509481984 + (5469000151567747*(x3**2)*x4*x5)/18014398509481984 + (651427578412907*x1*x2*x5)/1125899906842624 - (3056278760769427*x1*x3*x4)/4503599627370496 - (2474169676151269*x1*x3*x5)/18014398509481984 + (5800416867896625*x2*x3*x4)/4503599627370496 - (6838031967161513*x1*x3*x6)/9007199254740992 - (2410625286488745*x2*x3*x5)/9007199254740992 + (5260456502000859*x2*x3*x6)/4503599627370496 + (2296168764961959*x1*x5*x6)/4503599627370496 + (8412632997477619*x3*x4*x6)/18014398509481984 - (8539609750453113*x1*x2*x5*x6)/9007199254740992 - (5748018464844461*x1*(x2**2)*x4*x6)/4503599627370496 + 6230592657726943/9007199254740992;
                        self.fos_array[j-1,i-1] = 10 ** self.fos_array[j-1,i-1]

                    # self.fos_array[j,i] = (1605074512383065*(alpha**2)*(c**2)*(h**2)*phi)/151115727451828646838272 - (1414963042633059*(alpha**2)*(c**2)*h*phi)/18889465931478580854784 - (2774717211173289*(alpha**2)*(c**2)*hw*phi)/604462909807314587353088 + (2835477809945801*(alpha**2)*(c**2)*phi)/37778931862957161709568 + (6731555515546295*(alpha**2)*c)/73786976294838206464 + (5516753565726847*(alpha**2)*phi)/147573952589676412928 + (5653461066590515*alpha*(c**2)*h)/590295810358705651712 + (3025671568382675*alpha*(c**2)*phi)/590295810358705651712 - (2098110323770171*alpha*(c**2))/36893488147419103232 - (3002978305542275*alpha*c*(h**2))/4611686018427387904 + (2687741203999111*alpha*c*h)/576460752303423488 + (6472386681360727*alpha*c*hw*phi)/590295810358705651712 - (2982096583892561*alpha*c*(phi**2))/2361183241434822606848 - (4627184841729915*alpha*c)/288230376151711744 - (5688086807612743*alpha*(phi**2))/590295810358705651712 - (4311146912769217*alpha*phi)/1152921504606846976 - (4976341265194569*(c**2)*(h**2)*phi)/147573952589676412928 + (2283034929082703*(c**2)*h*phi)/9223372036854775808 + (1342385546936077*(c**2)*hw*phi)/147573952589676412928 - (1295331185150365*(c**2)*phi)/2305843009213693952 + (2592141320026855*c*(h**2))/72057594037927936 - (4971891995221437*c*h)/18014398509481984 - (4809409727287499*c*hw*phi)/9223372036854775808 + (2265715759669333*c*(phi**2))/36893488147419103232 + (3352624142374595*c)/4503599627370496 + (20768301037335*(h**2)*(hw**2)*phi)/2305843009213693952 - (1324783938325601*hw)/36028797018963968 + (3497832476657703*(phi**2))/4611686018427387904 + (6865366199800263*phi)/72057594037927936 + 1489595912300695/9007199254740992;

            z = np.array(imgx)
            self.fos_array3 = self.fos_array.copy()
            print(self.fos_array.shape)
            for i in range(1,imgx.size[0]):
                for j in range(1,imgx.size[1]):
                    if self.fos_array[j-1,i-1] > 2:
                        self.fos_array[j-1,i-1] = 2 #float("NaN")
                        self.fos_array3[j-1,i-1] = float("NaN")
                        # self.fos_array2[j-1,i-1] = 2 #float("NaN")
                        # self.fos_array3[j-1,i-1] = float("NaN")
                        z[j-1,i-1] = float("NaN")
            for i in range(1,imgx.size[0]):
                for j in range(1,imgx.size[1]):
                    if self.fos_array[j-1,i-1] < 1:
                        self.fos_array3[j-1,i-1] = 1
                        self.fos_array[j-1,i-1] = 1

            x2 = self.fos_array.shape[0]
            y2 = self.fos_array.shape[1]

            # print("X2: ", x2)
            # print("Y2: ", y2)
            # print("Z size: ", z.size)
            self.fos_array = self.fos_array.transpose()
            print(self.fos_array.shape)

            lin_x = np.linspace(0,1,self.fos_array.shape[0]-3,endpoint=False)
            lin_y = np.linspace(0,1,self.fos_array.shape[1],endpoint=False)
            y,x = np.meshgrid(lin_y,lin_x)

            #self.fos_array = self.fos_array.transpose()

            fig_fos, ax = plt.subplots(subplot_kw=dict(projection="3d"), constrained_layout=1, figsize=(12, 10))
            norm1 = plt.Normalize(vmin= self.fos_array.min().min(), vmax= self.fos_array.max().max())

            # print("X size: ", x.shape)
            # print("Y size: ", y.shape)
            # print("Z size: ", z.shape)
            # print("Fos size: ", self.fos_array.shape)
            # z = z.transpose()

            # z = np.fliplr(z)
            # self.fos_array = np.fliplr(self.fos_array)

            print(x2)
            print(y2)
            print(z.shape)

            z = np.flipud(z)
            self.fos_array = np.fliplr(self.fos_array)
            #x = x.transpose()
            #y = y.transpose()
            #self.fos_array = self.fos_array.transpose()
            z = z.transpose()

            print("X size: ", x.shape)
            print("Y size: ", y.shape)
            print("Z size: ", z.shape)
            print("Fos size: ", self.fos_array.shape)

            ax.plot_surface(y.transpose()[2:x2,], x.transpose()[2:x2,], z.transpose()[2:x2, 0:y2-3], facecolors= plt.cm.rainbow_r(norm1(self.fos_array.transpose()[2:x2, 0:y2-3])), antialiased=False, shade=False)
            #x[0:x2, 0:y2], y[0:x2, 0:y2], z[0:x2, 0:y2], facecolors= plt.cm.rainbow_r(norm1(self.fos_array[0:x2, 0:y2])), antialiased=False, shade=False)
            # FUNCIONOU: x.transpose(), y.transpose(), z, facecolors= plt.cm.rainbow_r(norm1(self.fos_array.transpose())), antialiased=False, shade=False)
            #x.transpose()[2:x2-2, 2:y2-2], y.transpose()[2:x2-2, 2:y2-2], z[2:x2-2, 2:y2-2], facecolors= plt.cm.rainbow_r(norm1(self.fos_array.transpose()[2:x2-2, 2:y2-2])), antialiased=False, shade=False) 
            # #x[2:x2-2, 2:y2-2], y[2:x2-2, 2:y2-2], z.transpose()[2:x2-2, 2:y2-2], facecolors= plt.cm.rainbow_r(norm1(self.fos_array[2:x2-2, 2:y2-2])), antialiased=False, shade=False) 
            # #z.transpose()[2:x2-1, 2:y2-1], facecolors= plt.cm.rainbow_r(norm1(self.fos_array.transpose()[2:x2-1, 2:y2-1])), antialiased=False, shade=False)
            m = mpl.cm.ScalarMappable(cmap= plt.cm.rainbow_r, norm= norm1)
            m.set_array(self.fos_array)
            plt.colorbar(m, ax= ax, location= "right")

            plt.xticks([])
            plt.yticks([])
            # ax.grid(False)
            # plt.axis('off')

            self.canvas_fos = FigureCanvas(fig_fos)
            self.toolb_fos = NavigationToolbar(self.canvas_fos, self)

            self.tabInc = QWidget()
            self.tabInc_layout = QVBoxLayout()
            self.tabInc_layout.addWidget(self.canvas_fos)
            self.tabInc_layout.addWidget(self.toolb_fos)
            self.tabInc.setLayout(self.tabInc_layout)

            self.tab_name = "Segurança (3D) " + str(self.inclina_tabs)
            self.tabs_2.addTab(self.tabInc,self.tab_name)

            plt.close('all')

            cmap = plt.get_cmap('rainbow_r')

            self.fos_array3 = np.fliplr(self.fos_array3)

            plt.imshow(np.fliplr(self.fos_array3), cmap)
            im_fos = ax2.imshow(np.fliplr(self.fos_array3), cmap)

            ax2.set_yticks([0, 0.2*(imgx.size[1]-2), 0.4*(imgx.size[1]-2), 0.6*(imgx.size[1]-2), 0.8*(imgx.size[1]-2), (imgx.size[1]-2)], labels=[0, 5*(imgx.size[1]), 10*(imgx.size[1]), 15*(imgx.size[1]), 20*(imgx.size[1]), 25*(imgx.size[1])])
            ax2.set_xticks([0, 0.2*(imgx.size[0]-2), 0.4*(imgx.size[0]-2), 0.6*(imgx.size[0]-2), 0.8*(imgx.size[0]-2), (imgx.size[0]-2)], labels=[0, 5*(imgx.size[0]), 10*(imgx.size[0]), 15*(imgx.size[0]), 20*(imgx.size[0]), 25*(imgx.size[0])])

            #print(imgx.size[0])
            #print(imgx.size[1])

            ax2.set_xlim(0, int(imgx.size[0])-2)
            ax2.set_ylim(0, int(imgx.size[1])-2) #, 0)

            plt.tight_layout()

            plt.colorbar(im_fos,ax=ax2)
            # plt.axis([0, imgx.size[0]/2, 0, imgx.size[1]/2])
            # ax2.invert_yaxis()
            # plt.subplots_adjust(left=0.5, right=0.5, bottom=0.5, top=0.5)

            ##################################################
            ax.view_init(elev= elev, azim= azim, roll= roll)
            ##################################################

            self.canvas_fos2 = FigureCanvas(fig_fos2)
            self.toolb_fos2 = NavigationToolbar(self.canvas_fos2, self)

            self.tabInc2 = QWidget()
            self.tabInc_layout2 = QVBoxLayout()
            self.tabInc_layout2.addWidget(self.canvas_fos2)
            self.tabInc_layout2.addWidget(self.toolb_fos2)
            self.tabInc2.setLayout(self.tabInc_layout2)

            self.tab_name2 = "Segurança (2D) " + str(self.inclina_tabs)
            self.tabs_2.addTab(self.tabInc2,self.tab_name2)

            def on_click(event):
                global azim
                global elev
                azim, elev = ax.azim, ax.elev

            cid = fig_fos.canvas.mpl_connect('button_release_event', on_click)

            # cmap = plt.get_cmap('rainbow_r')

            # plt.imshow(self.fos_array.transpose(), cmap)
            # im_fos = ax.imshow(self.fos_array.transpose(), cmap)

            # ax.set_yticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1], imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])
            # ax.set_xticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0], imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])

            # plt.colorbar(im_fos,ax=ax)
            # plt.axis([0, imgx.size[0], 0, imgx.size[1]])
            # ax.invert_yaxis()

            #######################################################################################################################################################

            # # Create arrays and declare x,y,z variables
            # lin_x = np.linspace(0,1,self.fos_array.transpose().shape[0],endpoint=False)
            # lin_y = np.linspace(0,1,self.fos_array.transpose().shape[1],endpoint=False)
            # y,x = np.meshgrid(lin_y,lin_x)
            # z = self.fos_array.transpose()

            # # Apply gaussian filter, with sigmas as variables. Higher sigma = more smoothing and more calculations. Downside: min and max values do change due to smoothing
            # sigma_y = 100
            # sigma_x = 100
            # sigma = [sigma_y, sigma_x]
            # z_smoothed = sp.ndimage.gaussian_filter(z, sigma)

            # # Creating figure
            # fig_fos = plt.figure(figsize=(12,10)) #12,10
            # ax = plt.axes(projection='3d')
            # ax.azim = -30
            # ax.elev = 42
            # # ax.set_box_aspect((x_ratio,y_ratio,((x_ratio+y_ratio)/8)))
            # surf = ax.plot_surface(x,y,z, cmap='rainbow_r', edgecolor='none')

            # # Setting colors for colorbar range
            # m = cm.ScalarMappable(cmap=surf.cmap, norm=surf.norm)
            # m.set_array(z_smoothed)

            # # plt.xticks([])  # Disabling xticks by Setting xticks to an empty list
            # # plt.yticks([])  # Disabling yticks by setting yticks to an empty list
            # # fig_fos.tight_layout()
            # ax.grid(False)
            # # plt.axis('off')
        #

        # Display figure
        # self.canvas_fos = FigureCanvas(fig_fos)
        # self.toolb_fos = NavigationToolbar(self.canvas_fos, self)

        # self.tabInc = QWidget()
        # self.tabInc_layout = QVBoxLayout()
        # self.tabInc_layout.addWidget(self.canvas_fos)
        # self.tabInc_layout.addWidget(self.toolb_fos)
        # self.tabInc.setLayout(self.tabInc_layout)

        if self.tabs_2.count() == 1:
            self.tabs_2.removeTab(0)
        #

        if self.tabs_2.count() >= 3:
            self.tabs_2.removeTab(0)
            self.tabs_2.removeTab(0)

        # self.tab_name = "Segurança (2D) " + str(self.inclina_tabs)
        # self.tabs_2.addTab(self.tabInc,self.tab_name)

        self.tabs_2.setCurrentIndex(self.tabAtual)

        plt.close('all')
        print("runAnalysis2")
    #

    def getfile(self):
        self.figure.clear()

        global fname
        fname, _ = QFileDialog.getOpenFileName(self, "Open File","c:\\Users\\paulobaccar\\Documents","Tif files(*.tif);;Tiff files(*.tiff)")

        # self.fname, _ = QFileDialog.getOpenFileName(self, "Open File","c:\\Users\\paulobaccar\\Documents","Tif files(*.tif);;Tiff files(*.tiff)")

        # self.tabs.setVisible(True)

        self.elev_incl(fname)
        # self.elev_incl(self.fname)
    #

    def elev_incl(self,arquivo):
        global fname
        img = Image.open(arquivo)
        self.label.setText(str('X: ' + str(img.size[-2]) + '     Y: ' + str(img.size[1])))

        # Convert the image to a NumPy array
        img_array = np.array(img)
        self.img_array = img_array

        # Get aspect ratio of tif file for late plot box-plot-ratio
        y_ratio,x_ratio = img.size

        # Create arrays and declare x,y,z variables
        lin_x = np.linspace(0,1,img_array.shape[0],endpoint=False)
        lin_y = np.linspace(0,1,img_array.shape[1],endpoint=False)
        y,x = np.meshgrid(lin_y,lin_x)
        z = img_array

        # Apply gaussian filter, with sigmas as variables. Higher sigma = more smoothing and more calculations. Downside: min and max values do change due to smoothing
        sigma_y = 100
        sigma_x = 100
        sigma = [sigma_y, sigma_x]
        z_smoothed = sp.ndimage.gaussian_filter(z, sigma)

        # Creating figure
        fig = plt.figure(figsize=(12,10)) #12,10
        ax = plt.axes(projection='3d')
        ax.azim = -30
        ax.elev = 42
        ax.set_box_aspect((x_ratio,y_ratio,((x_ratio+y_ratio)/8)))
        surf = ax.plot_surface(x,y,z, cmap='terrain', edgecolor='none')

        # Setting colors for colorbar range
        m = cm.ScalarMappable(cmap=surf.cmap, norm=surf.norm)
        m.set_array(z_smoothed)

        plt.xticks([])  # Disabling xticks by Setting xticks to an empty list
        plt.yticks([])  # Disabling yticks by setting yticks to an empty list
        fig.tight_layout()
        # ax.grid(False)
        # plt.axis('off')

        # Display the figure
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

        self.canvas = FigureCanvas(fig)
        plt.close('all')

        self.g_max = np.zeros((img.size[0],img.size[1]));
        L = 25;
        Ld = np.sqrt(2)*L

        # Getting the biggest angles of each location
        for i in range(1,img.size[1]-1): #Já testado o 199
            for j in range(1,img.size[0]-1):
                self.g_max[j,i] = max([abs(img_array[i+1,j]-img_array[i,j])/L,
                abs(img_array[i-1,j]-img_array[i,j])/L,
                abs(img_array[i,j+1]-img_array[i,j])/L ,
                abs(img_array[i,j-1]-img_array[i,j])/L,
                abs(img_array[i+1,j+1]-img_array[i,j])/Ld,
                abs(img_array[i-1,j-1]-img_array[i,j])/Ld,
                abs(img_array[i-1,j+1]-img_array[i,j])/Ld,
                abs(img_array[i+1,j-1]-img_array[i,j])/Ld])

                self.g_max[j,i] = np.arctan(self.g_max[j,i]) * 180/np.pi

        # Creating second figure
        fig2, ax = plt.subplots(1,1,figsize=(12,10))
        plt.imshow(self.g_max.transpose(), cmap='terrain')
        im = ax.imshow(self.g_max.transpose(), cmap='terrain')

        ax.set_xticks([0, 0.2*img.size[0], 0.4*img.size[0], 0.6*img.size[0], 0.8*img.size[0],img.size[0]], labels=[0, 5*img.size[0], 10*img.size[0], 15*img.size[0], 20*img.size[0], 25*img.size[0]])
        ax.set_yticks([0, 0.2*img.size[1], 0.4*img.size[1], 0.6*img.size[1], 0.8*img.size[1],img.size[1]], labels=[0, 5*img.size[0], 10*img.size[0], 15*img.size[0], 20*img.size[0], 25*img.size[0]])

        plt.colorbar(im, ax=ax)
        plt.axis([0, img.size[0]-1, 0, img.size[1]-1])
        ax.invert_yaxis()

        # plt.axis('off')

        # Display figures
        self.tabs_3.setVisible(True)

        self.toolb1 = NavigationToolbar(self.canvas,self.canvas)

        self.tabInc = QWidget()
        self.tabInc_layout = QVBoxLayout()
        self.tabInc_layout.addWidget(self.canvas)
        self.tabInc_layout.addWidget(self.toolb1)
        self.tabInc.setLayout(self.tabInc_layout)
        #####################################################################################################################################################################################################

        with rasterio.open(arquivo) as dataset:
            if dataset.count > 1:
                # Ler apenas a primeira banda
                banda1 = dataset.read(1)
                self.img_arrayR = banda1
                z_min = np.min(banda1)
                z_max = np.max(banda1)
            else:
                imgR = Image.open(arquivo)
                self.img_arrayR = np.array(imgR)
                z_min = np.min(np.array(imgR))
                z_max = np.max(np.array(imgR))

        # Gerar as coordenadas (sem georreferenciamento, vamos usar os índices de pixels)
        ny, nx = self.img_arrayR.shape  # cuidado: (rows, cols)
        xR = np.arange(nx)
        yR = np.arange(ny)
        xR, yR = np.meshgrid(xR, yR)
        zR = self.img_arrayR
        z_total = z_max - z_min

        # Proporção para escala de z
        altura, largura = self.g_max.shape
        incl_max, tam_y, tam_x = self.g_max, altura*L, largura*L              #self.calcula_incl_max(arquivo)
        prop_z = z_total/tam_x # a proporção de z por x e y da diferente, como saber quando usa-la?
        print("!!!!!!!!!!!!!", prop_z)

        # Inverte os eixos visualmente, se necessário
        xR = np.flip(xR, axis=1)  # inverte eixo X
        yR = np.flip(yR, axis=0)  # inverte eixo Y
        #zR = np.flip(zR, axis=0)  # inverte eixo Y do Z

        from qtpy import QtWidgets
        from pyvistaqt import QtInteractor

        #pv.start_xvfb()

        pv.set_plot_theme("document")                                     ##################         E 2270         ###################

        self.layoutX = QVBoxLayout()
        #self.stacked_widget = QStackedWidget()
        self.layoutX.addWidget(self.stacked_elevacao)

        pv.global_theme.window_size = [1000, 1000]
        self.pl = pv.Plotter(window_size=[1000, 1000], off_screen=True, image_scale=2) #, shape = (1, 3))#int(self.inclina_tabs)+1))
        #self.pl(shape = (1, int(self.inclina_tabs)+1))
        #pl.(image_scale=2)
        self.exibe_elevacao = self.findChild(QGraphicsView,"frame_exibicao_elevacao")
        self.plotter = QtInteractor(self.exibe_elevacao)
        #self.plotter.setFixedSize(1400, 800)
        #self.plotter.setMinimumSize(375,510)             #(750, 620)


        self.plotter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        #self.plotter.setMinimumSize(750, 820)
        # self.plotter = pv.Plotter(off_screen=False)
        self.plotter.set_scale(xscale=5, yscale=5, zscale=(5/25)) # muda a escala de z sem alterar o gráfico.
        # self.plotter.set_scale(xscale=1, yscale=1)
        grid = pv.StructuredGrid(xR, yR, zR)
        grid["elevation"] = z.ravel(order="F")

        #self.plotter(window_size=[1, 400000])

        #self.plotter(shape = (1, int(self.inclina_tabs)+1))
        #self.plotter.subplot(0, int((self.inclina_tabs)))
        
        self.plotter.add_mesh(pv.Sphere())
        self.plotter.add_mesh(grid, scalars="elevation", cmap="terrain", show_scalar_bar=True, scalar_bar_args={'title': 'Elevação',
        'vertical': True, 'position_x': 0.85, 'position_y': 0.25})

        # Adiciona o canvas do gráfico à cena
        self.stacked_elevacao.addWidget(self.plotter)
        self.stacked_elevacao.setCurrentWidget(self.plotter)
        self.stacked_elevacao.setVisible(True)
        #layout.addWidget(self.plotter)

        self.plots.append(self.plotter)

        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

        self.tabX = QWidget()
        # self.tabX_layout = QVBoxLayout()
        # self.tabX_layout.addWidget(self.plotter.interactor)
        self.tabX.setLayout(self.layoutX)
        #self.tabs_3.addTab(self.tabX)
        #.addWidget(self.plotter)
        #self.tabs_3.addTab.setCurrentWidget(self.plotter)

        # self.stacked_elevacao.addWidget(self.plotter.interactor)

        # self.scene.addWidget(self.toolbar)
        self.label_shape.setText(f"Shape: {self.img_array.shape}") # exibe o as dimensões do tif


        #####################################################################################################################################################################################################
        self.tab_name = "Elevação " + str((self.inclina_tabs)+1)
        self.tabs_3.addTab(self.tabX, self.tab_name)
        #self.tabs_3.setMinimumSize(1450,850)

        self.canvas2 = FigureCanvas(fig2)
        self.toolb2 = NavigationToolbar(self.canvas2, self)

        self.tabInc = QWidget()
        self.tabInc_layout = QVBoxLayout()
        self.tabInc_layout.addWidget(self.canvas2)
        self.tabInc_layout.addWidget(self.toolb2)
        self.tabInc.setLayout(self.tabInc_layout)

        if self.tabs.count()>0 and self.inclina_tabs == 0:
            self.tabs.removeTab(0)
        if self.tabs_3.count()>0 and self.inclina_tabs == 0:
            self.tabs_3.removeTab(0)

        print("Inclina_tabs = ",self.inclina_tabs)
        self.inclina_tabs += 1

        self.tab_name2 = "Inclinação " + str(self.inclina_tabs)
        self.tabs.addTab(self.tabInc, self.tab_name2)

        plt.close('all')

        # Show the limits
        self.x1label.setVisible(True)
        self.x2label.setVisible(True)
        self.y1label.setVisible(True)
        self.y2label.setVisible(True)
        self.label.setVisible(True)
        self.limits.setVisible(True)

        self.x1lineEdit.setVisible(True)
        self.x2lineEdit.setVisible(True)
        self.y1lineEdit.setVisible(True)
        self.y2lineEdit.setVisible(True)
        self.Adjust.setVisible(True)

        self.AnalysisBtn.setVisible(True)

        global fname
        self.imgname.setText(fname)

        # self.imgname.setText(self.fname)
        self.imgsizex.setText(str(img.size[1]))
        self.imgsizey.setText(str(img.size[-2]))

        #######################################################################
        
        self.plotter.update()
        self.plotter.resize(self.tabs_3.size())
        print("¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢")
        
        #self.tabs_3.layout().activate()
        #self.plotter.interactor.GetRenderWindow().Render()

        self.tabs_3.setMinimumSize(int(self.width()/2)-15, int(self.height()*6/10))
        
        size = self.tabX.size()
        self.plotter.resize(size)
        def resizeEvent(self, event):
            # Ajusta a QLabel para ocupar o mesmo tamanho do layout
            if self.layout:
                # Mantém a proporção ao redimensionar
                new_width = event.size().width()
                new_height = int(new_width / self.aspect_ratio)
                self.plotter.resize(new_width, new_height)

                super().resizeEvent(event)
        #######################################################################

        self.ClearBtn.clicked.connect(self.clearCanvas)
    #

    def figureAdjust(self):
        self.number_of_adjusts += 1

        # self.canvas.deleteLater()
        # self.toolb1.deleteLater()
        plt.close('all')

        x1 = int(self.x1lineEdit.text())
        x2 = int(self.x2lineEdit.text())
        y1 = int(self.y1lineEdit.text())
        y2 = int(self.y2lineEdit.text())

        # Convert the image to a NumPy array

        global fname

        fname = self.imgname.text()       ####
        img2 = Image.open(fname)             ####
        img_array2 = np.array(img2)

        img_array2 = img_array2[x1:x2,y1:y2]
        img2 = Image.fromarray(img_array2, 'RGB')
        self.label.setText(str('X: ' + str(img2.size[-2]) + '     Y: ' + str(img2.size[1])))
        self.imgsizex.setText(str(img2.size[1]))
        self.imgsizey.setText(str(img2.size[-2]))

        # Get aspect ratio of tif file for late plot box-plot-ratio
        y_ratio,x_ratio = img2.size

        # Create arrays and declare x,y,z variables
        lin_x = np.linspace(0,1,img_array2.shape[0],endpoint=False)
        lin_y = np.linspace(0,1,img_array2.shape[1],endpoint=False)
        y,x = np.meshgrid(lin_y,lin_x)
        z = img_array2

        # Apply gaussian filter, with sigmas as variables. Higher sigma = more smoothing and more calculations. Downside: min and max values do change due to smoothing
        sigma_y = 100
        sigma_x = 100
        sigma = [sigma_y, sigma_x]
        z_smoothed = sp.ndimage.gaussian_filter(z, sigma)

        # Some min and max and range values coming from gaussian_filter calculations
        z_smoothed_min = np.amin(z_smoothed)
        z_smoothed_max = np.amax(z_smoothed)
        z_range = z_smoothed_max - z_smoothed_min

        # Creating figure
        fig = plt.figure(figsize=(12,10))
        ax = plt.axes(projection='3d')
        ax.azim = -30
        ax.elev = 42
        ax.set_box_aspect((x_ratio,y_ratio,((x_ratio+y_ratio)/8)))
        surf = ax.plot_surface(x,y,z, cmap='terrain', edgecolor='none')

        # Setting colors for colorbar range
        m = cm.ScalarMappable(cmap=surf.cmap, norm=surf.norm)
        m.set_array(z_smoothed)

        plt.xticks([])  # disabling xticks by Setting xticks to an empty list
        plt.yticks([])  # disabling yticks by setting yticks to an empty list
        fig.tight_layout()
        ax.grid(False)
        plt.axis('off')

        # Display the figure
        self.canvas = FigureCanvas(fig)
        # plt.close('all')

        self.g_max2 = np.zeros((img2.size[0],img2.size[1]));
        L = 25;
        Ld = np.sqrt(2)*L

        # Getting the biggest angles of each location
        for i in range(1,img2.size[1]-1): #Já testado o 199
            for j in range(1,img2.size[0]-1):
                self.g_max2[j,i] = max([abs(img_array2[i+1,j]-img_array2[i,j])/L,
                abs(img_array2[i-1,j]-img_array2[i,j])/L,
                abs(img_array2[i,j+1]-img_array2[i,j])/L ,
                abs(img_array2[i,j-1]-img_array2[i,j])/L,
                abs(img_array2[i+1,j+1]-img_array2[i,j])/Ld,
                abs(img_array2[i-1,j-1]-img_array2[i,j])/Ld,
                abs(img_array2[i-1,j+1]-img_array2[i,j])/Ld,
                abs(img_array2[i+1,j-1]-img_array2[i,j])/Ld])

                self.g_max2[j,i] = np.arctan(self.g_max2[j,i]) * 180/np.pi
        #

        # Creating second figure
        fig2, ax = plt.subplots(1,1,figsize=(12,10))
        plt.imshow(self.g_max2.transpose(), cmap='terrain')
        im = ax.imshow(self.g_max2.transpose(), cmap='terrain')

        ax.set_xticks([0, 0.2*img2.size[0], 0.4*img2.size[0], 0.6*img2.size[0], 0.8*img2.size[0],img2.size[0]], labels=[0, 5*img2.size[0], 10*img2.size[0], 15*img2.size[0], 20*img2.size[0], 25*img2.size[0]])
        ax.set_yticks([0, 0.2*img2.size[1], 0.4*img2.size[1], 0.6*img2.size[1], 0.8*img2.size[1],img2.size[1]], labels=[0, 5*img2.size[1], 10*img2.size[1], 15*img2.size[1], 20*img2.size[1], 25*img2.size[1]]) # labels=[25*img2.size[1], 20*img2.size[1], 15*img2.size[1], 10*img2.size[1], 5*img2.size[1], 0])

        plt.colorbar(im, ax=ax)
        plt.axis([0, img2.size[0]-1, 0, img2.size[1]-1])
        ax.invert_yaxis()

        # Display figures
        self.toolb1 = NavigationToolbar(self.canvas, self)
        self.tabInc = QWidget()
        self.tabInc_layout = QVBoxLayout()
        self.tabInc_layout.addWidget(self.canvas)
        self.tabInc_layout.addWidget(self.toolb1)
        self.tabInc.setLayout(self.tabInc_layout)

        self.tab_name = "Elevação " + str((self.inclina_tabs)+1)
        self.tabs_3.addTab(self.tabInc, self.tab_name)

        self.canvas2 = FigureCanvas(fig2)
        self.toolb2 = NavigationToolbar(self.canvas2, self)

        self.tabInc2 = QWidget()
        self.tabInc_layout2 = QVBoxLayout()
        self.tabInc_layout2.addWidget(self.canvas2)
        self.tabInc_layout2.addWidget(self.toolb2)
        self.tabInc2.setLayout(self.tabInc_layout2)

        self.inclina_tabs +=1
        self.tab_name = "Inclinação " + str(self.inclina_tabs)
        self.tabs.addTab(self.tabInc2,self.tab_name)

        plt.close('all')

        # Show the limits
        self.x1label.setVisible(True)
        self.x2label.setVisible(True)
        self.y1label.setVisible(True)
        self.y2label.setVisible(True)
        self.label.setVisible(True)
        self.limits.setVisible(True)

        self.x1lineEdit.setVisible(True)
        self.x2lineEdit.setVisible(True)
        self.y1lineEdit.setVisible(True)
        self.y2lineEdit.setVisible(True)
        self.Adjust.setVisible(True)

        self.AnalysisBtn.setVisible(True)
        self.ClearBtn.clicked.connect(self.clearCanvas)
    #

    def clearCanvas(self):
        plt.close('all')

        self.x1label.setVisible(False)
        self.x2label.setVisible(False)
        self.y1label.setVisible(False)
        self.y2label.setVisible(False)
        self.label.setVisible(False)
        self.limits.setVisible(False)

        self.x1lineEdit.setVisible(False)
        self.x2lineEdit.setVisible(False)
        self.y1lineEdit.setVisible(False)
        self.y2lineEdit.setVisible(False)

        self.Adjust.setVisible(False)
        self.AnalysisBtn.setVisible(False)

        self.tabs.setVisible(False)
        self.tabs_2.setVisible(False)
        self.tabs_3.setVisible(False)

        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)

        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)

        for i in reversed(range(self.tabs.count())):
            self.tabs.removeTab(i)

        for i in reversed(range(self.tabs_2.count())):
            self.tabs_2.removeTab(i)

        for i in reversed(range(self.tabs_3.count()-1)):
            self.tabs_3.removeTab(i)

        self.inclina_tabs = 0
        self.number_of_adjusts = 0
        self.n_tabs = 0

        # self.tabInc = QWidget()
        # self.tabInc_layout = QVBoxLayout()
        # self.tabInc.setLayout(self.tabInc_layout)
        # self.tabs.addTab(self.tabInc)
    #

    def mostra_lista(self):
        # self.label_mapa_rio.setVisible(not self.label_mapa_rio.isVisible())
        # self.botao_regiao1.setVisible(not self.botao_regiao1.isVisible())
        # self.botao_regiao2.setVisible(not self.botao_regiao2.isVisible())
        # self.botao_regiao3.setVisible(not self.botao_regiao3.isVisible())
        # self.botao_regiao4.setVisible(not self.botao_regiao4.isVisible())
        # self.botao_regiao5.setVisible(not self.botao_regiao5.isVisible())
        # self.botao_regiao6.setVisible(not self.botao_regiao6.isVisible())
        # self.botao_regiao7.setVisible(not self.botao_regiao7.isVisible())
        # self.botao_regiao8.setVisible(not self.botao_regiao8.isVisible())
        # self.botao_regiao9.setVisible(not self.botao_regiao9.isVisible())
        # self.botao_regiao10.setVisible(not self.botao_regiao10.isVisible())
        # self.botao_regiao11.setVisible(not self.botao_regiao11.isVisible())
        # self.botao_regiao12.setVisible(not self.botao_regiao12.isVisible())
        # self.botao_regiao13.setVisible(not self.botao_regiao13.isVisible())
        # self.botao_regiao14.setVisible(not self.botao_regiao14.isVisible())
        # self.botao_regiao15.setVisible(not self.botao_regiao15.isVisible())
        # self.botao_regiao16.setVisible(not self.botao_regiao16.isVisible())
        # self.botao_regiao17.setVisible(not self.botao_regiao17.isVisible())
        # self.botao_regiao18.setVisible(not self.botao_regiao18.isVisible())
        # self.botao_regiao19.setVisible(not self.botao_regiao19.isVisible())
        # self.botao_regiao20.setVisible(not self.botao_regiao20.isVisible())
        # self.label_mapa_rio.lower()

        global fname
        global wind2
        global selected_map
        print(wind2)

        if wind2 == 1:
            self.window1.close()
            wind2 = 0
        elif wind2 == 0:
            self.window1 = Form2()
            self.window1.show()

        # if self.window1.isclosed()==True and wind2 == 0:
        #     self.elev_incl(fname)
        #     selected_map = 0

        # if self.window1 isclosed:
        #     self.elev_incl(fname)

        # self.window1.sig.connect(self.elev_incl(fname))

        # self.window1.closeEvent = self.elev_incl(fname)

        # self.window1.close.connect(self.elev_incl(fname))

        print("Mostra lista")
    #

    def mostra_recortar(self):
        self.corteArquivo_label.setVisible(not self.corteArquivo_label.isVisible())
        self.nome_arquivo_corte.setVisible(not self.nome_arquivo_corte.isVisible())
        self.recortar_Button.setVisible(not self.recortar_Button.isVisible())
    #

    def mostra_solo(self):
        self.lineEdit_areia.setVisible(not self.lineEdit_areia.isVisible())
        self.lineEdit_argila.setVisible(not self.lineEdit_argila.isVisible())
        self.label_areia.setVisible(not self.label_areia.isVisible())
        self.label_argila.setVisible(not self.label_argila.isVisible())
        self.label_silte.setVisible(not self.label_silte.isVisible())
        self.label_silte2.setVisible(not self.label_silte2.isVisible())
        self.label_material.setVisible(not self.label_material.isVisible())
        self.tabs_4.setVisible(not self.tabs_4.isVisible())
        if self.tri > 0:
            self.canvasT.setVisible(not self.canvasT.isVisible())
    #

    def mostra_chuva(self):
        self.tLbl.setVisible(not self.tLbl.isVisible())
        self.tlineEdit.setVisible(not self.tlineEdit.isVisible())
        self.horizontalSlider_t.setVisible(not self.horizontalSlider_t.isVisible())
        self.pLbl.setVisible(not self.pLbl.isVisible())
        self.plineEdit.setVisible(not self.plineEdit.isVisible())

        if self.plineEdit.isVisible() ==True:
            self.horizontalSlider_Hw.setVisible(False)
        else:
            self.horizontalSlider_Hw.setVisible(True)
    #

    def mostra_conversor(self):
        global wind3
        print(wind3)
        global fname

        if wind3 == 1:
            self.window2.close()
            wind3 = 0
        elif wind3 == 0:
            self.window2 = LatLon()
            self.window2.show()

            self.window2.ler_arquivo_popup(fname)
            resultado = self.window2.exec()  # Aguarda o usuário fechar o popup
    #

    def mostra_chuva2(self):
        global wind4
        print(wind4)
        global fname

        if wind4 == 1:
            self.window3.close()
            wind4 = 0
        elif wind4 == 0:
            self.window3 = Popup_rain()
            self.window3.show()
    #

    def mostra_vistas(self):
        # self.tLbl.setVisible(not self.tLbl.isVisible())
        # self.tlineEdit.setVisible(not self.tlineEdit.isVisible())
        # self.horizontalSlider_t.setVisible(not self.horizontalSlider_t.isVisible())
        # self.pLbl.setVisible(not self.pLbl.isVisible())
        # self.plineEdit.setVisible(not self.plineEdit.isVisible())

        self.topButton.setVisible(not self.topButton.isVisible())
        self.sideButton.setVisible(not self.sideButton.isVisible())
        self.frontButton.setVisible(not self.frontButton.isVisible())
    #

    def botao_clicado_regiao(self):
        botao_clicado = self.sender() # atribui o própio botão que foi clicado como uma variável

        arquivos_regiao =  {"botao_regiao1":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_1.tif",
                            "botao_regiao2":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_2.tif",
                            "botao_regiao3":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_3.tif",
                            "botao_regiao4":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_4.tif",
                            "botao_regiao5":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_5.tif",
                            "botao_regiao6":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_6.tif",
                            "botao_regiao7":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_7.tif",
                            "botao_regiao8":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_8.tif",
                            "botao_regiao9":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_9.tif",
                            "botao_regiao10":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_10.tif",
                            "botao_regiao11":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_11.tif",
                            "botao_regiao12":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_12.tif",
                            "botao_regiao13":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_13.tif",
                            "botao_regiao14":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_14.tif",
                            "botao_regiao15":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_15.tif",
                            "botao_regiao16":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_16.tif",
                            "botao_regiao17":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_17.tif",
                            "botao_regiao18":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_18.tif",
                            "botao_regiao19":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_19.tif",
                            "botao_regiao20":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_20.tif"}
        #

        self.label_mapa_rio.setVisible(False)
        self.botao_regiao1.setVisible(False)
        self.botao_regiao2.setVisible(False)
        self.botao_regiao3.setVisible(False)
        self.botao_regiao4.setVisible(False)
        self.botao_regiao5.setVisible(False)
        self.botao_regiao6.setVisible(False)
        self.botao_regiao7.setVisible(False)
        self.botao_regiao8.setVisible(False)
        self.botao_regiao9.setVisible(False)
        self.botao_regiao10.setVisible(False)
        self.botao_regiao11.setVisible(False)
        self.botao_regiao12.setVisible(False)
        self.botao_regiao13.setVisible(False)
        self.botao_regiao14.setVisible(False)
        self.botao_regiao15.setVisible(False)
        self.botao_regiao16.setVisible(False)
        self.botao_regiao17.setVisible(False)
        self.botao_regiao18.setVisible(False)
        self.botao_regiao19.setVisible(False)
        self.botao_regiao20.setVisible(False)

        # self.lista_rio.setVisible(False)

        global fname
        fname = arquivos_regiao[botao_clicado.objectName()]
        self.elev_incl(fname)

        # self.fname = arquivos_regiao[botao_clicado.objectName()]
        # self.elev_incl(self.fname)
    #

    def corta_tif(self):
        # Definir os índices para recortar
        recorte = self.img_array[int(self.x1lineEdit.text()):int(self.x2lineEdit.text()),int(self.y1lineEdit.text()):int(self.y2lineEdit.text())]    #Trocar x e y de lugar?

        # Converter o array NumPy de volta para um objeto de imagem PIL
        recorte_img = Image.fromarray(recorte)

        if str(self.nome_arquivo_corte.text()) == "":
            nome_arquivo_corte = 'recorte_arquivo.tif'
        else:
            nome_arquivo_corte =  str(self.nome_arquivo_corte.text()) + ".tif"

        # Salvar o recorte como um novo arquivo TIFF
        recorte_img.save(nome_arquivo_corte)

        print("Recorte realizado com sucesso!")
    #

    def view_top(self):
        self.plotter.camera_position = [
        (0, 0, 100),  # posição da câmera
        (0, 0, 0),  # ponto focal
        (0, -1, 0)   # vetor
        ]
        self.plotter.reset_camera()
    #

    def view_side(self):
        self.plotter.camera_position = [
        (1, 1, 1),  # posição da câmera
        (0, 0, 0),  # ponto focal
        (0, 0, 1)   # vetor
        ]
        self.plotter.reset_camera()
    #

    def view_front(self):
        self.plotter.camera_position = [
        (0, 1, 0),  # posição da câmera
        (0, 0, 0),  # ponto focal
        (0, 0, 1)   # vetor
        ]
        self.plotter.reset_camera()
    #
#

class Form2(QWidget):
    # sig = pyqtSignal()

    def __init__(self2,parent=None):
        #super().__init__(parent)
        super().__init__()
        #super(AppTaludes, self2).__init__()
        uic.loadUi("c:\\Users\\paulobaccar\\Documents\\AppTaludes\\form2.ui", self2)
        #self2 = Ui_Form2()
        #self2.setupUi(self2)
        self2.setMaximumSize(970,710)

        # Bairros RJ
        self2.botao_regiao1 = self2.findChild(QPushButton,"botao_regiao1")
        self2.botao_regiao2 = self2.findChild(QPushButton,"botao_regiao2")
        self2.botao_regiao3 = self2.findChild(QPushButton,"botao_regiao3")
        self2.botao_regiao4 = self2.findChild(QPushButton,"botao_regiao4")
        self2.botao_regiao5 = self2.findChild(QPushButton,"botao_regiao5")
        self2.botao_regiao6 = self2.findChild(QPushButton,"botao_regiao6")
        self2.botao_regiao7 = self2.findChild(QPushButton,"botao_regiao7")
        self2.botao_regiao8 = self2.findChild(QPushButton,"botao_regiao8")
        self2.botao_regiao9 = self2.findChild(QPushButton,"botao_regiao9")
        self2.botao_regiao10 = self2.findChild(QPushButton,"botao_regiao10")
        self2.botao_regiao11 = self2.findChild(QPushButton,"botao_regiao11")
        self2.botao_regiao12 = self2.findChild(QPushButton,"botao_regiao12")
        self2.botao_regiao13 = self2.findChild(QPushButton,"botao_regiao13")
        self2.botao_regiao14 = self2.findChild(QPushButton,"botao_regiao14")
        self2.botao_regiao15 = self2.findChild(QPushButton,"botao_regiao15")
        self2.botao_regiao16 = self2.findChild(QPushButton,"botao_regiao16")
        self2.botao_regiao17 = self2.findChild(QPushButton,"botao_regiao17")
        self2.botao_regiao18 = self2.findChild(QPushButton,"botao_regiao18")
        self2.botao_regiao19 = self2.findChild(QPushButton,"botao_regiao19")
        self2.botao_regiao20 = self2.findChild(QPushButton,"botao_regiao20")

        # Tornando os botões invisiveis e coloridos ao passar o mouse em cima
        self2.botao_regiao1.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao2.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao3.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao4.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao5.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao6.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao7.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao8.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao9.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao10.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao11.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao12.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao13.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao14.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao15.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao16.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao17.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao18.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao19.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self2.botao_regiao20.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")

        pixmap = QPixmap("c:\\Users\\paulobaccar\\Documents\\AppTaludes\\image.png")              #("c:\\Users\\paulobaccar\\Downloads\\mapa-rio-de-janeiro.jpg")
        self2.label_mapa_rio.setPixmap(pixmap)
        self2.label_mapa_rio.setScaledContents(True)
        # self2.gridLayout.setScaledContents(True)

        global wind2
        wind2 +=1
    #

    def botao_clicado_regiao(self2):
        botao_clicado = self2.sender() # atribui o própio botão que foi clicado como uma variável
        self2.label_mapa_rio.lower()

        arquivos_regiao =  {"botao_regiao1":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_1.tif",
                            "botao_regiao2":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_2.tif",
                            "botao_regiao3":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_3.tif",
                            "botao_regiao4":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_4.tif",
                            "botao_regiao5":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_5.tif",
                            "botao_regiao6":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_6.tif",
                            "botao_regiao7":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_7.tif",
                            "botao_regiao8":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_8.tif",
                            "botao_regiao9":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_9.tif",
                            "botao_regiao10":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_10.tif",
                            "botao_regiao11":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_11.tif",
                            "botao_regiao12":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_12.tif",
                            "botao_regiao13":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_13.tif",
                            "botao_regiao14":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_14.tif",
                            "botao_regiao15":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_15.tif",
                            "botao_regiao16":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_16.tif",
                            "botao_regiao17":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_17.tif",
                            "botao_regiao18":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_18.tif",
                            "botao_regiao19":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_19.tif",
                            "botao_regiao20":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\rj_recortes\\RJ_20.tif"}

        global fname
        global selected_map
        fname = arquivos_regiao[botao_clicado.objectName()]
        selected_map = 1
        # elev_incl(fname)
        # self2.setVisible(False)

        global wind2
        wind2 = 0

        # self2.sig.emit()
        # self2.connect(AppTaludes.elev_incl)

        global selfx
        AppTaludes.elev_incl(selfx,fname)

        self2.close()
    #

    def show_error_popup(self, error_message):
        # Cria a caixa de mensagem de erro
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)  # Define o ícone como erro
        msg.setWindowTitle("Erro")  # Define o título da janela
        msg.setText(error_message)  # Define o texto da mensagem
        msg.setStandardButtons(QMessageBox.Ok)  # Adiciona o botão OK
        msg.exec_()  # Exibe a mensagem
    #
#

# class Form3(QWidget):
#     def __init__(self3,parent=None):
#         super().__init__(parent)
#         self3.ui = Ui_Form()
#         self3.ui.setupUi(self3)


class LatLon(QDialog):
    global wind3
    def __init__(self4,parent=None):
        #super().__init__(parent)
        #self4.ui = Ui_Dialog()
        #self4.ui.setupUi(self4)
        #super(UI, self).__init__()
        super().__init__()
        uic.loadUi("c:\\Users\\paulobaccar\\Documents\\AppTaludes\\popup_LatLon.ui", self4)

        print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")

        self4.setWindowTitle("Conversor de Células")
        self4.botao_converte = self4.findChild(QPushButton,"botao_converte")
        self4.botao_converte.setWhatsThis("Após inserir as coordenadas, aperte para saber em qual célula(x,y) elas se encontram.")
        self4.botao_add_info = self4.findChild(QPushButton,"add_info")
        self4.botao_add_info.setWhatsThis("Insira as informações de latitude e longitude do seu arquivo aqui.")

        # Ativar o botão "?" na barra de título
        self4.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowContextHelpButtonHint)
        self4.botao_add_info = self4.findChild(QPushButton,"add_info")
        self4.botao_add_info.setEnabled(False)
        self4.lineEdit_celula = self4.findChild(QLineEdit,"lineEdit_celula")
        self4.lineEdit_latitude = self4.findChild(QLineEdit,"lineEdit_latitude")
        self4.lineEdit_longitude = self4.findChild(QLineEdit,"lineEdit_longitude")
        self4.label_lat_min = self4.findChild(QLabel,"lat_min")
        self4.label_lat_max = self4.findChild(QLabel,"lat_max")
        self4.label_long_min = self4.findChild(QLabel,"long_min")
        self4.label_long_max = self4.findChild(QLabel,"long_max")
        self4.label_info = self4.findChild(QLabel,"info")

        #self4.lay_principal = self4.findChild(QVBoxLayout,"lay_principal")
        #self4.setLayout(self4.lay_principal)

        global wind3
        wind3 +=1
    #

    def ler_arquivo_popup(self4, arquivo):
        self4.arquivo = arquivo
        self4.info_arquivo()
    #

    def info_arquivo(self4):
        print("função rodando...")
        with rasterio.open(self4.arquivo) as dataset:
            if dataset.crs is None:
                print("informações nulas")
                self4.botao_add_info.setEnabled(True)
                self4.label_info.setText("Informações: Seu arquivo não possui CRS")
                self4.label_lat_min.setText("Latitude Mínima: None")
                self4.label_lat_max.setText("Latitude Máxima: None")
                self4.label_long_min.setText("Longitude Mínima: None")
                self4.label_long_max.setText("Longitude Máxima: None")
                self4.lineEdit_latitude.setEnabled(False)
                self4.lineEdit_longitude.setEnabled(False)
                self4.lineEdit_celula.setEnabled(False)
            else:
                print("informações obtidas")
                bounds = dataset.bounds
                self4.label_lat_min.setText(f"Latitude Mínima: {bounds.bottom}")
                self4.label_lat_max.setText(f"Latitude Máxima: {bounds.top}")
                self4.label_long_min.setText(f"Longitude Mínima: {bounds.left}")
                self4.label_long_max.setText(f"Longitude Máxima: {bounds.right}")
    #

    def show_error_popup2(self4, error_message):
        # Cria a caixa de mensagem de erro
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)  # Define o ícone como erro
        msg.setWindowTitle("Erro")  # Define o título da janela
        msg.setText(error_message)  # Define o texto da mensagem
        msg.setStandardButtons(QMessageBox.Ok)  # Adiciona o botão OK
        msg.exec_()  # Exibe a mensagem
    #

    def show_add_info(self4):
        self4.popup_add_info = Popup_add_info()
        self4.popup_add_info.show()
        self4.lineEdit_latitude.setEnabled(True)
        self4.lineEdit_longitude.setEnabled(True)
        self4.lineEdit_celula.setEnabled(True)

        resultado = self4.popup_add_info.exec()
        # latmin,longmin,latmax,longmax = self4.popup_add_info.fornece_coordenadas()

        latmin,longmin,latmax,longmax = self4.popup_add_info.fornece_coordenadas()     #.fornece_coordenadas
        self4.label_lat_min.setText(f"Latitude Mínima: {latmin}")
        self4.label_lat_max.setText(f"Latitude Máxima: {latmax}")
        self4.label_long_min.setText(f"Longitude Mínima: {longmin}")
        self4.label_long_max.setText(f"Longitude Máxima: {longmax}")

        global wind3
        wind3 = 0
        # self4.close()
    #

    def converteLatLon(self4):
        print("chamou a função")
        if self4.lineEdit_latitude =='' or self4.lineEdit_longitude =='':
            self4.show_error_popup2("Um dos campos obrigatórios está vazio.")
        else:
            print("ARQUIVO: ",self4.arquivo)
            lat = self4.lineEdit_latitude.text()
            long = self4.lineEdit_longitude.text()
            with rasterio.open(self4.arquivo) as dataset:
                print(f"CRS do dataset: {dataset.crs!r}")
                if dataset.crs is None:
                    print(" O TIFF não tem CRS! Entrando no if...") # Se NÃO houver Sistema de referência espacial (CRS)

                    lat_inicial = Popup_add_info.fornece_coordenadas(self4)[0]
                    lon_inicial = self4.popup_add_info.fornece_coordenadas()[1]

                    lat_final = self4.popup_add_info.fornece_coordenadas()[2]
                    lon_final = self4.popup_add_info.fornece_coordenadas()[3]

                    self4.label_lat_min.setText(f"Latitude Mínima: {lat_inicial}")
                    self4.label_lat_max.setText(f"Latitude Máxima: {lat_final}")
                    self4.label_long_min.setText(f"Longitude Mínima: {lon_inicial}")
                    self4.label_long_max.setText(f"Longitude Máxima: {lon_final}")

                    # lat_inicial = -23
                    # lon_inicial = -43.15

                    # lat_final = -22.77
                    # lon_final = -43.5

                    latitude = float(lat)
                    longitude = float(long)

                    if (latitude > lat_inicial and latitude < lat_final) or latitude == lat_inicial or latitude == lat_final:
                        print('latitude', latitude)
                        if (longitude > lon_final and longitude < lon_inicial) or longitude == lon_inicial or longitude == lon_final:
                            print('longitude', longitude)
                            resto = latitude - lat_inicial
                            print("resto lat:",resto)
                            qt_celulay = resto/self4.popup_add_info.fornece_pixel()[0]

                            resto2 = longitude - lon_inicial
                            print("resto long:",abs(resto2))
                            qt_celulax = resto2/self4.popup_add_info.fornece_pixel()[1]

                            print(dataset.shape)
                            print(f"Célula: {abs(qt_celulax):.0f}, {abs(qt_celulay):.0f}")
                            self4.lineEdit_celula.setText(f"({abs(qt_celulax):.0f}, {abs(qt_celulay):.0f})")
                else:
                    print(" O TIFF tem CRS:", dataset.crs)
                    resolucao_x, resolucao_y = dataset.res[0], dataset.res[1] # Tamanho do pixel em graus (lon/lat)
                    bounds = dataset.bounds # Obter os limites (bounding box)

                    lat_inicial = bounds.bottom # Min Y (Latitude)
                    lon_inicial = bounds.left # Min X (Longitude)

                    lat_final = bounds.top # Max Y (Latitude)
                    lon_final = bounds.right # Max X (Longitude)

                    latitude = float(lat)
                    longitude = float(long)

                    print(f"Coordenadas iniciais: {bounds.bottom},{bounds.left}/Coordenadas finais: {bounds.top},{bounds.right}")

                    if (latitude > lat_inicial and latitude < lat_final) or latitude == lat_inicial or latitude == lat_final:
                        print("latitude",latitude)
                        if (longitude > lon_inicial and longitude < lon_final) or longitude == lon_inicial or longitude == lon_final:
                            print("longitude")
                            resto = latitude - lat_inicial
                            print("resto lat:",resto)
                            qt_celulax = resto/resolucao_x

                            resto2 = longitude - lon_inicial
                            print("resto long:",abs(resto2))
                            qt_celulay = resto2/resolucao_y

                            banda1 = dataset.read(1)
                            print(banda1.shape)
                            print(f"Célula: {abs(qt_celulax):.0f}, {abs(qt_celulay):.0f}")
                            self4.lineEdit_celula.setText(f"({abs(qt_celulax):.0f}, {abs(qt_celulay):.0f})")
        global wind3
        wind3 = 0
        # self4.close()
#

class Popup_add_info(QDialog):
    def __init__(self5,parent=None):
        #super().__init__(parent)
        #self5.ui = Ui_Dialog2()
        #self5.ui.setupUi(self5)
        super().__init__()
        uic.loadUi("c:\\Users\\paulobaccar\\Documents\\AppTaludes\\add_info.ui", self5)

        self5.latitude = self5.findChild(QLineEdit,"latitude")
        self5.longitude = self5.findChild(QLineEdit,"longitude")

        self5.lineEdit_lat_min = self5.findChild(QLineEdit,"add_lat_min")
        self5.lineEdit_long_min = self5.findChild(QLineEdit,"add_long_min")
        self5.lineEdit_lat_max = self5.findChild(QLineEdit,"add_lat_max")
        self5.lineEdit_long_max = self5.findChild(QLineEdit,"add_long_max")

        #self5.lay_principal = self5.findChild(QVBoxLayout,"lay_principal")
        #self5.setLayout(self5.lay_principal)

        def resizeEvent(self5, event):
            # Ajusta a QLabel para ocupar o mesmo tamanho do layout
            if self5.layout:
                # Mantém a proporção ao redimensionar
                new_width = event.size().width()
                new_height = int(new_width / self5.aspect_ratio)
                self5.resize(new_width, new_height)

                super().resizeEvent(event)
    #
    
    def fornece_pixel(self5):
        print("fornecendo pixel...")
        qtd_x = (float(self5.lineEdit_lat_max.text())-float(self5.lineEdit_lat_min.text()))
        print(qtd_x)
        qtd_y = (float(self5.lineEdit_long_max.text())-float(self5.lineEdit_long_min.text()))
        print(qtd_y)
        return (qtd_x,qtd_y)
    
        # return (float(self5.ui.latitude.text()),float(self5.ui.longitude.text()))
    #
    
    def fornece_coordenadas(self5):
        print("fornecendo coordenadas...")
        #self5.listLL = list(float(self5.lat_min.text()), float(self5.long_min.text()), float(self5.lat_max.text()), float(self5.long_max.text()))
        return (float(self5.lineEdit_lat_min.text()), float(self5.lineEdit_long_min.text()), float(self5.lineEdit_lat_max.text()), float(self5.lineEdit_long_max.text()))
    #
    
    def salvar(self5):
        print("salvando...")
        self5.accept()

        return
    #
#

class Material(QWidget):
    def __init__(self, type, theta_r, theta_500, theta_s, vg_a, vg_n, vg_m, vg_k, parent=None):

        self.type = type
        self.theta_r = theta_r
        self.theta_500 = theta_500
        self.theta_s = theta_s
        self.vg_alpha = vg_a
        self.vg_n = vg_n
        self.vg_m = vg_m
        self.vg_k = vg_k
    #
#

class Popup_rain(QDialog): 
    def __init__(self6):
        super().__init__()
        uic.loadUi("c:\\Users\\paulobaccar\\Documents\\AppTaludes\\rain.ui", self6)
        
        self6.slider_hours = self6.findChild(QSlider,"slider_hours")
        self6.line_edit_hw = self6.findChild(QLineEdit,"line_edit_hw")
        self6.line_edit_precipitation = self6.findChild(QLineEdit,"line_edit_precipitation")
        self6.label_time = self6.findChild(QLabel,"label_time")

        self6.line_edit_precipitation.setText("1")
        
        self6.show()
        
    # def rain_infiltration(self,h,p,t,theta_i):
    def rain_infiltration(self6):

        # variáveis fornecidas pelo usuario
        p = int(self6.line_edit_precipitation.text()) # mm
        p = p/1000 # mm/h -> m/h
        print("precipitação (m/h)=",p) 
        t = int(self6.slider_hours.value()) # h
        print("horas=",t) 

        # variáveis obtidas da função runAnalysis (necessario defini-las como variaveis globais)
        self6.theta_i = 0.3
        self6.h = 3 # m

        theta_i = self6.theta_i
        h = self6.h

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

        self6.line_edit_hw.setText(f'{hw:.7f}')
        print("hw (m) =", hw)
        print("------------------------------------------------------------")
        return 

        
#


#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    widget = AppTaludes()
#    widget.show()
#    sys.exit(app.exec_())

app = QApplication(sys.argv)
UIWindow = AppTaludes()
UIWindow.show()
sys.exit(app.exec_())
