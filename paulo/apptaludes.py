# This Python file uses the following encoding: utf-8
import sys

# from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QPushButton, QSizePolicy, QToolBar, QToolButton, QMainWindow
from PySide2.QtGui import QPixmap
from PyQt5 import uic
# from PySide2 import QtGui
from PyQt5.QtWidgets import QMainWindow

import scipy as sp
# from scipy.ndimage import gaussian_filter

import numpy as np
from PIL import Image

import rasterio

import matplotlib.cm as cm
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib as mpl
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mpltern
from mpltern.datasets import get_triangular_grid

from matplotlib.ticker import AutoMinorLocator, MultipleLocator

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar

# from matplotlib.colors import LinearSegmentedColormap

# #python -m pip install scipy (No terminal)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
#
# Needs to run
# python -m pip install -U mpltern
# to install mpltern
from ui_form import Ui_AppTaludes

class AppTaludes(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AppTaludes()
        self.ui.setupUi(self)


        # super(AppTaludes,self).__init__()



        uic.loadUi("C://Users//paulobaccar//Documents//AppTaludes//form.ui", self) # Carregar o arquivo .ui
        # self.setWindowTitle("22S435W - Rio de Janeiro")
        # self.setGeometry(200, 100, 572, 377)

        # # Imagem do mapa
        # self.fundo = QLabel(self)
        # self.fundo.setPixmap(QPixmap("c:\\Users\\paulobaccar\\Documents\\Projeto-Taludes\\betsabe\\Imagens Interface\\image.png"))  # Caminho da imagem
        # self.fundo.setScaledContents(True) # Ajusta a imagem ao tamanho do QLabel



        self.ui.tabs.tabCloseRequested.connect(self.tabs.removeTab)
        self.ui.tabs_2.tabCloseRequested.connect(self.ui.tabs_2.removeTab)
        self.ui.tabs_3.tabCloseRequested.connect(self.ui.tabs_3.removeTab)

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

        self.ui.horizontalSlider_C.valueChanged.connect(self.number_changed)             #c
        self.ui.horizontalSlider_Phi.valueChanged.connect(self.number_changed)           #phi
        self.ui.horizontalSlider_H.valueChanged.connect(self.number_changed)             #h
        self.ui.horizontalSlider_Hw.valueChanged.connect(self.number_changed)            #hw
        self.ui.horizontalSlider_Theta.valueChanged.connect(self.number_changed)         #theta
        self.ui.horizontalSlider_t.valueChanged.connect(self.number_changed)             #t

        self.ui.lineEdit_areia.textChanged.connect(self.number_changed_2)       #Areia
        self.ui.lineEdit_argila.textChanged.connect(self.number_changed_2)      #Argila

        self.material_type = 'GRANULAR FINE'
        self.ui.lineEdit_areia.textChanged.connect(self.define_material)       #Areia
        self.ui.lineEdit_argila.textChanged.connect(self.define_material)      #Argila

        self.ui.x1label.setVisible(False)
        self.ui.x2label.setVisible(False)
        self.ui.y1label.setVisible(False)
        self.ui.y2label.setVisible(False)
        self.ui.label.setVisible(False)
        self.ui.limits.setVisible(False)
        self.ui.imgname.setVisible(False)
        self.ui.imgsizex.setVisible(False)
        self.ui.imgsizey.setVisible(False)

        self.ui.x1lineEdit.setVisible(False)
        self.ui.x2lineEdit.setVisible(False)
        self.ui.y1lineEdit.setVisible(False)
        self.ui.y2lineEdit.setVisible(False)
        self.ui.Adjust.setVisible(False)

        self.ui.AnalysisBtn.setVisible(False)
        self.ui.tabs.setVisible(False)
        self.ui.tabs_2.setVisible(False)
        self.ui.tabs_3.setVisible(False)

        self.ui.lineEdit_areia.setVisible(False)
        self.ui.lineEdit_argila.setVisible(False)
        self.ui.label_areia.setVisible(False)
        self.ui.label_argila.setVisible(False)
        self.ui.label_silte.setVisible(False)
        self.ui.label_silte2.setVisible(False)
        self.ui.label_material.setVisible(False)

        self.ui.hLbl.setVisible(False)
        self.ui.hlineEdit.setVisible(False)
        self.ui.horizontalSlider_H.setVisible(False)
        self.ui.hwLbl.setVisible(False)
        self.ui.hwlineEdit.setVisible(False)
        self.ui.horizontalSlider_Hw.setVisible(False)
        self.ui.cLbl.setVisible(False)
        self.ui.ClineEdit.setVisible(False)
        self.ui.horizontalSlider_C.setVisible(False)
        self.ui.oLbl.setVisible(False)
        self.ui.philineEdit.setVisible(False)
        self.ui.horizontalSlider_Phi.setVisible(False)
        self.ui.thetaLbl.setVisible(False)
        self.ui.thetalineEdit.setVisible(False)
        self.ui.horizontalSlider_Theta.setVisible(False)
        self.ui.tLbl.setVisible(False)
        self.ui.tlineEdit.setVisible(False)
        self.ui.horizontalSlider_t.setVisible(False)
        self.ui.pLbl.setVisible(False)
        self.ui.plineEdit.setVisible(False)
        self.ui.ClearBtn.setVisible(False)
        self.ui.mapaRio_Button.setVisible(False)
        self.ui.corteArquivo_label.setVisible(False)
        self.ui.corteArquivo_label.setMaximumSize(170,15)
        self.ui.nome_arquivo_corte.setVisible(False)
        self.ui.recortar_Button.setVisible(False)
        self.ui.browse.setVisible(False)
        self.ui.prop_Button.setVisible(False)

        self.n_tabs = 0
        self.inclina_tabs = 0
        self.number_analysis = 0
        self.number_of_adjusts = 0

        self.ui.horizontalSlider_H.setSingleStep(0.1)

        self.figure = plt.figure()

        self.ui.AnalysisBtn.clicked.connect(self.analysisClick)
        self.ui.AnalysisBtn.clicked.connect(self.runAnalysis)
        self.ui.Adjust.clicked.connect(self.figureAdjust)
        self.ui.ClearBtn.clicked.connect(self.clearCanvas)
        self.hidden = 0
        self.toolButton3.clicked.connect(self.showProp)
        self.toolButton.clicked.connect(self.getfile)
        self.toolButton2.clicked.connect(self.mostra_solo)
        self.toolButton4.clicked.connect(self.mostra_lista)
        self.toolButton5.clicked.connect(self.mostra_recortar)
        self.toolButton6.clicked.connect(self.mostra_chuva)

        # Bairros RJ
        self.botao_regiao1 = self.findChild(QPushButton,"botao_regiao1")
        self.botao_regiao2 = self.findChild(QPushButton,"botao_regiao2")
        self.botao_regiao3 = self.findChild(QPushButton,"botao_regiao3")
        self.botao_regiao4 = self.findChild(QPushButton,"botao_regiao4")
        self.botao_regiao5 = self.findChild(QPushButton,"botao_regiao5")
        self.botao_regiao6 = self.findChild(QPushButton,"botao_regiao6")
        self.botao_regiao7 = self.findChild(QPushButton,"botao_regiao7")
        self.botao_regiao8 = self.findChild(QPushButton,"botao_regiao8")
        self.botao_regiao9 = self.findChild(QPushButton,"botao_regiao9")
        self.botao_regiao10 = self.findChild(QPushButton,"botao_regiao10")
        self.botao_regiao11 = self.findChild(QPushButton,"botao_regiao11")
        self.botao_regiao12 = self.findChild(QPushButton,"botao_regiao12")
        self.botao_regiao13 = self.findChild(QPushButton,"botao_regiao13")
        self.botao_regiao14 = self.findChild(QPushButton,"botao_regiao14")
        self.botao_regiao15 = self.findChild(QPushButton,"botao_regiao15")
        self.botao_regiao16 = self.findChild(QPushButton,"botao_regiao16")
        self.botao_regiao17 = self.findChild(QPushButton,"botao_regiao17")
        self.botao_regiao18 = self.findChild(QPushButton,"botao_regiao18")
        self.botao_regiao19 = self.findChild(QPushButton,"botao_regiao19")
        self.botao_regiao20 = self.findChild(QPushButton,"botao_regiao20")

        # Tornando os botões invisiveis e coloridos ao passar o mouse em cima
        self.botao_regiao1.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao2.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao3.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao4.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao5.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao6.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao7.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao8.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao9.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao10.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao11.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao12.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao13.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao14.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao15.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao16.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao17.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao18.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao19.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao20.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")

        # Botões começam invisíveis
        self.ui.label_mapa_rio.setVisible(False)
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
        self.ui.label_mapa_rio.setPixmap(pixmap)

        self.setMinimumSize(1500,1000)

        self.tri = 0
        self.material_definido = 0
        plt.close()
    #

    def showProp(self):
        if self.hidden == 0:
            self.ui.hLbl.setVisible(False)
            self.ui.hlineEdit.setVisible(False)
            self.ui.horizontalSlider_H.setVisible(False)
            self.ui.hwLbl.setVisible(False)
            self.ui.hwlineEdit.setVisible(False)
            self.ui.horizontalSlider_Hw.setVisible(False)
            self.ui.cLbl.setVisible(False)
            self.ui.ClineEdit.setVisible(False)
            self.ui.horizontalSlider_C.setVisible(False)
            self.ui.oLbl.setVisible(False)
            self.ui.philineEdit.setVisible(False)
            self.ui.horizontalSlider_Phi.setVisible(False)
            self.ui.thetaLbl.setVisible(False)
            self.ui.thetalineEdit.setVisible(False)
            self.ui.horizontalSlider_Theta.setVisible(False)
            self.ui.ClearBtn.setVisible(False)
            self.hidden = 1
        else:
            self.ui.hLbl.setVisible(True)
            self.ui.hlineEdit.setVisible(True)
            self.ui.horizontalSlider_H.setVisible(True)
            self.ui.hwLbl.setVisible(True)
            self.ui.hwlineEdit.setVisible(True)
            self.ui.horizontalSlider_Hw.setVisible(True)
            self.ui.cLbl.setVisible(True)
            self.ui.ClineEdit.setVisible(True)
            self.ui.horizontalSlider_C.setVisible(True)
            self.ui.oLbl.setVisible(True)
            self.ui.philineEdit.setVisible(True)
            self.ui.horizontalSlider_Phi.setVisible(True)
            self.ui.thetaLbl.setVisible(True)
            self.ui.thetalineEdit.setVisible(True)
            self.ui.horizontalSlider_Theta.setVisible(True)
            self.ui.ClearBtn.setVisible(True)
            self.hidden = 0
    #

    def define_material(self):
        if self.material_definido >=1 :
            self.canvasT.setParent(None)

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
            self.ui.horizontalSlider_C.setMaximum(0)
            self.ui.horizontalSlider_C.setMinimum(0)
        # else:
        #     self.ui.horizontalSlider_C.setVisible(True)

        self.ui.horizontalSlider_Theta.setMaximum(self.material_theta_s * 1000)
        self.ui.horizontalSlider_Theta.setMinimum(self.material_theta_500 * 1000)
        self.ui.horizontalSlider_Theta.setSliderPosition(self.material_theta_500 * 1000)
        self.ui.horizontalSlider_Theta.setSingleStep((self.material_theta_s - self.material_theta_500) * 100)
        self.ui.horizontalSlider_Theta.setPageStep((self.material_theta_s - self.material_theta_500) * 100)
        self.ui.horizontalSlider_Theta.setTickInterval((self.material_theta_s - self.material_theta_500)/100)

        self.ui.label_material.setText(str(self.material_type))

        fig = plt.figure()
        # fig.set_figwidth(4.5)
        # fig.set_figheight(3.9)

        ax = plt.subplot(111,projection="ternary")

        ax.taxis.set_major_locator(MultipleLocator(0.2))
        ax.laxis.set_major_locator(MultipleLocator(0.2))
        ax.raxis.set_major_locator(MultipleLocator(0.2))

        ax.set_tlabel("Argila")
        ax.set_llabel("Areia")
        ax.set_rlabel("Silte")
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

        self.tri+=1

        fig.tight_layout
        self.canvasT = FigureCanvas(fig)
        self.canvasT.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.canvasT.setMaximumSize(315,300)           #(390,345)

        plt.close('all')
        self.ui.verticalLayout_6.addWidget(self.canvasT)

        valueC = str(self.ui.horizontalSlider_C.value())
        self.ui.ClineEdit.setText(valueC)

        valuePhi = str(self.ui.horizontalSlider_Phi.value())
        self.ui.philineEdit.setText(valuePhi)

        valueH = str(self.ui.horizontalSlider_H.value()/10)
        self.ui.hlineEdit.setText(valueH)

        valueHw = str(self.ui.horizontalSlider_Hw.value() * self.ui.horizontalSlider_H.value()/1000)
        self.ui.hwlineEdit.setText(valueHw)

        valueTheta = str(self.ui.horizontalSlider_Theta.value()/1000)
        self.ui.thetalineEdit.setText(valueTheta)

        # self.ui.lineEdit_areia.setVisible(True)
        # self.ui.lineEdit_argila.setVisible(True)
        # self.ui.label_areia.setVisible(True)
        # self.ui.label_argila.setVisible(True)
        # self.ui.label_silte.setVisible(True)
        # self.ui.label_silte2.setVisible(True)
        # self.ui.label_material.setVisible(True)

        self.material_definido+=1
    #

    def number_changed(self):
        valueC = str(self.ui.horizontalSlider_C.value())
        self.ui.ClineEdit.setText(valueC)

        valuePhi = str(self.ui.horizontalSlider_Phi.value())
        self.ui.philineEdit.setText(valuePhi)

        valueH = str(self.ui.horizontalSlider_H.value()/10)
        self.ui.hlineEdit.setText(valueH)

        valueHw = str(self.ui.horizontalSlider_Hw.value() * self.ui.horizontalSlider_H.value()/1000)
        self.ui.hwlineEdit.setText(valueHw)

        valueTheta = str(self.ui.horizontalSlider_Theta.value()/1000)
        self.ui.thetalineEdit.setText(valueTheta)

        print("number_changed")

        self.runAnalysis2()
    #

    def number_changed_2(self):
        self.valueAreia = int(self.ui.lineEdit_areia.text())
        valueAreia = self.ui.lineEdit_areia.text()

        self.valueArgila = int(self.ui.lineEdit_argila.text())
        valueArgila = self.ui.lineEdit_argila.text()

        self.valueSilte = 100 - self.valueArgila - self.valueAreia
        valueSilte = str(self.valueSilte)
        self.ui.label_silte2.setText(valueSilte)

        # print(self.ui.lineEdit_areia.text())
        # print(self.ui.lineEdit_argila.text())

        print("number_changed_2")
    #

    def analysisClick(self):
        self.n_tabs += 1
    #

    def runAnalysis(self):
        self.fname = self.ui.imgname.text()
        imgx = Image.open(self.fname)

        # self.ui.tabs.setVisible(True)
        self.ui.tabs_2.setVisible(True)

        X1 = int(self.ui.x1lineEdit.text())
        X2 = int(self.ui.x2lineEdit.text())
        y1 = int(self.ui.y1lineEdit.text())
        y2 = int(self.ui.y2lineEdit.text())

        h_value = self.ui.horizontalSlider_H.value()/10;
        hw_value = self.ui.horizontalSlider_Hw.value();
        c_value = self.ui.horizontalSlider_C.value();
        phi_value = self.ui.horizontalSlider_Phi.value();
        theta_value = self.ui.horizontalSlider_Theta.value();

        c = c_value
        h = h_value
        phi = phi_value
        hw = h_value * hw_value/100
        theta_i = theta_value/1000
        self.fos_array = np.ones((imgx.size[0]+1,imgx.size[1]+1))   #[x1:x2, y1:y2]

        # Creating figure
        self.fos_array = self.fos_array.transpose()

        if self.number_of_adjusts >= 1:
            self.fos_array = self.fos_array[y1-1:y2, X1-1:X2]

            sizey = X2-X1
            sizex = y2-y1

            # print("SIZES:")
            # print(sizey)
            # print(sizex)

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

            for i in range(0, sizex):
                for j in range(0, sizey):
                    if self.fos_array[i-1,j-1] > 2:
                        self.fos_array[i-1,j-1] = float("NaN")
            for i in range(0, sizex):
                for j in range(0, sizey):
                    if self.fos_array[i-1,j-1] < 1:
                        self.fos_array[i-1,j-1] = 1

            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))

            cmap = plt.get_cmap('rainbow_r')

            plt.imshow(self.fos_array.transpose(), cmap)
            im_fos = ax.imshow(self.fos_array.transpose(), cmap)

            ax.set_yticks([0, 0.2*sizey, 0.4*sizey, 0.6*sizey, 0.8*sizey, sizey], labels=[0, 5*sizey, 10*sizey, 15*sizey, 20*sizey, 25*sizey])
            ax.set_xticks([0, 0.2*sizex, 0.4*sizex, 0.6*sizex, 0.8*sizex, sizex], labels=[0, 5*sizex, 10*sizex, 15*sizex, 20*sizex, 25*sizex])

            plt.colorbar(im_fos,ax=ax)
            plt.axis([0, sizex-1, 0, sizey-1])
            ax.invert_yaxis()
        else:
            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))

            # print("RANGES:")
            # print(imgx.size[0])
            # print(imgx.size[1])

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

            for i in range(1,imgx.size[0]-1):
                for j in range(1,imgx.size[1]):
                    if self.fos_array[j-1,i-1] > 2:
                        self.fos_array[j-1,i-1] = float("NaN")
            for i in range(1,imgx.size[0]-1):
                for j in range(1,imgx.size[1]):
                    if self.fos_array[j-1,i-1] < 1:
                        self.fos_array[j-1,i-1] = 1

            cmap = plt.get_cmap('rainbow_r')

            plt.imshow(self.fos_array, cmap)
            im_fos = ax.imshow(self.fos_array, cmap)

            ax.set_yticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1], imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])
            ax.set_xticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0], imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])

            plt.colorbar(im_fos,ax=ax)
            plt.axis([0, imgx.size[0], 0, imgx.size[1]])
            ax.invert_yaxis()



        # Display figure
        self.canvas_fos = FigureCanvas(fig_fos)
        self.toolb_fos = NavigationToolbar(self.canvas_fos, self)

        self.tabInc = QWidget()
        self.tabInc_layout = QVBoxLayout()
        self.tabInc_layout.addWidget(self.canvas_fos)
        self.tabInc_layout.addWidget(self.toolb_fos)
        self.tabInc.setLayout(self.tabInc_layout)

        if self.ui.tabs_2.count() == 1:
            self.ui.tabs_2.removeTab(0)
        #

        self.tab_name = "Segurança " + str(self.inclina_tabs)
        self.ui.tabs_2.addTab(self.tabInc,self.tab_name)

        plt.close('all')

        print("runAnalysis")
    #

    def runAnalysis2(self):
        self.ui.tabs_2.removeTab(-1)

        fname = self.ui.imgname.text()
        imgx = Image.open(fname)

        # self.ui.tabs.setVisible(True)
        self.ui.tabs_2.setVisible(True)

        X1 = int(self.ui.x1lineEdit.text())
        X2 = int(self.ui.x2lineEdit.text())
        y1 = int(self.ui.y1lineEdit.text())
        y2 = int(self.ui.y2lineEdit.text())

        h_value = self.ui.horizontalSlider_H.value()/10;
        hw_value = self.ui.horizontalSlider_Hw.value();
        c_value = self.ui.horizontalSlider_C.value();
        phi_value = self.ui.horizontalSlider_Phi.value();
        theta_value = self.ui.horizontalSlider_Theta.value();

        c = c_value
        h = h_value
        phi = phi_value
        hw = h_value * hw_value/100
        theta_i = theta_value/1000
        self.fos_array = np.ones((imgx.size[1],imgx.size[0]))   #[x1:x2, y1:y2]

        # Creating figure
        self.fos_array = self.fos_array.transpose()

        if self.number_of_adjusts >= 1:
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

            for i in range(0, sizex):
                for j in range(0, sizey):
                    if self.fos_array[i-1,j-1] > 2:
                        self.fos_array[i-1,j-1] = float("NaN")
            for i in range(0, sizex):
                for j in range(0, sizey):
                    if self.fos_array[i-1,j-1] < 1:
                        self.fos_array[i-1,j-1] = 1

            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))

            cmap = plt.get_cmap('rainbow_r')

            plt.imshow(self.fos_array.transpose(), cmap)
            im_fos = ax.imshow(self.fos_array.transpose(), cmap)

            ax.set_yticks([0, 0.2*sizey, 0.4*sizey, 0.6*sizey, 0.8*sizey, sizey], labels=[0, 5*sizey, 10*sizey, 15*sizey, 20*sizey, 25*sizey])
            ax.set_xticks([0, 0.2*sizex, 0.4*sizex, 0.6*sizex, 0.8*sizex, sizex], labels=[0, 5*sizex, 10*sizex, 15*sizex, 20*sizex, 25*sizex])

            plt.colorbar(im_fos,ax=ax)
            plt.axis([0, sizex-1, 0, sizey-1])
            ax.invert_yaxis()
        else:
            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))

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

                    # self.fos_array[j,i] = (1605074512383065*(alpha**2)*(c**2)*(h**2)*phi)/151115727451828646838272 - (1414963042633059*(alpha**2)*(c**2)*h*phi)/18889465931478580854784 - (2774717211173289*(alpha**2)*(c**2)*hw*phi)/604462909807314587353088 + (2835477809945801*(alpha**2)*(c**2)*phi)/37778931862957161709568 + (6731555515546295*(alpha**2)*c)/73786976294838206464 + (5516753565726847*(alpha**2)*phi)/147573952589676412928 + (5653461066590515*alpha*(c**2)*h)/590295810358705651712 + (3025671568382675*alpha*(c**2)*phi)/590295810358705651712 - (2098110323770171*alpha*(c**2))/36893488147419103232 - (3002978305542275*alpha*c*(h**2))/4611686018427387904 + (2687741203999111*alpha*c*h)/576460752303423488 + (6472386681360727*alpha*c*hw*phi)/590295810358705651712 - (2982096583892561*alpha*c*(phi**2))/2361183241434822606848 - (4627184841729915*alpha*c)/288230376151711744 - (5688086807612743*alpha*(phi**2))/590295810358705651712 - (4311146912769217*alpha*phi)/1152921504606846976 - (4976341265194569*(c**2)*(h**2)*phi)/147573952589676412928 + (2283034929082703*(c**2)*h*phi)/9223372036854775808 + (1342385546936077*(c**2)*hw*phi)/147573952589676412928 - (1295331185150365*(c**2)*phi)/2305843009213693952 + (2592141320026855*c*(h**2))/72057594037927936 - (4971891995221437*c*h)/18014398509481984 - (4809409727287499*c*hw*phi)/9223372036854775808 + (2265715759669333*c*(phi**2))/36893488147419103232 + (3352624142374595*c)/4503599627370496 + (20768301037335*(h**2)*(hw**2)*phi)/2305843009213693952 - (1324783938325601*hw)/36028797018963968 + (3497832476657703*(phi**2))/4611686018427387904 + (6865366199800263*phi)/72057594037927936 + 1489595912300695/9007199254740992;

            for i in range(1,imgx.size[0]):
                for j in range(1,imgx.size[1]):
                    if self.fos_array[i-1,j-1] > 2:
                        self.fos_array[i-1,j-1] = float("NaN")
            for i in range(1,imgx.size[0]):
                for j in range(1,imgx.size[1]):
                    if self.fos_array[i-1,j-1] < 1:
                        self.fos_array[i-1,j-1] = 1

            cmap = plt.get_cmap('rainbow_r')

            plt.imshow(self.fos_array.transpose(), cmap)
            im_fos = ax.imshow(self.fos_array.transpose(), cmap)

            ax.set_yticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1], imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])
            ax.set_xticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0], imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])

            plt.colorbar(im_fos,ax=ax)
            plt.axis([0, imgx.size[0], 0, imgx.size[1]])
            ax.invert_yaxis()
        #

        # Display figure
        self.canvas_fos = FigureCanvas(fig_fos)
        self.toolb_fos = NavigationToolbar(self.canvas_fos, self)

        self.tabInc = QWidget()
        self.tabInc_layout = QVBoxLayout()
        self.tabInc_layout.addWidget(self.canvas_fos)
        self.tabInc_layout.addWidget(self.toolb_fos)
        self.tabInc.setLayout(self.tabInc_layout)

        if self.ui.tabs_2.count() == 1:
            self.ui.tabs_2.removeTab(0)
        #

        self.tab_name = "Segurança " + str(self.inclina_tabs)
        self.ui.tabs_2.addTab(self.tabInc,self.tab_name)

        plt.close('all')
        print("runAnalysis2")
    #

    def getfile(self):
        self.figure.clear()

        self.fname, _ = QFileDialog.getOpenFileName(self, "Open File","c:\\Users\\paulobaccar\\Documents","Tif files(*.tif);;Tiff files(*.tiff)")

        # self.ui.tabs.setVisible(True)

        self.elev_incl(self.fname)
    #

    def elev_incl(self,arquivo):
        # fig = plt.figure()
        # fig.set_figwidth(4.5)
        # fig.set_figheight(3.9)

        # ax = plt.subplot(111,projection="ternary")

        # t, l, r = get_triangular_grid()
        # ax.triplot(t,l,r)

        # ax.taxis.set_major_locator(MultipleLocator(0.1))
        # ax.laxis.set_major_locator(MultipleLocator(0.1))
        # ax.raxis.set_major_locator(MultipleLocator(0.1))

        # ax.set_tlabel("Argila")
        # ax.set_llabel("Areia")
        # ax.set_rlabel("Silte")
        # ax.tick_params(labelrotation="axis")

        # ax.grid(which='major') #which="both")

        # t = [0.6, 0.6, 0.35, 0.35]
        # l = [0.4, 0, 0, 0.65]
        # r = [0, 0.4, 0.65, 0]
        # ax.fill(t, l, r, color="b") #Trapézio azul

        # t = [1, 0.6, 0.6]
        # l = [0, 0.4, 0]
        # r = [0, 0 , 0.4]
        # ax.fill(t, l, r, color="m") #Triângulo roxo

        # t = [0.35, 0.35, 0.18, 0.18]
        # l = [0.65, 0.15, 0.15, 0.82]
        # r = [0, 0.5, 0.67, 0]
        # ax.fill(t, l, r, color="y") #Trapézio amarelo

        # t = [0.35, 0.35, 0.18, 0.18]
        # l = [0.15, 0, 0, 0.15]
        # r = [0.5, 0.65, 0.82, 0.67]
        # ax.fill(t, l, r, color="lime") #Paralelogramo verde claro

        # t = [0.18, 0.18, 0, 0]
        # l = [0.15, 0, 0, 0.15]
        # r = [0.67, 0.82, 1, 0.85]
        # ax.fill(t, l, r, color="g") #Paralelogramo verde escuro

        # t = [0.18, 0.18, 0, 0]
        # l = [0.65, 0.15, 0.15, 0.65]
        # r = [0.17, 0.67, 0.82, 0.35]
        # ax.fill(t, l, r, color="orange") #Paralelogramo laranja

        # t = [0.18, 0.18, 0, 0]
        # l = [0.82, 0.65, 0.65, 1]
        # r = [0, 0.17, 0.35, 0]
        # ax.fill(t, l, r, color="r") #Trapézio vermelho

        # fig.tight_layout
        # self.canvasT = FigureCanvas(fig)
        # self.canvasT.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        # plt.close('all')
        # self.ui.verticalLayout_6.addWidget(self.canvasT)

        img = Image.open(arquivo)
        self.ui.label.setText(str('X: ' + str(img.size[-2]) + '     Y: ' + str(img.size[1])))

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
        ax.grid(False)
        plt.axis('off')

        # Display the figure
        self.canvas = FigureCanvas(fig)
        plt.close('all')

        print("------------")
        print(img.size[0])
        print(img.size[1])

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

        # z_smoothed2 = sp.ndimage.gaussian_filter(self.g_max.transpose(), sigma)

        # Some min and max and range values coming from gaussian_filter calculations
        # z_smoothed_min2 = np.amin(z_smoothed2)
        # z_smoothed_max2 = np.amax(z_smoothed2)
        # z_range2 = z_smoothed_max2 - z_smoothed_min2

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
        # self.ui.tabs.setVisible(True)
        self.ui.tabs_3.setVisible(True)

        self.toolb1 = NavigationToolbar(self.canvas, self)
        # self.ui.horizontalLayout_3.addWidget(self.canvas)     #Trocado com o debaixo
        # self.ui.horizontalLayout_browse.addWidget(self.toolb1)

        self.tabInc = QWidget()
        self.tabInc_layout = QVBoxLayout()
        self.tabInc_layout.addWidget(self.canvas)
        self.tabInc_layout.addWidget(self.toolb1)
        self.tabInc.setLayout(self.tabInc_layout)

        self.tab_name = "Elevação " + str((self.inclina_tabs)+1)
        self.ui.tabs_3.addTab(self.tabInc, self.tab_name)

        self.canvas2 = FigureCanvas(fig2)
        self.toolb2 = NavigationToolbar(self.canvas2, self)

        self.tabInc = QWidget()
        self.tabInc_layout = QVBoxLayout()
        self.tabInc_layout.addWidget(self.canvas2)
        self.tabInc_layout.addWidget(self.toolb2)
        self.tabInc.setLayout(self.tabInc_layout)

        if self.ui.tabs.count()>0 and self.inclina_tabs == 0:
            self.ui.tabs.removeTab(0)
        if self.ui.tabs_3.count()>0 and self.inclina_tabs == 0:
            self.ui.tabs_3.removeTab(0)

        print("Inclina_tabs = ",self.inclina_tabs)
        self.inclina_tabs += 1

        self.tab_name2 = "Inclinação " + str(self.inclina_tabs)
        self.ui.tabs.addTab(self.tabInc, self.tab_name2)

        plt.close('all')

        # Show the limits
        self.ui.x1label.setVisible(True)
        self.ui.x2label.setVisible(True)
        self.ui.y1label.setVisible(True)
        self.ui.y2label.setVisible(True)
        self.ui.label.setVisible(True)
        self.ui.limits.setVisible(True)

        self.ui.x1lineEdit.setVisible(True)
        self.ui.x2lineEdit.setVisible(True)
        self.ui.y1lineEdit.setVisible(True)
        self.ui.y2lineEdit.setVisible(True)
        self.ui.Adjust.setVisible(True)

        self.ui.AnalysisBtn.setVisible(True)

        self.ui.imgname.setText(self.fname)
        self.ui.imgsizex.setText(str(img.size[1]))
        self.ui.imgsizey.setText(str(img.size[-2]))

        self.ui.ClearBtn.clicked.connect(self.clearCanvas)
    #

    def figureAdjust(self):
        self.number_of_adjusts += 1

        # self.canvas.deleteLater()
        # self.toolb1.deleteLater()
        plt.close('all')

        x1 = int(self.ui.x1lineEdit.text())
        x2 = int(self.ui.x2lineEdit.text())
        y1 = int(self.ui.y1lineEdit.text())
        y2 = int(self.ui.y2lineEdit.text())

        # Convert the image to a NumPy array
        fname = self.ui.imgname.text()
        img2 = Image.open(fname)
        img_array2 = np.array(img2)

        img_array2 = img_array2[x1:x2,y1:y2]
        img2 = Image.fromarray(img_array2, 'RGB')
        self.ui.label.setText(str('X: ' + str(img2.size[-2]) + '     Y: ' + str(img2.size[1])))
        self.ui.imgsizex.setText(str(img2.size[1]))
        self.ui.imgsizey.setText(str(img2.size[-2]))

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
        self.ui.tabs_3.addTab(self.tabInc, self.tab_name)

        self.canvas2 = FigureCanvas(fig2)
        self.toolb2 = NavigationToolbar(self.canvas2, self)

        self.tabInc2 = QWidget()
        self.tabInc_layout2 = QVBoxLayout()
        self.tabInc_layout2.addWidget(self.canvas2)
        self.tabInc_layout2.addWidget(self.toolb2)
        self.tabInc2.setLayout(self.tabInc_layout2)

        self.inclina_tabs +=1
        self.tab_name = "Inclinação " + str(self.inclina_tabs)
        self.ui.tabs.addTab(self.tabInc2,self.tab_name)

        plt.close('all')

        # Show the limits
        self.ui.x1label.setVisible(True)
        self.ui.x2label.setVisible(True)
        self.ui.y1label.setVisible(True)
        self.ui.y2label.setVisible(True)
        self.ui.label.setVisible(True)
        self.ui.limits.setVisible(True)

        self.ui.x1lineEdit.setVisible(True)
        self.ui.x2lineEdit.setVisible(True)
        self.ui.y1lineEdit.setVisible(True)
        self.ui.y2lineEdit.setVisible(True)
        self.ui.Adjust.setVisible(True)

        self.ui.AnalysisBtn.setVisible(True)
        self.ui.ClearBtn.clicked.connect(self.clearCanvas)
    #

    def clearCanvas(self):
        plt.close('all')

        self.ui.x1label.setVisible(False)
        self.ui.x2label.setVisible(False)
        self.ui.y1label.setVisible(False)
        self.ui.y2label.setVisible(False)
        self.ui.label.setVisible(False)
        self.ui.limits.setVisible(False)

        self.ui.x1lineEdit.setVisible(False)
        self.ui.x2lineEdit.setVisible(False)
        self.ui.y1lineEdit.setVisible(False)
        self.ui.y2lineEdit.setVisible(False)

        self.ui.Adjust.setVisible(False)
        self.ui.AnalysisBtn.setVisible(False)

        self.ui.tabs.setVisible(False)
        self.ui.tabs_2.setVisible(False)
        self.ui.tabs_3.setVisible(False)

        # for i in reversed(range(self.ui.horizontalLayout_3.count())):
        #     self.ui.horizontalLayout_3.itemAt(i).widget().setParent(None)

        for i in reversed(range(self.ui.verticalLayout_2.count())):
            self.ui.verticalLayout_2.itemAt(i).widget().setParent(None)

        for i in reversed(range(self.ui.verticalLayout_3.count())):
            self.ui.verticalLayout_3.itemAt(i).widget().setParent(None)

        # for i in reversed(range(self.ui.verticalLayout_6.count())):
        #     self.ui.verticalLayout_6.itemAt(i).widget().setParent(None)

        # for i in reversed(range(self.ui.horizontalLayout_browse.count())):
        #     self.ui.horizontalLayout_browse.itemAt(i).widget().deleteLater()

        for i in reversed(range(self.ui.tabs.count())):
            self.ui.tabs.removeTab(i)

        for i in reversed(range(self.ui.tabs_2.count())):
            self.ui.tabs_2.removeTab(i)

        for i in reversed(range(self.ui.tabs_3.count()-1)):
            self.ui.tabs_3.removeTab(i)

        self.inclina_tabs = 0
        self.number_of_adjusts = 0
        self.n_tabs = 0

        # self.tabInc = QWidget()
        # self.tabInc_layout = QVBoxLayout()
        # self.tabInc.setLayout(self.tabInc_layout)
        # self.ui.tabs.addTab(self.tabInc)
    #

    def mostra_lista(self):
        self.ui.label_mapa_rio.setVisible(not self.ui.label_mapa_rio.isVisible())
        self.ui.botao_regiao1.setVisible(not self.ui.botao_regiao1.isVisible())
        self.ui.botao_regiao2.setVisible(not self.ui.botao_regiao2.isVisible())
        self.ui.botao_regiao3.setVisible(not self.ui.botao_regiao3.isVisible())
        self.ui.botao_regiao4.setVisible(not self.ui.botao_regiao4.isVisible())
        self.ui.botao_regiao5.setVisible(not self.ui.botao_regiao5.isVisible())
        self.ui.botao_regiao6.setVisible(not self.ui.botao_regiao6.isVisible())
        self.ui.botao_regiao7.setVisible(not self.ui.botao_regiao7.isVisible())
        self.ui.botao_regiao8.setVisible(not self.ui.botao_regiao8.isVisible())
        self.ui.botao_regiao9.setVisible(not self.ui.botao_regiao9.isVisible())
        self.ui.botao_regiao10.setVisible(not self.ui.botao_regiao10.isVisible())
        self.ui.botao_regiao11.setVisible(not self.ui.botao_regiao11.isVisible())
        self.ui.botao_regiao12.setVisible(not self.ui.botao_regiao12.isVisible())
        self.ui.botao_regiao13.setVisible(not self.ui.botao_regiao13.isVisible())
        self.ui.botao_regiao14.setVisible(not self.ui.botao_regiao14.isVisible())
        self.ui.botao_regiao15.setVisible(not self.ui.botao_regiao15.isVisible())
        self.ui.botao_regiao16.setVisible(not self.ui.botao_regiao16.isVisible())
        self.ui.botao_regiao17.setVisible(not self.ui.botao_regiao17.isVisible())
        self.ui.botao_regiao18.setVisible(not self.ui.botao_regiao18.isVisible())
        self.ui.botao_regiao19.setVisible(not self.ui.botao_regiao19.isVisible())
        self.ui.botao_regiao20.setVisible(not self.ui.botao_regiao20.isVisible())
        self.ui.label_mapa_rio.lower()
        print("Mostra lista")
    #

    def mostra_recortar(self):
        self.ui.corteArquivo_label.setVisible(not self.ui.corteArquivo_label.isVisible())
        self.ui.nome_arquivo_corte.setVisible(not self.ui.nome_arquivo_corte.isVisible())
        self.ui.recortar_Button.setVisible(not self.ui.recortar_Button.isVisible())
    #

    def mostra_solo(self):
        self.ui.lineEdit_areia.setVisible(not self.ui.lineEdit_areia.isVisible())
        self.ui.lineEdit_argila.setVisible(not self.ui.lineEdit_argila.isVisible())
        self.ui.label_areia.setVisible(not self.ui.label_areia.isVisible())
        self.ui.label_argila.setVisible(not self.ui.label_argila.isVisible())
        self.ui.label_silte.setVisible(not self.ui.label_silte.isVisible())
        self.ui.label_silte2.setVisible(not self.ui.label_silte2.isVisible())
        self.ui.label_material.setVisible(not self.ui.label_material.isVisible())
        if self.tri > 0:
            self.canvasT.setVisible(not self.canvasT.isVisible())
    #

    def mostra_chuva(self):
        self.ui.tLbl.setVisible(not self.ui.tLbl.isVisible())
        self.ui.tlineEdit.setVisible(not self.ui.tlineEdit.isVisible())
        self.ui.horizontalSlider_t.setVisible(not self.ui.horizontalSlider_t.isVisible())
        self.ui.pLbl.setVisible(not self.ui.pLbl.isVisible())
        self.ui.plineEdit.setVisible(not self.ui.plineEdit.isVisible())
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

        self.ui.label_mapa_rio.setVisible(False)
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
        self.fname = arquivos_regiao[botao_clicado.objectName()]
        self.elev_incl(self.fname)
    #

    def corta_tif(self):
        # Definir os índices para recortar
        recorte = self.img_array[int(self.ui.x1lineEdit.text()):int(self.ui.x2lineEdit.text()),int(self.ui.y1lineEdit.text()):int(self.ui.y2lineEdit.text())]    #Trocar x e y de lugar?

        # Converter o array NumPy de volta para um objeto de imagem PIL
        recorte_img = Image.fromarray(recorte)

        if str(self.ui.nome_arquivo_corte.text()) == "":
            nome_arquivo_corte = 'recorte_arquivo.tif'
        else:
            nome_arquivo_corte =  str(self.nome_arquivo_corte.text()) + ".tif"

        # Salvar o recorte como um novo arquivo TIFF
        recorte_img.save(nome_arquivo_corte)

        print("Recorte realizado com sucesso!")
    #


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = AppTaludes()
    widget.show()
    sys.exit(app.exec_())
