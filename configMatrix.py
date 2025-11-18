
SHADERS = [
    'None',         # sem shader explícito
    'shaded',       # iluminação básica por normal (face shading)
    'balloon',      # efeito “inflado” (menos comum)
    'edgeHilight'   # realce de bordas da malha
    ]

SURFACE_OPTS = {
    'meshdata': None,
    'color': (1., 1., 1., 1.),
    'drawEdges': False,
    'drawFaces': True,
    'edgeColor': (0.5, 0.5, 0.5, 1.0),
    'shader': None,
    'smooth': True,
    'computeNormals': True,
}

MATRIX_BACKGROUNDS = {
    'black' : 'black',
    'white' : 'white',
    'navy'  : 'navy',
    'grey'  : '#202020',

    }


COLORMAPS = [
    ('Padrao Tecgraf', [(1, 0, 0), (1, 0.5, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1)], [0.0, 1.15, 1.3, 1.45, 1.65, 2.0]),
    ('Padrao Tecgraf 2', [(1, 0.216, 0.216), (1, 0.588, 0.263), (0.969, 1, 0.263), (0.792, 1, 0.263), (0.357, 1, 0.216)], [0.0, 1.15, 1.3, 1.45, 1.65, 2.0]),

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

