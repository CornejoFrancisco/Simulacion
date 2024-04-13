from scripts.soporte import *


def prueba_chi_cuadrdado_uniforme(vector_nros_aleatorios_uniforme, cantidad_intervalos):
    minimo = min(vector_nros_aleatorios_uniforme)
    maximo = max(vector_nros_aleatorios_uniforme)
    vector_li, vector_ls, amplitud = limites(minimo, maximo, cantidad_intervalos)
    vector_fo = frecuencia_obs(vector_nros_aleatorios_uniforme, vector_li, vector_ls, maximo)
    vector_fe = [(len(vector_nros_aleatorios_uniforme)/cantidad_intervalos) for _ in range(cantidad_intervalos)]
    vector_chi = funcion_chi(vector_fo, vector_fe)
    valor_chi = calcular_chi(vector_chi)

    data = {
        "vector_li": vector_li,
        "vector_ls": vector_ls,
        "vector_fo": vector_fo,
        "vector_fe": vector_fe,
        "vector_chi": vector_chi,
        "valor_chi": valor_chi,
        "maximo": maximo,
        "minimo": minimo,
        "amplitud": amplitud
    }

    return data


def prueba_chi_cuadrado_exponencal(vector_nros_aleatorios_expo, cantidad_intervalos, variable_select, valor_variable):

    minimo = min(vector_nros_aleatorios_expo)
    maximo = max(vector_nros_aleatorios_expo)
    vector_li, vector_ls, amplitud = limites(minimo, maximo, cantidad_intervalos)
    vector_fo = frecuencia_obs(vector_nros_aleatorios_expo, vector_li, vector_ls, maximo)
    lambd = valor_variable
    if variable_select == 2:
        lambd = 1/valor_variable
    print(lambd)
    vector_fe = frecuencia_esp_expo(vector_li, vector_ls, lambd, len(vector_nros_aleatorios_expo))
    vector_new_fe, vector_new_fo = agrupamiento_fe(vector_fe, vector_fo)

    vector_chi = funcion_chi(vector_new_fo, vector_new_fe)
    valor_chi = calcular_chi(vector_chi)
    data = {
        "vector_li": vector_li,
        "vector_ls": vector_ls,
        "vector_fo": vector_fo,
        "vector_fe": vector_fe,
        "vector_fe_ag": vector_new_fe,
        "vector_fo_ag": vector_new_fo,
        "vector_chi": vector_chi,
        "valor_chi": valor_chi,
        "maximo": maximo,
        "minimo": minimo,
        "amplitud": amplitud
    }

    return data


def prueba_chi_cuadrado_normal(vector_nros_aleatorios_norm, cantidad_intervalos):
    minimo = min(vector_nros_aleatorios_norm)
    maximo = max(vector_nros_aleatorios_norm)
    vector_li, vector_ls, amplitud = limites(minimo, maximo, cantidad_intervalos)
    vector_fo = frecuencia_obs(vector_nros_aleatorios_norm, vector_li, vector_ls, maximo)
    media = calc_media(vector_nros_aleatorios_norm)
    desviacion = calc_desviacion(vector_nros_aleatorios_norm, media)

    vector_fe = frecuencia_esp_norm(vector_li, vector_ls, media, desviacion, len(vector_nros_aleatorios_norm))
    vector_new_fe, vector_new_fo = agrupamiento_fe(vector_fe, vector_fo)

    vector_chi = funcion_chi(vector_new_fo, vector_new_fe)
    valor_chi = calcular_chi(vector_chi)
    data = {
        "vector_li": vector_li,
        "vector_ls": vector_ls,
        "vector_fo": vector_fo,
        "vector_fe": vector_fe,
        "vector_fe_ag": vector_new_fe,
        "vector_fo_ag": vector_new_fo,
        "vector_chi": vector_chi,
        "valor_chi": valor_chi,
        "maximo": maximo,
        "minimo": minimo,
        "amplitud": amplitud
    }
    return data
