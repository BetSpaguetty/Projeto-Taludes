import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo Excel
df = pd.read_excel('tempo_precipitacao.xlsx')
print(df)

precipitacao = df['precipitacao (mm)']
precipitacao2 = df['precipitacao 2 (mm)']
precipitacao3 = df['precipitacao 3 (mm)']
tempo = df['tempo (h)']

# Criar o histograma
plt.figure(figsize=(8,6))
# plt.bar(tempo[:8],precipitacao2[:8], color='grey', edgecolor='black')
# plt.bar(tempo, precipitacao, color='grey', edgecolor='black')
plt.bar(tempo, precipitacao3, color='blue', edgecolor='black')
plt.bar(tempo, precipitacao2, color='red', edgecolor='black')


plt.ylabel('precipitacao (mm)')
plt.xlabel('tempo (h)')
plt.xticks(range(0, 50, 2))
plt.title('Histograma de Precipitação')
plt.show()
