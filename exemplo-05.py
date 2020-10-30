'''
Oficina Profissionalizante - Uninorte/2020
Python e suas Aplicações
Facilitador:    Orlewilson Bentes Maia
Data:           30/10/2020
Nome:           Seu nome
Descrição:      Pandas - usando variável do tipo DataFrame
'''

# importação de bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# criação

cursoPython = pd.DataFrame({'Aluno' : ["Wilson", "Bruno", "Nic", "Cris"],
                            'Faltas' : [1,2,0,4],
                            'Prova' : [5,6,9,6],
                            'Seminário': [5.3,8,7,6],
                            'Conceito': ['A', 'A', 'B', 'B']})

# manipulação
print(cursoPython)

print("Média Faltas: ", cursoPython["Faltas"].mean())

print("Média Notas Prova: ", cursoPython["Prova"].mean())

print(cursoPython.describe())

print(cursoPython.sort_values(by="Prova"))

print(cursoPython[(cursoPython["Faltas"] <= 2) & (cursoPython["Prova"] >= 6)])

# salvar DataFrame em um arquivo CSV
cursoPython.to_csv("oficina_python.csv")
