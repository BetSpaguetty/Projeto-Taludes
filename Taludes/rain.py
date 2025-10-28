import pandas as pd
from math import log, isnan
from Taludes.types import *













def calculo_hw(p: float, t: float, theta_i: float = 0.3, h=3, solo:Material=Materiais.COARSE) -> float:
    """Calcula o valor de hw com base nos parâmetros fornecidos."""
    theta_r = solo.THETA_R
    theta_s = solo.THETA_S
    alpha = solo.VG_ALPHA  # m^-1
    n = solo.VG_N
    m = solo.VG_M
    k_day = solo.VG_K  # m/dia

    try:
        k = k_day / 24  # m/h
        theta_e = (theta_i - theta_r) / (theta_s - theta_r)
        psi = ((1 - (theta_e ** (1 / m))) / ((alpha ** n) * (theta_e ** (1 / m)))) ** (1 / n)
        a = abs(psi) * (theta_s - theta_i)
        tp = k * abs(psi) * (theta_s - theta_i) / (p * (p - k))
        hwp = p * tp
        hw0 = k * (t - tp) + hwp
        hw = hw0 + a * log((hw0 + a) / (hwp + a)) * ((hw0 + a) / hw0)

        if isnan(hw) or hw < 0:
            hw = 0
        elif hw > h:
            hw = h
    except (ZeroDivisionError, ValueError):
        hw = 0

    return hw













