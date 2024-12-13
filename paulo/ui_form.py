# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AppTaludes(object):
    def setupUi(self, AppTaludes):
        if not AppTaludes.objectName():
            AppTaludes.setObjectName(u"AppTaludes")
        AppTaludes.resize(1307, 834)
        AppTaludes.setMinimumSize(QSize(1076, 626))
        AppTaludes.setMouseTracking(False)
        AppTaludes.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_4 = QGridLayout(AppTaludes)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(0, -1, 10, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_areia = QLabel(AppTaludes)
        self.label_areia.setObjectName(u"label_areia")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_areia.sizePolicy().hasHeightForWidth())
        self.label_areia.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.label_areia.setFont(font)
        self.label_areia.setMouseTracking(True)
        self.label_areia.setAutoFillBackground(True)
        self.label_areia.setFrameShape(QFrame.Panel)
        self.label_areia.setScaledContents(False)
        self.label_areia.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_areia)

        self.lineEdit_areia = QLineEdit(AppTaludes)
        self.lineEdit_areia.setObjectName(u"lineEdit_areia")

        self.horizontalLayout_4.addWidget(self.lineEdit_areia)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSlider_areia = QSlider(AppTaludes)
        self.horizontalSlider_areia.setObjectName(u"horizontalSlider_areia")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalSlider_areia.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_areia.setSizePolicy(sizePolicy1)
        self.horizontalSlider_areia.setMouseTracking(True)
        self.horizontalSlider_areia.setTabletTracking(True)
        self.horizontalSlider_areia.setAutoFillBackground(True)
        self.horizontalSlider_areia.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_areia)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_silte = QLabel(AppTaludes)
        self.label_silte.setObjectName(u"label_silte")
        sizePolicy.setHeightForWidth(self.label_silte.sizePolicy().hasHeightForWidth())
        self.label_silte.setSizePolicy(sizePolicy)
        self.label_silte.setFont(font)
        self.label_silte.setMouseTracking(True)
        self.label_silte.setAutoFillBackground(True)
        self.label_silte.setFrameShape(QFrame.Panel)
        self.label_silte.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_silte)

        self.lineEdit_silte = QLineEdit(AppTaludes)
        self.lineEdit_silte.setObjectName(u"lineEdit_silte")

        self.horizontalLayout_9.addWidget(self.lineEdit_silte)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalSlider_silte = QSlider(AppTaludes)
        self.horizontalSlider_silte.setObjectName(u"horizontalSlider_silte")
        self.horizontalSlider_silte.setMouseTracking(True)
        self.horizontalSlider_silte.setTabletTracking(True)
        self.horizontalSlider_silte.setAutoFillBackground(True)
        self.horizontalSlider_silte.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_silte)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.label_argila = QLabel(AppTaludes)
        self.label_argila.setObjectName(u"label_argila")
        sizePolicy.setHeightForWidth(self.label_argila.sizePolicy().hasHeightForWidth())
        self.label_argila.setSizePolicy(sizePolicy)
        self.label_argila.setFont(font)
        self.label_argila.setMouseTracking(True)
        self.label_argila.setAutoFillBackground(True)
        self.label_argila.setFrameShape(QFrame.Panel)
        self.label_argila.setAlignment(Qt.AlignCenter)
        self.label_argila.setWordWrap(False)

        self.horizontalLayout_7.addWidget(self.label_argila)

        self.lineEdit_argila = QLineEdit(AppTaludes)
        self.lineEdit_argila.setObjectName(u"lineEdit_argila")

        self.horizontalLayout_7.addWidget(self.lineEdit_argila)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalSlider_argila = QSlider(AppTaludes)
        self.horizontalSlider_argila.setObjectName(u"horizontalSlider_argila")
        self.horizontalSlider_argila.setMouseTracking(True)
        self.horizontalSlider_argila.setTabletTracking(True)
        self.horizontalSlider_argila.setAutoFillBackground(True)
        self.horizontalSlider_argila.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider_argila)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.h_hw_Layout = QGridLayout()
        self.h_hw_Layout.setObjectName(u"h_hw_Layout")
        self.h_hw_Layout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalSlider_H = QSlider(AppTaludes)
        self.horizontalSlider_H.setObjectName(u"horizontalSlider_H")
        sizePolicy1.setHeightForWidth(self.horizontalSlider_H.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_H.setSizePolicy(sizePolicy1)
        self.horizontalSlider_H.setMouseTracking(False)
        self.horizontalSlider_H.setTabletTracking(False)
        self.horizontalSlider_H.setAcceptDrops(False)
        self.horizontalSlider_H.setAutoFillBackground(True)
        self.horizontalSlider_H.setMinimum(10)
        self.horizontalSlider_H.setMaximum(50)
        self.horizontalSlider_H.setPageStep(0)
        self.horizontalSlider_H.setValue(10)
        self.horizontalSlider_H.setOrientation(Qt.Horizontal)
        self.horizontalSlider_H.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_H.setTickInterval(10)

        self.h_hw_Layout.addWidget(self.horizontalSlider_H, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.hLbl = QLabel(AppTaludes)
        self.hLbl.setObjectName(u"hLbl")
        sizePolicy.setHeightForWidth(self.hLbl.sizePolicy().hasHeightForWidth())
        self.hLbl.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        self.hLbl.setFont(font1)
        self.hLbl.setMouseTracking(True)
        self.hLbl.setAutoFillBackground(True)
        self.hLbl.setFrameShape(QFrame.Panel)
        self.hLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.hLbl)

        self.hlineEdit = QLineEdit(AppTaludes)
        self.hlineEdit.setObjectName(u"hlineEdit")
        sizePolicy1.setHeightForWidth(self.hlineEdit.sizePolicy().hasHeightForWidth())
        self.hlineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.hlineEdit)


        self.h_hw_Layout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetMaximumSize)
        self.hwLbl = QLabel(AppTaludes)
        self.hwLbl.setObjectName(u"hwLbl")
        sizePolicy.setHeightForWidth(self.hwLbl.sizePolicy().hasHeightForWidth())
        self.hwLbl.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.hwLbl.setFont(font2)
        self.hwLbl.setAutoFillBackground(True)
        self.hwLbl.setFrameShape(QFrame.Panel)
        self.hwLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.hwLbl)

        self.hwlineEdit = QLineEdit(AppTaludes)
        self.hwlineEdit.setObjectName(u"hwlineEdit")
        sizePolicy1.setHeightForWidth(self.hwlineEdit.sizePolicy().hasHeightForWidth())
        self.hwlineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.hwlineEdit)


        self.h_hw_Layout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.horizontalSlider_Hw = QSlider(AppTaludes)
        self.horizontalSlider_Hw.setObjectName(u"horizontalSlider_Hw")
        self.horizontalSlider_Hw.setAutoFillBackground(True)
        self.horizontalSlider_Hw.setMaximum(100)
        self.horizontalSlider_Hw.setSingleStep(4)
        self.horizontalSlider_Hw.setPageStep(1)
        self.horizontalSlider_Hw.setSliderPosition(0)
        self.horizontalSlider_Hw.setOrientation(Qt.Horizontal)
        self.horizontalSlider_Hw.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_Hw.setTickInterval(20)

        self.h_hw_Layout.addWidget(self.horizontalSlider_Hw, 3, 0, 1, 1)


        self.gridLayout.addLayout(self.h_hw_Layout, 0, 1, 1, 1)

        self.c_phi_Layout = QGridLayout()
        self.c_phi_Layout.setObjectName(u"c_phi_Layout")
        self.c_phi_Layout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalSlider_C = QSlider(AppTaludes)
        self.horizontalSlider_C.setObjectName(u"horizontalSlider_C")
        sizePolicy1.setHeightForWidth(self.horizontalSlider_C.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_C.setSizePolicy(sizePolicy1)
        self.horizontalSlider_C.setAutoFillBackground(True)
        self.horizontalSlider_C.setMaximum(20)
        self.horizontalSlider_C.setSingleStep(1)
        self.horizontalSlider_C.setPageStep(1)
        self.horizontalSlider_C.setValue(0)
        self.horizontalSlider_C.setOrientation(Qt.Horizontal)
        self.horizontalSlider_C.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_C.setTickInterval(4)

        self.c_phi_Layout.addWidget(self.horizontalSlider_C, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.oLbl = QLabel(AppTaludes)
        self.oLbl.setObjectName(u"oLbl")
        sizePolicy.setHeightForWidth(self.oLbl.sizePolicy().hasHeightForWidth())
        self.oLbl.setSizePolicy(sizePolicy)
        self.oLbl.setFont(font2)
        self.oLbl.setMouseTracking(True)
        self.oLbl.setAutoFillBackground(True)
        self.oLbl.setFrameShape(QFrame.Panel)
        self.oLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.oLbl)

        self.philineEdit = QLineEdit(AppTaludes)
        self.philineEdit.setObjectName(u"philineEdit")
        sizePolicy1.setHeightForWidth(self.philineEdit.sizePolicy().hasHeightForWidth())
        self.philineEdit.setSizePolicy(sizePolicy1)
        self.philineEdit.setAutoFillBackground(False)

        self.horizontalLayout_5.addWidget(self.philineEdit)


        self.c_phi_Layout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.horizontalSlider_Phi = QSlider(AppTaludes)
        self.horizontalSlider_Phi.setObjectName(u"horizontalSlider_Phi")
        self.horizontalSlider_Phi.setAutoFillBackground(True)
        self.horizontalSlider_Phi.setMinimum(15)
        self.horizontalSlider_Phi.setMaximum(45)
        self.horizontalSlider_Phi.setSingleStep(1)
        self.horizontalSlider_Phi.setPageStep(1)
        self.horizontalSlider_Phi.setOrientation(Qt.Horizontal)
        self.horizontalSlider_Phi.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_Phi.setTickInterval(6)

        self.c_phi_Layout.addWidget(self.horizontalSlider_Phi, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.cLbl = QLabel(AppTaludes)
        self.cLbl.setObjectName(u"cLbl")
        sizePolicy.setHeightForWidth(self.cLbl.sizePolicy().hasHeightForWidth())
        self.cLbl.setSizePolicy(sizePolicy)
        self.cLbl.setFont(font1)
        self.cLbl.setMouseTracking(True)
        self.cLbl.setTabletTracking(False)
        self.cLbl.setAutoFillBackground(True)
        self.cLbl.setFrameShape(QFrame.Panel)
        self.cLbl.setFrameShadow(QFrame.Plain)
        self.cLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.cLbl)

        self.ClineEdit = QLineEdit(AppTaludes)
        self.ClineEdit.setObjectName(u"ClineEdit")
        sizePolicy1.setHeightForWidth(self.ClineEdit.sizePolicy().hasHeightForWidth())
        self.ClineEdit.setSizePolicy(sizePolicy1)
        self.ClineEdit.setFocusPolicy(Qt.NoFocus)
        self.ClineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.ClineEdit)


        self.c_phi_Layout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.c_phi_Layout, 0, 2, 1, 1)

        self.btnLayout = QVBoxLayout()
        self.btnLayout.setObjectName(u"btnLayout")
        self.btnLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.browse = QPushButton(AppTaludes)
        self.browse.setObjectName(u"browse")
        sizePolicy1.setHeightForWidth(self.browse.sizePolicy().hasHeightForWidth())
        self.browse.setSizePolicy(sizePolicy1)

        self.btnLayout.addWidget(self.browse)

        self.AnalysisBtn = QPushButton(AppTaludes)
        self.AnalysisBtn.setObjectName(u"AnalysisBtn")
        sizePolicy1.setHeightForWidth(self.AnalysisBtn.sizePolicy().hasHeightForWidth())
        self.AnalysisBtn.setSizePolicy(sizePolicy1)

        self.btnLayout.addWidget(self.AnalysisBtn)

        self.ClearBtn = QPushButton(AppTaludes)
        self.ClearBtn.setObjectName(u"ClearBtn")
        sizePolicy1.setHeightForWidth(self.ClearBtn.sizePolicy().hasHeightForWidth())
        self.ClearBtn.setSizePolicy(sizePolicy1)

        self.btnLayout.addWidget(self.ClearBtn)


        self.gridLayout.addLayout(self.btnLayout, 0, 3, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 25, 0, 1, 8)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.imgname = QLabel(AppTaludes)
        self.imgname.setObjectName(u"imgname")
        self.imgname.setAutoFillBackground(True)

        self.gridLayout_2.addWidget(self.imgname, 0, 0, 1, 1)

        self.imgsizex = QLabel(AppTaludes)
        self.imgsizex.setObjectName(u"imgsizex")

        self.gridLayout_2.addWidget(self.imgsizex, 0, 1, 1, 1)

        self.imgsizey = QLabel(AppTaludes)
        self.imgsizey.setObjectName(u"imgsizey")

        self.gridLayout_2.addWidget(self.imgsizey, 0, 2, 1, 1)

        self.x1label = QLabel(AppTaludes)
        self.x1label.setObjectName(u"x1label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.x1label.sizePolicy().hasHeightForWidth())
        self.x1label.setSizePolicy(sizePolicy2)
        self.x1label.setFont(font2)
        self.x1label.setAutoFillBackground(True)
        self.x1label.setFrameShape(QFrame.NoFrame)
        self.x1label.setLineWidth(1)
        self.x1label.setScaledContents(True)
        self.x1label.setMargin(5)

        self.gridLayout_2.addWidget(self.x1label, 0, 3, 1, 1)

        self.y1lineEdit = QLineEdit(AppTaludes)
        self.y1lineEdit.setObjectName(u"y1lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.y1lineEdit.sizePolicy().hasHeightForWidth())
        self.y1lineEdit.setSizePolicy(sizePolicy3)
        self.y1lineEdit.setAutoFillBackground(True)
        self.y1lineEdit.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.y1lineEdit, 0, 4, 1, 1)

        self.x2label = QLabel(AppTaludes)
        self.x2label.setObjectName(u"x2label")
        sizePolicy2.setHeightForWidth(self.x2label.sizePolicy().hasHeightForWidth())
        self.x2label.setSizePolicy(sizePolicy2)
        self.x2label.setFont(font2)
        self.x2label.setAutoFillBackground(True)
        self.x2label.setFrameShape(QFrame.NoFrame)
        self.x2label.setScaledContents(True)
        self.x2label.setMargin(5)

        self.gridLayout_2.addWidget(self.x2label, 0, 5, 1, 1)

        self.y2lineEdit = QLineEdit(AppTaludes)
        self.y2lineEdit.setObjectName(u"y2lineEdit")
        sizePolicy3.setHeightForWidth(self.y2lineEdit.sizePolicy().hasHeightForWidth())
        self.y2lineEdit.setSizePolicy(sizePolicy3)
        self.y2lineEdit.setAutoFillBackground(True)
        self.y2lineEdit.setDragEnabled(False)
        self.y2lineEdit.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.y2lineEdit, 0, 6, 1, 1)

        self.y1label = QLabel(AppTaludes)
        self.y1label.setObjectName(u"y1label")
        sizePolicy2.setHeightForWidth(self.y1label.sizePolicy().hasHeightForWidth())
        self.y1label.setSizePolicy(sizePolicy2)
        self.y1label.setFont(font2)
        self.y1label.setAutoFillBackground(True)
        self.y1label.setFrameShape(QFrame.NoFrame)
        self.y1label.setScaledContents(True)
        self.y1label.setMargin(5)

        self.gridLayout_2.addWidget(self.y1label, 0, 7, 1, 1)

        self.x1lineEdit = QLineEdit(AppTaludes)
        self.x1lineEdit.setObjectName(u"x1lineEdit")
        sizePolicy3.setHeightForWidth(self.x1lineEdit.sizePolicy().hasHeightForWidth())
        self.x1lineEdit.setSizePolicy(sizePolicy3)
        self.x1lineEdit.setAutoFillBackground(True)
        self.x1lineEdit.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.x1lineEdit, 0, 8, 1, 1)

        self.y2label = QLabel(AppTaludes)
        self.y2label.setObjectName(u"y2label")
        sizePolicy2.setHeightForWidth(self.y2label.sizePolicy().hasHeightForWidth())
        self.y2label.setSizePolicy(sizePolicy2)
        self.y2label.setFont(font2)
        self.y2label.setLayoutDirection(Qt.LeftToRight)
        self.y2label.setAutoFillBackground(True)
        self.y2label.setFrameShape(QFrame.NoFrame)
        self.y2label.setScaledContents(True)
        self.y2label.setMargin(5)

        self.gridLayout_2.addWidget(self.y2label, 0, 9, 1, 1)

        self.x2lineEdit = QLineEdit(AppTaludes)
        self.x2lineEdit.setObjectName(u"x2lineEdit")
        sizePolicy3.setHeightForWidth(self.x2lineEdit.sizePolicy().hasHeightForWidth())
        self.x2lineEdit.setSizePolicy(sizePolicy3)
        self.x2lineEdit.setAutoFillBackground(True)
        self.x2lineEdit.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.x2lineEdit, 0, 10, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.limits = QLabel(AppTaludes)
        self.limits.setObjectName(u"limits")
        self.limits.setFont(font2)
        self.limits.setAutoFillBackground(True)
        self.limits.setFrameShape(QFrame.Panel)
        self.limits.setScaledContents(True)
        self.limits.setAlignment(Qt.AlignCenter)
        self.limits.setWordWrap(True)

        self.verticalLayout.addWidget(self.limits)

        self.label = QLabel(AppTaludes)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 11, 1, 1)

        self.Adjust = QPushButton(AppTaludes)
        self.Adjust.setObjectName(u"Adjust")

        self.gridLayout_2.addWidget(self.Adjust, 0, 12, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 24, 0, 1, 8)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.mapaRio_Button = QPushButton(AppTaludes)
        self.mapaRio_Button.setObjectName(u"mapaRio_Button")
        sizePolicy3.setHeightForWidth(self.mapaRio_Button.sizePolicy().hasHeightForWidth())
        self.mapaRio_Button.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.mapaRio_Button)

        self.recortar_Button = QPushButton(AppTaludes)
        self.recortar_Button.setObjectName(u"recortar_Button")
        sizePolicy3.setHeightForWidth(self.recortar_Button.sizePolicy().hasHeightForWidth())
        self.recortar_Button.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.recortar_Button)

        self.corteArquivo_label = QLabel(AppTaludes)
        self.corteArquivo_label.setObjectName(u"corteArquivo_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.corteArquivo_label.sizePolicy().hasHeightForWidth())
        self.corteArquivo_label.setSizePolicy(sizePolicy4)
        self.corteArquivo_label.setMouseTracking(True)
        self.corteArquivo_label.setTabletTracking(True)
        self.corteArquivo_label.setAcceptDrops(True)
        self.corteArquivo_label.setLayoutDirection(Qt.LeftToRight)
        self.corteArquivo_label.setAutoFillBackground(True)
        self.corteArquivo_label.setScaledContents(True)
        self.corteArquivo_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.corteArquivo_label)

        self.nome_arquivo_corte = QLineEdit(AppTaludes)
        self.nome_arquivo_corte.setObjectName(u"nome_arquivo_corte")
        self.nome_arquivo_corte.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.nome_arquivo_corte.sizePolicy().hasHeightForWidth())
        self.nome_arquivo_corte.setSizePolicy(sizePolicy5)
        self.nome_arquivo_corte.setMaximumSize(QSize(611, 16777215))
        self.nome_arquivo_corte.setAutoFillBackground(True)
        self.nome_arquivo_corte.setMaxLength(32767)
        self.nome_arquivo_corte.setDragEnabled(True)
        self.nome_arquivo_corte.setClearButtonEnabled(True)

        self.horizontalLayout_8.addWidget(self.nome_arquivo_corte)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 0, 0, 1, 8)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabs_3 = QTabWidget(AppTaludes)
        self.tabs_3.setObjectName(u"tabs_3")
        self.tabs_3.setTabletTracking(True)
        self.tabs_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);")
        self.tabs_3.setTabShape(QTabWidget.Triangular)
        self.tabs_3.setTabsClosable(True)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.layoutWidget = QWidget(self.tab_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-5, 0, 441, 171))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.tabs_3.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabs_3, 0, 0, 1, 1)

        self.tabs = QTabWidget(AppTaludes)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setTabletTracking(True)
        self.tabs.setAcceptDrops(True)
        self.tabs.setAutoFillBackground(False)
        self.tabs.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);")
        self.tabs.setTabShape(QTabWidget.Triangular)
        self.tabs.setElideMode(Qt.ElideNone)
        self.tabs.setUsesScrollButtons(True)
        self.tabs.setDocumentMode(False)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(False)
        self.tabs.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget_3 = QWidget(self.tab)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, -1, 621, 171))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabs.addTab(self.tab, "")

        self.gridLayout_3.addWidget(self.tabs, 0, 1, 1, 1)

        self.tabs_2 = QTabWidget(AppTaludes)
        self.tabs_2.setObjectName(u"tabs_2")
        self.tabs_2.setTabletTracking(True)
        self.tabs_2.setAcceptDrops(True)
        self.tabs_2.setAutoFillBackground(False)
        self.tabs_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);")
        self.tabs_2.setTabShape(QTabWidget.Triangular)
        self.tabs_2.setElideMode(Qt.ElideNone)
        self.tabs_2.setUsesScrollButtons(True)
        self.tabs_2.setDocumentMode(False)
        self.tabs_2.setTabsClosable(True)
        self.tabs_2.setMovable(False)
        self.tabs_2.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_2 = QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 621, 171))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabs_2.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabs_2, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 22, 0, 2, 8)

        self.label_mapa_rio = QLabel(AppTaludes)
        self.label_mapa_rio.setObjectName(u"label_mapa_rio")
        self.label_mapa_rio.setEnabled(True)
        self.label_mapa_rio.setMinimumSize(QSize(641, 263))
        self.label_mapa_rio.setAcceptDrops(True)
        self.label_mapa_rio.setAutoFillBackground(False)
        self.label_mapa_rio.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.label_mapa_rio.setPixmap(QPixmap(u":/teste 2/mapa-rio-de-janeiro.jpg"))
        self.label_mapa_rio.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_mapa_rio, 5, 0, 3, 8)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.botao_regiao7 = QPushButton(AppTaludes)
        self.botao_regiao7.setObjectName(u"botao_regiao7")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.botao_regiao7.sizePolicy().hasHeightForWidth())
        self.botao_regiao7.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao7, 2, 2, 1, 1)

        self.botao_regiao12 = QPushButton(AppTaludes)
        self.botao_regiao12.setObjectName(u"botao_regiao12")
        sizePolicy6.setHeightForWidth(self.botao_regiao12.sizePolicy().hasHeightForWidth())
        self.botao_regiao12.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao12, 0, 3, 1, 1)

        self.botao_regiao1 = QPushButton(AppTaludes)
        self.botao_regiao1.setObjectName(u"botao_regiao1")
        sizePolicy6.setHeightForWidth(self.botao_regiao1.sizePolicy().hasHeightForWidth())
        self.botao_regiao1.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao1, 2, 0, 1, 1)

        self.botao_regiao4 = QPushButton(AppTaludes)
        self.botao_regiao4.setObjectName(u"botao_regiao4")
        sizePolicy6.setHeightForWidth(self.botao_regiao4.sizePolicy().hasHeightForWidth())
        self.botao_regiao4.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao4, 2, 1, 1, 1)

        self.botao_regiao9 = QPushButton(AppTaludes)
        self.botao_regiao9.setObjectName(u"botao_regiao9")
        sizePolicy6.setHeightForWidth(self.botao_regiao9.sizePolicy().hasHeightForWidth())
        self.botao_regiao9.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao9, 0, 2, 1, 1)

        self.botao_regiao6 = QPushButton(AppTaludes)
        self.botao_regiao6.setObjectName(u"botao_regiao6")
        sizePolicy6.setHeightForWidth(self.botao_regiao6.sizePolicy().hasHeightForWidth())
        self.botao_regiao6.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao6, 0, 1, 1, 1)

        self.botao_regiao11 = QPushButton(AppTaludes)
        self.botao_regiao11.setObjectName(u"botao_regiao11")
        sizePolicy6.setHeightForWidth(self.botao_regiao11.sizePolicy().hasHeightForWidth())
        self.botao_regiao11.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao11, 1, 3, 1, 1)

        self.botao_regiao8 = QPushButton(AppTaludes)
        self.botao_regiao8.setObjectName(u"botao_regiao8")
        sizePolicy6.setHeightForWidth(self.botao_regiao8.sizePolicy().hasHeightForWidth())
        self.botao_regiao8.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao8, 1, 2, 1, 1)

        self.botao_regiao14 = QPushButton(AppTaludes)
        self.botao_regiao14.setObjectName(u"botao_regiao14")
        sizePolicy6.setHeightForWidth(self.botao_regiao14.sizePolicy().hasHeightForWidth())
        self.botao_regiao14.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao14, 1, 4, 1, 1)

        self.botao_regiao13 = QPushButton(AppTaludes)
        self.botao_regiao13.setObjectName(u"botao_regiao13")
        sizePolicy6.setHeightForWidth(self.botao_regiao13.sizePolicy().hasHeightForWidth())
        self.botao_regiao13.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao13, 2, 4, 1, 1)

        self.botao_regiao2 = QPushButton(AppTaludes)
        self.botao_regiao2.setObjectName(u"botao_regiao2")
        sizePolicy6.setHeightForWidth(self.botao_regiao2.sizePolicy().hasHeightForWidth())
        self.botao_regiao2.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao2, 1, 0, 1, 1)

        self.botao_regiao5 = QPushButton(AppTaludes)
        self.botao_regiao5.setObjectName(u"botao_regiao5")
        sizePolicy6.setHeightForWidth(self.botao_regiao5.sizePolicy().hasHeightForWidth())
        self.botao_regiao5.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao5, 1, 1, 1, 1)

        self.botao_regiao15 = QPushButton(AppTaludes)
        self.botao_regiao15.setObjectName(u"botao_regiao15")
        sizePolicy6.setHeightForWidth(self.botao_regiao15.sizePolicy().hasHeightForWidth())
        self.botao_regiao15.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao15, 0, 4, 1, 1)

        self.botao_regiao10 = QPushButton(AppTaludes)
        self.botao_regiao10.setObjectName(u"botao_regiao10")
        sizePolicy6.setHeightForWidth(self.botao_regiao10.sizePolicy().hasHeightForWidth())
        self.botao_regiao10.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao10, 2, 3, 1, 1)

        self.botao_regiao3 = QPushButton(AppTaludes)
        self.botao_regiao3.setObjectName(u"botao_regiao3")
        sizePolicy6.setHeightForWidth(self.botao_regiao3.sizePolicy().hasHeightForWidth())
        self.botao_regiao3.setSizePolicy(sizePolicy6)

        self.gridLayout_5.addWidget(self.botao_regiao3, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_5, 5, 0, 3, 8)


        self.retranslateUi(AppTaludes)
        self.ClearBtn.clicked.connect(self.philineEdit.clear)
        self.ClearBtn.clicked.connect(self.ClineEdit.clear)
        self.ClearBtn.clicked.connect(self.hwlineEdit.clear)
        self.ClearBtn.clicked.connect(self.hlineEdit.clear)
        self.browse.clicked.connect(AppTaludes.getfile)
        self.ClearBtn.clicked.connect(self.imgsizex.clear)
        self.mapaRio_Button.clicked.connect(AppTaludes.mostra_lista)
        self.botao_regiao3.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao6.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao9.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao12.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao15.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao1.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao4.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao7.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao10.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao13.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao2.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao14.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao5.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao8.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.botao_regiao11.clicked.connect(AppTaludes.botao_clicado_regiao)
        self.ClearBtn.clicked.connect(self.nome_arquivo_corte.clear)
        self.recortar_Button.clicked.connect(AppTaludes.corta_tif)
        self.ClearBtn.clicked.connect(self.label.clear)

        self.tabs_3.setCurrentIndex(0)
        self.tabs.setCurrentIndex(0)
        self.tabs_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AppTaludes)
    # setupUi

    def retranslateUi(self, AppTaludes):
        AppTaludes.setWindowTitle(QCoreApplication.translate("AppTaludes", u"AppTaludes", None))
        self.label_areia.setText(QCoreApplication.translate("AppTaludes", u"Areia", None))
        self.label_silte.setText(QCoreApplication.translate("AppTaludes", u"Silte", None))
        self.label_argila.setText(QCoreApplication.translate("AppTaludes", u"Argila", None))
        self.hLbl.setText(QCoreApplication.translate("AppTaludes", u"h(m)", None))
        self.hlineEdit.setText("")
        self.hwLbl.setText(QCoreApplication.translate("AppTaludes", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">w</span> (m)</p></body></html>", None))
        self.oLbl.setText(QCoreApplication.translate("AppTaludes", u"\u03d5' (\u00b0)", None))
        self.cLbl.setText(QCoreApplication.translate("AppTaludes", u"c'(kPa)", None))
        self.browse.setText(QCoreApplication.translate("AppTaludes", u"Browse", None))
        self.AnalysisBtn.setText(QCoreApplication.translate("AppTaludes", u"Run Analysis", None))
        self.ClearBtn.setText(QCoreApplication.translate("AppTaludes", u"Clear", None))
        self.imgname.setText(QCoreApplication.translate("AppTaludes", u"TextLabel", None))
        self.imgsizex.setText(QCoreApplication.translate("AppTaludes", u"TextLabel", None))
        self.imgsizey.setText(QCoreApplication.translate("AppTaludes", u"TextLabel", None))
        self.x1label.setText(QCoreApplication.translate("AppTaludes", u"<html><head/><body><p>X<span style=\" vertical-align:sub;\">1</span></p></body></html>", None))
        self.y1lineEdit.setText(QCoreApplication.translate("AppTaludes", u"20", None))
        self.y1lineEdit.setPlaceholderText("")
        self.x2label.setText(QCoreApplication.translate("AppTaludes", u"<html><head/><body><p>X<span style=\" vertical-align:sub;\">2</span></p></body></html>", None))
        self.y2lineEdit.setText(QCoreApplication.translate("AppTaludes", u"60", None))
        self.y2lineEdit.setPlaceholderText("")
        self.y1label.setText(QCoreApplication.translate("AppTaludes", u"<html><head/><body><p>Y<span style=\" vertical-align:sub;\">1</span></p></body></html>", None))
        self.x1lineEdit.setText(QCoreApplication.translate("AppTaludes", u"20", None))
        self.x1lineEdit.setPlaceholderText("")
        self.y2label.setText(QCoreApplication.translate("AppTaludes", u"<html><head/><body><p>Y<span style=\" vertical-align:sub;\">2</span></p></body></html>", None))
        self.x2lineEdit.setText(QCoreApplication.translate("AppTaludes", u"50", None))
        self.x2lineEdit.setPlaceholderText("")
        self.limits.setText(QCoreApplication.translate("AppTaludes", u"Tamanho de X e Y", None))
        self.label.setText("")
        self.Adjust.setText(QCoreApplication.translate("AppTaludes", u"Adjust image", None))
        self.mapaRio_Button.setText(QCoreApplication.translate("AppTaludes", u"Mapa Rio", None))
        self.recortar_Button.setText(QCoreApplication.translate("AppTaludes", u"Recortar", None))
        self.corteArquivo_label.setText(QCoreApplication.translate("AppTaludes", u"Defina o nome do seu arquivo de corte:", None))
        self.tabs_3.setTabText(self.tabs_3.indexOf(self.tab_3), QCoreApplication.translate("AppTaludes", u"Open a file to start", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QCoreApplication.translate("AppTaludes", u"Open a file to start", None))
        self.tabs_2.setTabText(self.tabs_2.indexOf(self.tab_2), QCoreApplication.translate("AppTaludes", u"Open a file to start", None))
        self.label_mapa_rio.setText("")
        self.botao_regiao7.setText("")
        self.botao_regiao12.setText("")
        self.botao_regiao1.setText("")
        self.botao_regiao4.setText("")
        self.botao_regiao9.setText("")
        self.botao_regiao6.setText("")
        self.botao_regiao11.setText("")
        self.botao_regiao8.setText("")
        self.botao_regiao14.setText("")
        self.botao_regiao13.setText("")
        self.botao_regiao2.setText("")
        self.botao_regiao5.setText("")
        self.botao_regiao15.setText("")
        self.botao_regiao10.setText("")
        self.botao_regiao3.setText("")
    # retranslateUi

