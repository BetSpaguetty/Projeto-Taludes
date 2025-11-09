from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import pyplot as plt
import numpy as np
import sys

class MatplotlibColorbar(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        fig, ax = plt.subplots(figsize=(1, 4))
        fig.subplots_adjust(left=0.5, right=0.7)

        cmap = plt.get_cmap("viridis")
        norm = plt.Normalize(vmin=0, vmax=100)
        fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=ax)

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MatplotlibColorbar()
    win.show()
    sys.exit(app.exec_())
