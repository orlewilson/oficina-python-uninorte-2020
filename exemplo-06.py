'''
Oficina Profissionalizante - Uninorte/2020
Python e suas Aplicações
Facilitador:    Orlewilson Bentes Maia
Data:           30/10/2020
Nome:           Seu nome
Descrição:      Pandas - leitura de arquivo .csv e visualização de dados
'''

# importação de bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# leitura de dados
df = pd.read_csv("airbnb-nyc-2019.csv", sep=";")


# manipulação dos dados lidos
print(df)

print(df.head())

print(df["neighbourhood"].unique())

print(df["neighbourhood"].value_counts())

print(df["neighbourhood"].value_counts(normalize=True))

print(df.groupby("neighbourhood").mean())

print(df.groupby("neighbourhood").mean()["price"].sort_values())

df2 = df[(df["price"] >= 0)]

print(df2.groupby("neighbourhood").mean()["price"].sort_values())

df2.groupby("neighbourhood").mean()["price"].sort_values().nlargest(5)

# visualização dos dados lidos
df2["price"].plot.hist()
plt.show() # mostrar janela

df2["price"].plot.hist(bins=30, edgecolor='black')
plt.show()


df2["neighbourhood"].value_counts().nlargest(5).plot.bar()
plt.show()

df2["neighbourhood"].value_counts().nlargest(5).plot.barh(title="Número de apartamentos")
plt.show()
