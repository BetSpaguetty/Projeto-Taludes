import os
from config import *
from configMatrix import *
from Filtros.Taludes.taludes import *
from Filtros.Taludes.presets import *
from _models.mapa import Mapa
from _views.ambienteView import AmbienteView
from _views.toolbar import *
from _views.matrixOptionsView import  *
from _views.configView import ConfigurationMatrixViewer
from _views.FOS.toolbarFOS import ToolBarFOS
from Filtros.filtro import *


class FiltroTaludes(Filter) : 

    def __init__(self):
        super().__init__()

        
