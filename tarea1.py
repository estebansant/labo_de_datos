#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 09:45:36 2026

@author: estebansant
"""

import pandas as pd

empleado_01 = [
        [20222333, 45, 2, 20000],
        [33456234, 40, 0, 25000],
        [45432345, 41, 1, 10000]
    ]

def superanSalarioActividad01(matriz, umbral):
    res = []
    for persona in matriz:
        if (persona[3] > umbral):
            res.append(persona)
    
    return res



print("Empleado 1", superanSalarioActividad01(empleado_01, 15000))

empleado_02 = [
        [20222333, 45, 2, 20000],
        [33456234, 40, 0, 25000],
        [45432345, 41, 1, 10000],
        [43967304, 37, 0, 12000],
        [42236276, 36, 0, 18000]
    ]

print("Empleado 2", superanSalarioActividad01(empleado_02, 15000))

empleado_03 = [
        [20222333, 20000, 45, 2],
        [33456234, 25000, 40, 0],
        [45432345, 10000, 41, 1],
        [43967304, 12000, 37, 0],
        [42236276, 18000, 36, 0]
    ]

def superanSalarioActividad03(matriz, umbral):
    res = []
    for persona in matriz:
        if (persona[1] > umbral):
            res.append(persona)
    
    for elem in res:
        item = elem.pop(1)
        elem.insert(3, item)
            
    return res

print("3",superanSalarioActividad03(empleado_03, 15000))

empleado_temp = [
        [20222333, 20000, 45, 2],
        [33456234, 25000, 40, 0],
        [45432345, 10000, 41, 1],
        [43967304, 12000, 37, 0],
        [42236276, 18000, 36, 0]
    ]

col_dni = []
col_salario = []
col_edad = []
col_hijos = []

for fila in empleado_temp:
    col_dni.append(fila[0])
    col_salario.append(fila[1])
    col_edad.append(fila[2])
    col_hijos.append(fila[3])


empleado_04 = [col_dni, col_salario, col_edad, col_hijos]
print("empleado 4", empleado_04)

print("---------")
print(superanSalarioActividad01(empleado_04, 15000))
print("---------")

print(superanSalarioActividad03(empleado_04, 15000))

def superanSalarioActividad04(matriz, umbral):
    res = []
    cont = 0
    while cont <=len(matriz):
        fila = []
        for i in range(len(matriz)):
            fila.append(matriz[i][cont])
        res.append(fila)    
        cont += 1
        
    return superanSalarioActividad03(res,umbral)

print("---------")
print("salarios 04",superanSalarioActividad04(empleado_04, 15000))


            