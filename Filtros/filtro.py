
from PyQt5.QtWidgets import QWidget


class Filter : 


    def __init__(self, matrixElevation):
        self.matrixElevation = matrixElevation
        self.properties()



    def properties(self) : 
        self.callbackFunction = None
        self.scale = None
        self.matrixFilter = None
        self.views = {}

    def addView(self, name:str, viewList:list[QWidget]): 
        self.views[name] = viewList




    def connectReceptor(self, function) : 
        self.callbackFunction = function

    def sendCallback(self, matrix) : 
        self.callbackFunction(matrix)

    def sendMatrix(self) : 
        raise NotImplementedError('Not implemented!')

    def calculateMatrix(self) : 
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


