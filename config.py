from Taludes.presets import *
from Taludes.types import *

TECGRAF_LINK = 'https://www.google.com/search?q=gatos'
TECGRAF_LINK = 'https://share.google/6WIu8CBn94VOoYM2S'




INITIAL_CLAY = 30
INITIAL_SAND = 30
INITIAL_SILT = 40




DEFAULT_COARSE          : dict[str, int] = {'clay': 15 , 'sand': 70}
DEFAULT_GRANULAR_MEDIUM : dict[str, int] = {'clay': 15 , 'sand': 50}
DEFAULT_GRANULAR_FINE   : dict[str, int] = {'clay': 15 , 'sand': 10}
DEFAULT_MEDIUM          : dict[str, int] = {'clay': 25 , 'sand': 20}
DEFAULT_MEDIUM_FINE     : dict[str, int] = {'clay': 25 , 'sand': 10}
DEFAULT_FINE            : dict[str, int] = {'clay': 50 , 'sand': 50}
DEFAULT_VERY_FINE       : dict[str, int] = {'clay': 70 , 'sand': 30}

DEFAULT_SOILS = {
    Materiais.COARSE          : DEFAULT_COARSE,
    Materiais.GRANULAR_MEDIUM : DEFAULT_GRANULAR_MEDIUM,
    Materiais.GRANULAR_FINE   : DEFAULT_GRANULAR_FINE,
    Materiais.MEDIUM          : DEFAULT_MEDIUM,
    Materiais.MEDIUM_FINE     : DEFAULT_MEDIUM_FINE,
    Materiais.FINE            : DEFAULT_FINE,
    Materiais.VERY_FINE       : DEFAULT_VERY_FINE,

    }















