from scripts.soporte import *


"""def prueba_chi_cuadrdado_uniforme(vector_nros_aleatorios_uniforme, cantidad_intervalos):
    minimo = min(vector_nros_aleatorios_uniforme)
    maximo = max(vector_nros_aleatorios_uniforme)
    vector_li, vector_ls, amplitud, vector_nro_intervalo = limites(minimo, maximo, cantidad_intervalos)
    vector_fo = frecuencia_obs(vector_nros_aleatorios_uniforme, vector_li, vector_ls, maximo)

    vector_fe, fe_menor_5 = frecuencia_esp_unif(len(vector_nros_aleatorios_uniforme), cantidad_intervalos)

    vector_fo_ag = None
    vector_fe_ag = None
    vec_intervalos_agrupados = None

    if fe_menor_5:
        vector_fe_ag, vector_fo_ag, vec_intervalos_agrupados = agrupamiento_fe(vector_fe, vector_fo)
        vector_chi = funcion_chi(vector_fo_ag, vector_fe_ag)
    else:
        vector_chi = funcion_chi(vector_fo, vector_fe)

    valor_chi = calcular_chi(vector_chi)

    data = {
        "vector_li": vector_li,
        "vector_ls": vector_ls,
        "vector_nro_intervalo": vector_nro_intervalo,
        "vector_fo": vector_fo,
        "vector_fe": vector_fe,
        "vector_fe_ag": vector_fe_ag,
        "vector_fo_ag": vector_fo_ag,
        "vector_int_ag": vec_intervalos_agrupados,
        "vector_chi": vector_chi,
        "valor_chi": valor_chi,
        "maximo": maximo,
        "minimo": minimo,
        "amplitud": amplitud,
        "fe_menor_5": fe_menor_5
    }

    return data"""


"""def prueba_chi_cuadrado_exponencal(vector_nros_aleatorios_expo, cantidad_intervalos, variable_select, valor_variable):

    minimo = min(vector_nros_aleatorios_expo)
    maximo = max(vector_nros_aleatorios_expo)
    vector_li, vector_ls, amplitud, vector_nro_intervalo = limites(minimo, maximo, cantidad_intervalos)
    vector_fo = frecuencia_obs(vector_nros_aleatorios_expo, vector_li, vector_ls, maximo)

    lambd = valor_variable
    if variable_select == 2:
        lambd = 1/valor_variable

    vector_fe, fe_menor_5 = frecuencia_esp_expo(vector_li, vector_ls, lambd, len(vector_nros_aleatorios_expo))

    vector_fo_ag = None
    vector_fe_ag = None
    vec_intervalos_agrupados = None

    if fe_menor_5:
        vector_fe_ag, vector_fo_ag, vec_intervalos_agrupados = agrupamiento_fe(vector_fe, vector_fo)
        vector_chi = funcion_chi(vector_fo_ag, vector_fe_ag)
    else:
        vector_chi = funcion_chi(vector_fo, vector_fe)

    valor_chi = calcular_chi(vector_chi)

    data = {
        "vector_li": vector_li,
        "vector_ls": vector_ls,
        "vector_nro_intervalo": vector_nro_intervalo,
        "vector_fo": vector_fo,
        "vector_fe": vector_fe,
        "vector_fe_ag": vector_fe_ag,
        "vector_fo_ag": vector_fo_ag,
        "vector_int_ag": vec_intervalos_agrupados,
        "vector_chi": vector_chi,
        "valor_chi": valor_chi,
        "maximo": maximo,
        "minimo": minimo,
        "amplitud": amplitud,
        "fe_menor_5": fe_menor_5
    }

    return data"""


