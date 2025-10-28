from Taludes.types   import * 
from Taludes.presets import * 
import numpy as np
from config import *


def calculateFos(matrix, lenI, lenJ, h, hw, c, phi, thetai, L, soil):
    LD = np.sqrt(2) * L
    FUNCTION = FOS_SOIL_FUNCTIONS[soil]
    # cria arrays preenchidos
    h_arr      = np.full((lenI, lenJ), h, dtype=float)
    hw_arr     = np.full((lenI, lenJ), hw, dtype=float)
    c_arr      = np.full((lenI, lenJ), c, dtype=float)
    phi_arr    = np.full((lenI, lenJ), phi, dtype=float)
    thetai_arr = np.full((lenI, lenJ), thetai, dtype=float)

    # calcula alpha já vetorizado
    alpha = calculateAlpha(matrix, lenI, lenJ, L, LD)

    # aplica fosFunction em todo o grid (se ela suportar vetores)
    fos = np.vectorize(FUNCTION)(h_arr, hw_arr, alpha, c_arr, phi_arr, thetai_arr)
    fos = np.clip(fos, 1, 2)
    return fos


def defineMaterial(clay, sand, silt) :
    for M in FOS_SOIL_FUNCTIONS.values() :
        if M['function'](clay, sand, silt) : 
            material = M['material']
            return material


def calculateAlpha(matriz, nLinhas, nColunas, L, LD):
    # diferenças centrais já vetorizadas
    diffs = np.zeros((nLinhas, nColunas, 8))

    diffs[1:-1,1:-1,0] = np.abs(matriz[2:,1:-1]  - matriz[1:-1,1:-1]) / L
    diffs[1:-1,1:-1,1] = np.abs(matriz[:-2,1:-1] - matriz[1:-1,1:-1]) / L
    diffs[1:-1,1:-1,2] = np.abs(matriz[1:-1,2:]  - matriz[1:-1,1:-1]) / L
    diffs[1:-1,1:-1,3] = np.abs(matriz[1:-1,:-2] - matriz[1:-1,1:-1]) / L
    diffs[1:-1,1:-1,4] = np.abs(matriz[2:,2:]    - matriz[1:-1,1:-1]) / LD
    diffs[1:-1,1:-1,5] = np.abs(matriz[:-2,:-2]  - matriz[1:-1,1:-1]) / LD
    diffs[1:-1,1:-1,6] = np.abs(matriz[:-2,2:]   - matriz[1:-1,1:-1]) / LD
    diffs[1:-1,1:-1,7] = np.abs(matriz[2:,:-2]   - matriz[1:-1,1:-1]) / LD

    gradientMax = diffs.max(axis=2)
    gradientMax[0, :] = 0
    gradientMax[-1,:] = 0
    gradientMax[:, 0] = 0
    gradientMax[:,-1] = 0

    alpha = np.degrees(np.arctan(gradientMax))
    alpha_deg = np.clip(alpha, 0.0, 90.0)
    return alpha_deg










