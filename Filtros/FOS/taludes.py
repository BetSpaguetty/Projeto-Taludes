
from Filtros.FOS.presets import *
from Filtros.FOS.types import *
import numpy as np
from math import log, isnan


class Taludes : 

    def __init__(self):
        pass

    
    def calculateTaludes(matrixElevation:np.ndarray, soil:Soils, h:float, hw:float, c:float, phi:float, thetai:float, L:int ) -> np.ndarray :
       
        lenI = matrixElevation.shape[0]
        lenJ = matrixElevation.shape[1]
        LD = np.sqrt(2) * L
        FUNCTION = FOS_SOIL_FUNCTIONS[soil]
        h_arr      = np.full((lenI, lenJ), h, dtype=float)
        hw_arr     = np.full((lenI, lenJ), hw, dtype=float)
        c_arr      = np.full((lenI, lenJ), c, dtype=float)
        phi_arr    = np.full((lenI, lenJ), phi, dtype=float)
        thetai_arr = np.full((lenI, lenJ), thetai, dtype=float)
        alpha = Taludes.calculateAlpha(matrixElevation, lenI, lenJ, L, LD)
        FOS = np.vectorize(FUNCTION)(h_arr, hw_arr, alpha, c_arr, phi_arr, thetai_arr)
        FOS = np.clip(FOS, 1, 2)
        return FOS

    

    def calculateAlpha(matriz, nLinhas, nColunas, L, LD):
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
    


    def calculateHW(p: float, t: float, theta_i: float = 0.3, h=3, solo:Soils=Soils.COARSE) -> float:
        solo = Taludes.getSoilMaterial(solo)
        theta_r = solo.THETA_R
        theta_s = solo.THETA_S 
        alpha = solo.VG_ALPHA  # m^-1
        n = solo.VG_N
        m = solo.VG_M 
        k_day = solo.VG_K  # m/dia

        try:
            k = k_day / 24  # m/h
            theta_e = (theta_i - theta_r) / (theta_s - theta_r)
            psi = ((1 - (theta_e ** (1 / m))) / ((alpha ** n) * (theta_e ** (1 / m)))) ** (1 / n)
            a = abs(psi) * (theta_s - theta_i)
            tp = k * abs(psi) * (theta_s - theta_i) / (p * (p - k))
            hwp = p * tp
            hw0 = k * (t - tp) + hwp
            hw = hw0 + a * log((hw0 + a) / (hwp + a)) * ((hw0 + a) / hw0)
            if isnan(hw) or hw < 0:
                hw = 0
            elif hw > h:
                hw = h
        except (ZeroDivisionError, ValueError):
            hw = 0

        return hw


    def getSoilMaterial(soilType:Soils) -> Soil : 
        return SOIL_MATERIALS[soilType]

    
    def getSoilType(clay, sand, silt) -> Soils:
        for S, F in SOIL_FUNCTIONS.items() : 
            if F(clay, sand, silt) : return S




