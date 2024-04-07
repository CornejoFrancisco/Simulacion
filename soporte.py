import math
from random import *



def validad_positivo(mensaje):
    cantidad = int(input(mensaje))
    while cantidad <= 0 and cantidad >= 1000000:
         cantidad = int(input("Ingrese un numero positivo: "))
    return cantidad;

def insercion_cantidad():
    cantidad = int(input("Ingrese el tamaño de la muestra (entre 1 y 1000000): "))
    while cantidad <= 0 or cantidad > 1000000:
        cantidad = int(input("Error, valor fuera de rango (0,1000000], reingrese: "))
    vector = vector_cargado(cantidad)
    return vector


def vector_cargado(cantidad):
    vector = []
    for i in range(cantidad):
        numero_random = round(random(), 4)
        vector.append(numero_random)
    return vector



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

#Uniforme
def intervalo_valido():

    print("Cantidad de intervalos permitidos 10, 15, 20 y 25")
    intervalos = int(input("Ingrese cantidad de intervalos: "))
    while intervalos not in [10, 15, 20, 25]:
            intervalos = int(input("Ingrese una cantidad de intervalo permitido: "))
    return intervalos

def frecuencia_fo_fe(cantidad_apareciones, intervalo, n):
    vector_fo_fe = []
    for i in cantidad_apareciones:
        cantidad_fe = round(n/intervalo, 4)
        vector_fo_fe.append([cantidad_fe])
    return vector_fo_fe


def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)

    return matriz



#Esto lo que realiza es realizar los limites que se emplean para la observaciones
#de los datos
def limites(min, max, intervalo):
    vector_limites = []
    rango = max - min
    amplitud = round(rango / intervalo, 4)
    nuevo_minimo = min
    nuevo_maximo = nuevo_minimo + amplitud

    for i in range(intervalo):
        if i == 0:
            vector_limites.append([nuevo_minimo, nuevo_maximo])
            nuevo_minimo = round(nuevo_maximo, 4)
            nuevo_maximo = round(nuevo_minimo + amplitud, 4)

        elif 0 < i < intervalo - 1:
            vector_limites.append([nuevo_minimo, nuevo_maximo])
            nuevo_minimo = round(nuevo_maximo, 4)
            nuevo_maximo = round(nuevo_minimo + amplitud, 4)

        elif i == (intervalo - 1):
            vector_limites.append([nuevo_minimo, max])
    return vector_limites


def contador_elementos(vector, vector_li_lf, max):
    contador_apariciones = []
    for limt in vector_li_lf:
        li, lf = limt[0], limt[1]
        contador = 0
        for i in vector:
            if i >= li and i < lf:
                contador += 1
        if lf == max:
            contador += 1

        contador_apariciones.append(contador)
    return contador_apariciones

def vector_uniforme(vector, a, b):
    vector_uniforme = []
    for i in vector:
        rnd_uniforme = a + i * (b-a)
        vector_uniforme.append(round(rnd_uniforme, 4))
    return vector_uniforme


def funcion_chi(frecuencia_observada, frecuencia_esperada):
    vector = []

    for i in range(len(frecuencia_observada)):
        fo = frecuencia_observada[i]
        fe = frecuencia_esperada[i]
        chi_calc = pow((fo - fe), 2) / fe
        chi_calc_rounded = round(chi_calc, 4)
        vector.append(chi_calc_rounded)

    return vector


def calcular_chi(funcion_chi_vector):
    contador = 0
    for i in funcion_chi_vector:
        contador += i
    return round(contador, 4)


