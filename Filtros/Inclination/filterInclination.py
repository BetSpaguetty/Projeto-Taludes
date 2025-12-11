

import numpy as np
from scipy.ndimage import uniform_filter
from Filtros.filtro import *

class FilterInclination(Filter) : 

    def __init__(self, ):
        super().__init__()


    def calculateMatrix(self) :
        return self.calcular_rugosidade(self.matrixElevation)

    def calcular_rugosidade(self, matriz_elevacao: np.ndarray, tamanho_janela: int = 3) -> np.ndarray:
        # Garantir tipo float para cálculos
        dem = matriz_elevacao.astype(float)
        # Média local
        media_local = uniform_filter(dem, tamanho_janela, mode='reflect')
        # Média do quadrado (para variância)
        media_local_quadrado = uniform_filter(dem**2, tamanho_janela, mode='reflect')
        # Desvio padrão local (rugosidade)
        rugosidade = np.sqrt(np.maximum(0, media_local_quadrado - media_local**2))
        return rugosidade


