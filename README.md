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
- apptaludes.py -> Arquivo que executa a interface gráfica.
   - showProp: mostra ou esconde os parâmetros do solo quando se clica no botão "Properties"
   - define_material: mostra o gráfico ternário
   - number_changed: muda números nos lineEdits quando o usuário mecher nos sliders
   - number_changed2: permite mudar a porcentagem de areia, silte e argila que compoêm o solo e faz com que sua soma seja sempre 100%
   - analysisClick: conta o número de vezes que o botão Analysis foi clicado
   - runAnalysis: cria e mostra o gráfico do fator de segurança quando o botão Analysis é clicado(Anteriormente: cria e mostra os gráficos das variáveis (h(m), hw(m), c'(kPa) e Phi(Graus)), que tem o mesmo tamanho do último gráfico criado)
   - runAnalysis2: cria/altera o gráfico do fator de segurança quando os sliders são movidos
   - getfile: recebe arquivos novos e chama "elev_incl"
   - elev_incl: cria os gráficos da elevação e inclinação
   - figureAdjust: faz cortes em gráficos do último arquivo recebidos
   - clearCanvas: limpa todos os valores e gráficos
   - mostra_lista: mostra o mapa e os botões para selecionar os arquivos criados pela Betsabé (Baseada na função de nome semelhante da Betsabé)
   - mostra_recortar: mostra ou esconde a etiqueta, o botão e a caixa de texto que criam novos arquivos quando se clica no botão "Save"
   - mostra_solo: mostra ou esconde a composição do solo quando se clica no botão "Soil"
   - botao_clicado_regiao: seleciona um dos arquivos criados pela Betsabé através do mapa mostrado por "mostra_lista" e chama "elev_incl" para esse arquivo (Baseada na função de mesmo nome da Betsabé
   - corta_tif: cria um novo arquivo TIF a partir de um recorte do arquivo sendo usado com base nas cordenadas em X1, X2, Y1 e Y2 (Baseada na função de mesmo nome da Betsabé)
  
# Como Usar?
Abra o Arquivo principal (.py) e execute no seu interpretador de código, logo aparecerá a interface.
