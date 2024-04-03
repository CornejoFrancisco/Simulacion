import random


def validad_positivo():
    cantidad = int(input("Ingrese el numero de cantidad de datos deseado: "))
    while cantidad <= 0:
         cantidad = int(input("Ingrese un numero positivo: "))
    return cantidad;

def carga_automatica(cantidad):
    vector = [];
    for i in range(cantidad):
        numero_random = random.uniform(0.0000,1.0000)
        vector.append(numero_random)
    return vector

def max(vector):
    numero_max = -1

    for i in vector:
        if i == 1:
            numero_max = i
        if numero_max < i:
            numero_max = i
    return numero_max

def min(vector):
    numero_min = 2
    for i in vector:
        if i == 1:
            numero_min = i
        if numero_min > i:
            numero_min = i
    return numero_min

def vector_cargado(cantidad):
    vector = carga_automatica(cantidad);
    return vector;

def media_datos(vector):
    suma_elementos = 0
    for i in vector:
        suma_elementos = suma_elementos + i
    cantidad_elementos = len(vector)
    media_elemt = suma_elementos/cantidad_elementos
    return media_elemt


def varianza_datos(vector):
    suma_cuadrados_diferencias = 0
    media = media_datos(vector)
    for x in vector:
        suma_cuadrados_diferencias += (x - media) ** 2
    varianza = suma_cuadrados_diferencias / len(vector)
    return varianza
def punto_2(vector):
    pass


def punto_3(vector):
    pass


def punto_4(vector):
    pass
