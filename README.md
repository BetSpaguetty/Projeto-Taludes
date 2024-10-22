# Projeto-Taludes
Este projeto propõe o desenvolvimento de uma interface gráfica utilizando PyQt (Python + Qt) que permite a abertura de arquivos TIFF e oferece múltiplas opções de visualização, ajustáveis conforme as necessidades do usuário. A ferramenta possibilita, além da visualização, a simulação de diversos eventos que podem impactar significativamente a segurança e estabilidade dos terrenos, especialmente em áreas de taludes. Taludes são estruturas críticas tanto em ambientes naturais quanto construídos, e sua análise é essencial para a mitigação de riscos, como deslizamentos e falhas estruturais, especialmente em regiões urbanizadas ou áreas de mineração.

# Funcionalidades
- Carregar e exibir arquivos TIFF geográficos.
- Simular eventos que afetam a estabilidade de taludes, como deslizamentos e erosões.
- Alterar e manipular visualizações raster.
- Suporte para zoom e rotação nas imagens.
- Exportar resultados das simulações para novos arquivos.

# Requisitos
Para executar este projeto, os seguintes pacotes precisam estar instalados:
- Python 3.12.3 
- PyQt5
- Rasterio
- NumPy
- Matplotlib

# Estrutura do Projeto
O projeto foi desenvolvido por Betsabé e Paulo. Aqui você vai encontrar inicialmente duas interfaces desenvolvidas por cada um deles, que buscam cumprir as mesmas funcionalidades, mas ao final teremos apenas uma interface.

Bet:
- open_tif_alterado.py -> Arquivo principal que executa a interface gráfica.
   - ler_arquivo -> Abre um seletor de arquivos e extrai o caminho do arquivo para ser usado no código.
   - gera_elevações -> Gera o gráfico de elevação, indicando o valor da altitude em cada ponto.
   - corta_tif -> Realiza o corte na matriz de acordo com o interfalo de corte definido pelo usuário.
   - volta_tif -> Volta para o arquivo original (anterior ao corte).
   - gera_gradiente -> Gera o gráfico de gradiente, mostrando ao usuário a inclinação máxima em cada ponto.
   
- open_tif_2.ui -> Interface gráfica desenvolvida no QtDesigner.

Paulo:
- open_tif_alterado.py -> Arquivo principal que executa a interface gráfica.
   - def number_changed(self): muda números nos lineEdits quando há mudanças nos sliders
   - def runAnalysis(self): cria e mostra os gráficos das variáveis
   - def getfile(self): recebe arquivos novos e cria os gráficos da sua elevação e inclinação
   - def figureAdjust(self): faz cortes em gráficos de arquivos já recebidos
   - def clearCanvas(self): limpa todos os valores e gráficos
  
# Como Usar?
Abra o Arquivo principal (.py) e execute no seu interpretador de código, logo aparecerá a interface.
