# -*- coding: utf-8 -*-
"""
@author: Clara
"""

# %% Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns


# %% WINE DATASET

# Import file
wine = pd.read_csv('/home/Estudiante/Documentos/clase6/Archivos/wine.csv', sep=";")
# wine = pd.read_csv('wine.csv', sep=";")

# Display the first few rows of the DataFrame
print(wine.head())

# %% SCATTER PLOT Acidez vs Contenido de acido citrico

fig, ax = plt.subplots()

wine_blanco = wine[wine['type']=='white']
wine_tinto = wine[wine['type']=='red']
ax.scatter(
    data=wine_blanco,
    x='fixed acidity',
    y='citric acid',
    s=8,
    color='yellow',
    edgecolor='k',
    label='blanco'
)

ax.scatter(
    data=wine_tinto,
    x='fixed acidity',
    y='citric acid',
    s=8,
    color='red',
    edgecolor='purple',
    label='tinto'
)

ax.set_title('Acidez vs contenido de ácido cítrico')
ax.set_xlabel('Acidez (g/dm³)', fontsize=12)
ax.set_ylabel('Ácido cítrico (g/dm³)', fontsize=12)
ax.legend()

plt.show()

# %% EJERCICIO VINO
# ¿Existe o no alguna relación entre el pH de los vinos (pH) 
# y alguna de las otras variables? Mostrarlo gráficamente 


wine_ph = wine['pH']
wine_acidity = wine['fixed acidity']

fig, ax = plt.subplots()

ax.scatter(
    data=wine,
    x='pH',
    y='fixed acidity')

ax.set_title('pH vs acidez')
ax.set_xlabel('pH', fontsize=12)
ax.set_ylabel('Acidez', fontsize=12)
ax.legend()

plt.show()

#-----------



for col in wine.columns:
    
    if col != 'pH':  # evitamos graficar pH contra pH
        
        fig, ax = plt.subplots()

        ax.scatter(
            data=wine,
            x='pH',
            y=col)

        ax.set_title(f'pH vs {col}')
        ax.set_xlabel('pH', fontsize=12)
        ax.set_ylabel(col, fontsize=12)
        ax.legend()

        plt.show()




# %% CHEETAH REGIONS                              #

# Cargamos el dataset
cheetahRegion= pd.read_csv("cheetahRegion.csv")

#%% GRAFICO DE LINEAS
# Genera el grafico de la serie temporal (grafico por defecto)
plt.scatter(data=cheetahRegion, x='Anio', y='Ventas')

# Genera el grafico de la serie temporal (mejorando la informacion mostrada)
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           

ax.plot('Anio', 'Ventas', data=cheetahRegion, marker="o")

ax.set_title('Ventas de la compañía Cheetah Sports')
ax.set_xlabel('Año', fontsize='medium')                       
ax.set_ylabel('Ventas (millones de $)', fontsize='medium')    
ax.set_xlim(0, 12)
ax.set_ylim(0, 250)

# %% EJERCICIO BIODIESEL
#Considerar los siguientes datos correspondientes a los precios del 
#biodiesel en distintos períodos en la Argentina
#(se encuentran subidos en el campus)






# %% GRAFICO DE BARRAS (BAR PLOT)

#### Genera el grafico de barras de las ventas mensuales (grafico por defecto)
fig, ax = plt.subplots()

ax.bar(data=cheetahRegion, x='Anio', height='Ventas')

#### Genera el grafico de barras de las ventas mensuales (mejorando la informacion mostrada)
fig, ax = plt.subplots()       

ax.bar(data=cheetahRegion, x='Anio', height='Ventas')
       
ax.set_title('Ventas de la compañía Cheetah Sports')
ax.set_xlabel('Año', fontsize='medium')                       
ax.set_ylabel('Ventas (millones de $)', fontsize='medium')    
ax.set_xlim(0, 11)
ax.set_ylim(0, 250)

ax.set_xticks(range(1,11,1))               # Muestra todos los ticks del eje x
ax.set_yticks([])                          # Remueve los ticks del eje y
ax.bar_label(ax.containers[0], fontsize=8)   # Agrega la etiqueta a cada barra

#%% 10. PIE PLOT

# Contamos cuantos vinos de cada tipo hay en el dataset
wine['type'].value_counts()

# Transformamos la salida de value_counts en
# un dataframe
conteos = pd.DataFrame(wine['type'].value_counts()).reset_index()
conteos.columns = ['type', 'count']

# Genera el grafico de barras torta (mejorando la informacion mostrada)
fig, ax = plt.subplots()

ax.pie(data=conteos, 
       x='count', 
       labels='type',          # Etiquetas
       autopct='%1.2f%%',       # porcentajes
       colors=['gold',
               'purple'],
       shadow = True, 
       explode = (0.1,0)        # separa las slices del pie plot
       )

#%% EJERCICIO Telefonos
# Sean los siguientes datos correspondientes a 
# poseedores de teléfonos 
# (se encuentran subidos en el campus) 


# Generar un gráfico para representarlos gráficamente
# Analizar los resultados obtenidos
# Discutir con el resto de la clase
# ¿Cuál fue su objetivo: Explorar, Explicar, Otro?
# ¿Qué tipos de variables estaban en juego?
# ¿Qué tipo de gráfico decidió utilizar?
# ¿Qué resultados obtuvo?
# ¿Mejoró alguna característica del gráfico para cumplir con el objetivo?
# Responder Verdadero o Falso y justificar visualmente. 
# “Es más probable que las personas mayores posean un teléfono 
# inteligente a que las personas más jóvenes posean uno inteligente.”






