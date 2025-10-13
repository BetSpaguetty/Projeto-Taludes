from Taludes.presets import *
from Taludes.types import *
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



  

COLORMAPS = [
    ('Padrao Tecgraf', ["red", "orange", "yellow", "green", "blue"]),

    # 🔹 Perceptualmente Uniformes (ótimos para dados científicos)
    "viridis",
    "plasma",
    "inferno",
    "magma",
    "cividis",
    "twilight",
    "twilight_shifted",
    "turbo",

    # 🔹 Sequenciais (do claro ao escuro)
    "Greys",
    "Purples",
    "Blues",
    "Greens",
    "Oranges",
    "Reds",
    "YlOrBr",
    "YlOrRd",
    "OrRd",
    "PuRd",
    "RdPu",
    "BuPu",
    "GnBu",
    "PuBu",
    "YlGnBu",
    "PuBuGn",
    "BuGn",
    "YlGn",

    # 🔹 Sequenciais (reversos, terminam com "_r")
    "Greys_r",
    "Purples_r",
    "Blues_r",
    "Greens_r",
    "Oranges_r",
    "Reds_r",
    "YlOrBr_r",
    "YlOrRd_r",
    "OrRd_r",
    "PuRd_r",
    "RdPu_r",
    "BuPu_r",
    "GnBu_r",
    "PuBu_r",
    "YlGnBu_r",
    "PuBuGn_r",
    "BuGn_r",
    "YlGn_r",

    # 🔹 Divergentes (bons para dados centrados em zero)
    "PiYG",
    "PRGn",
    "BrBG",
    "PuOr",
    "RdGy",
    "RdBu",
    "RdYlBu",
    "RdYlGn",
    "Spectral",
    "coolwarm",
    "bwr",
    "seismic",

    # 🔹 Divergentes reversos
    "PiYG_r",
    "PRGn_r",
    "BrBG_r",
    "PuOr_r",
    "RdGy_r",
    "RdBu_r",
    "RdYlBu_r",
    "RdYlGn_r",
    "Spectral_r",
    "coolwarm_r",
    "bwr_r",
    "seismic_r",

    # 🔹 Cíclicos (para ângulos, fases, etc.)
    "twilight",
    "twilight_shifted",
    "hsv",
    "twilight_r",
    "twilight_shifted_r",
    "hsv_r",

    # 🔹 Qualitativos (categorias diferentes)
    "Pastel1",
    "Pastel2",
    "Paired",
    "Accent",
    "Dark2",
    "Set1",
    "Set2",
    "Set3",
    "tab10",
    "tab20",
    "tab20b",
    "tab20c",

    # 🔹 Misc / Clássicos
    "flag",
    "prism",
    "ocean",
    "gist_earth",
    "terrain",
    "gist_stern",
    "gnuplot",
    "gnuplot2",
    "CMRmap",
    "cubehelix",
    "brg",
    "gist_rainbow",
    "rainbow",
    "jet",
    "nipy_spectral",
    "gist_ncar",

    # 🔹 Versões reversas dos clássicos
    "flag_r",
    "prism_r",
    "ocean_r",
    "gist_earth_r",
    "terrain_r",
    "gist_stern_r",
    "gnuplot_r",
    "gnuplot2_r",
    "CMRmap_r",
    "cubehelix_r",
    "brg_r",
    "gist_rainbow_r",
    "rainbow_r",
    "jet_r",
    "nipy_spectral_r",
    "gist_ncar_r",
]










