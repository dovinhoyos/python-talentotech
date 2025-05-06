import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("histograma_dataset.csv")

df_msc = df.loc[df['Sexo'] == 'Masculino']
df_fem = df.loc[df['Sexo'] == 'Femenino']
# print(df_fem)

fig, ax = plt.subplots(figsize=(5,4))
violin_parts = ax.violinplot(df_fem['Altura (cm)'])

for pc in violin_parts['bodies']:
    pc.set_facecolor('orchid')  # Cambia 'lightblue' por el color deseado
    pc.set_edgecolor('blue')      # Cambia 'blue' por el color del borde
    pc.set_alpha(0.5)    

ax.set_title('Distribucion de altura de mujeres')
ax.set_xlabel('Sexo')
ax.set_ylabel('Altura (cm)')

ax.grid(True)

plt.show()



