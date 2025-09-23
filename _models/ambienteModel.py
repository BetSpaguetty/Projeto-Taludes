from Taludes.presets import *
from Taludes.types import *
from Taludes.taludes import *
from PIL import Image
import pyvista as pv
import numpy as np
import tifffile

class AmbienteModel :


    def __init__(self):
        self.L = 25
        self.LD = np.sqrt(2) * self.L
        self.fos      : np.ndarray = None



    def calculateFos(self, h, hw, c, phi, thetai, fosfunc) :
        self.fos = calculateFos(self.matriz, self.nLinhas, self.nColunas, h, hw, c, phi, thetai, self.L, self.LD, fosfunc)
        return self.fos

 
    def calculateHW(self, material, p, t, h, thetai) :
        return calculateHW(material, p, t, h, thetai)
    








