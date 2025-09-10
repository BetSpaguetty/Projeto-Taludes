import matplotlib.pyplot as plt

# ---------- Função Green-Ampt (mesma que antes) ----------
def green_ampt_from_hyetograph(
    intens_mmph, dt_hours, Ks_mmph, psi_f_mm, theta_s, theta_i
):
    dtheta = max(1e-9, theta_s - theta_i)
    F = 1e-6  # mm
    f_list, F_list, zf_list = [], [], []

    for I, dt in zip(intens_mmph, dt_hours):
        fcap = Ks_mmph * (1.0 + (psi_f_mm * dtheta) / max(F, 1e-9))
        f_real = min(I, fcap)
        F += f_real * dt
        zf = F / dtheta  # mm
        f_list.append(f_real)
        F_list.append(F)
        zf_list.append(zf)

    return F_list, zf_list

# ---------- Exemplo ----------
# Hietograma: 6 intervalos de 10 min (0,1667 h)
dt = [10/60]*6
I = [5, 20, 30, 10, 5, 0]  # mm/h

# Parâmetros do solo
# Ks = 10.0      # mm/h
# psi_f = 110.0  # mm
# theta_s = 0.45
# theta_i = 0.20

Ks = 0.12/24      # mm/h
theta_s = 0.392
theta_i =  0.3

theta_r = 0.01
alpha = 2.49 # m^(-1)
n = 1.1689
m = 0.1445
theta_e = (theta_i-theta_r)/(theta_s-theta_r)
psi = ((1 - (theta_e**(1/m)))/((alpha**n)*(theta_e**(1/m))))**(1/n)
psi_f = psi  # mm

F, zf = green_ampt_from_hyetograph(I, dt, Ks, psi_f, theta_s, theta_i)

# Eixo de tempo acumulado em horas
tempo_h = [sum(dt[:i+1]) for i in range(len(dt))]

# ---------- Plot ----------
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Hietograma (chuva)
axes[0].bar(tempo_h, I, width=0.15, color='royalblue')
axes[0].set_title("Hietograma de chuva")
axes[0].set_xlabel("Tempo (h)")
axes[0].set_ylabel("Intensidade (mm/h)")

# Profundidade da frente de saturação
axes[1].plot(tempo_h, [z/10 for z in zf], marker='o', color='darkgreen')
axes[1].set_title("Profundidade da frente de saturação")
axes[1].set_xlabel("Tempo (h)")
axes[1].set_ylabel("z_f (cm)")
axes[1].grid(True)

plt.tight_layout()
plt.show()
