from dataclasses import dataclass
from enum import Enum

TECGRAF_LINK = 'https://www.google.com/search?q=gatos'
TECGRAF_LINK = 'https://share.google/6WIu8CBn94VOoYM2S'

DATA_PATH = 'DATA\mapsJson'

INITIAL_CLAY = 30
INITIAL_SAND = 30
INITIAL_SILT = 40

class GraphFilters(Enum) :
    ELEVATION = 'Elevation'
    FOS = 'FOS'
    RUGOSITY = 'Rugosity'
    FLOWAC = 'Flow Accumulation'


class GraphModes(Enum)  :
    _2D = '2D'
    _3D = '3D'















