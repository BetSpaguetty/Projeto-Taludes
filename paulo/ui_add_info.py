# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_info.ui'
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
        Dialog.resize(740, 429)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lay_principal = QVBoxLayout()
        self.lay_principal.setObjectName(u"lay_principal")
        self.lay_principal.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.add_long_max = QLineEdit(Dialog)
        self.add_long_max.setObjectName(u"add_long_max")

        self.gridLayout_2.addWidget(self.add_long_max, 2, 4, 1, 1)

        self.long_max = QLabel(Dialog)
        self.long_max.setObjectName(u"long_max")

        self.gridLayout_2.addWidget(self.long_max, 2, 3, 1, 1)

        self.long_min = QLabel(Dialog)
        self.long_min.setObjectName(u"long_min")

        self.gridLayout_2.addWidget(self.long_min, 2, 0, 1, 1)

        self.add_lat_max = QLineEdit(Dialog)
        self.add_lat_max.setObjectName(u"add_lat_max")

        self.gridLayout_2.addWidget(self.add_lat_max, 0, 4, 1, 1)

        self.lat_min = QLabel(Dialog)
        self.lat_min.setObjectName(u"lat_min")

        self.gridLayout_2.addWidget(self.lat_min, 0, 0, 1, 1)

        self.add_long_min = QLineEdit(Dialog)
        self.add_long_min.setObjectName(u"add_long_min")

        self.gridLayout_2.addWidget(self.add_long_min, 2, 2, 1, 1)

        self.add_lat_min = QLineEdit(Dialog)
        self.add_lat_min.setObjectName(u"add_lat_min")

        self.gridLayout_2.addWidget(self.add_lat_min, 0, 2, 1, 1)

        self.lat_max = QLabel(Dialog)
        self.lat_max.setObjectName(u"lat_max")

        self.gridLayout_2.addWidget(self.lat_max, 0, 3, 1, 1)


        self.lay_principal.addLayout(self.gridLayout_2)

        self.save = QPushButton(Dialog)
        self.save.setObjectName(u"save")

        self.lay_principal.addWidget(self.save)

        self.lay_principal.setStretch(0, 1)
        self.lay_principal.setStretch(1, 1)

        self.gridLayout.addLayout(self.lay_principal, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.save.clicked.connect(Dialog.salvar)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.long_max.setText(QCoreApplication.translate("Dialog", u"Longitude M\u00e1xima:", None))
        self.long_min.setText(QCoreApplication.translate("Dialog", u"Longitude M\u00ednima:", None))
        self.lat_min.setText(QCoreApplication.translate("Dialog", u"Latitude M\u00ednima:", None))
        self.lat_max.setText(QCoreApplication.translate("Dialog", u"Latitude M\u00e1xima:", None))
        self.save.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
    # retranslateUi

