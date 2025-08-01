# Módulos
from PyQt5 import uic
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QAction, QToolBar, QStackedWidget, QWidget, QVBoxLayout, QDialog, QMessageBox, QApplication, QMainWindow, QGraphicsScene, QFileDialog, QPushButton, QGraphicsView, QLineEdit, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap
from pyvistaqt import QtInteractor

import math
import numpy as np
import pyvista as pv
from PIL import Image
import rasterio
from matplotlib.ticker import FuncFormatter

import matplotlib.colors as mcolors
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg  import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from sys import argv, exit, path

# Classes
class Popup_add_info(QDialog):
    def __init__(self):
        super().__init__() #super(UI, self).__init__()
        uic.loadUi("Projeto-Taludes\\betsabe\\PyVista\\add_info.ui", self) # Carregar o arquivo .ui
        # self.latitude = self.findChild(QLineEdit,"latitude")
        # self.longitude = self.findChild(QLineEdit,"longitude")

        self.lineEdit_lat_min = self.findChild(QLineEdit,"add_lat_min")
        self.lineEdit_long_min = self.findChild(QLineEdit,"add_long_min")
        self.lineEdit_lat_max = self.findChild(QLineEdit,"add_lat_max")
        self.lineEdit_long_max = self.findChild(QLineEdit,"add_long_max")

        self.lay_principal = self.findChild(QVBoxLayout,"lay_principal")
        self.setLayout(self.lay_principal)

        def resizeEvent(self, event):
            # Ajusta a QLabel para ocupar o mesmo tamanho do layout
            if self.layout:
                # Mantém a proporção ao redimensionar
                new_width = event.size().width()
                new_height = int(new_width / self.aspect_ratio)
                self.resize(new_width, new_height)
                
                super().resizeEvent(event) 
        
    def fornece_pixel(self):
        print("fornecendo pixel...")
        qtd_x = (float(self.lineEdit_lat_max.text())-float(self.lineEdit_lat_min.text()))
        print(qtd_x)
        qtd_y = (float(self.lineEdit_long_max.text())-float(self.lineEdit_long_min.text()))
        print(qtd_y)
        return (qtd_x,qtd_y)
    
    def fornece_coordenadas(self):
        # print("fornecendo coordenadas...")
        return (float(self.lineEdit_lat_min.text()),float(self.lineEdit_long_min.text()),float(self.lineEdit_lat_max.text()),float(self.lineEdit_long_max.text()))
    
    def salvar(self):
        print("salvando...")
        self.accept()

        return 

