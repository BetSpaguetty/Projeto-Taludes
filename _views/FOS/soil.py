from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from __DDCores.base import *
import numpy as np
import pyqtgraph as pg

from Filtros.FOS.presets import *
from Filtros.FOS.taludes import *

class SoilView(DDWidget) :

    def __init__(self):
        super().__init__()
        self._vars()
        self._UI()
        self._initialization()
        

    def _vars(self) :   
        self.solo = Soils.COARSE
        self.solos = {}
        for SOLO, VALS in DEFAULT_SOILS.items() : self.solos[SOLO.value] = VALS
        self.callbackfuntion = None


    def onChange(self, function) : 
        self.callbackfuntion = function

    def _UI(self) : 
        self.mainBox.setObjectName('mainBox')
        self.setFixedHeight(400)
        # Main box layout
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setContentsMargins(2,2,2,2)
        self.mainBoxLayout.setSpacing(5)
        self.mainBoxLayout.setAlignment(Qt.AlignTop)
        self.mainBox.setLayout(self.mainBoxLayout)
        # Titulo
        self.labelTitle = QLabel('Soil')
        self.labelTitle.setObjectName('labelTitle')
        self.mainBoxLayout.addWidget(self.labelTitle, alignment=Qt.AlignCenter)
        # Layout dos spins
        self.spinsLayout = QHBoxLayout()
        self.spinsLayout.setContentsMargins(0,0,0,0)
        self.spinsLayout.setSpacing(0)
        self.mainBoxLayout.addLayout(self.spinsLayout)
        # Edits
        self.spinClay = self.createAddSpin('Clay')
        self.spinSand = self.createAddSpin('Sand')
        self.spinSilt = self.createAddSpin('Silt', readOnly=True)
        self.spinClay.valueChanged.connect( lambda : self.updateSpins('CLAY') )
        self.spinSand.valueChanged.connect( lambda : self.updateSpins('SAND') )

        # Soil Selector
        self.comboBoxSoil = QComboBox()
        self.mainBoxLayout.addWidget(self.comboBoxSoil, alignment=Qt.AlignHCenter)
        for SOLO, VALS in self.solos.items() : 
            self.comboBoxSoil.addItem(SOLO)
        self.comboBoxSoil.currentTextChanged.connect(self.setSoilByComboBox)

        # Ternary Triangle
        self.ternaryTriangle = TernaryPlotWidget()
        self.ternaryTriangle.setMaximumHeight(400)
        self.mainBoxLayout.addWidget(self.ternaryTriangle, alignment=Qt.AlignTop)
        self.setStyleSheet(QSS)


    def _initialization(self) : 
        self.comboBoxSoil.setCurrentIndex(1)


    def createAddSpin(self, title, readOnly=False) -> QSpinBox :
        box = QWidget()
        layout = QVBoxLayout()
        box.setLayout(layout)
        label = QLabel(title)
        label.setObjectName('labelSoil')
        spinBox = QSpinBox()
        spinBox.lineEdit().setReadOnly(readOnly)
        spinBox.setMinimum(0)
        spinBox.setMaximum(100)
        spinBox.setObjectName('spinSoil')
        spinBox.setMinimumWidth(50)
        spinBox.setReadOnly(readOnly)
        layout.addWidget(label)
        layout.addWidget(spinBox)
        self.spinsLayout.addWidget(box)
        return spinBox
    


    def setSoilByComboBox(self, value: str) : 
        solo = self.solos[value]
        sand = solo['sand']
        silt = solo['silt']
        clay = solo['clay']
        self.setSand(sand)
        self.setSilt(silt)
        self.setClay(clay)
        self.plot()
        if self.callbackfuntion: self.callbackfuntion()


    def updateSpins(self, editor:str) :
        self.spinClay.blockSignals(True)
        self.spinSand.blockSignals(True)
        self.spinSilt.blockSignals(True)
        if editor == 'CLAY' : second = self.spinSand
        if editor == 'SAND' : second = self.spinClay
        total = self.spinClay.value() + self.spinSand.value() + self.spinSilt.value()
        sobra = total - 100
        silt = self.spinSilt.value()
        silt += sobra * -1        
        soil = second.value()
        if silt < 0 :
            soil += silt 
            silt = 0
        if silt > 100 :
            soil += (silt - 100) * -1
            silt = 100
        second.setValue(soil)
        self.spinSilt.setValue(silt)
        self.plot()
        self.spinClay.blockSignals(False)
        self.spinSand.blockSignals(False)
        self.spinSilt.blockSignals(False)

        self.comboBoxSoil.blockSignals(True)
        self.comboBoxSoil.setCurrentText(self.getSoil().value)
        self.comboBoxSoil.blockSignals(False)


        if self.callbackfuntion: self.callbackfuntion()







    def plot(self) :
        clay = self.getClay()
        sand = self.getSand()
        silt = self.getSilt()
        self.ternaryTriangle.plot_point(clay, sand, silt)


    def setSilt(self, silt:int) :
        self.spinSilt.blockSignals(True)
        self.spinSilt.setValue(silt)
        self.spinSilt.blockSignals(False)
    
    def setSand(self, sand:int) :
        self.spinSand.blockSignals(True)
        self.spinSand.setValue(sand)
        self.spinSand.blockSignals(False)

    def setClay(self, clay:int) :
        self.spinClay.blockSignals(True)
        self.spinClay.setValue(clay)
        self.spinClay.blockSignals(False)


    def getSilt(self) : 
        return self.spinSilt.value()
    
    def getSand(self) : 
        return self.spinSand.value()
    
    def getClay(self) : 
        return self.spinClay.value()


    def getSoil(self) -> Soils : 
        return Taludes.getSoilType(self.getClay(), self.getSand(), self.getSilt())








