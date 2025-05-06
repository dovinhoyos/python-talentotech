import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("histograma_dataset.csv")

df_msc = df.loc[df['Sexo'] == 'Masculino']
df_fem = df.loc[df['Sexo'] == 'Femenino']
# print(df_fem)

plt.style.use('seaborn-v0_8-white')

fig, ax = plt.subplots(figsize=(5,4))
violin_parts = ax.violinplot([df_fem['Altura (cm)'], df_msc['Altura (cm)']], showmedians=True)

for i, pc in enumerate(violin_parts['bodies']):
    if i == 0:  # df_fem
        pc.set_facecolor('orchid')
        pc.set_edgecolor('red')
    elif i == 1:  # df_msc
        pc.set_facecolor('lightblue')
        pc.set_edgecolor('darkblue')
    pc.set_alpha(0.5)

ax.set_title('Distribucion de altura de mujeres')
ax.set_xlabel('Sexo')
ax.set_ylabel('Altura (cm)')

ax.grid(True)

etiquetas = ['Femenino', 'Masculino']
ax.set_xticks([1, 2], labels=etiquetas)

plt.show()

# Cálculo de la mediana y los cuartiles 1 y 3 para cada subset
q1_fem, med_fem, q3_fem = np.percentile(df_fem['Altura (cm)'], [25, 50, 75])
q1_msc, med_msc, q3_msc = np.percentile(df_msc['Altura (cm)'], [25, 50, 75])

# Almacenar los resultados en arreglos de NumPy
meds = np.array([med_fem, med_msc])
q1s = np.array([q1_fem, q1_msc])
q3s = np.array([q3_fem, q3_msc])

# Imprimir resultados en pantalla
print('Sexo: Femenino')
print(f'   Q1: {q1_fem}, Mediana: {med_fem}, Q3: {q3_fem}')
print('-'*20)
print('Sexo: Masculino')
print(f'   Q1: {q1_msc}, Mediana: {med_msc}, Q3: {q3_msc}')



