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

# Parámetros adicionales
nbins = 25
alfa = 0.5
densidad = True

# Generar histogramas básicos (conteo de ocurrencias normalizado si density=True)
fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

axs[0].hist(df_fem['Altura (cm)'], bins=nbins, alpha=alfa, density=densidad, color='orchid')
axs[1].hist(df_msc['Altura (cm)'], bins=nbins, alpha=alfa, density=densidad, color='skyblue')

# Títulos y etiquetas
axs[0].set_title('Distribución de altura - Mujeres')
axs[1].set_title('Distribución de altura - Hombres')
for ax in axs:
    ax.set_xlabel('Altura (cm)')
axs[0].set_ylabel('Densidad' if densidad else 'Conteos')

# Grilla para ambos subplots
[ax.grid(True) for ax in axs]

# Ajuste del layout para evitar solapamiento
plt.tight_layout()
plt.show()

