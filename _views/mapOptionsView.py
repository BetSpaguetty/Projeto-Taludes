from Taludes.taludes import *
from _models.mapa import Mapa
from _views.ambienteView import AmbienteView
from _views.toolsbar import *
import os
from app_config import *
from Taludes.presets import *
from app_types import *
from _views.soil import  *
from _views.rain import  *
from _views.mapOptionsView import  *



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


