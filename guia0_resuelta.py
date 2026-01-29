# Ejercicio 1

espesor_billete = 1.1*10**(-4) # 0.11mm Expresado en metros

cont = 1
dia = 1

pila_billetes = cont * espesor_billete

while pila_billetes < 67.5:
    cont = cont * 2
    pila_billetes = cont * espesor_billete
    dia += 1
    
print(dia)
print(pila_billetes)
print(cont)
    

# Ejercicio 2

cadena = 'Casa'
cadena_geringosa = ''

for c in cadena:
    cadena_geringosa += c
    
    if c.lower() in 'aeiou':
        cadena_geringosa += 'p' + c.lower()

print(cadena_geringosa)

# Ejercicio 3

def pertenece(lista, e):
    if e in lista:
        return True
    else:
        return False
    
lista = [1,2,3,4,5]
print(pertenece(lista, '1'))

# Ejercicio 4

def mas_larga(lista1, lista2):
    if (len(lista1) > len(lista2)):
        return lista1
    elif(len(lista1) < len(lista2)):
        return lista2
    else:
        return "ambas listas tienen igual longitud"
    
lista1= [1,2,3,4,5]
lista2=[1,2,3]

print(mas_larga(lista1,lista2))

# Ejercicio 5

altura = 100

def piques(altura):
    rebotes = []
    cont = 0

    while (altura > 0) and (cont<10):
        operacion = altura*(3/5)
        rebotes.append(operacion)
        altura = operacion
        cont+=1
    return rebotes

print("Rebotes", piques(altura))

# Ejercicio 6

def mezclar(cadena1, cadena2):
    min_len = min(len(cadena1), len(cadena2))
    resultado = ""
    for i in range(min_len):
        resultado += cadena1[i] + cadena2[i]
    resultado += cadena1[min_len:] + cadena2[min_len:]
    return resultado

print(mezclar("atun", "sol"))

# Ejercicio 7

saldo = 500000.0
tasa = 0.05 / 12  # Tasa mensual
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0

while saldo > 0:
    mes += 1
    saldo = saldo * (1 + tasa) 
    
    if pago_mensual > saldo:
        pago_mensual = saldo
        saldo = 0
    else:
        saldo = saldo - pago_mensual

    total_pagado += pago_mensual

print(f"Total pagado: ${total_pagado} en {mes} meses")

# Ejercicio 8

def geringosidad(palabra):
    palabra_geringosa = ''
    for p in palabra:
        palabra_geringosa += p
        
        if p.lower() in 'aeiou':
            palabra_geringosa += 'p' + p.lower()
    return palabra_geringosa

def traductor_geringoso(lista):
    dict = {}
    for i in range(len(lista)):
        dict[lista[i]] = geringosidad(lista[i])
    return dict

print(traductor_geringoso(['banana', 'manzana', 'mandarina']))



        
    
