import numpy as np

from Filtros.filtro import *
from _views.Componentes.sliders import * 
from scipy.ndimage import uniform_filter

class FilterFlow(Filter) : 

    def __init__(self, ):
        super().__init__()

        self.view()


    def calculateMatrix(self):
        
        """
        Calcula a matriz de acumulação de fluxo (Flow Accumulation) 
        a partir de uma matriz de elevação (DEM) usando o método D8.
        
        Parâmetros:
            dem (np.ndarray): matriz 2D com as elevações do terreno.

        Retorna:
            np.ndarray: matriz 2D com o número de células que drenam para cada ponto.
        """
        dem = self.matrixElevation
        nrows, ncols = dem.shape
        acc = np.ones_like(dem, dtype=float)  # começa com 1 (cada célula conta por si)
        
        # direções D8 (em ordem horária: N, NE, E, SE, S, SW, W, NW)
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                    (1, 0), (1, -1), (0, -1), (-1, -1)]
        
        # ordena as células da mais alta para a mais baixa
        flat_idx = np.argsort(-dem, axis=None)
        rows, cols = np.unravel_index(flat_idx, dem.shape)
        
        for r, c in zip(rows, cols):
            z = dem[r, c]
            # procura vizinho mais baixo
            min_drop = 0
            drn = None
            for dr, dc in directions:
                rr, cc = r + dr, c + dc
                if 0 <= rr < nrows and 0 <= cc < ncols:
                    drop = z - dem[rr, cc]
                    if drop > min_drop:
                        min_drop = drop
                        drn = (rr, cc)
            # acumula o fluxo
            if drn:
                acc[drn] += acc[r, c]
        
        return acc


        
    def view(self) : 
        self.sliderCellSize = BasicSlider('Cell Size', 0, 100)
        self.sliderHeight = BasicSlider('Height', 0, 500)

        views = []
        views.append(self.sliderCellSize)
        views.append(self.sliderHeight)


























