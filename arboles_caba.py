#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 15:25:18 2026

@author: Estudiante
"""
import numpy as np
import pandas as pd
import math

archivo_csv = "arbolado-en-espacios-verdes.csv"
df = pd.read_csv(archivo_csv)

jacarandas = df[df["nombre_com"] == "Jacarandá"]

# Cantidad de arboles de cada especie
cant_jacarandas = (df["nombre_com"] == "Jacarandá").sum()
print(cant_jacarandas)

borrachos = df[df["nombre_com"] == "Palo borracho rosado"]

cant_borrachos = (df["nombre_com"] == "Palo borracho rosado").sum()
print(cant_borrachos)

# altura maxima

altura_max_j = jacarandas["altura_tot"].max()
print(altura_max_j)

altura_max_b = borrachos["altura_tot"].max()
print(altura_max_b)

# altura minima

altura_min_j = jacarandas["altura_tot"].min()
print(altura_min_j)

altura_min_b = borrachos["altura_tot"].min()
print(altura_min_b)

# altura promedio

altura_prom_j = jacarandas["altura_tot"].mean()
print(altura_prom_j)

altura_prom_b = borrachos["altura_tot"].mean()
print(altura_prom_b)

# diametro maximo

altura_max_j = jacarandas["diametro"].max()
print(altura_max_j)

altura_max_b = borrachos["diametro"].max()
print(altura_max_b)

# diametro minimo

diametro_min_j = jacarandas["diametro"].min()
print(diametro_min_j)

diametro_min_b = borrachos["diametro"].min()
print(diametro_min_b)

# diametro promedio

diametro_prom_j = jacarandas["diametro"].mean()
print(diametro_prom_j)

diametro_prom_b = borrachos["diametro"].mean()
print(diametro_prom_b)

# Cantidad de arboles por parque

def cantidad_arboles_j(parque):
    return ((jacarandas["espacio_ve"]==parque).sum())

print("Jacarandas en el parque:", cantidad_arboles_j("ANDES, LOS"))

def cantidad_arboles_b(parque):
    return ((borrachos["espacio_ve"]==parque).sum())

print("Palos Borrachos en el parque:", cantidad_arboles_b("DE LAS VICTORIAS"))

# Cantidad Nativos

def cantidad_nativos(parque):
    return((df["espacio_ve"]==parque).sum())

print("arboles nativos por parque: ",cantidad_nativos("DE LAS VICTORIAS"))