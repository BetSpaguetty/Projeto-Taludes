# This Python file uses the following encoding: utf-8
import sys

# from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton
from PySide2.QtGui import QPixmap
# from PySide2 import QtGui

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

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar

# from matplotlib.colors import LinearSegmentedColormap

# #python -m pip install scipy (No terminal)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_AppTaludes

class AppTaludes(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AppTaludes()
        self.ui.setupUi(self)

        self.ui.tabs.tabCloseRequested.connect(self.ui.tabs.removeTab)
        self.ui.tabs_2.tabCloseRequested.connect(self.ui.tabs_2.removeTab)

        self.ui.horizontalSlider_C.valueChanged.connect(self.number_changed) #c
        self.ui.horizontalSlider_Phi.valueChanged.connect(self.number_changed) #phi
        self.ui.horizontalSlider_H.valueChanged.connect(self.number_changed) #h
        self.ui.horizontalSlider_Hw.valueChanged.connect(self.number_changed) #hw

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

        # Tornando os botões invisiveis e coloridos ao passar o mouse em cima
        self.botao_regiao1.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao2.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao3.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao4.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao5.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao6.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao7.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao8.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao9.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao10.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao11.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao12.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao13.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao14.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao15.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;} QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")

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

        pixmap = QPixmap("c:\\Users\\paulobaccar\\Downloads\\mapa-rio-de-janeiro.jpg")
        self.ui.label_mapa_rio.setPixmap(pixmap)

        self.setMinimumSize(300,300)
        plt.close()
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

        self.runAnalysis2()
    #

    def analysisClick(self):
        self.n_tabs += 1
    #

    def runAnalysis(self):
        self.fname = self.ui.imgname.text()
        imgx = Image.open(self.fname)
        img_arrayx = np.array(imgx)

        self.ui.tabs.setVisible(True)
        self.ui.tabs_2.setVisible(True)

        x1 = int(self.ui.x1lineEdit.text())
        x2 = int(self.ui.x2lineEdit.text())
        y1 = int(self.ui.y1lineEdit.text())
        y2 = int(self.ui.y2lineEdit.text())

        # if self.number_of_adjusts == 0:
        #     imgx = Image.fromarray(img_arrayx, 'RGB')
        # else:
        #     img_arrayx = img_arrayx[x1:x2, y1:y2]
        #     imgx = Image.fromarray(img_arrayx, 'RGB')

        h_value = self.ui.horizontalSlider_H.value()/10;
        hw_value = self.ui.horizontalSlider_Hw.value();
        c_value = self.ui.horizontalSlider_C.value();
        phi_value = self.ui.horizontalSlider_Phi.value();

        # h_array = h_value * np.ones((imgx.size[0]+1,imgx.size[1]+1))
        # hw_array = h_value * hw_value/100 * np.ones((imgx.size[0]+1,imgx.size[1]+1))
        # c_array = c_value * np.ones((imgx.size[0]+1,imgx.size[1]+1))
        # phi_array = phi_value * np.ones((imgx.size[0]+1,imgx.size[1]+1))

        # # Creating plots
        # h_fig, h_ax = plt.subplots(1,1,figsize=(12,10))
        # plt.imshow(h_array, cmap='terrain')
        # h_im = h_ax.imshow(h_array, cmap='terrain')

        # h_ax.set_yticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0],imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])
        # h_ax.set_xticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1],imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])

        # plt.colorbar(h_im, ax=h_ax)
        # plt.axis([0, imgx.size[1], 0, imgx.size[0]])

        ######################################################################

        # hw_fig, hw_ax = plt.subplots(1,1,figsize=(12,10))
        # plt.imshow(hw_array, cmap='terrain')
        # hw_im = hw_ax.imshow(hw_array, cmap='terrain')

        # hw_ax.set_yticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0],imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])
        # hw_ax.set_xticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1],imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])

        # plt.colorbar(hw_im, ax=hw_ax)
        # plt.axis([0, imgx.size[1], 0, imgx.size[0]])

        ######################################################################

        # c_fig, c_ax = plt.subplots(1,1,figsize=(12,10))
        # plt.imshow(c_array, cmap='terrain')
        # c_im = c_ax.imshow(c_array, cmap='terrain')

        # c_ax.set_yticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0],imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])
        # c_ax.set_xticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1],imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])

        # plt.colorbar(c_im, ax=c_ax)
        # plt.axis([0, imgx.size[1], 0, imgx.size[0]])

        ######################################################################

        # phi_fig, phi_ax = plt.subplots(1,1,figsize=(12,10))
        # plt.imshow(phi_array, cmap='terrain')
        # phi_im = phi_ax.imshow(phi_array, cmap='terrain')

        # phi_ax.set_yticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0],imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])
        # phi_ax.set_xticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1],imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])

        # plt.colorbar(phi_im, ax=phi_ax)
        # plt.axis([0, imgx.size[1], 0, imgx.size[0]])

        # # Creating tabs

        # self.canvas_h = FigureCanvas(h_fig)
        # self.canvas_hw = FigureCanvas(hw_fig)
        # self.canvas_c = FigureCanvas(c_fig)
        # self.canvas_phi = FigureCanvas(phi_fig)

        # self.tabh = QWidget()
        # self.tabh_layout = QHBoxLayout()
        # self.tabh_layout.addWidget(self.canvas_h)
        # self.tabh.setLayout(self.tabh_layout)

        # self.tabc = QWidget()
        # self.tabc_layout = QHBoxLayout()
        # self.tabc_layout.addWidget(self.canvas_c)
        # self.tabc.setLayout(self.tabc_layout)

        # self.tabhw = QWidget()
        # self.tabhw_layout = QHBoxLayout()
        # self.tabhw_layout.addWidget(self.canvas_hw)
        # self.tabhw.setLayout(self.tabhw_layout)

        # self.tabphi = QWidget()
        # self.tabphi_layout = QHBoxLayout()
        # self.tabphi_layout.addWidget(self.canvas_phi)
        # self.tabphi.setLayout(self.tabphi_layout)

        # self.tab_1_name = "h(m) - " + str(self.inclina_tabs)
        # self.ui.tabs.addTab(self.tabh, self.tab_1_name)
        # self.tab_2_name = "c'(kPa) - " + str(self.inclina_tabs)
        # self.ui.tabs.addTab(self.tabc, self.tab_2_name)
        # self.tab_3_name = "hw(m) - " + str(self.inclina_tabs)
        # self.ui.tabs.addTab(self.tabhw, self.tab_3_name)
        # self.tab_4_name = "ϕ' (°) - " + str(self.inclina_tabs)
        # self.ui.tabs.addTab(self.tabphi, self.tab_4_name)

        c = c_value
        h = h_value
        phi = phi_value
        hw = h_value * hw_value/100
        self.fos_array = np.ones((imgx.size[0]+1,imgx.size[1]+1))   #[x1:x2, y1:y2]

        # Getting the biggest angles of each location
        for i in range(1,imgx.size[1]-1):
            for j in range(1,imgx.size[0]-1):
                alpha = self.g_max[j,i]

                self.fos_array[j,i] = (1605074512383065*(alpha**2)*(c**2)*(h**2)*phi)/151115727451828646838272 - (1414963042633059*(alpha**2)*(c**2)*h*phi)/18889465931478580854784 - (2774717211173289*(alpha**2)*(c**2)*hw*phi)/604462909807314587353088 + (2835477809945801*(alpha**2)*(c**2)*phi)/37778931862957161709568 + (6731555515546295*(alpha**2)*c)/73786976294838206464 + (5516753565726847*(alpha**2)*phi)/147573952589676412928 + (5653461066590515*alpha*(c**2)*h)/590295810358705651712 + (3025671568382675*alpha*(c**2)*phi)/590295810358705651712 - (2098110323770171*alpha*(c**2))/36893488147419103232 - (3002978305542275*alpha*c*(h**2))/4611686018427387904 + (2687741203999111*alpha*c*h)/576460752303423488 + (6472386681360727*alpha*c*hw*phi)/590295810358705651712 - (2982096583892561*alpha*c*(phi**2))/2361183241434822606848 - (4627184841729915*alpha*c)/288230376151711744 - (5688086807612743*alpha*(phi**2))/590295810358705651712 - (4311146912769217*alpha*phi)/1152921504606846976 - (4976341265194569*(c**2)*(h**2)*phi)/147573952589676412928 + (2283034929082703*(c**2)*h*phi)/9223372036854775808 + (1342385546936077*(c**2)*hw*phi)/147573952589676412928 - (1295331185150365*(c**2)*phi)/2305843009213693952 + (2592141320026855*c*(h**2))/72057594037927936 - (4971891995221437*c*h)/18014398509481984 - (4809409727287499*c*hw*phi)/9223372036854775808 + (2265715759669333*c*(phi**2))/36893488147419103232 + (3352624142374595*c)/4503599627370496 + (20768301037335*(h**2)*(hw**2)*phi)/2305843009213693952 - (1324783938325601*hw)/36028797018963968 + (3497832476657703*(phi**2))/4611686018427387904 + (6865366199800263*phi)/72057594037927936 + 1489595912300695/9007199254740992;

        for i in range(1,imgx.size[1]-1):
            for j in range(1,imgx.size[0]-1):
                if self.fos_array[j,i] > 2:
                    self.fos_array[j,i] = float("NaN")
                # elif self.g_max[j,i] < 1:
                #     self.fos_array[j,i] = 1
        for i in range(1,imgx.size[1]-1):
            for j in range(1,imgx.size[0]-1):
                if self.fos_array[j,i] < 1:
                    self.fos_array[j,i] = 1

        # Creating figure
        self.fos_array = self.fos_array.transpose()

        if self.number_of_adjusts >= 1:
            self.fos_array = self.fos_array[x1:x2, y1:y2]

            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))

            cmap = mpl.cm.rainbow

            plt.imshow(self.fos_array, cmap)                               ################'RdBu'
            im_fos = ax.imshow(self.fos_array, cmap)                       ################'RdBu'

            sizey = x2-x1
            sizex = y2-y1

            ax.set_yticks([0, 0.2*sizey, 0.4*sizey, 0.6*sizey, 0.8*sizey, sizey], labels=[0, 5*sizey, 10*sizey, 15*sizey, 20*sizey, 25*sizey])
            ax.set_xticks([0, 0.2*sizex, 0.4*sizex, 0.6*sizex, 0.8*sizex, sizex], labels=[0, 5*sizex, 10*sizex, 15*sizex, 20*sizex, 25*sizex])

            plt.colorbar(im_fos,ax=ax)
            plt.axis([0, sizex-1, 0, sizey-1])
            ax.invert_yaxis()
        else:
            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))

            cmap = mpl.cm.rainbow

            plt.imshow(self.fos_array, cmap)                               ################'RdBu'
            im_fos = ax.imshow(self.fos_array, cmap)                       ################'RdBu'

            ax.set_yticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1], imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])
            ax.set_xticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0], imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])

            plt.colorbar(im_fos,ax=ax)                        #mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
            plt.axis([0, imgx.size[0]-1, 0, imgx.size[1]-1])
            ax.invert_yaxis()
        #

        # Display figure
        self.canvas_fos = FigureCanvas(fig_fos)
        self.toolb_fos = NavigationToolbar(self.canvas_fos, self)
        # self.ui.horizontalLayout_tabs2.addWidget(self.toolb_fos)
        # self.ui.verticalLayout_2.addWidget(self.canvas_fos)

        self.tabInc = QWidget()
        self.tabInc_layout = QVBoxLayout()
        self.tabInc_layout.addWidget(self.canvas_fos)
        self.tabInc_layout.addWidget(self.toolb_fos)
        self.tabInc.setLayout(self.tabInc_layout)

        if self.ui.tabs_2.count() == 1: #and self.n_tabs==1:
            self.ui.tabs_2.removeTab(0)

        # self.n_tabs += 1
        self.tab_name = "Segurança " + str(self.inclina_tabs)
        self.ui.tabs_2.addTab(self.tabInc,self.tab_name)

        plt.close('all')
    #

    def runAnalysis2(self):
        self.ui.tabs_2.removeTab(-1)
        # self.runAnalysis()

        fname = self.ui.imgname.text()
        imgx = Image.open(fname)
        # img_arrayx = np.array(imgx)

        self.ui.tabs.setVisible(True)
        self.ui.tabs_2.setVisible(True)

        x1 = int(self.ui.x1lineEdit.text())
        x2 = int(self.ui.x2lineEdit.text())
        y1 = int(self.ui.y1lineEdit.text())
        y2 = int(self.ui.y2lineEdit.text())

        h_value = self.ui.horizontalSlider_H.value()/10;
        hw_value = self.ui.horizontalSlider_Hw.value();
        c_value = self.ui.horizontalSlider_C.value();
        phi_value = self.ui.horizontalSlider_Phi.value();

        c = c_value
        h = h_value
        phi = phi_value
        hw = h_value * hw_value/100
        self.fos_array = np.ones((imgx.size[0]+1,imgx.size[1]+1))   #[x1:x2, y1:y2]

        # Creating figure
        self.fos_array = self.fos_array.transpose()

        if self.number_of_adjusts >= 1:
            self.fos_array = self.fos_array[y1-1:y2, x1-1:x2]

            sizey = x2-x1
            sizex = y2-y1

            for i in range(0, sizex):
                for j in range(0, sizey):
                    alpha = self.g_max[y1+i,x1+j]   #[x1+j,y1+i]

                    self.fos_array[i,j] = (1605074512383065*(alpha**2)*(c**2)*(h**2)*phi)/151115727451828646838272 - (1414963042633059*(alpha**2)*(c**2)*h*phi)/18889465931478580854784 - (2774717211173289*(alpha**2)*(c**2)*hw*phi)/604462909807314587353088 + (2835477809945801*(alpha**2)*(c**2)*phi)/37778931862957161709568 + (6731555515546295*(alpha**2)*c)/73786976294838206464 + (5516753565726847*(alpha**2)*phi)/147573952589676412928 + (5653461066590515*alpha*(c**2)*h)/590295810358705651712 + (3025671568382675*alpha*(c**2)*phi)/590295810358705651712 - (2098110323770171*alpha*(c**2))/36893488147419103232 - (3002978305542275*alpha*c*(h**2))/4611686018427387904 + (2687741203999111*alpha*c*h)/576460752303423488 + (6472386681360727*alpha*c*hw*phi)/590295810358705651712 - (2982096583892561*alpha*c*(phi**2))/2361183241434822606848 - (4627184841729915*alpha*c)/288230376151711744 - (5688086807612743*alpha*(phi**2))/590295810358705651712 - (4311146912769217*alpha*phi)/1152921504606846976 - (4976341265194569*(c**2)*(h**2)*phi)/147573952589676412928 + (2283034929082703*(c**2)*h*phi)/9223372036854775808 + (1342385546936077*(c**2)*hw*phi)/147573952589676412928 - (1295331185150365*(c**2)*phi)/2305843009213693952 + (2592141320026855*c*(h**2))/72057594037927936 - (4971891995221437*c*h)/18014398509481984 - (4809409727287499*c*hw*phi)/9223372036854775808 + (2265715759669333*c*(phi**2))/36893488147419103232 + (3352624142374595*c)/4503599627370496 + (20768301037335*(h**2)*(hw**2)*phi)/2305843009213693952 - (1324783938325601*hw)/36028797018963968 + (3497832476657703*(phi**2))/4611686018427387904 + (6865366199800263*phi)/72057594037927936 + 1489595912300695/9007199254740992;

            for i in range(0, sizex):
                for j in range(0, sizey):
                    if self.fos_array[i,j] > 2:
                        self.fos_array[i,j] = float("NaN")
            for i in range(0, sizex):
                for j in range(0, sizey):
                    if self.fos_array[i,j] < 1:
                        self.fos_array[i,j] = 1

            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))

            # self.fos_array = self.fos_array.transpose()

            cmap = mpl.cm.rainbow

            plt.imshow(self.fos_array.transpose(), cmap)                               ################'RdBu'
            im_fos = ax.imshow(self.fos_array.transpose(), cmap)                       ################'RdBu'

            ax.set_yticks([0, 0.2*sizey, 0.4*sizey, 0.6*sizey, 0.8*sizey, sizey], labels=[0, 5*sizey, 10*sizey, 15*sizey, 20*sizey, 25*sizey])
            ax.set_xticks([0, 0.2*sizex, 0.4*sizex, 0.6*sizex, 0.8*sizex, sizex], labels=[0, 5*sizex, 10*sizex, 15*sizex, 20*sizex, 25*sizex])

            plt.colorbar(im_fos,ax=ax)
            plt.axis([0, sizex-1, 0, sizey-1])
            ax.invert_yaxis()
        else:
            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))

            for i in range(1,imgx.size[0]-1):
                for j in range(1,imgx.size[1]-1):
                    alpha = self.g_max[i,j]

                    self.fos_array[j,i] = (1605074512383065*(alpha**2)*(c**2)*(h**2)*phi)/151115727451828646838272 - (1414963042633059*(alpha**2)*(c**2)*h*phi)/18889465931478580854784 - (2774717211173289*(alpha**2)*(c**2)*hw*phi)/604462909807314587353088 + (2835477809945801*(alpha**2)*(c**2)*phi)/37778931862957161709568 + (6731555515546295*(alpha**2)*c)/73786976294838206464 + (5516753565726847*(alpha**2)*phi)/147573952589676412928 + (5653461066590515*alpha*(c**2)*h)/590295810358705651712 + (3025671568382675*alpha*(c**2)*phi)/590295810358705651712 - (2098110323770171*alpha*(c**2))/36893488147419103232 - (3002978305542275*alpha*c*(h**2))/4611686018427387904 + (2687741203999111*alpha*c*h)/576460752303423488 + (6472386681360727*alpha*c*hw*phi)/590295810358705651712 - (2982096583892561*alpha*c*(phi**2))/2361183241434822606848 - (4627184841729915*alpha*c)/288230376151711744 - (5688086807612743*alpha*(phi**2))/590295810358705651712 - (4311146912769217*alpha*phi)/1152921504606846976 - (4976341265194569*(c**2)*(h**2)*phi)/147573952589676412928 + (2283034929082703*(c**2)*h*phi)/9223372036854775808 + (1342385546936077*(c**2)*hw*phi)/147573952589676412928 - (1295331185150365*(c**2)*phi)/2305843009213693952 + (2592141320026855*c*(h**2))/72057594037927936 - (4971891995221437*c*h)/18014398509481984 - (4809409727287499*c*hw*phi)/9223372036854775808 + (2265715759669333*c*(phi**2))/36893488147419103232 + (3352624142374595*c)/4503599627370496 + (20768301037335*(h**2)*(hw**2)*phi)/2305843009213693952 - (1324783938325601*hw)/36028797018963968 + (3497832476657703*(phi**2))/4611686018427387904 + (6865366199800263*phi)/72057594037927936 + 1489595912300695/9007199254740992;

            for i in range(1,imgx.size[0]-1):
                for j in range(1,imgx.size[1]):
                    if self.fos_array[j,i] > 2:
                        self.fos_array[j,i] = float("NaN")
            for i in range(1,imgx.size[0]-1):
                for j in range(1,imgx.size[1]):
                    if self.fos_array[j,i] < 1:
                        self.fos_array[j,i] = 1

            cmap = mpl.cm.rainbow

            plt.imshow(self.fos_array, cmap)                               ################'RdBu'
            im_fos = ax.imshow(self.fos_array, cmap)                       ################'RdBu'

            ax.set_yticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1], imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])
            ax.set_xticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0], imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])

            plt.colorbar(im_fos,ax=ax)                        #mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
            plt.axis([0, imgx.size[0], 0, imgx.size[1]])
            ax.invert_yaxis()
        #

        # Display figure
        self.canvas_fos = FigureCanvas(fig_fos)
        self.toolb_fos = NavigationToolbar(self.canvas_fos, self)
        # self.ui.horizontalLayout_tabs2.addWidget(self.toolb_fos)
        # self.ui.verticalLayout_2.addWidget(self.canvas_fos)

        self.tabInc = QWidget()
        self.tabInc_layout = QVBoxLayout()
        self.tabInc_layout.addWidget(self.canvas_fos)
        self.tabInc_layout.addWidget(self.toolb_fos)
        self.tabInc.setLayout(self.tabInc_layout)

        if self.ui.tabs_2.count() == 1: #and self.n_tabs==1:
            self.ui.tabs_2.removeTab(0)

        # self.n_tabs += 1
        self.tab_name = "Segurança " + str(self.inclina_tabs)
        self.ui.tabs_2.addTab(self.tabInc,self.tab_name)

        plt.close('all')
    #

    def getfile(self):
        self.figure.clear()

        self.fname, _ = QFileDialog.getOpenFileName(self, "Open File","c:\\Users\\paulobaccar\\Documents","Tif files(*.tif);;Tiff files(*.tiff)")

        self.ui.tabs.setVisible(True)
        self.elev_incl(self.fname)

        # img = Image.open(fname)
        # self.ui.label.setText(str('X: ' + str(img.size[-2]) + '     Y: ' + str(img.size[1])))

        # # Convert the image to a NumPy array
        # img_array = np.array(img)

        # # Get aspect ratio of tif file for late plot box-plot-ratio
        # y_ratio,x_ratio = img.size

        # # Create arrays and declare x,y,z variables
        # lin_x = np.linspace(0,1,img_array.shape[0],endpoint=False)
        # lin_y = np.linspace(0,1,img_array.shape[1],endpoint=False)
        # y,x = np.meshgrid(lin_y,lin_x)
        # z = img_array

        # # Apply gaussian filter, with sigmas as variables. Higher sigma = more smoothing and more calculations. Downside: min and max values do change due to smoothing
        # sigma_y = 100
        # sigma_x = 100
        # sigma = [sigma_y, sigma_x]
        # z_smoothed = sp.ndimage.gaussian_filter(z, sigma)

        # # Creating figure
        # fig = plt.figure(figsize=(12,10)) #12,10
        # ax = plt.axes(projection='3d')
        # ax.azim = -30
        # ax.elev = 42
        # ax.set_box_aspect((x_ratio,y_ratio,((x_ratio+y_ratio)/8)))
        # surf = ax.plot_surface(x,y,z, cmap='terrain', edgecolor='none')

        # # Setting colors for colorbar range
        # m = cm.ScalarMappable(cmap=surf.cmap, norm=surf.norm)
        # m.set_array(z_smoothed)

        # plt.xticks([])  # Disabling xticks by Setting xticks to an empty list
        # plt.yticks([])  # Disabling yticks by setting yticks to an empty list
        # fig.tight_layout()
        # ax.grid(False)
        # plt.axis('off')

        # # Display the figure
        # self.canvas = FigureCanvas(fig)
        # plt.close('all')

        # self.g_max = np.zeros((img.size[0],img.size[1]));
        # L = 25;
        # Ld = np.sqrt(2)*L

        # # Getting the biggest angles of each location
        # for i in range(1,img.size[1]-1): #Já testado o 199
        #     for j in range(1,img.size[0]-1):
        #         self.g_max[j,i] = max([abs(img_array[i+1,j]-img_array[i,j])/L,
        #         abs(img_array[i-1,j]-img_array[i,j])/L,
        #         abs(img_array[i,j+1]-img_array[i,j])/L ,
        #         abs(img_array[i,j-1]-img_array[i,j])/L,
        #         abs(img_array[i+1,j+1]-img_array[i,j])/Ld,
        #         abs(img_array[i-1,j-1]-img_array[i,j])/Ld,
        #         abs(img_array[i-1,j+1]-img_array[i,j])/Ld,
        #         abs(img_array[i+1,j-1]-img_array[i,j])/Ld])

        #         self.g_max[j,i] = np.arctan(self.g_max[j,i]) * 180/np.pi

        # z_smoothed2 = sp.ndimage.gaussian_filter(self.g_max.transpose(), sigma)

        # # Some min and max and range values coming from gaussian_filter calculations
        # z_smoothed_min2 = np.amin(z_smoothed2)
        # z_smoothed_max2 = np.amax(z_smoothed2)
        # z_range2 = z_smoothed_max2 - z_smoothed_min2

        # # Creating second figure
        # fig2, ax = plt.subplots(1,1,figsize=(12,10))
        # plt.imshow(self.g_max.transpose(), cmap='terrain')
        # im = ax.imshow(self.g_max.transpose(), cmap='terrain')

        # ax.set_xticks([0, 0.2*img.size[0], 0.4*img.size[0], 0.6*img.size[0], 0.8*img.size[0],img.size[0]], labels=[0, 5*img.size[0], 10*img.size[0], 15*img.size[0], 20*img.size[0], 25*img.size[0]])
        # ax.set_yticks([0, 0.2*img.size[1], 0.4*img.size[1], 0.6*img.size[1], 0.8*img.size[1],img.size[1]], labels=[0, 5*img.size[0], 10*img.size[0], 15*img.size[0], 20*img.size[0], 25*img.size[0]])

        # plt.colorbar(im, ax=ax)
        # plt.axis([0, img.size[0]-1, 0, img.size[1]-1])
        # ax.invert_yaxis()

        # # plt.axis('off')

        # # Display figures

        # self.toolb1 = NavigationToolbar(self.canvas, self)
        # self.ui.horizontalLayout_browse.addWidget(self.toolb1)
        # self.ui.horizontalLayout_3.addWidget(self.canvas)

        # self.canvas2 = FigureCanvas(fig2)
        # self.toolb2 = NavigationToolbar(self.canvas2, self)


        # self.tabInc = QWidget()
        # self.tabInc_layout = QVBoxLayout()
        # self.tabInc_layout.addWidget(self.canvas2)
        # self.tabInc_layout.addWidget(self.toolb2)
        # self.tabInc.setLayout(self.tabInc_layout)

        # if self.ui.tabs.count()>0 and self.inclina_tabs == 0: # self.inclina_tabs == 1 and
        #     self.ui.tabs.removeTab(0)

        # self.inclina_tabs += 1
        # self.tab_name = "Inclinação " + str(self.inclina_tabs)
        # self.ui.tabs.addTab(self.tabInc, self.tab_name)

        # plt.close('all')

        # # Show the limits
        # self.ui.x1label.setVisible(True)
        # self.ui.x2label.setVisible(True)
        # self.ui.y1label.setVisible(True)
        # self.ui.y2label.setVisible(True)
        # self.ui.label.setVisible(True)
        # self.ui.limits.setVisible(True)

        # self.ui.x1lineEdit.setVisible(True)
        # self.ui.x2lineEdit.setVisible(True)
        # self.ui.y1lineEdit.setVisible(True)
        # self.ui.y2lineEdit.setVisible(True)
        # self.ui.Adjust.setVisible(True)

        # self.ui.AnalysisBtn.setVisible(True)

        # self.ui.imgname.setText(fname)
        # self.ui.imgsizex.setText(str(img.size[1]))
        # self.ui.imgsizey.setText(str(img.size[-2]))

        # self.ui.ClearBtn.clicked.connect(self.clearCanvas)
    #

    def elev_incl(self,arquivo):
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

        z_smoothed2 = sp.ndimage.gaussian_filter(self.g_max.transpose(), sigma)

        # Some min and max and range values coming from gaussian_filter calculations
        z_smoothed_min2 = np.amin(z_smoothed2)
        z_smoothed_max2 = np.amax(z_smoothed2)
        z_range2 = z_smoothed_max2 - z_smoothed_min2

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

        self.ui.tabs.setVisible(True)
        self.toolb1 = NavigationToolbar(self.canvas, self)
        self.ui.horizontalLayout_browse.addWidget(self.toolb1)
        self.ui.horizontalLayout_3.addWidget(self.canvas)

        self.canvas2 = FigureCanvas(fig2)
        self.toolb2 = NavigationToolbar(self.canvas2, self)

        self.tabInc = QWidget()
        self.tabInc_layout = QVBoxLayout()
        self.tabInc_layout.addWidget(self.canvas2)
        self.tabInc_layout.addWidget(self.toolb2)
        self.tabInc.setLayout(self.tabInc_layout)

        if self.ui.tabs.count()>0 and self.inclina_tabs == 0: # self.inclina_tabs == 1 and
            self.ui.tabs.removeTab(0)

        self.inclina_tabs += 1
        self.tab_name = "Inclinação " + str(self.inclina_tabs)
        self.ui.tabs.addTab(self.tabInc, self.tab_name)

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

        self.canvas.deleteLater()
        self.toolb1.deleteLater()
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
        self.ui.horizontalLayout_browse.addWidget(self.toolb1)
        self.ui.horizontalLayout_3.addWidget(self.canvas)

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
        self.ui.tabs_2.setVisible(False)

        for i in reversed(range(self.ui.horizontalLayout_3.count())):
            self.ui.horizontalLayout_3.itemAt(i).widget().setParent(None)

        for i in reversed(range(self.ui.verticalLayout_2.count())):
            self.ui.verticalLayout_2.itemAt(i).widget().setParent(None)

        for i in reversed(range(self.ui.verticalLayout_3.count())):
            self.ui.verticalLayout_3.itemAt(i).widget().setParent(None)

        for i in reversed(range(self.ui.horizontalLayout_browse.count())):
            self.ui.horizontalLayout_browse.itemAt(i).widget().deleteLater()

        for i in reversed(range(self.ui.tabs.count())):
            self.ui.tabs.removeTab(i)

        for i in reversed(range(self.ui.tabs_2.count())):
            self.ui.tabs_2.removeTab(i)

        self.inclina_tabs = 0
        self.number_of_adjusts = 0
        self.n_tabs = 0
    #

    def mostra_lista(self):
        # self.lista_rio.setVisible(True) #not self.lista_rio.isVisible())
        self.ui.label_mapa_rio.setVisible(True)
        self.ui.botao_regiao1.setVisible(True)
        self.ui.botao_regiao2.setVisible(True)
        self.ui.botao_regiao3.setVisible(True)
        self.ui.botao_regiao4.setVisible(True)
        self.ui.botao_regiao5.setVisible(True)
        self.ui.botao_regiao6.setVisible(True)
        self.ui.botao_regiao7.setVisible(True)
        self.ui.botao_regiao8.setVisible(True)
        self.ui.botao_regiao9.setVisible(True)
        self.ui.botao_regiao10.setVisible(True)
        self.ui.botao_regiao11.setVisible(True)
        self.ui.botao_regiao12.setVisible(True)
        self.ui.botao_regiao13.setVisible(True)
        self.ui.botao_regiao14.setVisible(True)
        self.ui.botao_regiao15.setVisible(True)
    #

    def botao_clicado_regiao(self):
        botao_clicado = self.sender() # atribui o própio botão que foi clicado como uma variável

        arquivos_regiao =  {"botao_regiao1":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.1.tif",
                            "botao_regiao2":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.2.tif",
                            "botao_regiao3":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.3.tif",
                            "botao_regiao4":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.4.tif",
                            "botao_regiao5":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.5.tif",
                            "botao_regiao6":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.6.tif",
                            "botao_regiao7":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.7.tif",
                            "botao_regiao8":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.8.tif",
                            "botao_regiao9":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.9.tif",
                            "botao_regiao10":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.10.tif",
                            "botao_regiao11":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.11.tif",
                            "botao_regiao12":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.12.tif",
                            "botao_regiao13":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.13.tif",
                            "botao_regiao14":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.14.tif",
                            "botao_regiao15":"c:\\Users\\paulobaccar\\Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.15.tif"}

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
            nome_arquivo_corte =  str(self.ui.nome_arquivo_corte.text()) + ".tif"

        # Salvar o recorte como um novo arquivo TIFF
        recorte_img.save(nome_arquivo_corte)

        print("Recorte realizado com sucesso!")
    #


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = AppTaludes()
    widget.show()
    sys.exit(app.exec_())
