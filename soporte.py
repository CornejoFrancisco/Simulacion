import math
from random import*



def validad_positivo(mensaje):
    cantidad = int(input(mensaje))
    while cantidad <= 0 and cantidad >= 1000000:
         cantidad = int(input("Ingrese un numero positivo: "))
    return cantidad;

def vector_cargado(cantidad):
    vector = []
    for i in range(cantidad):
        numero_random = random()
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

def frecuencia_fo_fe(cantidad_apareciones, intervalo):
    vector_fo_fe = []
    for i in cantidad_apareciones:
        cantidad_fo = i/intervalo
        cantidad_fe = 1/intervalo
        vector_fo_fe.append([cantidad_fo,cantidad_fe])
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
    amplitud = rango / intervalo

    for i in range(intervalo):
        if i == 0:
            vector_limites.append([min, amplitud + min])

            nuevo_minimo = amplitud + min
            nuevo_maxio = amplitud + amplitud + min
        if i == (intervalo - 1):
            vector_limites.append([nuevo_minimo, max])

        elif i not in [0, intervalo - 1]:

            vector_limites.append([nuevo_minimo, nuevo_maxio])
            nuevo_minimo += amplitud
            nuevo_maxio = nuevo_minimo + amplitud
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
        vector_uniforme.append(a + i * (b-a))
    return vector_uniforme


def funcion_chi_uniforme(frecuencia):
    vector = []

    for i in frecuencia:
        fo, fe = i[0], i[1]
        calculo = ((fo - fe) * (fo - fe)) / fe
        vector.append(calculo)
    return vector


def calcular_chi(funcion_chi_vector):
    contador = 0
    for i in funcion_chi_vector:
        contador += i
    return contador



def punto_4(vector):
    pass
