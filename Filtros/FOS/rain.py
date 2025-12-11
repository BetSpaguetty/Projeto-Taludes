# rain_math.py
import pandas as pd
from math import log, isnan

# ------------------------------------------------------------
# LEITURA DO ARQUIVO
# ------------------------------------------------------------
def read_rain_file(path):
    """
    Lê um CSV ou XLSX contendo duas colunas:
    Coluna 0: período (tempo em horas)
    Coluna 1: precipitação (mm)
    Retorna:
        period -> lista de tempos
        precipitation -> lista de precipitações
        dict_rain -> dict {tempo: precipitação}
    """
    if path.endswith(".csv"):
        df = pd.read_csv(path)
    else:
        df = pd.read_excel(path)

    period = df.iloc[:, 0].to_list()
    precipitation = df.iloc[:, 1].to_list()
    dict_rain = dict(zip(period, precipitation))

    return period, precipitation, dict_rain


# ------------------------------------------------------------
# CÁLCULO DO GREEN–AMPT
# ------------------------------------------------------------
def calc_hw(precip_mm, t, theta_i=0.3):
    """
    precip_mm: precipitação em mm/h
    t: tempo em horas
    """
    if precip_mm <= 0 or t <= 0:
        return 0

    p = precip_mm / 1000  # mm/h → m/h
    h = 3  # profundidade máxima (m)

    # Parâmetros médium (fixos no seu código original)
    theta_r = 0.01
    theta_s = 0.392
    alpha = 2.49
    n = 1.1689
    m = 0.1445
    k_day = 0.12  # m/dia

    try:
        k = k_day / 24
        theta_e = (theta_i - theta_r) / (theta_s - theta_r)
        psi = ((1 - theta_e ** (1 / m)) /
              ((alpha ** n) * (theta_e ** (1 / m)))) ** (1 / n)

        a = abs(psi) * (theta_s - theta_i)
        tp = k * abs(psi) * (theta_s - theta_i) / (p * (p - k))
        hwp = p * tp
        hw0 = k * (t - tp) + hwp

        hw = hw0 + a * log((hw0 + a) / (hwp + a)) * ((hw0 + a) / hw0)

        if isnan(hw) or hw < 0:
            return 0
        if hw > h:
            return h

        return hw

    except Exception:
        return 0


# ------------------------------------------------------------
# GERA LISTA HW PARA TODOS OS TEMPOS
# ------------------------------------------------------------
def generate_hw_list(dict_rain, theta_i=0.3):
    lista = []
    for t, precip in dict_rain.items():
        hw = calc_hw(precip, 1, theta_i)
        lista.append(hw)
    return lista


# ------------------------------------------------------------
# SOMA DOS VALORES ATÉ UM PERÍODO
# ------------------------------------------------------------
def total_hw_until(dict_rain, limit_period, theta_i=0.3):
    hw_list = generate_hw_list(dict_rain, theta_i)

    total = 0
    for i in range(limit_period):
        if i >= len(hw_list):
            break
        total += hw_list[i]

    return min(total, 3)
