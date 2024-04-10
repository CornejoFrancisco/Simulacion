from soporte import *


def prueba_chi_cuadrdado_uniforme(vector_nros_aleatorios_uniforme, cantidad_intervalos):
    minimo = min(vector_nros_aleatorios_uniforme)
    maximo = max(vector_nros_aleatorios_uniforme)
    vector_li, vector_ls, amplitud = limites(minimo, maximo, cantidad_intervalos)
    vector_fo = frecuencia_obs(vector_nros_aleatorios_uniforme, vector_li, vector_ls, maximo)
    vector_fe = [(len(vector_nros_aleatorios_uniforme)/cantidad_intervalos) for _ in range(cantidad_intervalos)]
    vector_chi = funcion_chi(vector_fo, vector_fe)
    valor_chi = calcular_chi(vector_chi)
    matriz = [vector_nros_aleatorios_uniforme, vector_li, vector_ls, vector_fo, vector_fe, vector_chi, valor_chi,
              cantidad_intervalos, minimo, maximo, amplitud]
    return matriz

def prueba_chi_cuadrado_exponencal(vector_nros_aleatorios_expo, cantidad_intervalos, variable_select, valor_variable):
    minimo = min(vector_nros_aleatorios_expo)
    maximo = max(vector_nros_aleatorios_expo)
    print("Encuentra minimo y maximo")
    vector_li, vector_ls, amplitud = limites(minimo, maximo, cantidad_intervalos)
    vector_fo = frecuencia_obs(vector_nros_aleatorios_expo, vector_li, vector_ls, maximo)
    lambd = valor_variable
    if variable_select == 2:
        lambd = 1/valor_variable
    vector_fe = frecuencia_esp_expo(vector_li, vector_ls, lambd, len(vector_nros_aleatorios_expo))
    vector_chi = funcion_chi(vector_fo, vector_fe)
    valor_chi = calcular_chi(vector_chi)
    matriz = [vector_nros_aleatorios_expo, vector_li, vector_ls, vector_fo, vector_fe, vector_chi, valor_chi,
              cantidad_intervalos, minimo, maximo, amplitud]
    return matriz

def prueba_chi_cuadrado_normal(vector_nros_aleatorios_norm, cantidad_intervalos, media, desviacion):
    minimo = min(vector_nros_aleatorios_norm)
    maximo = max(vector_nros_aleatorios_norm)
    vector_li, vector_ls, amplitud = limites(minimo, maximo, cantidad_intervalos)
    vector_fo = frecuencia_obs(vector_nros_aleatorios_norm, vector_li, vector_ls, maximo)
    vector_fe = frecuencia_esp_norm(vector_li, vector_ls, media, desviacion, len(vector_nros_aleatorios_norm))
    vector_chi = funcion_chi(vector_fo, vector_fe)
    valor_chi = calcular_chi(vector_chi)
    matriz = [vector_nros_aleatorios_norm, vector_li, vector_ls, vector_fo, vector_fe, vector_chi, valor_chi,
              cantidad_intervalos, minimo, maximo, amplitud]
    return matriz
