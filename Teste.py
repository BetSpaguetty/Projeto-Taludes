import sys
import numpy as np
from pyqtgraph.Qt import QtWidgets
import pyqtgraph as pg

app = QtWidgets.QApplication(sys.argv)

# Criar o stack de imagens (10 imagens 100x100)
stack = np.random.rand(10, 100, 100)

# Criar ImageView
win = pg.ImageView()
win.setImage(stack)  # passa o stack 3D

win.show()
sys.exit(app.exec_())