# --------------------------------------------------------------------------------------------------------------------------------------------------- >>>
class TernaryPlotWidget(pg.PlotWidget):

    SQRT3_2 = np.sqrt(3) / 2

    def __init__(self, parent=None):
        super().__init__(parent)
        self._configure_plot()
        self._draw_triangle()
        self._add_labels()
        self._create_scatter()


    def _configure_plot(self):
        self.setAspectLocked(True)
        self.hideAxis("left")
        self.hideAxis("bottom")


    def _draw_triangle(self):
        triangle = np.array([
            [0, 0],
            [1, 0],
            [0.5, self.SQRT3_2],
            [0, 0]
        ])
        self.plot(triangle[:, 0], triangle[:, 1], pen=pg.mkPen("w", width=2))

    def _add_labels(self):
        labels = {
            "SAND": (0.0, 0.0),
            "CLAY": (0.5, self.SQRT3_2 + 0.05),
            "SILT": (1.05, -0.05)
        }

        for text, pos in labels.items():
            item = pg.TextItem(text)
            item.setPos(*pos)
            self.addItem(item)

    def _create_scatter(self):
        self.scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush("r"))
        self.addItem(self.scatter)


    @staticmethod
    def ternary_to_cartesian(clay, sand, silt):
        total = clay + sand + silt
        if total == 0:
            return 0.0, 0.0

        x = (sand + silt / 2) / total
        y = TernaryPlotWidget.SQRT3_2 * (silt / total)
        return x, y


    def plot_point(self, clay, sand, silt):
        x, y = self.ternary_to_cartesian(clay, sand, silt)
        self.scatter.setData([x], [y])




QSS = """


#mainBox {
    border: 1px solid #606060;
    border-radius: 5px;
    background-color: black;

}


#labelMaterial {
    color: white;

}

#lineEditMaterial {

}

QSpinBox {
    selection-background-color: #808080;
    }



QSpinBox:focus {
    border: 1px solid #007acc;
    background-color: black;
    color: white;
    }


#labelSoil {
    color:white;

}

#lineSoil {
    height: 20px;
    text-align: center;
    font-size: 14px;
    font-weight: 500;
    border-radius: 10px;
    padding: 5px;

}

"""
