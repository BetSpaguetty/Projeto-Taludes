from Taludes.presets import *
from Taludes.types import *
from app_types import *
from dataclasses import dataclass
from enum import Enum

TECGRAF_LINK = 'https://www.google.com/search?q=gatos'
TECGRAF_LINK = 'https://share.google/6WIu8CBn94VOoYM2S'



INITIAL_CLAY = 30
INITIAL_SAND = 30
INITIAL_SILT = 40

class GraphFilters(Enum) :
    ELEVATION = 'Elevation'
    FOS = 'FOS'


class GraphModes(Enum)  :
    D2 = '2D'
    D3 = '3D'


GRAPH_MODES = {
    GraphModes.D2 : DictButton('2D'),
    GraphModes.D3 : DictButton('3D'),
    }


GRAPH_FILTERS : dict[GraphFilters, DictButton] =  {
    GraphFilters.ELEVATION : DictButton('elevation'),
    GraphFilters.FOS       : DictButton('fos'),

    }


  










