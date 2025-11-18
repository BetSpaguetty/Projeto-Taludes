
import numpy as np

from Filtros.filtro import *
from _views.Componentes.sliders import * 
from scipy.ndimage import uniform_filter


class FilterTWI(Filter) : 

    def __init__(self):
        super().__init__()

    def calculateMatrix(self) : 
        dem = self.matrixElevation
        cellsize = 1.0 
        max_distance: int = 20

        """
        Calcula o Índice Topográfico de Umidade (TWI) para uma matriz de elevação.
        TWI = ln(A / tan(slope))

        Parâmetros:
            dem (np.ndarray): matriz de elevação
            cellsize (float): resolução espacial

        Retorna:
            np.ndarray: matriz TWI
        """
        rows, cols = dem.shape
        # ---------------------------
        # 1. Declividade (slope)
        # ---------------------------
        dzdx = (np.roll(dem, -1, axis=1) - np.roll(dem, 1, axis=1)) / (2 * cellsize)
        dzdy = (np.roll(dem, -1, axis=0) - np.roll(dem, 1, axis=0)) / (2 * cellsize)
        slope = np.sqrt(dzdx**2 + dzdy**2)
        # Evita slope zero → coloca inclinação mínima
        slope = np.maximum(slope, 1e-6)
        # ---------------------------
        # 2. Direção de fluxo (D8)
        # ---------------------------
        directions = [
            (-1,0),(-1,1),(0,1),(1,1),
            (1,0),(1,-1),(0,-1),(-1,-1)
        ]
        dist = np.array([
            cellsize, cellsize*np.sqrt(2), cellsize,
            cellsize*np.sqrt(2), cellsize, cellsize*np.sqrt(2),
            cellsize, cellsize*np.sqrt(2)
        ])
        flow_dir = np.zeros_like(dem, dtype=np.int8)
        for r in range(rows):
            for c in range(cols):
                z = dem[r, c]
                best = 0
                max_drop = -1e9

                for i, (dr, dc) in enumerate(directions):
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        drop = (z - dem[rr, cc]) / dist[i]
                        if drop > max_drop:
                            max_drop = drop
                            best = i

                flow_dir[r, c] = best
        # ---------------------------
        # 3. Acumulação de fluxo
        # ---------------------------
        flow_acc = np.ones_like(dem, dtype=float)
        coords = [(r, c) for r in range(rows) for c in range(cols)]
        coords.sort(key=lambda x: dem[x[0], x[1]], reverse=True)

        for r, c in coords:
            dr, dc = directions[flow_dir[r, c]]
            rr = r + dr
            cc = c + dc
            if 0 <= rr < rows and 0 <= cc < cols:
                flow_acc[rr, cc] += flow_acc[r, c]

        A = flow_acc * (cellsize * cellsize)
        # ---------------------------
        # 4. TWI
        # ---------------------------
        tan_slope = np.tan(slope)
        # evita divisão por zero
        tan_slope = np.maximum(tan_slope, 1e-9)
        twi_raw = A / tan_slope
        # evita log(0)
        twi_raw = np.maximum(twi_raw, 1e-12)
        twi_matrix = np.log(twi_raw)
        return twi_matrix





class FilterD8(Filter)  :


    def __init__(self):
        super().__init__()



    def calculateMatrix(self):
        """
        Calcula a direção de fluxo usando o método D8.
        Retorna uma matriz com valores de 0 a 7 representando a direção
        em que cada célula escoa (vizinho de menor cota).

        Parâmetros:
            dem (np.ndarray): matriz de elevação

        Retorna:
            np.ndarray: matriz flow_dir com valores de 0 a 7
        """
        dem = self.matrixElevation
        rows, cols = dem.shape
        flow_dir = np.zeros_like(dem, dtype=np.int8)

        # 8 direções possíveis: (drow, dcol)
        directions = [
            (-1, 0),  # 0: N
            (-1, 1),  # 1: NE
            (0, 1),   # 2: E
            (1, 1),   # 3: SE
            (1, 0),   # 4: S
            (1, -1),  # 5: SW
            (0, -1),  # 6: W
            (-1, -1)  # 7: NW
        ]

        for r in range(rows):
            for c in range(cols):
                z = dem[r, c]
                best_dir = 0
                min_elev = z  # queremos o vizinho mais baixo

                for d, (dr, dc) in enumerate(directions):
                    rr = r + dr
                    cc = c + dc

                    # ignora vizinhos fora da matriz
                    if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
                        continue

                    if dem[rr, cc] < min_elev:
                        min_elev = dem[rr, cc]
                        best_dir = d

                flow_dir[r, c] = best_dir

        return flow_dir


class FilterSolar(Filter) :


    def __init__(self):
        super().__init__()



    def calculateMatrix(self):
        solar_azimuth_deg=135
        solar_elevation_deg=40
        dem = self.matrixElevation
        cellsize = 1.0 


        """
        Calcula a radiação solar direta recebida por cada célula
        de uma matriz de elevação (DEM).

        Parâmetros:
        ------------
        dem : np.ndarray
            Matriz de elevação.
        solar_azimuth_deg : float
            Azimute solar em graus (0° = norte, aumenta no sentido horário).
        solar_elevation_deg : float
            Elevação solar em graus (ângulo acima do horizonte).
        cellsize : float
            Tamanho da célula (dx = dy). Padrão = 1.

        Retorna:
        ---------
        irradiance : np.ndarray
            Matriz com os valores de radiação relativa (0–1).
        """

        # Converte para radianos
        az = np.radians(solar_azimuth_deg)
        el = np.radians(solar_elevation_deg)

        # Derivadas espaciais
        dzdx = np.gradient(dem, axis=1) / cellsize
        dzdy = np.gradient(dem, axis=0) / cellsize

        # Declividade
        slope = np.arctan(np.sqrt(dzdx**2 + dzdy**2))

        # Aspecto (orientação do declive)
        aspect = np.arctan2(dzdy, -dzdx)
        aspect = np.where(aspect < 0, aspect + 2*np.pi, aspect)

        # COS do ângulo de incidência
        cos_i = (
            np.sin(el) * np.sin(slope)
            + np.cos(el) * np.cos(slope) * np.cos(az - aspect)
        )

        # Radiação não pode ser negativa: sombra local
        irradiance = np.clip(cos_i, 0, None)

        return irradiance
        





