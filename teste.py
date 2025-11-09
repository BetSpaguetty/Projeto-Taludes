import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PyQt5.QtWidgets import QApplication
from skimage.measure import find_contours

# >>> Crie o QApplication antes de qualquer QWidget <<<
app = QApplication([])

# --- Dados ---
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# --- Janela 3D ---
w = gl.GLViewWidget()
w.show()
w.setWindowTitle("Superfície com Contornos")
w.setCameraPosition(distance=30)

# --- Superfície colorida ---
surface = gl.GLSurfacePlotItem(
    x=x, y=y, z=Z,
    shader='heightColor',
    computeNormals=False,
)
w.addItem(surface)

# --- Contornos com find_contours ---
levels = np.linspace(Z.min(), Z.max(), 10)
for lvl in levels:
    contours = find_contours(Z, lvl)
    for c in contours:
        xi = np.interp(c[:, 1], [0, Z.shape[1]], [x.min(), x.max()])
        yi = np.interp(c[:, 0], [0, Z.shape[0]], [y.min(), y.max()])
        zi = np.full_like(xi, lvl)
        line = np.column_stack((xi, yi, zi))
        w.addItem(gl.GLLinePlotItem(pos=line, color=(1, 1, 1, 1), width=1))

# --- Loop principal ---
app.exec_()

  