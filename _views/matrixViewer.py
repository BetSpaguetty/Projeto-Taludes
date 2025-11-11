from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from __DDCores.base  import *
from __DDCores.components.matrixGL  import *
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import pyqtgraph.opengl as gl
import pyqtgraph as pg
from PIL import Image


class MatrixViewer(MatrixGLWidget) :

    def __init__(self):
        super().__init__()
       
 


    # MATRIX FILTER ------------------------------------------------------------------------------- >>>

    def saveMatrix(self,  matrixFilter:np.ndarray, matrixElevation:np.ndarray=None, vX:np.ndarray=None, vY:np.ndarray=None) :
        self.matrixFilter = matrixFilter
        self.matrixElevation = matrixElevation
        if vX is not None : self.vectorX = vX 
        if vY is not None : self.vectorY = vY


    def renderMatrix(self, matrixFilter, *args) : 
        self.ploted = True
        self.saveMatrix(matrixFilter, *args)
        self.renderFunction(matrixFilter, *args)


    def autoRender(self) :
        if self.ploted :  
            self.renderMatrix(self.matrixFilter, self.matrixElevation, self.vectorX, self.vectorY)


    def renderMatrix3D(self, matrixFilter, matrixElevation=None, vectorX=None, vectorY=None) :
        colors = self.getColorMap(matrixFilter, TO1D=True)
        self.matrixItem3D.setData(x=vectorY, y=vectorX, z=matrixElevation, colors=colors)
 


    def renderMatrix2D(self, matrixFilter, *args) :
        colors = self.getColorMap(matrixFilter)
        self.matrixItem2D.setImage(colors)



    def imageToMatrix(self, img:str, TO1D = False) : 
        image = Image.open(img).convert("RGBA") 
        matriz = np.array(image, dtype=np.float32)
        if TO1D : matriz = matriz.reshape(-1, 4)
        return matriz



    def getColorMap(self, matrix:np.ndarray, TO1D = False) :
        if TO1D : matrix = matrix.flatten()
        # Color map
        if self.listColors is None : cmap = cm.get_cmap(self.colorMap)
        else : cmap = mcolors.ListedColormap(self.listColors)
        # Normalização
        if self.listBounds is None : norm = mcolors.Normalize(vmin=np.min(matrix), vmax=np.max(matrix))
        else : norm = mcolors.BoundaryNorm(boundaries=self.listBounds, ncolors=cmap.N)
        # Cores
        colorMap = cmap(norm(matrix))

        colorMap[..., -1] = self.transparency 
        self.colorbar.setColorMap(cmap, norm)
        return colorMap


    def cleanViewer3D(self) :
        for item in self.viewWidget3D.items :
            self.viewWidget3D.removeItem(item)


    def addImage(self) : 
        pass


    # MATRIX CONFIG ------------------------------------------------------------------------------- >>>

    def setViewer2D(self) :
        self.viewMode = '2D'
        self.ViewWidget2D.setVisible(True)
        self.viewWidget3D.setVisible(False) 
        self.renderFunction = self.renderMatrix2D
        self.autoRender()

    def setViewer3D(self) :
        self.viewMode = '3D'
        self.ViewWidget2D.setVisible(False)
        self.viewWidget3D.setVisible(True)
        self.renderFunction = self.renderMatrix3D
        self.autoRender()



    def setMatrixShader(self, shader:str) : 
        if shader == 'None' : shader = None
        self.matrixItem3D.setShader(shader)

    def setMatrixSmooth(self, smooth:bool) : 
        self.matrixItem3D.opts['smooth'] = smooth
        self.autoRender()

    def setMatrixDrawEdges(self, a0:bool) : 
        self.matrixItem3D.opts['drawEdges'] = a0
        self.autoRender()

    def setMatrixDrawFaces(self, a0:bool) : 
        self.matrixItem3D.opts['drawFaces'] = a0
        self.autoRender()

    def setComputeNormals(self, a0:bool) : 
        self.matrixItem3D.opts['computeNormals'] = a0
        self.autoRender()



    def setColorMap(self, colorMap, listColors:list[str] = None, listBounds:list[float] = None ) :
        self.colorMap   = colorMap
        self.listColors = listColors
        self.listBounds = listBounds
        self.autoRender()


    def setOpacity(self, opacity:float=1.0) : 
        self.transparency = opacity
        self.autoRender()

    
    def setLayer(self, img:str) :
        pass


    def setModelTransformations(self, vX:np.ndarray, vY:np.ndarray) :
        self.vectorX = vX 
        self.vectorY = vY 
        self.autoRender()





# =================================================================================================================================================== |||










