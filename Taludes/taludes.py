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

def calculateGrid(matriz, nLinhas, nColunas) :
    pass



def calculateFos(matriz, nLinhas, nColunas, h, hw, c, phi, thetai, L, LD, fosFunction) :
    h      = np.full((nLinhas, nColunas), h)
    hw     = np.full((nLinhas, nColunas), hw)
    c      = np.full((nLinhas, nColunas), c)
    phi    = np.full((nLinhas, nColunas), phi)
    thetai = np.full((nLinhas, nColunas), thetai)
    alpha  = calculateAlpha(matriz, nLinhas, nColunas, L, LD)

    fos = np.zeros((nLinhas, nColunas))

    for i in range(nLinhas):
        for j in range(nColunas):
            fos[i,j] = fosFunction( h[i,j], hw[i,j], alpha[i,j], c[i,j], phi[i,j], thetai[i,j] )

    fosFiltro = np.copy(fos)
    fosFiltro[fosFiltro > 2] = 2
    fosFiltro[fosFiltro < 1] = 1
    return fosFiltro




def calculateAlpha(matriz, nLinhas, nColunas, L, LD) :
    gradientMax = np.zeros_like(matriz)
    for i in range(1, nLinhas-1):
        for j in range(1, nColunas-1):
            diffs = [
                abs(matriz[i+1,j]-matriz[i,j])/L,
                abs(matriz[i-1,j]-matriz[i,j])/L,
                abs(matriz[i,j+1]-matriz[i,j])/L,
                abs(matriz[i,j-1]-matriz[i,j])/L,
                abs(matriz[i+1,j+1]-matriz[i,j])/LD,
                abs(matriz[i-1,j-1]-matriz[i,j])/LD,
                abs(matriz[i-1,j+1]-matriz[i,j])/LD,
                abs(matriz[i+1,j-1]-matriz[i,j])/LD
                ]
            gradientMax[i,j] = max(diffs)

    gradientMax[ 0,:] = 0
    gradientMax[-1,:] = 0
    gradientMax[:, 0] = 0
    gradientMax[:,-1] = 0
    alpha = np.degrees(np.arctan(gradientMax))

    return alpha







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