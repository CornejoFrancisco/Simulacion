from random import*





def validad_positivo(mensaje):
    cantidad = int(input(mensaje))
    while cantidad <= 0 and cantidad >= 1000000:
         cantidad = int(input("Ingrese un numero positivo: "))
    return cantidad;

def carga_automatica(cantidad):
    vector = []
    for i in range(cantidad):
        numero_random = random()
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
    vector = carga_automatica(cantidad)
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


def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)

    return matriz


def insersion_dato(matriz, li, ls, fo, fe):
    for fila in matriz:
        for j in fila:
            fila.append(li)
        matriz.append(fila)

    print(matriz)
    return matriz


#Esto lo que realiza es realizar los limites que se emplean para la observaciones
#de los datos
def limites(min, max, intervalo):
    vector_limites = []
    rango = max - min
    amplitud = rango / intervalo

    for i in range(intervalo):
        if i == 0:
            vector_limites.append([min, amplitud])

            nuevo_minimo = amplitud
            nuevo_maxio = amplitud + amplitud
        if i == (intervalo - 1):
            vector_limites.append([nuevo_minimo, max])

        elif i not in [0, intervalo - 1]:

            vector_limites.append([nuevo_minimo, nuevo_maxio])
            nuevo_minimo += amplitud
            nuevo_maxio = nuevo_minimo + amplitud
    return vector_limites


def contador_elementos(vector, vector_li_lf):
    contador_apariciones = []

    for limt in vector_li_lf:
        li, lf = limt[0], limt[1]
        contador = 0

        for i in vector:
            if i >= li and i <= lf:
                contador += 1

        contador_apariciones.append(contador)
    print(vector_li_lf)
    print(contador_apariciones)
    return contador_apariciones


def frecuencia_fo_fe(cantidad_apareciones, vector):
    vector_fo_fe = []
    for i in cantidad_apareciones:
        cantidad_fo = i/len(vector)
        cantidad_fe = 1/len(vector)
        vector_fo_fe.append([cantidad_fo,cantidad_fe])
    return vector_fo_fe



def matriz_muestra(vector, cantidad_intervalo, limites_li_lf, frecuencia_apareciones):
    print(vector)
    matriz = crear_matriz(cantidad_intervalo, 5)


def uniforme_calculadora(vector, variable_a, variable_b, cantidad_intervalo):
    minimo = min(vector)
    maximo = max(vector)
    matriz = crear_matriz(5, cantidad_intervalo)
    limites_li_lf = limites(minimo, maximo, cantidad_intervalo)
    cantidad_apareciones = contador_elementos(vector, limites_li_lf)
    frecuencia_apareciones = frecuencia_fo_fe(cantidad_apareciones, vector)
    matriz_muestra(vector, cantidad_intervalo, limites_li_lf, frecuencia_apareciones)
    return None


def punto_2(vector, variable_a, variable_b):
    if variable_a > variable_b:
        cantidad_intervalo = intervalo_valido()
        simulador_uniforme = uniforme_calculadora(vector, variable_a, variable_b, cantidad_intervalo)

    if variable_b > variable_a:
        cantidad_intervalo = intervalo_valido()



def punto_3_media(vector, media):
    pass

def punto_3_lambda(vector, v_lambda):
    pass

def punto_4(vector):
    pass
