# Módulos

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog, QPushButton, QGraphicsView, QLineEdit, QLabel, QGridLayout

import scipy as sp
from scipy.ndimage import gaussian_filter

import numpy as np
from PIL import Image
# import rasterio

import matplotlib.cm as cm
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg  import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from sys import argv, exit, path

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("C:\\Users\\betsabenogueira\\Documents\\Visualizador de tiff\\Projeto-Taludes\\betsabe\\open_tif_2.ui",self)
        self.pushButton = self.findChild(QPushButton,"botao_abrir_arquivo")
        self.graphicsView = self.findChild(QGraphicsView,"frame_exibicao_elevacao")
        self.exibe_gradiente = self.findChild(QGraphicsView,"frame_exibicao_gradiente")
        self.pushButton2 = self.findChild(QPushButton,"botao_recorte")
        self.intervalo_x_inicio = self.findChild(QLineEdit,"intervalo_x_inicio")
        self.intervalo_x_final = self.findChild(QLineEdit,"intervalo_x_final")
        self.intervalo_y_inicio = self.findChild(QLineEdit,"intervalo_y_inicio")
        self.intervalo_y_final = self.findChild(QLineEdit,"intervalo_y_final")
        self.label_shape = self.findChild(QLabel,"label_shape")

        self.setLayout(self.findChild(QGridLayout,"Layout_Principal"))

        # Cria uma cena para o QGraphicsView
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.scene_gradiente = QGraphicsScene()
        self.exibe_gradiente.setScene(self.scene_gradiente)

        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.exibe_gradiente.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.exibe_gradiente.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.show()


    def ler_arquivo(self):
         # Abre uma janela de diálogo para selecionar um arquivo .tif
        self.caminho_do_arquivo, filtro = QFileDialog.getOpenFileName(None, "Selecione um arquivo TIF", "", "Arquivos TIF (*.tif);;Todos os arquivos (*)")
        self.gera_elevacoes(self.caminho_do_arquivo)
        self.gera_gradiente(self.caminho_do_arquivo)
        print(self.caminho_do_arquivo)
    
    def gera_elevacoes(self,arquivo):
        img = Image.open(arquivo)
        self.img_array = np.array(img)
        # self.img_array = self.img_array[3500:3600,900:1000]
        # self.img_array = self.img_array[:,:] # corte na exibição do tif

        y_ratio, x_ratio = img.size
        lin_x = np.linspace(0, 1, self.img_array.shape[0], endpoint=False)
        lin_y = np.linspace(0, 1, self.img_array.shape[1], endpoint=False)
        y, x = np.meshgrid(lin_y, lin_x)
        z = self.img_array

        sigma_y = 100
        sigma_x = 100
        sigma = [sigma_y, sigma_x]
        z_smoothed = sp.ndimage.gaussian_filter(z, sigma)

        # z_smoothed_min = np.amin(z_smoothed)
        # z_smoothed_max = np.amax(z_smoothed)
        # z_range = z_smoothed_max - z_smoothed_min

        # Creating figure
        self.fig = plt.figure(figsize=(12,10))
        ax = plt.axes(projection='3d')
        ax.azim = -30
        ax.elev = 42
        ax.set_box_aspect((x_ratio,y_ratio,((x_ratio+y_ratio)/8)))
        surf = ax.plot_surface(x,y,z, cmap='terrain', edgecolor='none')


        m = cm.ScalarMappable(cmap=surf.cmap, norm=surf.norm)
        m.set_array(z_smoothed)

        # cbar =  self.fig.colorbar(m, ax=ax, shrink=0.5, aspect=20, ticks=[z_smoothed_min, 0, (z_range * 0.25 + z_smoothed_min), (z_range * 0.5 + z_smoothed_min), (z_range * 0.75 + z_smoothed_min), z_smoothed_max])
        # cbar.ax.set_yticklabels([f'{z_smoothed_min}', ' ',  f'{(z_range*0.25+z_smoothed_min)}', f'{(z_range*0.5+z_smoothed_min)}', f'{(z_range*0.75+z_smoothed_min)}', f'{z_smoothed_max}'])

        plt.xticks([])  # disabling xticks
        plt.yticks([])  # disabling yticks

        self.fig.tight_layout()

        # Cria uma figura e um canvas para o gráfico
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.setFixedSize(280, 30)

        # redimensiona o gráfico
        size = self.graphicsView.size()
        self.canvas.resize(size)

        # Adiciona o canvas do gráfico à cena
        self.scene.addWidget(self.canvas)
        self.scene.addWidget(self.toolbar)
        self.label_shape.setText(f"Shape: {self.img_array.shape}") # exibe o as dimensões do tif
        print(f"função abrir arquivo com tamanho {self.img_array.shape} funcionou")

    def corta_tif(self):
        # Definir os índices para recortar
        recorte = self.img_array[ int(self.intervalo_x_inicio.text()):int(self.intervalo_x_final.text()),int(self.intervalo_y_inicio.text()):int(self.intervalo_y_final.text())]

        # Converter o array NumPy de volta para um objeto de imagem PIL
        recorte_img = Image.fromarray(recorte)

        # Salvar o recorte como um novo arquivo TIFF
        recorte_img.save('recorte_arquivo.tif')

        self.gera_elevacoes('recorte_arquivo.tif')
        self.gera_gradiente('recorte_arquivo.tif')

        print("Recorte realizado com sucesso!")

    def volta_tif(self):
        self.gera_elevacoes(self.caminho_do_arquivo)
        self.gera_gradiente(self.caminho_do_arquivo)

    def gera_gradiente(self,arquivo):
        # Abrir o arquivo TIFF e extrair a matriz de elevações
        tif_file = arquivo
        with rasterio.open(tif_file) as src:
            matriz = src.read(1)  # banda de elevações

        L = 25  # quantidade de metros por pixel
        
        incl_max = np.zeros(matriz.shape) # calcula o gradiente máximo
    
        for i in range(1, matriz.shape[0] - 1):
            for j in range(1, matriz.shape[1] - 1):
                # obtem as diferenças de elevação
                alpha = [
                    np.degrees(np.arctan(abs((matriz[i, j+1] - matriz[i, j]) / L))),
                    np.degrees(np.arctan(abs((matriz[i, j-1] - matriz[i, j]) / L))),
                    np.degrees(np.arctan(abs((matriz[i-1, j] - matriz[i, j]) / L))),
                    np.degrees(np.arctan(abs((matriz[i+1, j] - matriz[i, j]) / L))),
                    np.degrees(np.arctan(abs((matriz[i-1, j+1] - matriz[i, j]) / (L * np.sqrt(2))))),
                    np.degrees(np.arctan(abs((matriz[i-1, j-1] - matriz[i, j]) / (L * np.sqrt(2))))),
                    np.degrees(np.arctan(abs((matriz[i+1, j+1] - matriz[i, j]) / (L * np.sqrt(2))))),
                    np.degrees(np.arctan(abs((matriz[i+1, j-1] - matriz[i, j]) / (L * np.sqrt(2)))))
                ]
                
                # inclinação máxima
                incl_max[i, j] = np.max(alpha)

        self.fig_gradiente = plt.figure(figsize=(10, 5))  

        plt.imshow(incl_max, cmap='viridis')
        plt.colorbar(label='Inclinação Máxima')

        # Cria uma figura e um canvas para o gráfico
        self.canvas_gradiente = FigureCanvas(self.fig_gradiente)
        self.toolbar_gradiente = NavigationToolbar(self.canvas_gradiente)
        self.toolbar_gradiente.setFixedSize(280, 30)

        # Redimensiona o gráfico
        size_1 = self.exibe_gradiente.size()
        self.canvas_gradiente.resize(size_1)
        print(size_1)

        # Adiciona o canvas do gráfico à cena
        self.scene_gradiente.addWidget(self.canvas_gradiente)
        self.scene_gradiente.addWidget(self.toolbar_gradiente)
        print('função do gradiente funcionou')

        # alterar dimensão x,y
        # formatar janela para os widgets aumentarem juntos.
        # tirar informação do relevo do primeiro grafico.




app = QApplication(argv)
UIWindow = UI()
exit(app.exec_())