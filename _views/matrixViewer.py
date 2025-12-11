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

        self.ploted   = False
        self.showAxis = False
        self.showGrid = False
        self.vars()


    def vars(self) : 
        self.matrixFilter = None

    # MATRIX FILTER ------------------------------------------------------------------------------- >>>

    def renderMatrix(self, matrixFilter) : 
        self.saveMatrix(matrixFilter)
        self.renderFunction(matrixFilter)


    def render(self) :
        if self.ploted and self.matrixFilter is not None: self.renderMatrix(self.matrixFilter)


    def saveMatrix(self,  matrixFilter:np.ndarray) :
        self.matrixFilter = matrixFilter



    def renderMatrix3D(self, matrixFilter) :
        colors = self.getColorMap(matrixFilter, TO1D=True)
        
        self.matrixItem3D.setData(x=self.vectorY, y=self.vectorX, z=self.matrixScale, colors=colors)

    def renderMatrix2D(self, matrixFilter, *args) :
        colors = self.getColorMap(matrixFilter)
        self.matrixItem2D.setImage(colors)



    # CONFIGURATION ------------------------------------------------------------------------------- >>>

    def setMatrixElevation(self,  matrixElevation, vX, vY) : 
        self.ploted = True
        self.matrixElevation = matrixElevation
        self.matrixScale = matrixElevation
        self.vectorX = vX 
        self.vectorY = vY
        self.createAxis()




    # AUX ----------------------------------------------------------------------------------------- >>>

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


    def createAxis(self):
        shape = self.matrixElevation.shape
        w, h = shape[1], shape[0]
        # Comprimento dos eixos
        size_x = w
        size_y = h
        size_z = 20
        # Posição inicial (mesmo deslocamento usado antes)
        off_x = (-w / 2) - 1
        off_y = (-h / 2) - 1
        off_z = -1
        # --- EIXO X (vermelho) ---
        pts_x = np.array([ [0, 0, 0], [size_x, 0, 0] ])
        axis_x = gl.GLLinePlotItem( pos=pts_x, color=(1, 0, 0, 1), width=1, antialias=True )
        axis_x.translate(off_x, off_y, off_z)
        # --- EIXO Y (verde) ---
        pts_y = np.array([ [0, 0, 0], [0, size_y, 0] ])
        axis_y = gl.GLLinePlotItem( pos=pts_y, color=(0, 1, 0, 1), width=1, antialias=True )
        axis_y.translate(off_x, off_y, off_z)
        # --- EIXO Z (azul) ---
        pts_z = np.array([ [0, 0, 0], [0, 0, size_z] ])
        axis_z = gl.GLLinePlotItem( pos=pts_z, color=(0, 0, 1, 1), width=1, antialias=True )
        axis_z.translate(off_x, off_y, off_z)
        # Guarda em uma lista para mostrar/ocultar facilmente
        self.axis = [axis_x, axis_y, axis_z]


    def setRenderAxis(self, a0: bool):
        if a0:
            for axis in self.axis:
                self.viewWidget3D.addItem(axis)
        else:
            for axis in self.axis:
                self.viewWidget3D.removeItem(axis)


    # MATRIX CONFIG ------------------------------------------------------------------------------- >>>

    def setViewer2D(self) :
        self.viewMode = '2D'
        self.viewWidget2D.setVisible(True)
        self.viewWidget3D.setVisible(False) 
        self.renderFunction = self.renderMatrix2D
        self.render()

    def setViewer3D(self) :
        self.viewMode = '3D'
        self.viewWidget2D.setVisible(False)
        self.viewWidget3D.setVisible(True)
        self.renderFunction = self.renderMatrix3D
        self.render()



    def setMatrixShader(self, shader:str) : 
        if shader == 'None' : shader = None
        self.matrixItem3D.setShader(shader)

    def setMatrixSmooth(self, smooth:bool) : 
        self.matrixItem3D.opts['smooth'] = smooth
        self.render()

    def setMatrixDrawEdges(self, a0:bool) : 
        self.matrixItem3D.opts['drawEdges'] = a0
        self.render()

    def setMatrixDrawFaces(self, a0:bool) : 
        self.matrixItem3D.opts['drawFaces'] = a0
        self.render()

    def setComputeNormals(self, a0:bool) : 
        self.matrixItem3D.opts['computeNormals'] = a0
        self.render()


    def setMatrixBackgroundColor(self, color:str):
        self.viewWidget3D.setBackgroundColor(color)
        self.viewWidget2D.setBackground(color)


    def setColorMap(self, colorMap, listColors:list[str] = None, listBounds:list[float] = None ) :
        self.colorMap   = colorMap
        self.listColors = listColors
        self.listBounds = listBounds
        self.render()


    def setOpacity(self, opacity:float=1.0) : 
        self.transparency = opacity
        self.render()


    def setScale(self, scale:int) :
        self.matrixScale = self.matrixElevation / scale
        self.render()





# =================================================================================================================================================== |||










