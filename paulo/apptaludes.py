# This Python file uses the following encoding: utf-8
import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QHBoxLayout
from PySide2 import QtGui

import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.cm as cm
from PIL import Image

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure

import scipy as sp
# from scipy.ndimage import gaussian_filter

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
        # self.ui.tabs.setVisible(False)
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
        # self.ui.Adjust.clicked.connect(self.runAnalysis)

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
        fname = self.ui.imgname.text()
        imgx = Image.open(fname)
        img_arrayx = np.array(imgx)

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

        # Creating figure
        self.fos_array = self.fos_array.transpose()

        if self.number_of_adjusts >= 1:
            self.fos_array = self.fos_array[x1:x2, y1:y2]

            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))
            plt.imshow(self.fos_array, cmap='RdBu')
            im_fos = ax.imshow(self.fos_array, cmap='RdBu')

            sizey = x2-x1
            sizex = y2-y1

            ax.set_yticks([0, 0.2*sizey, 0.4*sizey, 0.6*sizey, 0.8*sizey, sizey], labels=[0, 5*sizey, 10*sizey, 15*sizey, 20*sizey, 25*sizey])
            ax.set_xticks([0, 0.2*sizex, 0.4*sizex, 0.6*sizex, 0.8*sizex, sizex], labels=[0, 5*sizex, 10*sizex, 15*sizex, 20*sizex, 25*sizex])

            plt.colorbar(im_fos, ax=ax)
            plt.axis([0, sizex-1, 0, sizey-1])
            ax.invert_yaxis()
        else:
            fig_fos, ax = plt.subplots(1,1,figsize=(12,10))
            plt.imshow(self.fos_array, cmap='RdBu')
            im_fos = ax.imshow(self.fos_array, cmap='RdBu')

            ax.set_yticks([0, 0.2*imgx.size[1], 0.4*imgx.size[1], 0.6*imgx.size[1], 0.8*imgx.size[1], imgx.size[1]], labels=[0, 5*imgx.size[1], 10*imgx.size[1], 15*imgx.size[1], 20*imgx.size[1], 25*imgx.size[1]])
            ax.set_xticks([0, 0.2*imgx.size[0], 0.4*imgx.size[0], 0.6*imgx.size[0], 0.8*imgx.size[0], imgx.size[0]], labels=[0, 5*imgx.size[0], 10*imgx.size[0], 15*imgx.size[0], 20*imgx.size[0], 25*imgx.size[0]])

            plt.colorbar(im_fos, ax=ax)
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
    #

    def runAnalysis2(self):
        self.ui.tabs_2.removeTab(-1)
        self.runAnalysis()
    #

    def getfile(self):
        self.figure.clear()
        # self.ui.tabs.setVisible(True)

        fname, _ = QFileDialog.getOpenFileName(self, "Open File","c:\\Users\\paulobaccar\\Documents","Tif files(*.tif);;Tiff files(*.tiff)")
        img = Image.open(fname)
        self.ui.label.setText(str('X: ' + str(img.size[-2]) + '     Y: ' + str(img.size[1])))

        # Convert the image to a NumPy array
        img_array = np.array(img)

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

        self.ui.imgname.setText(fname)
        self.ui.imgsizex.setText(str(img.size[1]))
        self.ui.imgsizey.setText(str(img.size[-2]))

        self.ui.ClearBtn.clicked.connect(self.clearCanvas)
    #

    def figureAdjust(self):
        self.number_of_adjusts += 1

        # self.canvas.setVisible(False)
        # self.canvas2.setVisible(False)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = AppTaludes()
    widget.show()
    sys.exit(app.exec_())
