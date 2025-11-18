import tifffile
import numpy as np


class Mapa :


    def __init__(self, filepath:str, scale:int=25):
        self._properties()
        self.setTiff(filepath, scale)


    def _properties(self) :
        self.filepath  : str = None
        self.tif       : tifffile.TiffFile = None
        self.matrices  : list[np.ndarray] = []
        self.lenPages  : int = None
        self.vX        : np.ndarray = None
        self.vY        : np.ndarray = None
        self.scale     : int = None
        self.subLayers : dict = {}


    # Usa a matriz e escala setados
    def _createXYScaleVector(self) : 
        Z = self.getElevationMatrix()
        self.vX = np.arange( -(Z.shape[1]//2), (Z.shape[1]//2) )
        self.vY = np.arange( -(Z.shape[0]//2), (Z.shape[0]//2) )


    def _createMatrices(self, tif:tifffile.TiffFile) :
        for page in tif.pages :
            matrix = page.asarray()
            self.matrices.append(matrix)


    def setTiff(self, filepath : str, scale : int = 25) :
        self.filepath = filepath
        self.tif      = tifffile.TiffFile(filepath)
        self.lenPages = len(self.tif.pages)
        self._createMatrices(self.tif)
        self.setScale(scale)


    def setScale(self, scale:int) :
        self.scale = scale
        self._createXYScaleVector()



    # GETTERS ------------------------------------------------------------------------------------- >>>

    def getAllPages(self) :
        return self.tif.pages
        
    def getMainPage(self) : 
        return self.tif.pages[0]

    def getPage(self, id) : 
        return self.tif.pages[id]
    

    def getAllMatrices(self) -> list[np.ndarray]:
        return self.matrices

    def getElevationMatrix(self) -> np.ndarray: 
        return self.matrices[0]

    def getMatrix(self, id:int) -> np.ndarray :
        return self.matrices[id]


    def getScale(self) : 
        return self.scale

    def getXYScaleVector(self) :
        return self.vX, self.vY

    def getXScaleVector(self) : 
        return self.vX

    def getYScaleVector(self) : 
        return self.vY

