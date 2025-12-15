
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

    def addView(self, name:str, view:QWidget): 
        self.views[name] = view


    def calculateMatrix(self) -> np.ndarray : 
        raise NotImplementedError('Not implemented!')

    def connectReceptor(self, function) : 
        self.callbackFunction = function

    def sendMatrixToReceptor(self) : 
        if self.matrixElevation is None : return
        matrixFilter = self.calculateMatrix()
        self.callbackFunction(matrixFilter)



    def getFilterMatrix(self) : 
        return self.matrixFilter
    
    def setFilterMatrix(self, matrix) : 
        self.matrixFilter = matrix


    def setElevationMatrix(self, matrixElevation) : 
        self.matrixElevation = matrixElevation

    def getElevationMatrix(self) : 
        return self.matrixElevation




