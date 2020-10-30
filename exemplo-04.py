'''
Oficina Profissionalizante - Uninorte/2020
Python e suas Aplicações
Facilitador:    Orlewilson Bentes Maia
Data:           30/10/2020
Nome:           Seu nome
Descrição:      Pandas - usando variável do tipo Series
'''

# importação de bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# criação
notas = pd.Series([2,7,5,10,6])

# manipulação
print(notas)

print(notas.values)

print(notas.index)

notas = pd.Series([2,7,10,5], index=["Wilson", "Bruno", "Nic", "Cris", ])

print(notas)

print(notas["Bruno"])

print("Média:", notas.mean())
print("Desvio padrão:", notas.std())

print(notas.describe())

print(notas**2)

print(np.log(notas)) # aplicando a operação matemática logarítmo nos dados numéricos