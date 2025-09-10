from math import *
import pandas as pd

def calculo_hw(p,t,theta_i):
    # variáveis obtidas da função runAnalysis
    # theta_i = 0.3
    h = 3
    # médium
    theta_r = 0.01
    theta_s = 0.392
    alpha = 2.49 # m^(-1)
    n = 1.1689
    m = 0.1445
    k_day = 0.12 # m/dia

    try:
        k = k_day/24 # m/h
        theta_e = (theta_i-theta_r)/(theta_s-theta_r)
        psi = ((1 - (theta_e**(1/m)))/((alpha**n)*(theta_e**(1/m))))**(1/n)
        a = abs(psi) * (theta_s - theta_i)
        tp = k*abs(psi)*(theta_s-theta_i)/(p*(p-k))
        hwp = p*tp # m
        hw0 = k*(t-tp) + hwp
        hw = hw0 + a*log((hw0 + a)/(hwp + a))*((hw0 + a)/hw0)

        # Possibilidades
        if isnan(hw): # se hw não tiver valor ou se o periodo for 0
            hw = 0
        elif hw<0: # se hw for negativo
            hw = 0
        elif hw>h: # se hw for maior que o h
            hw = h
    except (ZeroDivisionError, ValueError) as e:
        hw = 0
    return hw

def cria_lista_hw():
    lista_hw = []
    for tempo in dicionario_chuva:
        hw = calculo_hw(dicionario_chuva[tempo],1,0.3)
        # print(hw)
        lista_hw.append(hw)
    return lista_hw

def hw_total(lista, j):
    i = 0
    hw_total = 0
    while i < j:
        hw_total += lista[i]
        i+=1
    return hw_total

df = pd.read_excel("C:\\Users\\betsabenogueira\\Downloads\\Book1.xlsx") # Ler o arquivo Excel
precipt = df.iloc[:,1] # Pega todas as linhas ":" da coluna 1
periodo = df.iloc[:,0] # Pega todas as linhas ":" da coluna 0

dicionario_chuva = dict(zip(periodo, precipt))
# dicionario_chuva = {1:0,2:5,3:8,4:10,5:12,6:10,7:8,8:6,9:3}

lista_hw = cria_lista_hw()

print(lista_hw)
print(hw_total(lista_hw, 5))

