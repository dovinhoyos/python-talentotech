import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("histograma_dataset.csv")

df_msc = df.loc[df['Sexo'] == 'Masculino']
df_fem = df.loc[df['Sexo'] == 'Femenino']
# print(df_fem)

plt.style.use('seaborn-v0_8-white')

fig, ax = plt.subplots(figsize=(5,4))
violin_parts = ax.violinplot(df_fem['Altura (cm)'], 
                              showmedians=True)   

ax.set_title('Distribucion de altura de mujeres')
ax.set_xlabel('Sexo')
ax.set_ylabel('Altura (cm)')

ax.grid(True)

plt.show()



