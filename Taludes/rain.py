import pandas as pd
from math import log, isnan

class RainHistogramLogic:
    def __init__(self):
        self.file = None
        self.precipitation = None
        self.period = None
        self.dict_rain = None

    def read_file(self, file_path: str):
        """Lê o arquivo Excel ou CSV e extrai período e precipitação."""
        self.file = file_path

        if file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            raise ValueError("Formato de arquivo não suportado")

        # Assume: coluna 0 = período | coluna 1 = precipitação
        self.period = df.iloc[:, 0]
        self.precipitation = df.iloc[:, 1]
        self.dict_rain = dict(zip(self.period, self.precipitation))

        return self.period, self.precipitation

    def calculo_hw(self, p: float, t: float, theta_i: float = 0.3) -> float:
        """Calcula o valor de hw com base nos parâmetros fornecidos."""
        h = 3
        theta_r = 0.01
        theta_s = 0.392
        alpha = 2.49  # m^-1
        n = 1.1689
        m = 0.1445 
        k_day = 0.12  # m/dia

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

    def cria_lista_hw(self, theta_i: float = 0.3):
        """Cria uma lista de hw para todos os tempos."""
        if self.dict_rain is None:
            raise ValueError("Arquivo não carregado com read_file().")

        lista_hw = []
        for tempo, p in self.dict_rain.items():
            hw = self.calculo_hw(p, 1, theta_i)
            lista_hw.append(hw)
        return lista_hw

    def hw_total(self, t_final: int, theta_i: float = 0.3):
        """Soma dos valores hw até o tempo t_final."""
        lista = self.cria_lista_hw(theta_i)
        hw_total = sum(lista[:t_final])
        h_limite = 3

        if isnan(hw_total) or hw_total < 0:
            hw_total = 0
        elif hw_total > h_limite:
            hw_total = h_limite

        return hw_total











def calculo_hw(p: float, t: float, theta_i: float = 0.3) -> float:
    """Calcula o valor de hw com base nos parâmetros fornecidos."""
    h = 3
    theta_r = 0.01
    theta_s = 0.392
    alpha = 2.49  # m^-1
    n = 1.1689
    m = 0.1445 
    k_day = 0.12  # m/dia

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













