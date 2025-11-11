import os
from config import * 
from pathlib import Path

def getMaps() : 

    for nome_arquivo in os.listdir(DATA_PATH):
        caminho_completo = os.path.join(DATA_PATH, nome_arquivo)
        if os.path.isfile(caminho_completo):  # garante que é um arquivo
            print(caminho_completo)






def getMaps() : 

    pasta = Path(DATA_PATH)

    for arquivo in pasta.glob("*.json"):
        print(arquivo)






