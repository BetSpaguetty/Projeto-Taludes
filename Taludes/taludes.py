from Taludes.types   import * 
from Taludes.presets import * 
import numpy as np
from PIL import Image
import pyvista as pv
from config import *

def defineMaterial(clay, sand, silt) :
    
    for M in SOIL_TYPES.values() :
        if M['function'](clay, sand, silt) : 
            material = M['material']
            return material





import numpy as np

def calculateAlpha(matriz, nLinhas, nColunas, L, LD):
    # diferenças centrais já vetorizadas
    diffs = np.zeros((nLinhas, nColunas, 8))

    diffs[1:-1,1:-1,0] = np.abs(matriz[2:,1:-1] - matriz[1:-1,1:-1]) / L
    diffs[1:-1,1:-1,1] = np.abs(matriz[:-2,1:-1] - matriz[1:-1,1:-1]) / L
    diffs[1:-1,1:-1,2] = np.abs(matriz[1:-1,2:] - matriz[1:-1,1:-1]) / L
    diffs[1:-1,1:-1,3] = np.abs(matriz[1:-1,:-2] - matriz[1:-1,1:-1]) / L

    diffs[1:-1,1:-1,4] = np.abs(matriz[2:,2:] - matriz[1:-1,1:-1]) / LD
    diffs[1:-1,1:-1,5] = np.abs(matriz[:-2,:-2] - matriz[1:-1,1:-1]) / LD
    diffs[1:-1,1:-1,6] = np.abs(matriz[:-2,2:] - matriz[1:-1,1:-1]) / LD
    diffs[1:-1,1:-1,7] = np.abs(matriz[2:,:-2] - matriz[1:-1,1:-1]) / LD

    gradientMax = diffs.max(axis=2)
    gradientMax[0,:]  = 0
    gradientMax[-1,:] = 0
    gradientMax[:,0]  = 0
    gradientMax[:,-1] = 0

    alpha = np.degrees(np.arctan(gradientMax))
    return alpha


def calculateFos(matrix, lenI, lenJ, h, hw, c, phi, thetai, L, soil):



    LD = np.sqrt(L)
    FUNCTION = SOIL_FUNCTIONS[soil]
    # cria arrays preenchidos
    h_arr      = np.full((lenI, lenJ), h, dtype=float)
    hw_arr     = np.full((lenI, lenJ), hw, dtype=float)
    c_arr      = np.full((lenI, lenJ), c, dtype=float)
    phi_arr    = np.full((lenI, lenJ), phi, dtype=float)
    thetai_arr = np.full((lenI, lenJ), thetai, dtype=float)

    # calcula alpha já vetorizado
    alpha = calculateAlpha(matrix, lenI, lenJ, L, LD)

    # aplica fosFunction em todo o grid (se ela suportar vetores)
    try: fos = FUNCTION(h_arr, hw_arr, alpha, c_arr, phi_arr, thetai_arr)
    except Exception: fos = np.vectorize(FUNCTION)(h_arr, hw_arr, alpha, c_arr, phi_arr, thetai_arr)
        # fallback se fosFunction for escalar → aplica em vetor

    # clamping vetorizado
    fos = np.clip(fos, 1, 2)

    return fos




def calculateHW(material: Materiais, p, t, h, theta_i):
    solo = SOIL_MATERIALS[material]
    
    theta_r = solo.THETA_R
    theta_s = solo.THETA_S
    alpha   = solo.VG_ALPHA
    m       = solo.VG_M
    n       = solo.VG_N
    k_day   = solo.VG_K
    k = k_day / 24.0

    theta_e = (theta_i - theta_r) / (theta_s - theta_r)
    Psi = ((1 - theta_e ** (1/m)) / (alpha**n * theta_e ** (1/m))) ** (1/n)  # [m]
    a = abs(Psi) * (theta_s - theta_i)  # [m]
    tp = k * abs(Psi) * (theta_s - theta_i) / (p * (p - k))  # [h]
    hwp = p * tp  # [m]
    hw0 = k * (t - tp) + hwp

    hw = hw0 + a * np.log((hw0 + a) / (hwp + a)) * ((hw0 + a) / hw0)

    if np.isnan(hw): hw = 0.0
    if hw < 0: hw = 0.0
    elif hw > h: hw = h

    return hw



# def calculateFos(matriz, nLinhas, nColunas, h, hw, c, phi, thetai, L, LD, fosFunction) :
#     h      = np.full((nLinhas, nColunas), h)
#     hw     = np.full((nLinhas, nColunas), hw)
#     c      = np.full((nLinhas, nColunas), c)
#     phi    = np.full((nLinhas, nColunas), phi)
#     thetai = np.full((nLinhas, nColunas), thetai)
#     alpha  = calculateAlpha(matriz, nLinhas, nColunas, L, LD)

#     fos = np.zeros((nLinhas, nColunas))

#     for i in range(nLinhas):
#         for j in range(nColunas):
#             fos[i,j] = fosFunction( h[i,j], hw[i,j], alpha[i,j], c[i,j], phi[i,j], thetai[i,j] )

#     fos[fos > 2] = 2
#     fos[fos < 1] = 1
#     return fos




# def calculateAlpha(matriz, nLinhas, nColunas, L, LD) :
#     gradientMax = np.zeros_like(matriz)
#     for i in range(1, nLinhas-1):
#         for j in range(1, nColunas-1):
#             diffs = [
#                 abs(matriz[i+1,j]-matriz[i,j])/L,
#                 abs(matriz[i-1,j]-matriz[i,j])/L,
#                 abs(matriz[i,j+1]-matriz[i,j])/L,
#                 abs(matriz[i,j-1]-matriz[i,j])/L,
#                 abs(matriz[i+1,j+1]-matriz[i,j])/LD,
#                 abs(matriz[i-1,j-1]-matriz[i,j])/LD,
#                 abs(matriz[i-1,j+1]-matriz[i,j])/LD,
#                 abs(matriz[i+1,j-1]-matriz[i,j])/LD
#                 ]
#             gradientMax[i,j] = max(diffs)

#     gradientMax[ 0,:] = 0
#     gradientMax[-1,:] = 0
#     gradientMax[:, 0] = 0
#     gradientMax[:,-1] = 0
#     alpha = np.degrees(np.arctan(gradientMax))

#     return alpha






