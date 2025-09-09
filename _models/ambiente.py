from Taludes.presets import *
from Taludes.types import *
from Taludes.taludes import *
from PIL import Image
import pyvista as pv
import numpy as np


class Ambiente :


    def __init__(self):
        self.L = 25
        self.LD = np.sqrt(2) * self.L
        self.filename : str = None
        self.matriz   : np.ndarray = None
        self.fos      : np.ndarray = None
        self.nLinhas  : int = None
        self.nColunas : int = None
        self.mLinhas  : np.ndarray = None
        self.mColunas : np.ndarray = None
        self._configurtion()


    def _configurtion(self) :
        pass


    def uploadFile(self, filepath) :
        self.filename = filepath
        self.matriz, self.nLinhas, self.nColunas = self.openTifFile(filepath)
        self.matriz = np.transpose(self.matriz)
        self.mLinhas, self.mColunas = self.createGrid(self.nLinhas, self.nColunas)

    def openTifFile(self, filename) :
        img = Image.open(filename)
        matriz = np.array(img)
        nLinhas  = matriz.shape[0]
        nColunas = matriz.shape[1]
        return matriz, nLinhas, nColunas

    def createGrid(self, nLinhas, nColunas) :
        coluna = np.linspace(1, nLinhas, nLinhas)
        linha  = np.linspace(1, nColunas, nColunas)
        mLinhas, mColunas = np.meshgrid(linha, coluna) 
        return mLinhas, mColunas



    def calculateFos(self, h, hw, c, phi, thetai, fosfunc) :
        self.fos = calculateFos(self.matriz, self.nLinhas, self.nColunas, h, hw, c, phi, thetai, self.L, self.LD, fosfunc)
        return self.fos

 
    def calculateHW(self, material, p, t, h, thetai) :
        return calculateHW(material, p, t, h, thetai)
    

