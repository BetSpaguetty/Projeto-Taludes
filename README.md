# Projeto-Taludes
Esse projeto consiste em criar uma interface gráfica usando PyQt (Python + Qt) onde é possível abrir arquivos tiff e simular diversos acontecimentos que alteram significativamente a estabilidade dos taludes.

# Resumo do projeto


# Funcionalidades
- Carregar e exibir arquivos TIFF geográficos.
- Simular eventos que afetam a estabilidade de taludes, como deslizamentos e erosões.
- Alterar e manipular visualizações raster.
- Suporte para zoom e rotação nas imagens.
- Exportar resultados das simulações para novos arquivos.

# Requisitos
Para executar este projeto, os seguintes pacotes precisam estar instalados:
Python 3.12.3 
PyQt5
Rasterio
NumPy
Matplotlib

# Estrutura do Projeto
O projeto foi desenvolvido por Betsabé e Paulo. Aqui você vai encontrar inicialmente duas interfaces desenvolvidas por cada um deles, que buscam cumprir as mesmas funcionalidades, mas ao final teremos apenas uma interface.
\nBet:
- open_tif_alterado.py -> Arquivo principal que executa a interface gráfica.
   - ler_arquivo -> Abre um seletor de arquivos e extrai o caminho do arquivo para ser usado no código.
   - gera_elevações -> Gera o gráfico de elevação, indicando o valor da altitude em cada ponto.
   - corta_tif -> Realiza o corte na matriz de acordo com o interfalo de corte definido pelo usuário.
   - volta_tif -> Volta para o arquivo original (anterior ao corte).
   - gera_gradiente -> Gera o gráfico de gradiente, mostrando ao usuário a inclinação máxima em cada ponto.
   
- open_tif.ui -> Interface gráfica desenvolvida no QtDesigner.

\nPaulo:

# Como Usar?