class Popup_LatLon(QDialog):
    def __init__(self):
        super().__init__() #super(UI, self).__init__()
        uic.loadUi("Projeto-Taludes\\betsabe\\PyVista\\popup_LatLon.ui", self) # Carregar o arquivo .ui
        self.setWindowTitle("Conversor de Células")
        self.botao_converte = self.findChild(QPushButton,"botao_converte")
        self.botao_converte.setWhatsThis("Após inserir as coordenadas, aperte para saber em qual célula(x,y) elas se encontram.")
        self.botao_add_info = self.findChild(QPushButton,"add_info")
        self.botao_add_info.setWhatsThis("Insira as informações de latitude e longitude do seu arquivo aqui.")
        # Ativar o botão "?" na barra de título
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowContextHelpButtonHint)
        self.botao_add_info = self.findChild(QPushButton,"add_info")
        self.botao_add_info.setEnabled(False)
        self.lineEdit_celula = self.findChild(QLineEdit,"lineEdit_celula")
        self.lineEdit_latitude = self.findChild(QLineEdit,"lineEdit_latitude")
        self.lineEdit_longitude = self.findChild(QLineEdit,"lineEdit_longitude")
        self.label_lat_min = self.findChild(QLabel,"lat_min")
        self.label_lat_max = self.findChild(QLabel,"lat_max")
        self.label_long_min = self.findChild(QLabel,"long_min")
        self.label_long_max = self.findChild(QLabel,"long_max")
        self.label_info = self.findChild(QLabel,"info")

        self.lay_principal = self.findChild(QVBoxLayout,"lay_principal")
        self.setLayout(self.lay_principal)
        
    def ler_arquivo_popup(self, arquivo):
        self.arquivo = arquivo
        self.info_arquivo()

    def info_arquivo(self):
        print("função rodando...")
        with rasterio.open(self.arquivo) as dataset:
            if dataset.crs is None:
                print(f"informações nulas")
                self.botao_add_info.setEnabled(True)
                self.label_info.setText("Informações: Seu arquivo não possui CRS")
                self.label_lat_min.setText("Latitude Mínima: None")
                self.label_lat_max.setText("Latitude Máxima: None")
                self.label_long_min.setText("Longitude Mínima: None")
                self.label_long_max.setText("Longitude Máxima: None")
                self.lineEdit_latitude.setEnabled(False)
                self.lineEdit_longitude.setEnabled(False)
                self.lineEdit_celula.setEnabled(False)
            else:
                print("informações obtidas")
                bounds = dataset.bounds
                self.label_lat_min.setText(f"Latitude Mínima: {bounds.bottom}")
                self.label_lat_max.setText(f"Latitude Máxima: {bounds.top}")
                self.label_long_min.setText(f"Longitude Mínima: {bounds.left}")
                self.label_long_max.setText(f"Longitude Máxima: {bounds.right}")

    def salva_info(self,latmin,latmax,longmin,longmax):
        # self.label_lat_min.setText(f"Latitude Mínima: {latmin}")
        # self.label_lat_max.setText(f"Latitude Máxima: {latmax}")
        # self.label_long_min.setText(f"Longitude Mínima: {longmin}")
        # self.label_long_max.setText(f"Longitude Máxima: {longmax}")
        return
        
    def show_error_popup2(self, error_message):
        # Cria a caixa de mensagem de erro
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)  # Define o ícone como erro
        msg.setWindowTitle("Erro")  # Define o título da janela
        msg.setText(error_message)  # Define o texto da mensagem
        msg.setStandardButtons(QMessageBox.Ok)  # Adiciona o botão OK
        msg.exec_()  # Exibe a mensagem

    def show_add_info(self):
        self.popup_add_info = Popup_add_info()
        self.lineEdit_latitude.setEnabled(True)
        self.lineEdit_longitude.setEnabled(True)
        self.lineEdit_celula.setEnabled(True)
        resultado = self.popup_add_info.exec()
        latmin,longmin,latmax,longmax = self.popup_add_info.fornece_coordenadas()
        self.label_lat_min.setText(f"Latitude Mínima: {latmin}")
        self.label_lat_max.setText(f"Latitude Máxima: {latmax}")
        self.label_long_min.setText(f"Longitude Mínima: {longmin}")
        self.label_long_max.setText(f"Longitude Máxima: {longmax}")
        
    def converteLatLon(self):
        print("chamou a função")
        if self.lineEdit_latitude =='' or self.lineEdit_longitude =='':
            self.show_error_popup2("Um dos campos obrigatórios está vazio.")
        else:
            print("ARQUIVO: ",self.arquivo)
            lat = self.lineEdit_latitude.text()
            long = self.lineEdit_longitude.text()
            with rasterio.open(self.arquivo) as dataset:
                print(f"CRS do dataset: {dataset.crs!r}")
                if dataset.crs is None:
                    print("⚠️ O TIFF não tem CRS! Entrando no if...") # Se NÃO houver Sistema de referência espacial (CRS)
                    
                    lat_inicial = self.popup_add_info.fornece_coordenadas()[0]
                    lon_inicial = self.popup_add_info.fornece_coordenadas()[1]

                    lat_final = self.popup_add_info.fornece_coordenadas()[2]
                    lon_final = self.popup_add_info.fornece_coordenadas()[3]
                    print("captou as coordenadas.......................1")
                    # lat_inicial = -23
                    # lon_inicial = -43.15

                    # lat_final = -22.77
                    # lon_final = -43.5

                    latitude = float(lat)
                    longitude = float(long)
                    print("captou as coordenadas.......................2")
                    if (latitude > lat_inicial and latitude < lat_final) or latitude == lat_inicial or latitude == lat_final: 
                        print('latitude', latitude)
                        if (longitude > lon_inicial and longitude < lon_final) or longitude == lon_inicial or longitude == lon_final:
                            print('longitude', longitude)
                            resto = latitude - lat_inicial
                            print("resto lat:",resto) 
                            qt_celulay = resto/(self.popup_add_info.fornece_pixel()[0]/dataset.shape[1])
                            print("!!!!!!!!!!!betttttttt!!!!!!",self.popup_add_info.fornece_pixel()[0])

                            resto2 = longitude - lon_inicial
                            print("resto long:",abs(resto2)) 
                            qt_celulax = resto2/(self.popup_add_info.fornece_pixel()[1]/dataset.shape[0])

                            print(dataset.shape)
                            print(f"Célula: {abs(qt_celulax):.0f}, {abs(qt_celulay):.0f}")
                            self.lineEdit_celula.setText(f"({abs(qt_celulax):.0f}, {abs(qt_celulay):.0f})")
                else:
                    print("✅ O TIFF tem CRS:", dataset.crs)
                    resolucao_x, resolucao_y = dataset.res[0], dataset.res[1] # Tamanho do pixel em graus (lon/lat)
                    bounds = dataset.bounds # Obter os limites (bounding box)

                    lat_inicial = bounds.bottom # Min Y (Latitude)
                    lon_inicial = bounds.left # Min X (Longitude)

                    lat_final = bounds.top # Max Y (Latitude)
                    lon_final = bounds.right # Max X (Longitude)

                    latitude = float(lat)
                    longitude = float(long)

                    print(f"Coordenadas iniciais: {bounds.bottom},{bounds.left}/Coordenadas finais: {bounds.top},{bounds.right}")
                    
                    if (latitude > lat_inicial and latitude < lat_final) or latitude == lat_inicial or latitude == lat_final: 
                        print("latitude",latitude)
                        if (longitude > lon_inicial and longitude < lon_final) or longitude == lon_inicial or longitude == lon_final:
                            print("longitude")
                            resto = latitude - lat_inicial
                            print("resto lat:",resto) 
                            qt_celulax = resto/resolucao_x

                            resto2 = longitude - lon_inicial
                            print("resto long:",abs(resto2)) 
                            qt_celulay = resto2/resolucao_y

                            banda1 = dataset.read(1)
                            print(banda1.shape)
                            print(f"Célula: {abs(qt_celulax):.0f}, {abs(qt_celulay):.0f}")
                            self.lineEdit_celula.setText(f"({abs(qt_celulax):.0f}, {abs(qt_celulay):.0f})")
        