"""def prueba_chi_cuadrado_normal(vector_nros_aleatorios_norm, cantidad_intervalos):
    minimo = min(vector_nros_aleatorios_norm)
    maximo = max(vector_nros_aleatorios_norm)
    vector_li, vector_ls, amplitud, vector_nro_intervalo = limites(minimo, maximo, cantidad_intervalos)
    vector_fo = frecuencia_obs(vector_nros_aleatorios_norm, vector_li, vector_ls, maximo)

    media = calc_media(vector_nros_aleatorios_norm)
    desviacion = calc_desviacion(vector_nros_aleatorios_norm, media)
    vector_fe, fe_menor_5 = frecuencia_esp_norm(vector_li, vector_ls, media, desviacion, len(vector_nros_aleatorios_norm))

    vector_fo_ag = None
    vector_fe_ag = None
    vec_intervalos_agrupados = None

    if fe_menor_5:
        vector_fe_ag, vector_fo_ag, vec_intervalos_agrupados = agrupamiento_fe(vector_fe, vector_fo)
        vector_chi = funcion_chi(vector_fo_ag, vector_fe_ag)
    else:
        vector_chi = funcion_chi(vector_fo, vector_fe)

    valor_chi = calcular_chi(vector_chi)
    data = {
        "vector_li": vector_li,
        "vector_ls": vector_ls,
        "vector_nro_intervalo": vector_nro_intervalo,
        "vector_fo": vector_fo,
        "vector_fe": vector_fe,
        "vector_fe_ag": vector_fe_ag,
        "vector_fo_ag": vector_fo_ag,
        "vector_int_ag": vec_intervalos_agrupados,
        "vector_chi": vector_chi,
        "valor_chi": valor_chi,
        "maximo": maximo,
        "minimo": minimo,
        "amplitud": amplitud,
        "fe_menor_5": fe_menor_5
    }

    return data"""


def prueba_ji_cuadrado(vector_nros_aleatorios, cantidad_intervalos,
                       tipo_dist, variable_expo=None, valor_variable_expo=None):
    maximo = (Decimal(max(vector_nros_aleatorios))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    print("maximo: ", maximo)
    minimo = (Decimal(min(vector_nros_aleatorios))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    print("minimo: ", minimo)
    vector_li, vector_ls, amplitud, vector_nro_intervalo = limites(minimo, maximo, cantidad_intervalos)
    print("amplitud ", amplitud)
    vector_fo = frecuencia_obs(vector_nros_aleatorios, vector_li, vector_ls, maximo)
    vector_fe = []

    fe_menor_5 = False
    if tipo_dist == 'uniforme':
        vector_fe, fe_menor_5 = frecuencia_esp_unif(len(vector_nros_aleatorios), cantidad_intervalos)

    elif tipo_dist == 'normal':
        media = calc_media(vector_nros_aleatorios)
        desviacion = calc_desviacion(vector_nros_aleatorios, media)
        vector_fe, fe_menor_5 = frecuencia_esp_norm(vector_li, vector_ls, media, desviacion,
                                                    len(vector_nros_aleatorios))
    elif tipo_dist == 'exponencial':
        lambd = valor_variable_expo
        if variable_expo == 2:
            lambd = (Decimal(1 / valor_variable_expo)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
        vector_fe, fe_menor_5 = frecuencia_esp_expo(vector_li, vector_ls, lambd, len(vector_nros_aleatorios))

    vector_fo_ag = None
    vector_fe_ag = None
    vec_intervalos_agrupados = None

    if fe_menor_5:
        vector_fe_ag, vector_fo_ag, vec_intervalos_agrupados = agrupamiento_fe(vector_fe, vector_fo)
        vector_chi = funcion_chi(vector_fo_ag, vector_fe_ag)
    else:
        vector_chi = funcion_chi(vector_fo, vector_fe)

    valor_chi = calcular_chi(vector_chi)
    data = {
        "vector_li": vector_li,
        "vector_ls": vector_ls,
        "vector_nro_intervalo": vector_nro_intervalo,
        "vector_fo": vector_fo,
        "vector_fe": vector_fe,
        "vector_fe_ag": vector_fe_ag,
        "vector_fo_ag": vector_fo_ag,
        "vector_int_ag": vec_intervalos_agrupados,
        "vector_chi": vector_chi,
        "valor_chi": valor_chi,
        "maximo": maximo,
        "minimo": minimo,
        "amplitud": amplitud,
        "fe_menor_5": fe_menor_5
    }

    return data
