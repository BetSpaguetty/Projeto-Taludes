from Filtros.FOS.taludes import *
from _models.mapa import Mapa
from _views.ambienteView import AmbienteView
from _views.toolbar import *
import os
from config import *
from Filtros.FOS.presets import *
from _views.FOS.soil import  *
from _views.FOS.rain import  *
from _views.matrixOptionsView import  *



class MinhaCaixinha(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caixinha personalizada")
        self.setFixedSize(250, 150)

        layout = QVBoxLayout()

        label = QLabel("Digite algo:")
        self.input = QLineEdit()
        btn_ok = QPushButton("OK")

        btn_ok.clicked.connect(self.close)  # Fecha a caixinha ao clicar

        layout.addWidget(label)
        layout.addWidget(self.input)
        layout.addWidget(btn_ok)

        self.setLayout(layout)


