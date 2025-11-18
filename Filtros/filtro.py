
from PyQt5.QtWidgets import QWidget
import numpy as np

class Filter : 


    def __init__(self):
        self.properties()



    def properties(self) : 
        self.matrixElevation = None
        self.callbackFunction = lambda *args : None
        self.scale = None
        self.matrixFilter = None
        self.views = {}

    def addView(self, name:str, viewList:list[QWidget]): 
        self.views[name] = viewList



    def connectReceptor(self, function) : 
        self.callbackFunction = function

    def sendMatrix(self) : 
        if self.matrixElevation is None : return
        matrixFilter = self.calculateMatrix()
        self.callbackFunction(matrixFilter)


    def calculateMatrix(self) -> np.ndarray : 
        raise NotImplementedError('Not implemented!')



    def getFilterMatrix(self) : 
        return self.matrixFilter
    
    def setFilterMatrix(self, matrix) : 
        self.matrixFilter = matrix


    def setElevationMatrix(self, matrixElevation) : 
        self.matrixElevation = matrixElevation

    def getElevationMatrix(self) : 
        return self.matrixElevation


    def setScale(self, scale) : 
        self.scale = scale

    def getScale(self) : 
        return self.scale


