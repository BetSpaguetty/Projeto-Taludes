import matplotlib.pyplot as plt
import numpy as np
from math import *

def rain_infiltration(t,p):
    p = p/100 # cm/h -> m/h
    theta_i = 0.25
    h = 3 # m
    # médium
    theta_r = 0.01
    theta_s = 0.392
    alpha = 2.49 # m^(-1)
    n = 1.1689
    m = 0.1445
    k_day = 0.12 # m/dia

    # cálculos com essas variáveis
    k = k_day/24 # m/h
    theta_e = (theta_i-theta_r)/(theta_s-theta_r)
    psi = ((1 - (theta_e**(1/m)))/((alpha**n)*(theta_e**(1/m))))**(1/n)
    a = abs(psi) * (theta_s - theta_i)
    tp = k*abs(psi)*(theta_s-theta_i)/(p*(p-k))
    hwp = p*tp # m
    hw0 = k*(t-tp) + hwp
    hw = hw0 + a*np.log((hw0 + a)/(hwp + a))*((hw0 + a)/hw0)

    # possibilidades
    # if isnan(hw): # se hw não tiver valor
    #     hw = 0
    hw = np.where(np.isnan(hw), 0, hw)
    # if hw<0: # se hw for negativo
    #     hw = 0
    hw = np.where(hw < 0, 0, hw)
    # elif hw>h: # se hw for maior que o h
    #     hw = h
    hw = np.where(hw > h, h, hw)


    return hw*100 # m -> cm

x = np.linspace(0,30,1000)
# theta = 0.25
y = rain_infiltration(x,1) # p = 1
y1 = rain_infiltration(x,5) # p = 5
y2 = rain_infiltration(x,10) # p = 10
y3 = rain_infiltration(x,15) # p = 15
y4 = rain_infiltration(x,20) # p = 20
y5 = rain_infiltration(x,25) # p = 25

# Legenda nos eixos
plt.xlabel("p (cm/h)")
plt.ylabel("hw (cm)")

# plt.ylim(0, 100)
plt.plot(x,y,color='blue',linewidth=2)
plt.plot(x,y1,color='red',linewidth=2)
plt.plot(x,y2,color='yellow',linewidth=2)
plt.plot(x,y3,color='purple',linewidth=2)
plt.plot(x,y4,color='green',linewidth=2)
plt.plot(x,y5,color='aqua',linewidth=2)
plt.show()

