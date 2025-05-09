# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_LatLon.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(633, 496)
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.lineEdit_latitude = QLineEdit(Dialog)
        self.lineEdit_latitude.setObjectName(u"lineEdit_latitude")

        self.gridLayout.addWidget(self.lineEdit_latitude, 2, 0, 1, 1)

        self.lineEdit_longitude = QLineEdit(Dialog)
        self.lineEdit_longitude.setObjectName(u"lineEdit_longitude")

        self.gridLayout.addWidget(self.lineEdit_longitude, 2, 2, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.lineEdit_celula = QLineEdit(Dialog)
        self.lineEdit_celula.setObjectName(u"lineEdit_celula")

        self.gridLayout.addWidget(self.lineEdit_celula, 2, 4, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.botao_converte = QPushButton(Dialog)
        self.botao_converte.setObjectName(u"botao_converte")

        self.gridLayout.addWidget(self.botao_converte, 3, 4, 1, 1)

        self.info = QLabel(Dialog)
        self.info.setObjectName(u"info")

        self.gridLayout.addWidget(self.info, 3, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.long_min = QLabel(Dialog)
        self.long_min.setObjectName(u"long_min")

        self.gridLayout_2.addWidget(self.long_min, 2, 0, 1, 1)

        self.lat_min = QLabel(Dialog)
        self.lat_min.setObjectName(u"lat_min")

        self.gridLayout_2.addWidget(self.lat_min, 0, 0, 1, 1)

        self.long_max = QLabel(Dialog)
        self.long_max.setObjectName(u"long_max")

        self.gridLayout_2.addWidget(self.long_max, 2, 1, 1, 1)

        self.lat_max = QLabel(Dialog)
        self.lat_max.setObjectName(u"lat_max")

        self.gridLayout_2.addWidget(self.lat_max, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.add_info = QPushButton(Dialog)
        self.add_info.setObjectName(u"add_info")

        self.gridLayout_3.addWidget(self.add_info, 3, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.botao_converte.clicked.connect(Dialog.converteLatLon)
        self.add_info.clicked.connect(Dialog.show_add_info)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Longitude(E-W):", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"C\u00e9lula (x,y):", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Latitude (N-S):", None))
        self.botao_converte.setText(QCoreApplication.translate("Dialog", u"Converter (Ctrl + E)", None))
#if QT_CONFIG(shortcut)
        self.botao_converte.setShortcut(QCoreApplication.translate("Dialog", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.info.setText(QCoreApplication.translate("Dialog", u"Informa\u00e7\u00f5es:", None))
        self.long_min.setText(QCoreApplication.translate("Dialog", u"Longitude M\u00ednima:", None))
        self.lat_min.setText(QCoreApplication.translate("Dialog", u"Latitude M\u00ednima:", None))
        self.long_max.setText(QCoreApplication.translate("Dialog", u"Longitude M\u00e1xima:", None))
        self.lat_max.setText(QCoreApplication.translate("Dialog", u"Latitude M\u00e1xima:", None))
        self.add_info.setText(QCoreApplication.translate("Dialog", u"Adicionar Informa\u00e7\u00f5es", None))
    # retranslateUi

