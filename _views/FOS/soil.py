from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from __DDCores.base import *
import numpy as np
import pyqtgraph as pg

from Filtros.Taludes.presets import *
from Filtros.Taludes.taludes import *

class SoilView(DDWidget) :

    def __init__(self):
        super().__init__()

        self._view()
        self.properties()
        self.association()


    def _view(self) : 
        self.setFixedHeight(400)
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setContentsMargins(2,2,2,2)
        self.mainBoxLayout.setSpacing(5)
        self.mainBoxLayout.setAlignment(Qt.AlignTop)
        self.mainBox.setObjectName('soil')
        self.mainBox.setLayout(self.mainBoxLayout)
        self.labelTitle = QLabel('Soil')
        self.labelTitle.setObjectName('labelTitle')
        self.mainBoxLayout.addWidget(self.labelTitle, alignment=Qt.AlignCenter)
        self.spinsLayout = QHBoxLayout()
        self.spinsLayout.setContentsMargins(0,0,0,0)
        self.spinsLayout.setSpacing(0)
        self.mainBoxLayout.addLayout(self.spinsLayout)
        # Edits
        self.editClay = self.addSpin('Clay')
        self.editSand = self.addSpin('Sand')
        self.editSilt = self.addSpin('Silt', readOnly=True)
        # Soil Selector
        self.comboSoil = QComboBox()
        self.mainBoxLayout.addWidget(self.comboSoil, alignment=Qt.AlignHCenter)
        # Ternary Triangle
        self.ternaryTriangle = TernaryPlotWidget()
        self.ternaryTriangle.setMaximumHeight(400)
        self.mainBoxLayout.addWidget(self.ternaryTriangle, alignment=Qt.AlignTop)
        self.setStyleSheet(QSS)

    def addSpin(self, title, readOnly=False) -> QSpinBox :
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
    
    def plot(self) :
        clay = self.getClay()
        sand = self.getSand()
        silt = self.getSilt()
        self.ternaryTriangle.plot_point(clay, sand, silt)

    def properties(self) : 
        self.soilValues = []
        self.soilIndex  = {}
        self.indexSoil  = []


    def association(self) :
        self.editClay.valueChanged.connect( lambda : self.updateSpins('CLAY') )
        self.editSand.valueChanged.connect( lambda : self.updateSpins('SAND') )
        id = 0
        for soil, values in DEFAULT_SOILS.items() : 
            self.comboSoil.addItem(soil.value)
            self.soilValues.append(values)
            self.soilIndex[soil] = id
            self.indexSoil.append(soil)
            id+=1
        self.comboSoil.currentIndexChanged.connect(self.functionComboBoxSolo)


    def setSilt(self, silt:int) :
        self.editSilt.setValue(silt)
    
    def setSand(self, sand:int) :
        self.editSand.setValue(sand)

    def setClay(self, clay:int) :
        self.editClay.setValue(clay)

    def getSilt(self) : 
        return self.editSilt.value()
    
    def getSand(self) : 
        return self.editSand.value()
    
    def getClay(self) : 
        return self.editClay.value()


    def updateSpins(self, editor:str) :
        self.editClay.blockSignals(True)
        self.editSand.blockSignals(True)
        self.editSilt.blockSignals(True)
        if editor == 'CLAY' : 
            second = self.editSand
        if editor == 'SAND' : 
            second = self.editClay
        total = self.editClay.value() + self.editSand.value() + self.editSilt.value()
        sobra = total - 100
        silt = self.editSilt.value()
        silt += sobra * -1        
        soil = second.value()
        if silt < 0 :
            soil += silt 
            silt = 0
        if silt > 100 :
            soil += (silt - 100) * -1
            silt = 100
        second.setValue(soil)
        self.editSilt.setValue(silt)
        self.functionSpinSolo()
        self.plot()
        self.editClay.blockSignals(False)
        self.editSand.blockSignals(False)
        self.editSilt.blockSignals(False)



    def defineSoil(self) :
        clay = self.getClay()
        sand = self.getSand()
        silt = self.getSilt()
        soil = Taludes.getSoilType(clay, sand, silt)
        return soil



    def setValues(self, index) :
        values = self.soilValues[index]
        clay = values['clay']
        sand = values['sand']
        self.setSand(sand)
        self.setClay(clay)



    def functionComboBoxSolo(self, index) : 
        values = self.soilValues[index]
        clay = values['clay']
        sand = values['sand']
        silt = values['silt']
        self.editClay.blockSignals(True)
        self.editSand.blockSignals(True)
        self.editSilt.blockSignals(True)
        self.setSand(sand)
        self.setClay(clay)
        self.setSilt(silt)
        self.editClay.blockSignals(False)
        self.editSand.blockSignals(False)
        self.editSilt.blockSignals(False)
        self.plot()

    

    def functionSpinSolo(self) : 
        soil = self.defineSoil()
        index = self.soilIndex[soil]
        self.comboSoil.blockSignals(True)
        self.comboSoil.setCurrentIndex(index)
        self.comboSoil.blockSignals(False)


    def getSolo(self) : 
        return self.indexSoil[self.comboSoil.currentIndex()]

# --------------------------------------------------------------------------------------------------------------------------------------------------- >>>

class TernaryPlotWidget(pg.PlotWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Configura o triângulo equilátero (CLAY, SAND, SILT)
        self.setAspectLocked(True)
        self.hideAxis('left')
        self.hideAxis('bottom')

        # Desenha triângulo
        triangle = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2], [0, 0]])
        self.plot(triangle[:, 0], triangle[:, 1], pen=pg.mkPen('w', width=2))

        # Rótulos
        self.textItems = []
        self.textItems.append(pg.TextItem("SAND", anchor=(0.5, 0)))
        self.textItems.append(pg.TextItem("CLAY", anchor=(0.5, 1)))
        self.textItems.append(pg.TextItem("SILT", anchor=(1, 0.5)))
        self.addItem(self.textItems[0])
        self.addItem(self.textItems[1])
        self.addItem(self.textItems[2])

        self.textItems[0].setPos(0.0,  0.0)
        self.textItems[1].setPos(0.5, np.sqrt(3)/2 + 0.05)
        self.textItems[2].setPos(1.05, -0.05)

        # Cria scatter vazio
        self.scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush('r'))
        self.addItem(self.scatter)

    def ternary_to_cartesian(self, clay, sand, silt):
        """Converte (clay, sand, silt) -> coordenadas cartesianas"""
        total = clay + sand + silt
        if total == 0:
            return 0, 0
        x = (sand + silt/2) / total
        y = (np.sqrt(3)/2) * (silt / total)
        return x, y

    def plot_point(self, clay, sand, silt):
        x, y = self.ternary_to_cartesian(sand, silt, clay)
        self.scatter.setData([x], [y])





QSS = """


#soil {
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
