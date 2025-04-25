# Módulos
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMessageBox, QListWidget, QApplication, QMainWindow, QGraphicsScene, QFileDialog, QPushButton, QGraphicsView, QLineEdit, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

import scipy as sp
from scipy.ndimage import gaussian_filter

import numpy as np
from PIL import Image

import rasterio

import matplotlib.cm as cm
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qt5agg  import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from sys import argv, exit, path

# Classes
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("c:\\Users\\paulobaccar\\Downloads\\open_tif_2 (1).ui",self)
        self.pushButton = self.findChild(QPushButton,"botao_abrir_arquivo")
        self.graphicsView = self.findChild(QGraphicsView,"frame_exibicao_elevacao")
        self.exibe_gradiente = self.findChild(QGraphicsView,"frame_exibicao_gradiente")
        self.pushButton2 = self.findChild(QPushButton,"botao_recorte")
        self.intervalo_x_inicio = self.findChild(QLineEdit,"intervalo_x_inicio")
        self.intervalo_x_final = self.findChild(QLineEdit,"intervalo_x_final")
        self.intervalo_y_inicio = self.findChild(QLineEdit,"intervalo_y_inicio")
        self.intervalo_y_final = self.findChild(QLineEdit,"intervalo_y_final")
        self.label_shape = self.findChild(QLabel,"label_shape")
        self.nome_corte = self.findChild(QLineEdit,"nome_arquivo_corte")
        self.label_nome_arquivo = self.findChild(QLabel,"label_nomeArquivo")
        self.label_mapa_rio = self.findChild(QLabel,"label_mapa_rio")
        self.label_coordinates = self.findChild(QLabel,"label_coordinates")

        # bairros RJ
        self.botao_regiao1 = self.findChild(QPushButton,"botao_regiao1")
        self.botao_regiao2 = self.findChild(QPushButton,"botao_regiao2")
        self.botao_regiao3 = self.findChild(QPushButton,"botao_regiao3")
        self.botao_regiao4 = self.findChild(QPushButton,"botao_regiao4")
        self.botao_regiao5 = self.findChild(QPushButton,"botao_regiao5")
        self.botao_regiao6 = self.findChild(QPushButton,"botao_regiao6")
        self.botao_regiao7 = self.findChild(QPushButton,"botao_regiao7")
        self.botao_regiao8 = self.findChild(QPushButton,"botao_regiao8")
        self.botao_regiao9 = self.findChild(QPushButton,"botao_regiao9")
        self.botao_regiao10 = self.findChild(QPushButton,"botao_regiao10")
        self.botao_regiao11 = self.findChild(QPushButton,"botao_regiao11")
        self.botao_regiao12 = self.findChild(QPushButton,"botao_regiao12")
        self.botao_regiao13 = self.findChild(QPushButton,"botao_regiao13")
        self.botao_regiao14 = self.findChild(QPushButton,"botao_regiao14")
        self.botao_regiao15 = self.findChild(QPushButton,"botao_regiao15")

        pixmap = QPixmap("c:\\Users\\paulobaccar\\Downloads\\mapa-rio-de-janeiro.jpg")
        self.label_mapa_rio.setPixmap(pixmap)

        # torna os botões invisiveis e coloridos ao passar o mouse em cima
        self.botao_regiao1.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao2.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao3.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao4.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao5.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao6.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao7.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao8.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao9.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao10.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao11.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao12.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao13.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao14.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao15.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")

        
        # Começa não visivel (não clicável)
        self.label_mapa_rio.setVisible(False)
        self.botao_regiao1.setVisible(False)
        self.botao_regiao2.setVisible(False)
        self.botao_regiao3.setVisible(False)
        self.botao_regiao4.setVisible(False)
        self.botao_regiao5.setVisible(False)
        self.botao_regiao6.setVisible(False)
        self.botao_regiao7.setVisible(False)
        self.botao_regiao8.setVisible(False)
        self.botao_regiao9.setVisible(False)
        self.botao_regiao10.setVisible(False)
        self.botao_regiao11.setVisible(False)
        self.botao_regiao12.setVisible(False)
        self.botao_regiao13.setVisible(False)
        self.botao_regiao14.setVisible(False)
        self.botao_regiao15.setVisible(False)

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
        self.caminho_do_arquivo, filtro = QFileDialog.getOpenFileName(None, "Selecione um arquivo TIF", "", "Arquivos TIF (*.tif);;Todos os arquivos (*)")
        self.gera_elevacoes(self.caminho_do_arquivo)
        self.gera_gradiente(self.caminho_do_arquivo)
        self.exibe_nome_arquivo(self.caminho_do_arquivo[-30:])
  
        print(self.caminho_do_arquivo)

    def exibe_nome_arquivo(self,arquivo):
        self.label_nome_arquivo.setText(f"Arquivo Selecionado : {arquivo}")

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
        # z_smoothed = sp.ndimage.gaussian_filter(z, sigma)

        # z_smoothed_min = np.amin(z_smoothed)
        # z_smoothed_max = np.amax(z_smoothed)
        # z_range = z_smoothed_max - z_smoothed_min

        # Creating figure
        self.fig = plt.figure(figsize=(12,10))
        ax = plt.axes(projection='3d')
        ax.azim = -30
        ax.elev = 42
        ax.set_box_aspect((x_ratio,y_ratio,((x_ratio+y_ratio)/8)))
        surf = ax.plot_surface(x,y,z, cmap='terrain', edgecolor='none', vmin=0, vmax=2000)
        ax.axis('off')


        m = cm.ScalarMappable(cmap=surf.cmap, norm=surf.norm)
        # m.set_array(z_smoothed)

        # cbar =  self.fig.colorbar(m, ax=ax, shrink=0.5, aspect=20, ticks=[z_smoothed_min, 0, (z_range * 0.25 + z_smoothed_min), (z_range * 0.5 + z_smoothed_min), (z_range * 0.75 + z_smoothed_min), z_smoothed_max])
        # cbar.ax.set_yticklabels([f'{z_smoothed_min}', ' ',  f'{(z_range*0.25+z_smoothed_min)}', f'{(z_range*0.5+z_smoothed_min)}', f'{(z_range*0.75+z_smoothed_min)}', f'{z_smoothed_max}'])

        # Adicionando a colorbar ao gráfico
        self.fig.colorbar(surf, ax=ax, shrink=0.5, aspect=13)

        plt.xticks([])  # disabling xticks
        plt.yticks([])  # disabling yticks

        self.fig.tight_layout()

        # Cria uma figura e um canvas para o gráfico
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.setFixedSize(280, 30)

        # Redimensiona o gráfico
        size = self.graphicsView.size()
        self.canvas.resize(size)

        # Conectar o evento de movimento do mouse
        self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)

        # Adiciona o canvas do gráfico à cena
        self.scene.addWidget(self.canvas)
        self.scene.addWidget(self.toolbar)
        self.label_shape.setText(f"Shape: {self.img_array.shape}") # exibe o as dimensões do tif
        print(f"função abrir arquivo com tamanho {self.img_array.shape} funcionou")

    def on_mouse_move(self, event):
        if event.inaxes is not None:
            ax = event.inaxes
            # Checa se o eixo é o 3D correto
            if isinstance(ax, Axes3D):
                # Coleta as coordenadas do mouse no gráfico
                xdata, ydata = event.xdata, event.ydata
                if xdata is not None and ydata is not None:
                    # Converter coordenadas do gráfico para índices da matriz
                    x_idx = int(xdata * self.img_array.shape[1])
                    y_idx = int(ydata * self.img_array.shape[0])

                    if 0 <= x_idx < self.img_array.shape[1] and 0 <= y_idx < self.img_array.shape[0]:
                        z_value = self.img_array[y_idx, x_idx]
                        # print(f"Coordenadas: x={x_idx}, y={y_idx}, z={z_value})")

                        # Exemplo: Atualizar texto de um QLabel
                        self.label_coordinates.setText(f"Coordenadas:({x_idx},{y_idx},{z_value:.2f})")

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

        plt.imshow(incl_max, cmap='terrain')
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

    def corta_tif(self):
        # Definir os índices para recortar
        recorte = self.img_array[ int(self.intervalo_x_inicio.text()):int(self.intervalo_x_final.text()),int(self.intervalo_y_inicio.text()):int(self.intervalo_y_final.text())]

        # Converter o array NumPy de volta para um objeto de imagem PIL
        recorte_img = Image.fromarray(recorte)
        
        if str(self.nome_corte.text())=="":
            nome_do_corte = 'recorte_arquivo.tif'
        else:
            nome_do_corte =  str(self.nome_corte.text()) + ".tif"

        # Salvar o recorte como um novo arquivo TIFF
        recorte_img.save(nome_do_corte)

        self.gera_elevacoes(nome_do_corte)
        self.gera_gradiente(nome_do_corte)
        print("Recorte realizado com sucesso!")

    def volta_tif(self):
        self.gera_elevacoes(self.caminho_do_arquivo)
        self.gera_gradiente(self.caminho_do_arquivo)

    def mostra_mapa(self):
        self.label_mapa_rio.setVisible(not self.label_mapa_rio.isVisible())
        self.botao_regiao1.setVisible(not self.botao_regiao1.isVisible())
        self.botao_regiao2.setVisible(not self.botao_regiao2.isVisible())
        self.botao_regiao3.setVisible(not self.botao_regiao3.isVisible())
        self.botao_regiao4.setVisible(not self.botao_regiao4.isVisible())
        self.botao_regiao5.setVisible(not self.botao_regiao5.isVisible())
        self.botao_regiao6.setVisible(not self.botao_regiao6.isVisible())
        self.botao_regiao7.setVisible(not self.botao_regiao7.isVisible())
        self.botao_regiao8.setVisible(not self.botao_regiao8.isVisible())
        self.botao_regiao9.setVisible(not self.botao_regiao9.isVisible())
        self.botao_regiao10.setVisible(not self.botao_regiao10.isVisible())
        self.botao_regiao11.setVisible(not self.botao_regiao11.isVisible())
        self.botao_regiao12.setVisible(not self.botao_regiao12.isVisible())
        self.botao_regiao13.setVisible(not self.botao_regiao13.isVisible())
        self.botao_regiao14.setVisible(not self.botao_regiao14.isVisible())
        self.botao_regiao15.setVisible(not self.botao_regiao15.isVisible())
        print('funçaõ mostra mapa funcionou')
        print(f"Visibilidade atual: {self.label_mapa_rio.isVisible()}")

    def botao_clicado_regiao(self):
        botao_clicado = self.sender() # atribui o própio botão que foi clicado como uma variável
        
        arquivos_regiao = {"botao_regiao1":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.1.tif" ,
                           "botao_regiao2":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.2.tif",
                           "botao_regiao3":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.3.tif",
                           "botao_regiao4":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.4.tif",
                           "botao_regiao5":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.5.tif",
                           "botao_regiao6":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.6.tif",
                           "botao_regiao7":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.7.tif",
                           "botao_regiao8":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.8.tif",
                           "botao_regiao9":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.9.tif",
                           "botao_regiao10":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.10.tif",
                           "botao_regiao11":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.11.tif",
                           "botao_regiao12":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.12.tif",
                           "botao_regiao13":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.13.tif",
                           "botao_regiao14":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.14.tif",
                           "botao_regiao15":"Projeto-Taludes\\betsabe\\Cidade do Rio\\regiao_8.15.tif"}

        self.label_mapa_rio.setVisible(False)
        self.botao_regiao1.setVisible(False)
        self.botao_regiao2.setVisible(False)
        self.botao_regiao3.setVisible(False)
        self.botao_regiao4.setVisible(False)
        self.botao_regiao5.setVisible(False)
        self.botao_regiao6.setVisible(False)
        self.botao_regiao7.setVisible(False)
        self.botao_regiao8.setVisible(False)
        self.botao_regiao9.setVisible(False)
        self.botao_regiao10.setVisible(False)
        self.botao_regiao11.setVisible(False)
        self.botao_regiao12.setVisible(False)
        self.botao_regiao13.setVisible(False)
        self.botao_regiao14.setVisible(False)
        self.botao_regiao15.setVisible(False)

        self.caminho_do_arquivo = arquivos_regiao[botao_clicado.objectName()]
        self.gera_elevacoes(self.caminho_do_arquivo)
        self.gera_gradiente(self.caminho_do_arquivo)
        self.exibe_nome_arquivo(self.caminho_do_arquivo)


    # WGS84 EPSG:4326
    # Coordenadas do Rio: 22.9068° S, 43.1729° W
    # tarefa!!! fazer recortes do rj cidade mesmo
    # fixar escala
    # concertar coordenadas

app = QApplication(argv)
UIWindow = UI()
exit(app.exec_())