

import numpy as np
from scipy.ndimage import uniform_filter
from Filtros.filtro import *
from _views.Componentes.sliders import *

class FilterInclination(Filter) : 

    def __init__(self, ):
        super().__init__()
        self.viewsInclination()


    def viewsInclination(self ) :
        self.sliderView = BasicSlider('Scale', 1, 100)
        self.sliderView.slider.setValue(25)        
        self.sliderView.slider.valueChanged.connect(self.sendMatrixToReceptor)
        self.views['Scale'] = self.sliderView


    def calculateMatrix(self) :
        return self.calcular_rugosidade()

    def calcular_rugosidade(self) -> np.ndarray:
        
        matrix = self.getElevationMatrix()
        lenI = matrix.shape[0]
        lenJ = matrix.shape[1]
        L = self.sliderView.getValue()
        LD = np.sqrt(2) * L

        return self.calculateAlpha(matrix, lenI, lenJ, L, LD)



    def calculateAlpha(self, matriz, nLinhas, nColunas, L, LD):
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
