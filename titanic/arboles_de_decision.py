#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 14:29:20 2026

@author: Estudiante
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
import duckdb as dd

#%%
ruta_archivo=("/home/Estudiante/Documentos/clase8/titanic/titanic.csv")

df = pd.read_csv(ruta_archivo)

consultaSQL = """
    SELECT *
    FROM df
    WHERE Survived = 1
"""

sobrevivientes = dd.query(consultaSQL).df()

ratio_tot = len(sobrevivientes)/(len(df))
print(ratio_tot)

consultaSQL = """
    SELECT Sex
    FROM sobrevivientes
    WHERE Sex = 'male'
"""

varones = dd.query(consultaSQL).df()

cant_mujeres = len(sobrevivientes)-len(varones)

print(cant_mujeres)
print(len(varones))

ratio_sexo = len(varones)/cant_mujeres

print(ratio_sexo)

consultaSQL= """
    SELECT Pclass
    FROM sobrevivientes
    WHERE Pclass = 1
"""

primera_clase = dd.query(consultaSQL).df()

consultaSQL= """
    SELECT Pclass
    FROM sobrevivientes
    WHERE Pclass = 2
"""

segunda_clase = dd.query(consultaSQL).df()

consultaSQL= """
    SELECT Pclass
    FROM sobrevivientes
    WHERE Pclass = 3
"""

tercera_clase = dd.query(consultaSQL).df()

ratio_1era_clase = len(primera_clase)/len(df)
ratio_2da_clase = len(segunda_clase)/len(df)
ratio_3era_clase = len(tercera_clase)/len(df)

print("---------------------------------------------------")
print("pasajeros en 1era", len(primera_clase))
print(ratio_1era_clase, "\n")
print("pasajeros en 2da", len(segunda_clase))
print(ratio_2da_clase, "\n")
print("pasajeros en 3era", len(tercera_clase))
print(ratio_3era_clase, "\n")

