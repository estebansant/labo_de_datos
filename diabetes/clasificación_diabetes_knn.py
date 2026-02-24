#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 11:00:22 2025

@author: mcerdeiro
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
#%% cargar datos de diabetes
df_diabetes = pd.read_csv('diabetes.csv')
df_diabetes.columns
#%% X atributos, y etiqueta
X = df_diabetes[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = df_diabetes['Outcome']
#%% para usar solo 2 atributos
X2 = df_diabetes[['Glucose', 'BMI']].values
y = df_diabetes['Outcome'].values
#%% gráfico de dispersión
plt.figure(figsize=(6, 4))
plt.scatter(X2[:, 0], X2[:, 1], c=y)
plt.xlabel('Glucose')
plt.ylabel('BMI')
plt.title('Distribución de los datos: Glucose vs BMI')
plt.show()
#%% construyo y ajusto el clasificador
clasificador = KNeighborsClassifier(n_neighbors=12)
clasificador.fit(X2, y)
#%% predicción para un nuevo paciente
nuevo_paciente = [[130, 32.0]] 
prediccion = clasificador.predict(nuevo_paciente)
print("Predicción para el nuevo paciente:", "Diabetes" if prediccion[0] == 1 else "No diabetes")

y_pred = clasificador.predict(X2)
matriz = confusion_matrix(y,y_pred)
precision = accuracy_score(y,y_pred)

print(matriz)
print(precision)
#%%
# Nuevo calsificador

X3 = df_diabetes[['Glucose', 'Insulin']].values

clasificador2 = KNeighborsClassifier(n_neighbors=8)
clasificador2.fit(X3, y)

nuevo_paciente2 = [[130, 32.0]] 
prediccion2 = clasificador2.predict(nuevo_paciente2)
print("Predicción para el nuevo paciente:", "Diabetes" if prediccion2[0] == 1 else "No diabetes")

y_pred2 = clasificador.predict(X3)
matriz2 = confusion_matrix(y,y_pred2)
precision2 = accuracy_score(y,y_pred2)

print(matriz2)
print(precision2)





