#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 27 11:30:57 2025

@author: mcerdeiro
"""

#%% imports
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

#%% cargar el dataset de autos
df_mpg = pd.read_csv("auto-mpg.xls")
df_mpg.columns  

#%% modelo lineal con una variable
modelo_lineal1 = LinearRegression()
modelo_lineal1.fit(df_mpg[['weight']], df_mpg['mpg'])

print("Coeficiente:", modelo_lineal1.coef_)
print("Intercepto:", modelo_lineal1.intercept_)

# visualización 
plt.scatter(df_mpg['weight'], df_mpg['mpg'], alpha=0.3)
plt.plot(df_mpg['weight'], modelo_lineal1.predict(df_mpg[['weight']]), color='red')
plt.title("MPG vs Weight (modelo lineal)")
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.show()

# Parametros de error y bonanza
MSE1= mean_squared_error(df_mpg['mpg'],modelo_lineal1.predict(df_mpg[['weight']]))
r2_1 = modelo_lineal1.score(df_mpg[['weight']],df_mpg['mpg'])

print(MSE1)
print(r2_1)
#%%
# Modelo para mpg vs displacement
modelo_lineal1 = LinearRegression()
modelo_lineal1.fit(df_mpg[['displacement']], df_mpg['mpg'])

print("Coeficientes:", modelo_lineal1.coef_)
print("Intercepto:", modelo_lineal1.intercept_)

plt.scatter(df_mpg['displacement'], df_mpg['mpg'], alpha=0.3)
plt.plot(df_mpg['displacement'], modelo_lineal1.predict(df_mpg[['displacement']]), color='red')
plt.title("MPG vs Displacement (modelo lineal)")
plt.xlabel("Displacement")
plt.ylabel("MPG")
plt.show()

# Parametros de error y bonanza
MSE2= mean_squared_error(df_mpg['mpg'],modelo_lineal1.predict(df_mpg[['displacement']]))
r2_2 = modelo_lineal1.score(df_mpg[['displacement']],df_mpg['mpg'])

print(MSE2)
print(r2_2)
#%%
# Modelo para mpg vs acceleration
modelo_lineal1 = LinearRegression()
modelo_lineal1.fit(df_mpg[['acceleration']], df_mpg['mpg'])

print("Coeficientes:", modelo_lineal1.coef_)
print("Intercepto:", modelo_lineal1.intercept_)

plt.scatter(df_mpg['acceleration'], df_mpg['mpg'], alpha=0.3)
plt.plot(df_mpg['acceleration'], modelo_lineal1.predict(df_mpg[['acceleration']]), color='red')
plt.title("MPG vs Acceleration (modelo lineal)")
plt.xlabel("Acceleration")
plt.ylabel("MPG")
plt.show()


# Parametros de error y bonanza
MSE3= mean_squared_error(df_mpg['mpg'],modelo_lineal1.predict(df_mpg[['acceleration']]))
r2_3 = modelo_lineal1.score(df_mpg[['acceleration']],df_mpg['mpg'])

print(MSE3)
print(r2_3)

#%%
# r2 mas cercano a 1

print(f"El maximo es {max(r2_1,r2_2,r2_3)}, que corresponde a mpg vs peso")

#%% modelo lineal con dos variables
modelo_lineal2 = LinearRegression()
modelo_lineal2.fit(df_mpg[['weight', 'displacement']], df_mpg['mpg'])

print("Coeficientes:", modelo_lineal2.coef_)
print("Intercepto:", modelo_lineal2.intercept_)

#%% modelo cuadrático en una variable (weight)
poly_feat_1v = PolynomialFeatures(degree=2).fit_transform(df_mpg[['weight']])
modelo_cuad_1v = LinearRegression(fit_intercept=False)
modelo_cuad_1v.fit(poly_feat_1v, df_mpg['mpg'])

print("Coeficientes cuadráticos (una variable):", modelo_cuad_1v.coef_)

#%% división en train/test
X = df_mpg[['weight', 'displacement', 'acceleration']]
y = df_mpg['mpg']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=12, shuffle=True)

#%% modelo lineal multivariable

modelo_lineal = LinearRegression()
modelo_lineal.fit(X_train, y_train)

y_pred_train_lin = modelo_lineal.predict(X_train)
y_pred_test_lin = modelo_lineal.predict(X_test)

print("Modelo lineal:")
print("  Train - MSE:", mean_squared_error(y_train, y_pred_train_lin))
print("  Train - R²:", r2_score(y_train, y_pred_train_lin))
print("  Test  - MSE:", mean_squared_error(y_test, y_pred_test_lin))
print("  Test  - R²:", r2_score(y_test, y_pred_test_lin))

#%% modelo polinómico multivariable (grado 2)

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

modelo_cuad = LinearRegression(fit_intercept=False)
modelo_cuad.fit(X_train_poly, y_train)

y_pred_train_cuad = modelo_cuad.predict(X_train_poly)
y_pred_test_cuad = modelo_cuad.predict(X_test_poly)

print("\nModelo cuadrático (polinómico grado 2):")
print("  Train - MSE:", mean_squared_error(y_train, y_pred_train_cuad))
print("  Train - R²:", r2_score(y_train, y_pred_train_cuad))

print("  Test  - MSE :", mean_squared_error(y_test, y_pred_test_cuad))
print("  Test  - RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_test_cuad)))
print("  Test  - MAE :", mean_absolute_error(y_test, y_pred_test_cuad))
