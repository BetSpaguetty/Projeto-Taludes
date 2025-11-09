from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QColor
import numpy as np
import sys

class ColorBar(QWidget):
    def __init__(self, cmap="jet", n=256):
        super().__init__()
        layout = QVBoxLayout(self)

        # Gera gradiente vertical
        data = np.linspace(0, 1, n)
        img = np.zeros((n, 1, 3), dtype=np.uint8)

        # Colormap (aqui exemplo manual de azul → vermelho)
        img[:, 0, 0] = (data * 255).astype(np.uint8)          # R
        img[:, 0, 2] = (255 - data * 255).astype(np.uint8)    # B

        qimg = QImage(img, 1, n, 3, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg).scaled(40, 256)

        label = QLabel()
        label.setPixmap(pixmap)
        layout.addWidget(label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ColorBar()
    win.show()
    sys.exit(app.exec_())