class PopupWindow(QDialog):
    def __init__(self):
        super().__init__() #super(UI, self).__init__()
        uic.loadUi("Projeto-Taludes\\betsabe\\PyVista\\popup.ui", self) # Carregar o arquivo .ui
        self.setWindowTitle("22S435W - Rio de Janeiro")
        self.setGeometry(200, 100, 572, 377)
    
        # Imagem do mapa
        self.fundo = QLabel(self)
        self.fundo.setPixmap(QPixmap("Projeto-Taludes\\betsabe\\Imagens Interface\\image.png"))  # Caminho da imagem
        self.fundo.setScaledContents(True) # Ajusta a imagem ao tamanho do QLabel
    
        # Layout dos botões
        self.layout = self.findChild(QGridLayout,"gridLayout_botoes")
        self.setLayout(self.layout) # fixando na janela

        # botões
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
        self.botao_regiao16 = self.findChild(QPushButton,"botao_regiao16")
        self.botao_regiao17 = self.findChild(QPushButton,"botao_regiao17")
        self.botao_regiao18 = self.findChild(QPushButton,"botao_regiao18")
        self.botao_regiao19 = self.findChild(QPushButton,"botao_regiao19")
        self.botao_regiao20 = self.findChild(QPushButton,"botao_regiao20")

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
        self.botao_regiao16.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao17.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao18.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao19.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
        self.botao_regiao20.setStyleSheet("""background-color: rgba(255, 255, 255, 0);border: none;}
                                        QPushButton:hover {background-color: rgba(100, 150, 200, 0.5);}""")
    
         # Caminho dos arquivos pré definidos
        self.caminho_do_arquivo = None  # Guarda o caminho selecionado
        self.arquivos_regiao = {"botao_regiao1":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_1.tif",
                                "botao_regiao2":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_2.tif",
                                "botao_regiao3":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_3.tif",
                                "botao_regiao4":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_4.tif",
                                "botao_regiao5":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_5.tif",
                                "botao_regiao6":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_6.tif",
                                "botao_regiao7":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_7.tif",
                                "botao_regiao8":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_8.tif",
                                "botao_regiao9":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_9.tif",
                                "botao_regiao10":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_10.tif",
                                "botao_regiao11":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_11.tif",
                                "botao_regiao12":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_12.tif",
                                "botao_regiao13":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_13.tif",
                                "botao_regiao14":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_14.tif",
                                "botao_regiao15":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_15.tif",
                                "botao_regiao16":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_16.tif",
                                "botao_regiao17":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_17.tif",
                                "botao_regiao18":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_18.tif",
                                "botao_regiao19":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_19.tif",
                                "botao_regiao20":"Projeto-Taludes\\betsabe\\rj_recortes\\RJ_20.tif"}
        # Define um tamanho inicial
        self.resize(600, 450)
        self.aspect_ratio = 600 / 450  # Largura/Altura

    def resizeEvent(self, event):
        # Ajusta a QLabel para ocupar o mesmo tamanho do layout
        if self.layout:
            area_layout = self.layout.geometry()  # Obtém o tamanho do layout
            self.fundo.setGeometry(area_layout)  # Define o tamanho da QLabel igual ao layout
            # Mantém a proporção ao redimensionar
        new_width = event.size().width()
        new_height = int(new_width / self.aspect_ratio)
        self.resize(new_width, new_height)
        
        super().resizeEvent(event)  

    def botao_clicado_regiao(self):
        botao_clicado = self.sender() # atribui o própio botão que foi clicado à uma variável
        
        if botao_clicado:
            texto = botao_clicado.objectName()
            print(f"Texto do botão: {texto}")

            if str(botao_clicado.objectName()) in self.arquivos_regiao:
                print("entrou no if")
                self.caminho_do_arquivo = self.arquivos_regiao[texto]
                print(self.caminho_do_arquivo)
                self.accept()  # Fecha o popup corretamente
            else:
                print("entrou no else")
                self.show_error_popup("Região de 22S435W não foi selecionada ou não existe.")

    def show_error_popup(self, error_message):
        # Cria a caixa de mensagem de erro
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)  # Define o ícone como erro
        msg.setWindowTitle("Erro")  # Define o título da janela
        msg.setText(error_message)  # Define o texto da mensagem
        msg.setStandardButtons(QMessageBox.Ok)  # Adiciona o botão OK
        msg.exec_()  # Exibe a mensagem

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("Projeto-Taludes\\betsabe\\PyVista\\open_tif_pyvista.ui",self)
        self.pushButton = self.findChild(QPushButton,"botao_abrir_arquivo")
        self.pushButton2 = self.findChild(QPushButton,"botao_recorte")
        self.button_conversor = self.findChild(QPushButton,"button_conversor")
        self.button_conversor.setEnabled(False)

        # self.exibe_elevacao = self.findChild(QGraphicsView,"frame_exibicao_elevacao")
        self.exibe_elevacao = self.findChild(QStackedWidget,"stacked_elevacao")
        self.exibe_gradiente = self.findChild(QGraphicsView,"frame_exibicao_gradiente")

        self.intervalo_x_inicio = self.findChild(QLineEdit,"intervalo_x_inicio")
        self.intervalo_x_final = self.findChild(QLineEdit,"intervalo_x_final")
        self.intervalo_y_inicio = self.findChild(QLineEdit,"intervalo_y_inicio")
        self.intervalo_y_final = self.findChild(QLineEdit,"intervalo_y_final")
        self.nome_corte = self.findChild(QLineEdit,"nome_arquivo_corte")

        self.label_shape = self.findChild(QLabel,"label_shape")
        self.label_nome_arquivo = self.findChild(QLabel,"label_nomeArquivo")
        self.label_mapa_rio = self.findChild(QLabel,"label_mapa_rio")
        self.label_coordinates = self.findChild(QLabel,"label_coordinates")

        self.layout = self.findChild(QGridLayout,"layout_P")
        self.layout_exibicoes = self.findChild(QGridLayout,"gridLayout")
        self.stacked_elevacao = self.findChild(QStackedWidget,"stacked_elevacao")
        self.layout_elevacoes = self.findChild(QGridLayout,"layout_elevacoes")
        self.metros_por_pixel = self.findChild(QLineEdit,"metros_por_pixel")
        self.metros_por_pixel.setText("25")

        # Cria a toolbar
        toolbar = QToolBar("Toolbar de Visualização")
        self.addToolBar(toolbar)

        # Botões de visualização
        action_top = QAction("Top view", self)
        action_top.triggered.connect(self.view_top)
        toolbar.addAction(action_top)

        action_side = QAction("3D view", self)
        action_side.triggered.connect(self.view_side)
        toolbar.addAction(action_side)

        action_front = QAction("Elevation", self)
        action_front.triggered.connect(self.view_front)
        toolbar.addAction(action_front)

        # Cria o widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Aplica o layout ao widget central
        central_widget.setLayout(self.layout)

        # Classe PopupWindow
        self.classe_popup = PopupWindow()
        self.scene_gradiente = QGraphicsScene()
        self.exibe_gradiente.setScene(self.scene_gradiente)
        self.exibe_gradiente.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.exibe_gradiente.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.resize(1200, 600)
        self.show()

    def retorna_metros(self):
        with rasterio.open(self.caminho_do_arquivo) as dataset:
            if dataset.crs is None:
                print(f"informações nulas")
                metros = 25
            else:
                print("informações obtidas")
                bounds = dataset.bounds
                self.label_lat_min.setText(f"Latitude Mínima: {bounds.bottom}")
                self.label_lat_max.setText(f"Latitude Máxima: {bounds.top}")
                self.label_long_min.setText(f"Longitude Mínima: {bounds.left}")
                self.label_long_max.setText(f"Longitude Máxima: {bounds.right}")
        
        return metros
        
    def resizeEvent(self, event):
        new_width = event.size().width()
        new_height = int(new_width / (1200/649))
        self.resize(new_width, new_height)

    def show_conversor(self):
        popup = Popup_LatLon()
        popup.ler_arquivo_popup(self.caminho_do_arquivo)
        resultado = popup.exec()  # Aguarda o usuário fechar o popup

    def show_popup(self):
        popup = PopupWindow()
        resultado = popup.exec()  # Aguarda o usuário fechar o popup

        if resultado == QDialog.Accepted and popup.caminho_do_arquivo:
            self.caminho_do_arquivo = popup.caminho_do_arquivo
            self.gera_elevacoes(self.caminho_do_arquivo)
            self.gera_gradiente(self.caminho_do_arquivo)
            self.exibe_nome_arquivo(self.caminho_do_arquivo)
            self.button_conversor.setEnabled(True)
        else:
            print("Nenhum arquivo selecionado.")
    
    def show_error_popup(self, error_message):
        # Cria a caixa de mensagem de erro
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)  # Define o ícone como erro
        msg.setWindowTitle("Erro")  # Define o título da janela
        msg.setText(error_message)  # Define o texto da mensagem
        msg.setStandardButtons(QMessageBox.Ok)  # Adiciona o botão OK
        msg.exec_()  # Exibe a mensagem
    
    def ler_arquivo(self):
        self.caminho_do_arquivo, filtro = QFileDialog.getOpenFileName(None, "Selecione um arquivo TIF", "", "Arquivos TIF (*.tif);;Todos os arquivos (*)")
        self.L_pixel = self.meters_per_pixel(self.caminho_do_arquivo)[1]
        

        if self.caminho_do_arquivo == "":
            self.show_error_popup("Arquivo não selecionado.")
            print(self.caminho_do_arquivo)
        else:
            self.button_conversor.setEnabled(True)
            self.gera_elevacoes(self.caminho_do_arquivo)
            self.gera_gradiente(self.caminho_do_arquivo)
            self.exibe_nome_arquivo(self.caminho_do_arquivo[-60:])
            self.L_pixel = self.meters_per_pixel(self.caminho_do_arquivo)[1]
            self.metros_por_pixel.setText(str(self.L_pixel))

    def exibe_nome_arquivo(self,arquivo):
        self.label_nome_arquivo.setText(f"Arquivo Selecionado : {arquivo}")
        
    def gera_elevacoes(self,arquivo):
        with rasterio.open(arquivo) as dataset:
            print(f"Formato: {dataset.driver}")
            print(f"Dimensões: {dataset.width} x {dataset.height}")
            print(f"Número de bandas: {dataset.count}")

            if dataset.count > 1:
                # Ler apenas a primeira banda
                banda1 = dataset.read(1)
                self.img_array = banda1
                z_min = np.min(banda1)
                z_max = np.max(banda1)
            else:
                img = Image.open(arquivo)
                self.img_array = np.array(img)
                z_min = np.min(np.array(img))
                z_max = np.max(np.array(img))

        # Gerar as coordenadas (sem georreferenciamento, vamos usar os índices de pixels)
        ny, nx = self.img_array.shape  # cuidado: (rows, cols)
        x = np.arange(nx)
        y = np.arange(ny)
        x, y = np.meshgrid(x, y)
        z = self.img_array 
        z_total = z_max - z_min
        
        # Proporção para escala de z
        incl_max, tam_y, tam_x = self.calcula_incl_max(arquivo)
        prop_z = z_total/tam_x # a proporção de z por x e y da diferente, como saber quando usa-la?
        print("!!!!!!!!!!!!!", prop_z) 


        # Inverte os eixos visualmente, se necessário
        x = np.flip(x, axis=1)  # inverte eixo X
        y = np.flip(y, axis=0)  # inverte eixo Y
        z = np.flip(z, axis=0)  # inverte eixo Y do Z

        self.plotter = QtInteractor(self.exibe_elevacao)
        # self.plotter = pv.Plotter(off_screen=False)
        # self.plotter.set_scale(xscale=1, yscale=1, zscale=(1/25)) # muda a escala de z sem alterar o gráfico.
        self.plotter.set_scale(xscale=1, yscale=1, zscale=(1/self.L_pixel))
        # self.plotter.set_scale(xscale=1, yscale=1)
        grid = pv.StructuredGrid(x, y, z)
        grid["elevation"] = z.ravel(order="F")
        
        self.plotter.add_mesh(pv.Sphere())
        self.plotter.add_mesh(grid, scalars="elevation", cmap="terrain", show_scalar_bar=True, scalar_bar_args={'title': 'Elevação',
        'vertical': True, 'position_x': 0.85, 'position_y': 0.25})

        # Adiciona o canvas do gráfico à cena
        self.stacked_elevacao.addWidget(self.plotter)
        self.stacked_elevacao.setCurrentWidget(self.plotter)
        
        # self.scene.addWidget(self.toolbar)
        self.label_shape.setText(f"Shape: {self.img_array.shape}") # exibe o as dimensões do tif
        print(f"função abrir arquivo com tamanho {self.img_array.shape} funcionou")

    def view_top(self):
        self.plotter.camera_position = [
        (0, 0, 100),  # posição da câmera
        (0, 0, 0),  # ponto focal
        (0, -1, 0)   # vetor
        ]
        self.plotter.reset_camera()

    def view_side(self):
        self.plotter.camera_position = [
        (1, 1, 1),  # posição da câmera
        (0, 0, 0),  # ponto focal
        (0, 0, 1)   # vetor
        ]
        self.plotter.reset_camera()

    def view_front(self):
        self.plotter.camera_position = [
        (0, 1, 0),  # posição da câmera
        (0, 0, 0),  # ponto focal
        (0, 0, 1)   # vetor
        ]
        self.plotter.reset_camera()

    def on_mouse_move(self, event):
        # if event.inaxes is not None:
        #     ax = event.inaxes
        #     # Checa se o eixo é o 3D correto
        #     if isinstance(ax, Axes3D):
        #         # Coleta as coordenadas do mouse no gráfico
        #         xdata, ydata = event.xdata, event.ydata
        #         if xdata is not None and ydata is not None:
        #             # Converter coordenadas do gráfico para índices da matriz
        #             x_idx = int(xdata * self.img_array.shape[1])
        #             y_idx = int(ydata * self.img_array.shape[0])

        #             if 0 <= x_idx < self.img_array.shape[1] and 0 <= y_idx < self.img_array.shape[0]:
        #                 z_value = self.img_array[y_idx, x_idx]
        #                 # print(f"Coordenadas: x={x_idx}, y={y_idx}, z={z_value})")

        #                 # Exemplo: Atualizar texto de um QLabel
        #                 self.label_coordinates.setText(f"Coordenadas:({x_idx},{y_idx},{z_value:.2f})")
        return
    
    def calcula_distancia_lat(self):
        c = 2 * math.pi * 6371000
        return c/360

    def meters_per_pixel(self, file_path):
        with rasterio.open(file_path) as dataset:
            if dataset.crs is None:
                print(f"informações nulas")
                # largura = dataset.width      # número de colunas (pixels no eixo X)
                # altura = dataset.height      # número de linhas (pixels no eixo Y)

                # res_x_m = (1.5/largura) * (111320 * math.cos(math.radians(largura)))
                # res_y_m = (1/altura) * 111320 
                return(25,25)
            else:
                print("informações obtidas")
                transform = dataset.transform
                pixel_width = transform.a      # tamanho do pixel no eixo X
                pixel_height = -transform.e    # tamanho do pixel no eixo Y (negativo, por convenção)

                res_x_m = pixel_width * self.calcula_distancia_lat() * math.cos(math.radians(pixel_width)) # (lon) -> meia luas
                res_y_m = pixel_height * self.calcula_distancia_lat()                                      # (lat) -> paralelos
                print(pixel_width,pixel_height)

                return (round(res_x_m),round(res_y_m))
        
    def calcula_incl_max(self, arquivo):
        with rasterio.open(arquivo) as dataset:
            print(f"Formato: {dataset.driver}")
            print(f"Dimensões: {dataset.width} x {dataset.height}")
            print(f"Número de bandas: {dataset.count}")

            matriz = dataset.read(1) # Ler apenas a primeira banda

        # L = 25  # quantidade de metros por pixel
        
        L = self.L_pixel
        print(L)
        
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

        # Define os limites do eixo em metros (multiplicando pelo tamanho do pixel)
        altura, largura = incl_max.shape
        return (incl_max, altura*L, largura*L)
    
    def gera_gradiente(self,arquivo):

        incl_max, altura, largura = self.calcula_incl_max(arquivo)
        
        extent = [0, largura, altura, 0]  # [xmin, xmax, ymin, ymax]

        plt.imshow(incl_max, cmap='terrain', extent=extent)
        plt.xlabel("Distância (m)")
        plt.ylabel("Distância (m)")
        plt.colorbar(label='Inclinação Máxima (graus)')

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

    # WGS84 EPSG:4326
    # Coordenadas do Rio: 22.9068° S, 43.1729° W

app = QApplication(argv)
UIWindow = UI()
exit(app.exec_())

