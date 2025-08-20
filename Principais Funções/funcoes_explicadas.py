# Nesse documento você encontra o código das funções e a explicação de cada uma delas e de suas variáveis.
# --------------------------------------------------------------------------------------------------------
# Importando alguns módulos:
from PyQt5.QtWidgets import QFileDialog

# --------------------------------------------------------------------------------------------------------
# Funções
# 1. Ler Arquivo
def ler_arquivo(self):
    self.caminho_do_arquivo, filtro = QFileDialog.getOpenFileName(None, "Selecione um arquivo TIF", "", "Arquivos TIF (*.tif);;Todos os arquivos (*)")

    if self.caminho_do_arquivo == "":
        self.show_error_popup("Arquivo não selecionado.")
        print(self.caminho_do_arquivo)
    else:
        self.button_conversor.setEnabled(True)
        self.gera_elevacoes(self.caminho_do_arquivo)
        self.gera_gradiente(self.caminho_do_arquivo)
        self.exibe_nome_arquivo(self.caminho_do_arquivo[-60:])

"""
Essa função está conectada ao botão "Open File" e não recebe nenhuma variável. 
Quando acionada, ela abre o explorador de arquivos e permite que os usuários selecione um arquivo do tipo .tif.
Primeiro usamos a função .getOpenFileName que nos reetorna 2 variáveis, a primeira sendo o caminho do arquivo e a única que vamos utilizar.
O if e else são usados para que o programa não desligue quando o usuário não selecionar um arquivo, então se o caminho do arquivo for "" (Nada), será exibido um erro.
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2.Função corte
from PIL import Image
def corta_tif(self):
    # Definir os índices para recortar
    # recorte = self.img_array[xi:xf,yi:xf]
    recorte = self.img_array[int(self.intervalo_x_inicio.text()):int(self.intervalo_x_final.text()),int(self.intervalo_y_inicio.text()):int(self.intervalo_y_final.text())]

    # Converter o array NumPy de volta para um objeto de imagem PIL
    recorte_img = Image.fromarray(recorte)

    # Se o usuário não inserir um nome para o arquivo, o nome será "recorte_arquivo.tif"
    if str(self.nome_corte.text())=="": 
        nome_do_corte = 'recorte_arquivo.tif'
    else:
        nome_do_corte =  str(self.nome_corte.text()) + ".tif"

    # Salvar o recorte como um novo arquivo TIFF
    recorte_img.save(nome_do_corte)

    # Chamando as funções que exibem os gráficos agora usando o caminho do arquivo cortado (nome_do_corte)
    self.gera_elevacoes(nome_do_corte) 
    self.gera_gradiente(nome_do_corte) # Esse gráfico de inclinação não é mais utilizado na interface principal.
    return
"""
Essa função recebe os intervalos que o usuário inserir, intervalo de início e fim para x e y, e ao final os exibe.
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2.Triângulo de Texturas
""" 
"""
def define_material(self):
        clay = self.valueArgila
        sand = self.valueAreia
        silt = self.valueSilte

        if (clay + silt + sand) != 100: 
            self.material_type = 'A soma não da 100%'
        elif clay <= 18 and sand >= 65:
            self.material_type = 'COARSE'
            self.material_theta_r = 0.025
            self.material_theta_500 = 0.046
            self.material_theta_s = 0.366
            self.material_vg_alpha = 4.30 #%[m^-1]
            self.material_vg_n = 1.5206
            self.material_vg_m = 0.3424
            self.material_vg_k = 0.70     #%{m/dia}
        elif clay<=18 and sand >= 15 and sand <= 65:
            self.material_type = 'GRANULAR MEDIUM'
            self.material_theta_r = 0.010
            self.material_theta_500 = 0.179
            self.material_theta_s = 0.392
            self.material_vg_alpha = 2.49
            self.material_vg_n = 1.1689
            self.material_vg_m = 0.1445
            self.material_vg_k = 0.12
        elif clay<=18 and sand <=15:
            self.material_type = 'GRANULAR FINE'
            self.material_theta_r = 0.010
            self.material_theta_500 = 0.188
            self.material_theta_s = 0.412
            self.material_vg_alpha = 0.82
            self.material_vg_n = 1.2179
            self.material_vg_m = 0.1789
            self.material_vg_k = 0.04
        elif clay>=18 and clay <= 35 and sand >= 15: #or clay<=18 and sand >= 15 and sand <= 65:
            self.material_type = 'MEDIUM'
            self.material_theta_r = 0.010
            self.material_theta_500 = 0.179
            self.material_theta_s = 0.392
            self.material_vg_alpha = 2.49
            self.material_vg_n = 1.1689
            self.material_vg_m = 0.1445
            self.material_vg_k = 0.12
        elif clay>=18 and clay<=35  and sand <= 15:
            self.material_type = 'MEDIUM FINE'
            self.material_theta_r = 0.010
            self.material_theta_500 = 0.188
            self.material_theta_s = 0.412
            self.material_vg_alpha = 0.82
            self.material_vg_n = 1.2179
            self.material_vg_m = 0.1789
            self.material_vg_k = 0.04
        elif clay>=35 and clay <= 60:
            self.material_type = 'FINE'
            self.material_theta_r = 0.010
            self.material_theta_500 = 0.327
            self.material_theta_s = 0.481
            self.material_vg_alpha = 1.98
            self.material_vg_n = 1.0861
            self.material_vg_m = 0.0793
            self.material_vg_k = 0.09
        elif clay > 60:
            self.material_type = 'VERY FINE'
            self.material_theta_r = 0.010
            self.material_theta_500 = 0.392
            self.material_theta_s = 0.538
            self.material_vg_alpha = 1.68
            self.material_vg_n = 1.0730
            self.material_vg_m = 0.068
            self.material_vg_k = 0.08
        #

        if clay <= 18:
            self.horizontalSlider_C.setMaximum(0)
            self.horizontalSlider_C.setMinimum(0)
            print("Solo 0")
        else:
            self.horizontalSlider_C.setMaximum(20)
            self.horizontalSlider_C.setMinimum(0)

        self.horizontalSlider_Theta.setMaximum(int(self.material_theta_s * 1000))
        self.horizontalSlider_Theta.setMinimum(int(self.material_theta_500 * 1000))
        self.horizontalSlider_Theta.setSliderPosition(int(self.material_theta_500 * 1000))
        self.horizontalSlider_Theta.setSingleStep(int((self.material_theta_s - self.material_theta_500) * 100))
        self.horizontalSlider_Theta.setPageStep(int((self.material_theta_s - self.material_theta_500) * 100))
        self.horizontalSlider_Theta.setTickInterval(int((self.material_theta_s - self.material_theta_500)/100))

        self.label_material.setText(str(self.material_type))

        fig = plt.figure()
        ax = plt.subplot(111,projection="ternary")
        ax.taxis.set_major_locator(MultipleLocator(0.2))
        ax.laxis.set_major_locator(MultipleLocator(0.2))
        ax.raxis.set_major_locator(MultipleLocator(0.2))

        ax.tick_params(labelrotation="axis")
        ax.grid(which='major') #which="both")

        t = [0.6, 0.6, 0.35, 0.35]
        l = [0.4, 0, 0, 0.65]
        r = [0, 0.4, 0.65, 0]
        ax.fill(t, l, r, color="b") #Trapézio azul

        t = [1, 0.6, 0.6]
        l = [0, 0.4, 0]
        r = [0, 0 , 0.4]
        ax.fill(t, l, r, color="m") #Triângulo roxo

        t = [0.35, 0.35, 0.18, 0.18]
        l = [0.65, 0.15, 0.15, 0.82]
        r = [0, 0.5, 0.67, 0]
        ax.fill(t, l, r, color="y") #Trapézio amarelo

        t = [0.35, 0.35, 0.18, 0.18]
        l = [0.15, 0, 0, 0.15]
        r = [0.5, 0.65, 0.82, 0.67]
        ax.fill(t, l, r, color="lime") #Paralelogramo verde claro

        t = [0.18, 0.18, 0, 0]
        l = [0.15, 0, 0, 0.15]
        r = [0.67, 0.82, 1, 0.85]
        ax.fill(t, l, r, color="g") #Paralelogramo verde escuro

        t = [0.18, 0.18, 0, 0]
        l = [0.65, 0.15, 0.15, 0.65]
        r = [0.17, 0.67, 0.82, 0.35]
        ax.fill(t, l, r, color="orange") #Paralelogramo laranja

        t = [0.18, 0.18, 0, 0]
        l = [0.82, 0.65, 0.65, 1]
        r = [0, 0.17, 0.35, 0]
        ax.fill(t, l, r, color="r") #Trapézio vermelho

        ax.scatter((clay/100),(sand/100),(silt/100), color="black")

        ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
        labels = ["Sl", "0.2", "0.4", "0.6", "0.8", "1"]
        ax.taxis.set_ticks(ticks, labels=labels)
        labels = ["Cl", "0.2", "0.4", "0.6", "0.8", "1"]
        ax.laxis.set_ticks(ticks, labels=labels)
        labels = ["Sd", "0.2", "0.4", "0.6", "0.8", "1"]
        ax.raxis.set_ticks(ticks, labels=labels)

        self.tri+=1

        fig.tight_layout
        self.canvasT = FigureCanvas(fig)
        self.canvasT.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.canvasT.setMaximumSize(315,300)           #(390,345)
        
        self.tabMat = QWidget()
        self.tabMat_layout = QVBoxLayout()
        self.tabMat_layout.addWidget(self.canvasT)
        self.tabMat.setLayout(self.tabMat_layout)

        self.tab_name = "Solo"
        self.tabs_4.addTab(self.tabMat, self.tab_name)

        if self.tabs_4.count() >= 2:
            self.tabs_4.removeTab(0)

        self.tabs_4.setVisible(True)


        valueC = str(self.horizontalSlider_C.value())
        self.ClineEdit.setText(valueC)

        valuePhi = str(self.horizontalSlider_Phi.value())
        self.philineEdit.setText(valuePhi)

        valueH = str(self.horizontalSlider_H.value()/10)
        self.hlineEdit.setText(valueH)

        valueHw = str(self.horizontalSlider_Hw.value() * self.horizontalSlider_H.value()/1000)
        self.hwlineEdit.setText(valueHw)

        valueTheta = str(self.horizontalSlider_Theta.value()/1000)
        self.thetalineEdit.setText(valueTheta)

        self.stacked_elevacao.resize

        print("Muda solo")
        self.material_definido+=1
    #

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Propriedades do Solo

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4.Mapa Pré-definido (Essa função exibe um Popup)
"""
Para explicar essa função, será preciso mostrar a classe que abre essa janela e destacar que foram realizadas edições no arquivo ui através do próprio qt design para 
diminuir a quantidade de código. Verificar por favor os atributos de estilo do botão.
"""
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog, QPushButton, QLabel, QGridLayout

class Popup_Mapa_RJ(QDialog):
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
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Conversor de células
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Função da chuva
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
