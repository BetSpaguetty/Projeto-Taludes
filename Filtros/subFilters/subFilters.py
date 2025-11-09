import numpy as np
from scipy.ndimage import uniform_filter

# ============================================================
# 1. Gradientes básicos (derivadas em x e y)
# ============================================================
def gradientes(dem, cellsize=1.0):
    dzdx = (np.roll(dem, -1, axis=1) - np.roll(dem, 1, axis=1)) / (2 * cellsize)
    dzdy = (np.roll(dem, -1, axis=0) - np.roll(dem, 1, axis=0)) / (2 * cellsize)
    return dzdx, dzdy


# ============================================================
# 2. Declividade (em graus)
# ============================================================
def declividade(dem, cellsize=1.0):
    dzdx, dzdy = gradientes(dem, cellsize)
    slope = np.degrees(np.arctan(np.hypot(dzdx, dzdy)))
    return slope


# ============================================================
# 3. Orientação (aspecto, em graus 0–360)
# ============================================================
def orientacao(dem, cellsize=1.0):
    dzdx, dzdy = gradientes(dem, cellsize)
    aspect = np.degrees(np.arctan2(dzdy, -dzdx))
    aspect = np.mod(450.0 - aspect, 360.0)
    return aspect


# ============================================================
# 4. Hillshade (sombreamento)
# ============================================================
def hillshade(dem, azimuth=315, altitude=45, cellsize=1.0):
    dzdx, dzdy = gradientes(dem, cellsize)
    slope = np.arctan(np.hypot(dzdx, dzdy))
    aspect = np.arctan2(dzdy, -dzdx)
    az = np.radians(azimuth)
    alt = np.radians(altitude)
    hs = (np.cos(alt) * np.cos(slope)) + (np.sin(alt) * np.sin(slope) * np.cos(az - aspect))
    return (hs - hs.min()) / (hs.max() - hs.min())


# ============================================================
# 5. Curvatura (segunda derivada)
# ============================================================
def curvatura(dem, cellsize=1.0):
    dzdx, dzdy = gradientes(dem, cellsize)
    d2zdx2 = (np.roll(dzdx, -1, axis=1) - np.roll(dzdx, 1, axis=1)) / (2 * cellsize)
    d2zdy2 = (np.roll(dzdy, -1, axis=0) - np.roll(dzdy, 1, axis=0)) / (2 * cellsize)
    curv = d2zdx2 + d2zdy2
    return curv


# ============================================================
# 6. Rugosidade (desvio padrão local)
# ============================================================
def rugosidade(dem, size=3):
    mean = uniform_filter(dem, size)
    mean_sq = uniform_filter(dem**2, size)
    rug = np.sqrt(np.maximum(0, mean_sq - mean**2))
    return rug


# ============================================================
# 7. TPI (Topographic Position Index)
# ============================================================
def tpi(dem, size=5):
    mean = uniform_filter(dem, size)
    return dem - mean


# ============================================================
# 8. Alívio local (diferença máx - mín local)
# ============================================================
def alivio_local(dem, size=5):
    from scipy.ndimage import maximum_filter, minimum_filter
    max_local = maximum_filter(dem, size)
    min_local = minimum_filter(dem, size)
    return max_local - min_local


# ============================================================
# 9. Normalização simples (para criar mapa de cores)
# ============================================================
def normalizar(matriz):
    m_min, m_max = np.nanmin(matriz), np.nanmax(matriz)
    return (matriz - m_min) / (m_max - m_min)
