import rasterio
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

# --- Abrir o GeoTIFF ---
with rasterio.open("DATA/mapa1.tif") as src:
    img = src.read(1)  # lê só a primeira banda (2D)

print(img)
# --- Criar app do PyQtGraph ---
app = QtGui.QGuiApplication([])

win = pg.GraphicsLayoutWidget()
view = win.addViewBox()
view.setAspectLocked(True)  # mantém proporção

# --- Criar ImageItem ---
img_item = pg.ImageItem(img)
view.addItem(img_item)

win.show()
app.exec_()