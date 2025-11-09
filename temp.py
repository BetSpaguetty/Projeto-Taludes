import matplotlib.pyplot as plt
import numpy as np

def calcular_curva_hipsometrica(matriz_elevacao: np.ndarray, n_classes: int = 100):
    """
    Calcula a curva hipsométrica (relação entre área acumulada e elevação).
    
    Parâmetros
    ----------
    matriz_elevacao : np.ndarray
        Matriz 2D com valores de elevação (float ou int).
    n_classes : int, opcional
        Número de classes (bins) para discretização. Padrão = 100.
    
    Retorna
    -------
    elev_norm : np.ndarray
        Elevação normalizada entre 0 e 1 (do mínimo ao máximo).
    area_acumulada : np.ndarray
        Fração acumulada da área (de 0 a 1) correspondente à elevação.
    """
    # Flatten e remove valores NaN
    z = matriz_elevacao.flatten()
    z = z[~np.isnan(z)]

    # Normaliza elevação entre 0 e 1
    z_min, z_max = np.min(z), np.max(z)
    elev_norm = (z - z_min) / (z_max - z_min)

    # Ordena valores
    elev_norm_sorted = np.sort(elev_norm)

    # Calcula fração acumulada da área
    area_acumulada = np.linspace(0, 1, len(elev_norm_sorted))

    # Reduz para número fixo de classes (opcional)
    idx = np.linspace(0, len(elev_norm_sorted) - 1, n_classes).astype(int)
    elev_norm_bins = elev_norm_sorted[idx]
    area_bins = area_acumulada[idx]

    return elev_norm_bins, area_bins
# Exemplo simples
dem = np.array([
    [100, 120, 130, 150],
    [110, 140, 160, 170],
    [115, 145, 155, 165],
    [100, 105, 110, 115]
], dtype=float)

elev, area = calcular_curva_hipsometrica(dem, n_classes=50)

plt.plot(area, elev, color='green')
plt.title("Curva Hipsométrica")
plt.xlabel("Área acumulada (fração)")
plt.ylabel("Elevação normalizada")
plt.grid(True)
plt.show()
