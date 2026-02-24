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
#%%

#TRAIN DATA
x_train=X2[:500]
y_train=y[:500]
print(len(x_train))

# TEST DATA

x_test=X2[500:]
y_test=y[500:]

clasif1 = KNeighborsClassifier(n_neighbors=5)
clasif1.fit(x_train, y_train)

y_pred1=clasif1.predict(x_test)
acc1=accuracy_score(y_test, y_pred1)

print(acc1)

clasif2 = KNeighborsClassifier(n_neighbors=10)
clasif2.fit(x_train, y_train)

y_pred2=clasif2.predict(x_test)
acc2=accuracy_score(y_test, y_pred2)

print(acc2)

k_valores = [5,10,15,20,25,30,40,45,50]
precisiones = []

for k in k_valores:
    modelo = KNeighborsClassifier(n_neighbors=k)
    
    modelo.fit(x_train, y_train)
    y_pred_def=modelo.predict(x_test)
    
    precisiones.append(accuracy_score(y_test,y_pred_def))

plt.plot(k_valores, precisiones, marker='o')
plt.xlabel("Valores de K")
plt.ylabel("Precision del modelo en test")
plt.grid()
plt.show()