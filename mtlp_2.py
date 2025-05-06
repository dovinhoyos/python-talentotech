import matplotlib.pyplot as plt
import pandas as pd

# crear el set de datos sintetico
# x = [3, 2, 4, 12, 17, 22, 21, 30, 22]

# generar un histograma simple
# fig, ax = plt.subplots()
# ax.hist(x, bins=5)
# ax.set_xlabel('Rangos')
# ax.set_ylabel('Conteos')
# ax.grid()

df = pd.read_csv("histograma_dataset.csv")

df_msc = df.loc[df['Sexo'] == 'Masculino']
df_fem = df.loc[df['Sexo'] == 'Femenino']

# parametros adicionales en formato diccionario
kwargs = dict(bins=35, alpha=0.3, density=True)

# generar histogramas basicos (conteo de ocurrencias)
fig, axs = plt.subplots(figsize=(6,4))
axs.hist(df_fem['Altura (cm)'], **kwargs, label='Mujeres')
axs.hist(df_msc['Altura (cm)'], **kwargs, label='Hombres')

# agregar titulo y etiquetas a los ejes
axs.set_title('Distribucion de altura de mujeres y hombres')
axs.set_xlabel('Altura (cm)')
axs.set_ylabel('Densidad')
axs.legend()
axs.grid(True)

plt.tight_layout()
plt.show()

