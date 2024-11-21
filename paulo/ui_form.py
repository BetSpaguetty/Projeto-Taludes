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
        AppTaludes.resize(1076, 626)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AppTaludes.sizePolicy().hasHeightForWidth())
        AppTaludes.setSizePolicy(sizePolicy)
        AppTaludes.setMinimumSize(QSize(1076, 626))
        AppTaludes.setMouseTracking(False)
        AppTaludes.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(AppTaludes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.canvas_Layout = QHBoxLayout()
        self.canvas_Layout.setObjectName(u"canvas_Layout")
        self.canvas_Layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.canvas_Layout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, -1, 6, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_browse = QHBoxLayout()
        self.horizontalLayout_browse.setObjectName(u"horizontalLayout_browse")

        self.verticalLayout_4.addLayout(self.horizontalLayout_browse)


        self.canvas_Layout.addLayout(self.verticalLayout_4)

        self.tabs = QTabWidget(AppTaludes)
        self.tabs.setObjectName(u"tabs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy1)
        self.tabs.setTabletTracking(True)
        self.tabs.setAcceptDrops(True)
        self.tabs.setAutoFillBackground(True)
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
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 511, 391))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabs.addTab(self.tab, "")

        self.canvas_Layout.addWidget(self.tabs)

        self.tabs_2 = QTabWidget(AppTaludes)
        self.tabs_2.setObjectName(u"tabs_2")
        sizePolicy1.setHeightForWidth(self.tabs_2.sizePolicy().hasHeightForWidth())
        self.tabs_2.setSizePolicy(sizePolicy1)
        self.tabs_2.setTabletTracking(True)
        self.tabs_2.setAcceptDrops(True)
        self.tabs_2.setAutoFillBackground(True)
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
        self.verticalLayoutWidget_2.setGeometry(QRect(-1, -1, 521, 391))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabs_2.addTab(self.tab_2, "")

        self.canvas_Layout.addWidget(self.tabs_2)


        self.gridLayout.addLayout(self.canvas_Layout, 2, 1, 1, 1)

        self.middle_Layout = QHBoxLayout()
        self.middle_Layout.setObjectName(u"middle_Layout")
        self.middle_Layout.setSizeConstraint(QLayout.SetFixedSize)
        self.imgname = QLabel(AppTaludes)
        self.imgname.setObjectName(u"imgname")
        self.imgname.setAutoFillBackground(True)

        self.middle_Layout.addWidget(self.imgname)

        self.imgsizex = QLabel(AppTaludes)
        self.imgsizex.setObjectName(u"imgsizex")

        self.middle_Layout.addWidget(self.imgsizex)

        self.imgsizey = QLabel(AppTaludes)
        self.imgsizey.setObjectName(u"imgsizey")

        self.middle_Layout.addWidget(self.imgsizey)

        self.x1label = QLabel(AppTaludes)
        self.x1label.setObjectName(u"x1label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.x1label.sizePolicy().hasHeightForWidth())
        self.x1label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.x1label.setFont(font)
        self.x1label.setAutoFillBackground(True)
        self.x1label.setFrameShape(QFrame.NoFrame)
        self.x1label.setLineWidth(1)
        self.x1label.setScaledContents(True)
        self.x1label.setMargin(5)

        self.middle_Layout.addWidget(self.x1label)

        self.y1lineEdit = QLineEdit(AppTaludes)
        self.y1lineEdit.setObjectName(u"y1lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.y1lineEdit.sizePolicy().hasHeightForWidth())
        self.y1lineEdit.setSizePolicy(sizePolicy3)
        self.y1lineEdit.setAutoFillBackground(True)
        self.y1lineEdit.setClearButtonEnabled(True)

        self.middle_Layout.addWidget(self.y1lineEdit)

        self.x2label = QLabel(AppTaludes)
        self.x2label.setObjectName(u"x2label")
        sizePolicy2.setHeightForWidth(self.x2label.sizePolicy().hasHeightForWidth())
        self.x2label.setSizePolicy(sizePolicy2)
        self.x2label.setFont(font)
        self.x2label.setAutoFillBackground(True)
        self.x2label.setFrameShape(QFrame.NoFrame)
        self.x2label.setScaledContents(True)
        self.x2label.setMargin(5)

        self.middle_Layout.addWidget(self.x2label)

        self.y2lineEdit = QLineEdit(AppTaludes)
        self.y2lineEdit.setObjectName(u"y2lineEdit")
        sizePolicy3.setHeightForWidth(self.y2lineEdit.sizePolicy().hasHeightForWidth())
        self.y2lineEdit.setSizePolicy(sizePolicy3)
        self.y2lineEdit.setAutoFillBackground(True)
        self.y2lineEdit.setDragEnabled(False)
        self.y2lineEdit.setClearButtonEnabled(True)

        self.middle_Layout.addWidget(self.y2lineEdit)

        self.y1label = QLabel(AppTaludes)
        self.y1label.setObjectName(u"y1label")
        sizePolicy2.setHeightForWidth(self.y1label.sizePolicy().hasHeightForWidth())
        self.y1label.setSizePolicy(sizePolicy2)
        self.y1label.setFont(font)
        self.y1label.setAutoFillBackground(True)
        self.y1label.setFrameShape(QFrame.NoFrame)
        self.y1label.setScaledContents(True)
        self.y1label.setMargin(5)

        self.middle_Layout.addWidget(self.y1label)

        self.x1lineEdit = QLineEdit(AppTaludes)
        self.x1lineEdit.setObjectName(u"x1lineEdit")
        sizePolicy3.setHeightForWidth(self.x1lineEdit.sizePolicy().hasHeightForWidth())
        self.x1lineEdit.setSizePolicy(sizePolicy3)
        self.x1lineEdit.setAutoFillBackground(True)
        self.x1lineEdit.setClearButtonEnabled(True)

        self.middle_Layout.addWidget(self.x1lineEdit)

        self.y2label = QLabel(AppTaludes)
        self.y2label.setObjectName(u"y2label")
        sizePolicy2.setHeightForWidth(self.y2label.sizePolicy().hasHeightForWidth())
        self.y2label.setSizePolicy(sizePolicy2)
        self.y2label.setFont(font)
        self.y2label.setLayoutDirection(Qt.LeftToRight)
        self.y2label.setAutoFillBackground(True)
        self.y2label.setFrameShape(QFrame.NoFrame)
        self.y2label.setScaledContents(True)
        self.y2label.setMargin(5)

        self.middle_Layout.addWidget(self.y2label)

        self.x2lineEdit = QLineEdit(AppTaludes)
        self.x2lineEdit.setObjectName(u"x2lineEdit")
        sizePolicy3.setHeightForWidth(self.x2lineEdit.sizePolicy().hasHeightForWidth())
        self.x2lineEdit.setSizePolicy(sizePolicy3)
        self.x2lineEdit.setAutoFillBackground(True)
        self.x2lineEdit.setClearButtonEnabled(True)

        self.middle_Layout.addWidget(self.x2lineEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.limits = QLabel(AppTaludes)
        self.limits.setObjectName(u"limits")
        self.limits.setFont(font)
        self.limits.setFrameShape(QFrame.Panel)
        self.limits.setScaledContents(True)
        self.limits.setAlignment(Qt.AlignCenter)
        self.limits.setWordWrap(False)

        self.verticalLayout.addWidget(self.limits)

        self.label = QLabel(AppTaludes)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.label)


        self.middle_Layout.addLayout(self.verticalLayout)

        self.Adjust = QPushButton(AppTaludes)
        self.Adjust.setObjectName(u"Adjust")

        self.middle_Layout.addWidget(self.Adjust)

        self.middle_Layout.setStretch(3, 1)
        self.middle_Layout.setStretch(4, 1)
        self.middle_Layout.setStretch(5, 1)
        self.middle_Layout.setStretch(6, 1)
        self.middle_Layout.setStretch(7, 1)
        self.middle_Layout.setStretch(8, 1)
        self.middle_Layout.setStretch(9, 1)
        self.middle_Layout.setStretch(10, 1)
        self.middle_Layout.setStretch(11, 1)
        self.middle_Layout.setStretch(12, 1)

        self.gridLayout.addLayout(self.middle_Layout, 3, 1, 1, 1)

        self.down_Layout = QHBoxLayout()
        self.down_Layout.setObjectName(u"down_Layout")
        self.down_Layout.setSizeConstraint(QLayout.SetMaximumSize)
        self.down_Layout.setContentsMargins(4, 4, 4, 4)
        self.h_hw_Layout = QGridLayout()
        self.h_hw_Layout.setObjectName(u"h_hw_Layout")
        self.h_hw_Layout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSlider_H = QSlider(AppTaludes)
        self.horizontalSlider_H.setObjectName(u"horizontalSlider_H")
        sizePolicy3.setHeightForWidth(self.horizontalSlider_H.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_H.setSizePolicy(sizePolicy3)
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
        self.hLbl = QLabel(AppTaludes)
        self.hLbl.setObjectName(u"hLbl")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.hLbl.sizePolicy().hasHeightForWidth())
        self.hLbl.setSizePolicy(sizePolicy4)
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
        sizePolicy3.setHeightForWidth(self.hlineEdit.sizePolicy().hasHeightForWidth())
        self.hlineEdit.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.hlineEdit)


        self.h_hw_Layout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.hwLbl = QLabel(AppTaludes)
        self.hwLbl.setObjectName(u"hwLbl")
        sizePolicy4.setHeightForWidth(self.hwLbl.sizePolicy().hasHeightForWidth())
        self.hwLbl.setSizePolicy(sizePolicy4)
        self.hwLbl.setFont(font)
        self.hwLbl.setAutoFillBackground(True)
        self.hwLbl.setFrameShape(QFrame.Panel)
        self.hwLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.hwLbl)

        self.hwlineEdit = QLineEdit(AppTaludes)
        self.hwlineEdit.setObjectName(u"hwlineEdit")
        sizePolicy3.setHeightForWidth(self.hwlineEdit.sizePolicy().hasHeightForWidth())
        self.hwlineEdit.setSizePolicy(sizePolicy3)

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


        self.down_Layout.addLayout(self.h_hw_Layout)

        self.c_phi_Layout = QGridLayout()
        self.c_phi_Layout.setObjectName(u"c_phi_Layout")
        self.c_phi_Layout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalSlider_C = QSlider(AppTaludes)
        self.horizontalSlider_C.setObjectName(u"horizontalSlider_C")
        sizePolicy3.setHeightForWidth(self.horizontalSlider_C.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_C.setSizePolicy(sizePolicy3)
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
        sizePolicy4.setHeightForWidth(self.oLbl.sizePolicy().hasHeightForWidth())
        self.oLbl.setSizePolicy(sizePolicy4)
        self.oLbl.setFont(font)
        self.oLbl.setMouseTracking(True)
        self.oLbl.setAutoFillBackground(True)
        self.oLbl.setFrameShape(QFrame.Panel)
        self.oLbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.oLbl)

        self.philineEdit = QLineEdit(AppTaludes)
        self.philineEdit.setObjectName(u"philineEdit")
        sizePolicy3.setHeightForWidth(self.philineEdit.sizePolicy().hasHeightForWidth())
        self.philineEdit.setSizePolicy(sizePolicy3)
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
        sizePolicy4.setHeightForWidth(self.cLbl.sizePolicy().hasHeightForWidth())
        self.cLbl.setSizePolicy(sizePolicy4)
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
        sizePolicy3.setHeightForWidth(self.ClineEdit.sizePolicy().hasHeightForWidth())
        self.ClineEdit.setSizePolicy(sizePolicy3)
        self.ClineEdit.setFocusPolicy(Qt.NoFocus)
        self.ClineEdit.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.ClineEdit)


        self.c_phi_Layout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.down_Layout.addLayout(self.c_phi_Layout)

        self.btnLayout = QVBoxLayout()
        self.btnLayout.setObjectName(u"btnLayout")
        self.btnLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.browse = QPushButton(AppTaludes)
        self.browse.setObjectName(u"browse")

        self.btnLayout.addWidget(self.browse)

        self.AnalysisBtn = QPushButton(AppTaludes)
        self.AnalysisBtn.setObjectName(u"AnalysisBtn")

        self.btnLayout.addWidget(self.AnalysisBtn)

        self.ClearBtn = QPushButton(AppTaludes)
        self.ClearBtn.setObjectName(u"ClearBtn")

        self.btnLayout.addWidget(self.ClearBtn)


        self.down_Layout.addLayout(self.btnLayout)

        self.down_Layout.setStretch(0, 1)
        self.down_Layout.setStretch(1, 1)
        self.down_Layout.setStretch(2, 1)

        self.gridLayout.addLayout(self.down_Layout, 4, 1, 1, 1)


        self.retranslateUi(AppTaludes)
        self.ClearBtn.clicked.connect(self.philineEdit.clear)
        self.ClearBtn.clicked.connect(self.ClineEdit.clear)
        self.ClearBtn.clicked.connect(self.hwlineEdit.clear)
        self.ClearBtn.clicked.connect(self.hlineEdit.clear)
        self.browse.clicked.connect(AppTaludes.getfile)
        self.ClearBtn.clicked.connect(self.y2lineEdit.clear)
        self.ClearBtn.clicked.connect(self.y1lineEdit.clear)
        self.ClearBtn.clicked.connect(self.x2lineEdit.clear)
        self.ClearBtn.clicked.connect(self.label.clear)
        self.ClearBtn.clicked.connect(self.imgsizex.clear)
        self.ClearBtn.clicked.connect(self.x1lineEdit.clear)

        self.tabs.setCurrentIndex(0)
        self.tabs_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AppTaludes)
    # setupUi

    def retranslateUi(self, AppTaludes):
        AppTaludes.setWindowTitle(QCoreApplication.translate("AppTaludes", u"AppTaludes", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QCoreApplication.translate("AppTaludes", u"Open a file to start", None))
        self.tabs_2.setTabText(self.tabs_2.indexOf(self.tab_2), QCoreApplication.translate("AppTaludes", u"Open a file to start", None))
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
        self.hLbl.setText(QCoreApplication.translate("AppTaludes", u"h(m)", None))
        self.hlineEdit.setText("")
        self.hwLbl.setText(QCoreApplication.translate("AppTaludes", u"<html><head/><body><p>h<span style=\" vertical-align:sub;\">w</span> (m)</p></body></html>", None))
        self.oLbl.setText(QCoreApplication.translate("AppTaludes", u"\u03d5' (\u00b0)", None))
        self.cLbl.setText(QCoreApplication.translate("AppTaludes", u"c'(kPa)", None))
        self.browse.setText(QCoreApplication.translate("AppTaludes", u"Browse", None))
        self.AnalysisBtn.setText(QCoreApplication.translate("AppTaludes", u"Run Analysis", None))
        self.ClearBtn.setText(QCoreApplication.translate("AppTaludes", u"Clear", None))
    # retranslateUi

