# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import random
import copy
import csv
import numpy as np
import pandas as pd

a = [1,2,[6,7], 9]

b = copy.deepcopy(a)

dado = random.randint(1, 6)

print(dado)

prueba = random.random()
print(prueba)

#%%

print("hola mundo")

#%%

print("chau mundo")

#%%

# Abrir archivo

nombre_archivo = "datame.txt"
f = open(nombre_archivo, "rt")
data = f.read()

data_nuevo = "Este 2026 retomamos con nuestras ya clásicas charlas Datame \n \n" + data

data_nuevo = data_nuevo + "\nFin del comunicado"

datame = open("datame2026.txt", "w")

datame.write(data_nuevo)

datame.close()

f.close()

#%%

nombre_csv = "cronograma_sugerido.csv"

with open(nombre_csv, "rt") as file:
    materias = []
    for line in file:
        datos_linea= line.split(",")
        print(datos_linea)
        materias.append(datos_linea[1])
    print("\nEsta es la lista de materias:\n\n",materias)

f = open(nombre_csv)
filas = csv.reader(nombre_csv)
encabezado = next(filas)
    
f.close()

#%%


# Escribir una función generala_tirar() que simule una tirada de dados para el juego de la generala. Es decir, debe
#devolver una lista aleatoria de 5 valores de dados. Por ejemplo [2,3,2,1,6].

# *Opcional: Agregar al ejercicio generala_tirar() que además imprima en pantalla si salió poker, full, generala, escalera
# o ninguna de las anteriores. Por ejemplo, si sale 2,1,1,2,2 debe devolver [2,1,1,2,2] e imprimir en pantalla Full


def generala_tirar():
    tirada = []
    for i in range(5):
        dado=random.randint(1,6)
        tirada.append(dado)
        
    if (tirada == [2,1,1,2,2]):
        print("FULL!")
    if (tirada == [1,2,3,4,5]):
        print("ESCALERA!")
    elif(tirada == [2,3,4,5,6]):
        print("ESCALERA!")
        
    return tirada

print(generala_tirar())


# Escribir un programa que recorra las líneas del archivo ‘datame.txt’ e imprima solamente las líneas que contienen la
# palabra ‘estudiante’
 
            
#%%

# Numpy

M = np.array([[1,2,3],[5,4,-1],[2,0,8]])

def sustituir_elemento(M,e):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if (M[i][j]==e):
                M[i][j] = -1
            
    return M

print(sustituir_elemento(M, 2))

#%%

# Pandas

ruta_csv = "cronograma_sugerido.csv"

df = pd.read_csv(ruta_csv)


