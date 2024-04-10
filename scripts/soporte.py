from random import *
from scipy.stats import expon, norm
import pandas as pd
import math


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



# LIMITES
def limites(min, max, intervalo):
    vector_li = []
    vector_ls = []
    rango = round(max - min,4)
    amplitud = round(rango / intervalo, 4)
    nuevo_minimo = round(min, 4)
    nuevo_maximo = round(nuevo_minimo + amplitud, 4)

    for i in range(intervalo):
        if i == 0:
            vector_li.append(nuevo_minimo)
            vector_ls.append(nuevo_maximo)
            nuevo_minimo = round(nuevo_maximo, 4)
            nuevo_maximo = round(nuevo_minimo + amplitud, 4)

        elif 0 < i < intervalo - 1:
            vector_li.append(nuevo_minimo)
            vector_ls.append(nuevo_maximo)
            nuevo_minimo = round(nuevo_maximo, 4)
            nuevo_maximo = round(nuevo_minimo + amplitud, 4)

        elif i == (intervalo - 1):
            vector_li.append(nuevo_minimo)
            vector_ls.append(nuevo_maximo)
    return vector_li, vector_ls, amplitud


# FRECUENCIAS
def frecuencia_obs(vector,vector_li, vector_ls, max):
    contador_apariciones = []
    for i in range(len(vector_li)):
        li = vector_li[i]
        ls = vector_ls[i]
        contador = 0

        for i in vector:
            if i >= li and i < ls:
                contador += 1
        if ls == max:
            contador += 1
        contador_apariciones.append(contador)

    return contador_apariciones

def frecuencia_esp_expo(vector_li, vector_ls, lambd, n):
    vector_fe = []
    for i in range(len(vector_li)):
        li = vector_li[i]
        ls = vector_ls[i]
        fe = round((expon.cdf(ls, scale= 1/lambd ) - (expon.cdf(li, scale= 1/lambd) )) * n, 4)
        vector_fe.append(fe)
    return vector_fe

def frecuencia_esp_norm(vector_li, vector_ls, media, desviacion, n):
    vector_fe = []
    for i in range(len(vector_li)):
        li = vector_li[i]
        ls = vector_ls[i]
        fe = round(((norm.cdf(ls, loc=media, scale=desviacion)) - (norm.cdf(li, loc=media, scale=desviacion))) * n, 4)
        vector_fe.append(fe)
    return vector_fe

# GENERADORES
def generar_vector_uniforme(a, b, cantidad_nros):
    vector_uniforme = []
    for i in range(cantidad_nros):
        rnd = round(random(), 4)
        rnd_uniforme = a + rnd * (b-a)
        vector_uniforme.append(round(rnd_uniforme, 4))
    return vector_uniforme

def generador_vector_exponencial(variable_select, valor_variable, cantidad_nros):
    vector_exponencial = []
    if variable_select == 1:
        for i in range(cantidad_nros):
            rnd = round(random(),4)
            if rnd >= 1:
                rnd_expo = -(1/valor_variable)*(math.log(1-0.9999))
                vector_exponencial.append(round(rnd_expo, 4))
            else:
                rnd_expo = -(1 / valor_variable) * (math.log(1 - rnd))
                vector_exponencial.append(round(rnd_expo, 4))
    elif variable_select == 2:
        rnd = random()
        for i in range(cantidad_nros):
            if rnd >= 1:
                rnd_expo = -valor_variable * (math.log(1 - 0.9999))
                vector_exponencial.append(round(rnd_expo, 4))
            else:
                rnd_expo = -valor_variable * (math.log(1 - rnd))
                vector_exponencial.append(round(rnd_expo, 4))
    return vector_exponencial


def generar_vector_normal(cantidad_nros_aleatorios, desviacion, media):
    vector_normal = []
    vueltas = cantidad_nros_aleatorios // 2
    print(vueltas)
    for i in range(vueltas):
        rnd1, rnd2 = random(), random()
        n1 = (math.sqrt(-2 * math.log(rnd1)) *
                math.cos(2 * math.pi * rnd2)) * desviacion + media
        n2 = (math.sqrt(-2 * math.log(rnd1)) *
                math.sin(2 * math.pi * rnd2)) * desviacion + media
        vector_normal.append(round(n1, 4))
        vector_normal.append(round(n2, 4))
        if i == vueltas-1 and cantidad_nros_aleatorios % 2 != 0:
            n1 = (math.sqrt(-2 * math.log(rnd1)) *
                  math.cos(2 * math.pi * rnd2)) * desviacion + media
            vector_normal.append(round(n1, 4))

    print(len(vector_normal))
    return vector_normal


# CALCULOS CHI
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

# OTROS
def create_data_frame(matriz):
    head = ["rnd_expo", "li", "ls", "fo", "fe", "((O-E)^2)/E"]
    df = pd.DataFrame(
        list(
            zip(matriz[0], matriz[1], matriz[2], matriz[3], matriz[4], matriz[5])
        ),
        columns=head
    )
    return df