# %% DISTRIBUCION DE DATOS CATEGORICOS

#### Cargamos dataset gaseosas
gaseosas= pd.read_csv("gaseosas.csv")

# Mostramos las primeras observaciones
gaseosas.head()

# Tabla de frecuencias
gaseosas['Compras_gaseosas'].value_counts()    

##### Genera el grafico de frecuencias (grafico por defecto)
gaseosas['Compras_gaseosas'].value_counts().plot.bar()

#### Genera el grafico de frecuencias mejorado

plt.rcParams['axes.spines.right'] = False            # Elimina linea derecha  del recuadro
plt.rcParams['axes.spines.left']  = False            # Elimina linea izquierda  del recuadro
plt.rcParams['axes.spines.top']   = False            # Elimina linea superior del recuadro

fig, ax = plt.subplots()
gaseosas['Compras_gaseosas'].value_counts().plot.bar(ax = ax)

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title('Frecuencia Venta de Gaseosas')
ax.set_xlabel('Marcas de gaseosas') 
ax.set_yticks([])                                  # Remueve los ticks del eje y
ax.bar_label(ax.containers[0], fontsize=8)         # Agrega la etiqueta a cada barra
ax.tick_params(axis='x', labelrotation=0)          # Rota las etiquetas del eje x
                                                    # para que las muestre horizontales
plt.show()      

# %% DISTRIBUCION DE DATOS CONTINUOS

ageAtDeath= pd.read_csv("/home/Estudiante/Documentos/clase6/Archivos/ageAtDeath.csv")

#### Genera el grafico de frecuencias

#Graficar la distribucion usando seaborn
plt.figure(figsize=(8, 6))
sns.histplot(ageAtDeath['AgeAtDeath'], kde=True, bins=16, color='purple') # kde=True agrega la curva de densidad

plt.title('Distribución de edades al momento de muerte')
plt.xlabel('Edad al momento de muerte (años)')
plt.ylabel('Cantidad de personas')

# Mostrar el grafico
plt.show()

#%% DISTRIBUCION DE DATOS CONTINUOS SEGUN DOS VARIABLES

sns.histplot(data=ageAtDeath, x='AgeAtDeath', hue='Sex', kde=False)#hue='Sex' separa los datos por ese atributo

plt.title('Distribución de Edad al Morir por Sexo')
plt.xlabel('Edad al momento de la muerte (años)')
plt.ylabel('Cantidad de Personas')
plt.show()

# %% DISTRIBUCION DE DATOS CONTINUOS SEGUN DOS VARIABLES en forma de linea

# Suponiendo que tu DataFrame se llama df
sns.kdeplot(data=ageAtDeath, x='AgeAtDeath', hue='Sex')

plt.title('Distribución de Edad al Morir (Suavizada)')
plt.xlabel('Edad')
plt.ylabel('Densidad de Frecuencia')
plt.show()

# %% EJERCICIO Propinas
# Sean los datos correspondientes a las propinas de un bar 
# (están cargados en el campus en el archivo tips.csv)
# Generar un gráfico para analizar la distribución de la propina en función del:
# Sexo
# Día de la semana
# Comentar los resultados obtenidos


tips= pd.read_csv("/home/Estudiante/Documentos/clase6/Archivos/tips.csv")

plt.figure(figsize=(8, 6))



for i in range(len(tips['day'])):
    if tips['day'][i] == 'Sun':
        tips['day'][i] = 7
    elif tips['day'][i] == 'Sat':
        tips['day'][i] = 6
    elif tips['day'][i] == 'Fri':
        tips['day'][i] = 5
    elif tips['day'][i] == 'Thur':
        tips['day'][i] = 4
    elif tips['day'][i] == 'Wed':
        tips['day'][i] = 3
    elif tips['day'][i] == 'Tue':
        tips['day'][i] = 2
    elif tips['day'][i] == 'Mon':
        tips['day'][i] = 1
        
        
sns.histplot(data=tips, x='day', hue='sex', kde=False) # kde=True agrega la curva de densidad

sns.kdeplot(data=tips, x='day', hue='sex')

#plt.title('Propinas para cada sexo por dia de la semana')
# #plt.xlabel('Dia')
# ax.set_xticks([1,2,3,4,5,6,7])               # Muestra todos los ticks del eje x
# #plt.ylabel('Propina')

#%%

fig, ax = plt.subplots()
x = tips['tip']
mujeres = tips[tips['sex'] == 'Female']
hombres = tips[tips['sex'] == 'Male']
width = 0.4
#ax.bar(x - width/2, mujeres, width=width, label='Mujeres')
#ax.bar(x + width/2, hombres, width=width, label='Hombres')
ax.set_title('Propinas por sexo y dia de la semana')
ax.set_xlabel('Dia')
ax.set_xticks([1,2,3,4,5,6,7])
ax.set_xticklabels(['Lun','Mar','Mie','Jue','Vie','Sab','Dom'])
ax.set_ylabel('Cantidad')
ax.legend()
plt.show()

