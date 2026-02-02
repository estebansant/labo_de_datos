#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:13:10 2026

@author: Estudiante
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("transportes.csv")
df = pd.DataFrame(data)

df = df.drop(columns="Si querés dejar algún comentario, este es el espacio para hacerlo")

print(df.columns)

df = df["¿Cuál es el transporte que utilizó hoy para llegar a Ciudad Universitaria? \n- En caso de utilizar más de uno responder en base al trayecto final."]


numpy_arr = df.to_numpy()

print(numpy_arr)

plt.hist(numpy_arr)
plt.show()