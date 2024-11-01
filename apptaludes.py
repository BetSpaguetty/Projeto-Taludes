# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog,QDialog
from PyQt5.uic import loadUi

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_AppTaludes

class AppTaludes(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AppTaludes()
        self.ui.setupUi(self)
        loadUi("form.ui",self)
        self.ClearBtn.clicked.connect(self.browsefiles)

    def browsefiles(self):
        fname=QFileDialog.getOpenFileName(self,"Open file",'C:','PNG files (*.png)')
        self.filename.setText(fname[0])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = AppTaludes()
    widget.show()
    sys.exit(app.exec_())
