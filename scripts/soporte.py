from random import *
from scipy.stats import expon, norm
import pandas as pd
import math
from decimal import ROUND_HALF_UP, Decimal


def calc_media(vector):
    return (Decimal(sum(vector)/len(vector))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)


def calc_desviacion(vector, media):
    suma_dif_cuadrados = 0
    for x in vector:
        suma_dif_cuadrados += pow((x - media), 2)
    var_s = suma_dif_cuadrados/(len(vector) - 1)
    return (Decimal(math.sqrt(var_s))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)


# LIMITES
def limites(min, max, intervalo):
    vector_li = []
    vector_ls = []
    vector_nro_intervalo = []
    rango = (Decimal(max - min)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    print(rango)
    amplitud = (Decimal(rango/intervalo)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    nuevo_minimo = (Decimal(min)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    nuevo_maximo = (Decimal(nuevo_minimo + amplitud)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)

    for i in range(intervalo):
        vector_nro_intervalo.append(i + 1)
        if i == 0:
            vector_li.append(nuevo_minimo)
            vector_ls.append(nuevo_maximo)
            nuevo_minimo = (Decimal(nuevo_maximo)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
            nuevo_maximo = (Decimal(nuevo_minimo + amplitud)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)

        elif 0 < i < intervalo - 1:
            vector_li.append(nuevo_minimo)
            vector_ls.append(nuevo_maximo)
            nuevo_minimo = (Decimal(nuevo_maximo)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
            nuevo_maximo = (Decimal(nuevo_minimo + amplitud)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)

        elif i == (intervalo - 1):
            vector_li.append(nuevo_minimo)
            vector_ls.append(nuevo_maximo)
    return vector_li, vector_ls, amplitud, vector_nro_intervalo


# FRECUENCIAS
def frecuencia_obs(vector, vector_li, vector_ls, maximo):
    contador_apariciones = []
    for i in range(len(vector_li)):
        li = vector_li[i]
        ls = vector_ls[i]
        contador = 0

        for i in vector:
            if i >= li and i < ls:
                contador += 1
        if ls == maximo:
            contador += 1
        contador_apariciones.append(contador)

    return contador_apariciones


def frecuencia_esp_unif(cantidad_nros, cantidad_intervalos):
    fe = (Decimal(cantidad_nros / cantidad_intervalos)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    fe_menor_5 = False
    if fe < 5:
        fe_menor_5 = True
    vector_fe = cantidad_intervalos * [fe]
    return vector_fe, fe_menor_5


def frecuencia_esp_expo(vector_li, vector_ls, lambd, n):
    vector_fe = []
    fe_menor_5 = False
    for i in range(len(vector_li)):
        li = float(vector_li[i])
        ls = float(vector_ls[i])
        lambd = float(lambd)
        fe = (expon.cdf(ls, scale=1/lambd) - (expon.cdf(li, scale=1/lambd))) * n
        vector_fe.append((Decimal(fe)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
        if fe < 5:
            fe_menor_5 = True
    return vector_fe, fe_menor_5


def frecuencia_esp_norm(vector_li, vector_ls, media, desviacion, n):
    vector_fe = []
    fe_menor_5 = False
    for i in range(len(vector_li)):

        li = float(vector_li[i])
        ls = float(vector_ls[i])
        media = float(media)
        desviacion = float(desviacion)
        n = float(n)

        fe = (norm.cdf(ls, loc=media, scale=desviacion) - norm.cdf(li, loc=media, scale=desviacion)) * n
        vector_fe.append((Decimal(fe)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
        if fe < 5:
            fe_menor_5 = True
    return vector_fe, fe_menor_5


def agrupamiento_fe(vec_f, vec_o):
    vec_agrupados = []
    vec_oac = []
    vec_int_i = []
    vec_int_s = []
    vec_int_agrupados = []
    suma = 0
    acum = 0
    primero = True

    for i in range(len(vec_f)):
        x = vec_f[i]
        suma = (Decimal(suma + x)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
        acum = (Decimal(vec_o[i])).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)

        if primero:
            vec_int_i.append(i)
            primero = False

        if suma >= 5:
            vec_agrupados.append((Decimal(suma)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
            vec_oac.append((Decimal(acum)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
            suma = 0
            acum = 0
            vec_int_s.append(i)
            primero = True

        elif 0 < suma < 5 and i == len(vec_f) - 1:
            vec_agrupados[-1] += (Decimal(suma)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
            vec_oac[-1] += (Decimal(acum)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
            del vec_int_i[-1]
            vec_int_s[-1] = i

    for i in range(len(vec_int_s)):
        inicial = vec_int_i[i]
        final = vec_int_s[i]
        if inicial != final:
            intervalo = f"{inicial + 1} - {final + 1}"
            vec_int_agrupados.append(intervalo)
        elif inicial == final:
            intervalo = f"{inicial + 1}"
            vec_int_agrupados.append(intervalo)

    return vec_agrupados, vec_oac, vec_int_agrupados


# GENERADORES
def generar_vector_uniforme(a, b, cantidad_nros):
    vector_uniforme = []
    for i in range(cantidad_nros):
        rnd = random()
        rnd_uniforme = a + rnd * (b-a)
        vector_uniforme.append((Decimal(rnd_uniforme)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
    return vector_uniforme


def generador_vector_exponencial(variable_select, valor_variable, cantidad_nros):
    vector_exponencial = []
    if variable_select == 1:
        for i in range(cantidad_nros):
            rnd = random()
            rnd_expo = -(1 / valor_variable) * (math.log(1 - rnd))
            vector_exponencial.append((Decimal(rnd_expo)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
    elif variable_select == 2:
        for i in range(cantidad_nros):
            rnd = random()
            rnd_expo = -valor_variable * (math.log(1 - rnd))
            vector_exponencial.append((Decimal(rnd_expo)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
    return vector_exponencial


def generar_vector_normal(cantidad_nros_aleatorios, desviacion, media):
    vector_normal = []
    vueltas = cantidad_nros_aleatorios // 2
    for i in range(vueltas):
        rnd1, rnd2 = random(), random()
        n1 = (math.sqrt(-2 * math.log(rnd1)) *
                math.cos(2 * math.pi * rnd2)) * desviacion + media
        n2 = (math.sqrt(-2 * math.log(rnd1)) *
                math.sin(2 * math.pi * rnd2)) * desviacion + media
        vector_normal.append((Decimal(n1)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
        vector_normal.append((Decimal(n2)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))

        if i == vueltas-1 and cantidad_nros_aleatorios % 2 != 0:
            n1 = (math.sqrt(-2 * math.log(rnd1)) *
                  math.cos(2 * math.pi * rnd2)) * desviacion + media
            vector_normal.append((Decimal(n1)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))

    return vector_normal


# CALCULOS CHI
def funcion_chi(frecuencia_observada, frecuencia_esperada):
    vector = []

    for i in range(len(frecuencia_observada)):
        fo = frecuencia_observada[i]
        fe = frecuencia_esperada[i]
        chi_calc = pow((fo - fe), 2) / fe
        vector.append((Decimal(chi_calc)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))

    return vector

def calcular_chi(funcion_chi_vector):
    contador = 0
    for i in funcion_chi_vector:
        contador += i
    return (Decimal(contador)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)

# OTROS


def create_df_final(dict_data):
    minimo = dict_data["minimo"]
    maximo = dict_data["maximo"]
    amplitud = dict_data["amplitud"]
    vector_li = dict_data["vector_li"]
    vector_ls = dict_data["vector_ls"]
    vector_nro_intervalo = dict_data["vector_nro_intervalo"]
    vector_fo = dict_data["vector_fo"]
    vector_fe = dict_data["vector_fe"]
    vector_int_ag = dict_data["vector_int_ag"]
    vector_fo_ag = dict_data["vector_fo_ag"]
    vector_fe_ag = dict_data["vector_fe_ag"]
    vector_chi = dict_data["vector_chi"]
    valor_chi = dict_data["valor_chi"]
    fe_menor_5 = dict_data["fe_menor_5"]

    vector_relleno_frecuencias = ["" for i in range(len(vector_li) - 1)]

    if fe_menor_5:
        vector_relleno_frecuencias_agrupadas = ["" for i in range(len(vector_li) - len(vector_int_ag))]
        vector_relleno_valor_una_fila = ["" for i in range(len(vector_li) - 1)]
        vector_int_ag += vector_relleno_frecuencias_agrupadas
        vector_fo_ag += vector_relleno_frecuencias_agrupadas
        vector_fe_ag += vector_relleno_frecuencias_agrupadas
        vector_chi += vector_relleno_frecuencias_agrupadas
        valor_chi = [valor_chi] + vector_relleno_valor_una_fila

        head = ["Numero intervalo", "limite inferior", "limite superior", "frecuencia obsevada",
                "frecuencia esperada", "intervalos agrupados", "frecuenia observada agrupada",
                "frecuencia esperada ag", "((O-E)^2)/ E", "valor chi"]
        df = pd.DataFrame(
            list(
                zip(vector_nro_intervalo, vector_li, vector_ls, vector_fo, vector_fe, vector_int_ag,
                    vector_fo_ag, vector_fe_ag, vector_chi, valor_chi)
            ),
            columns=head)
        return df
    else:
        valor_chi = [valor_chi] + vector_relleno_frecuencias

        head = ["vector_nro_intervalo", "limite inferior", "limite superior", "frecuencia obsevada",
                "frecuencia esperada", "((O-E)^2)/ E", "valor chi"]
        df = pd.DataFrame(
            list(
                zip(vector_nro_intervalo, vector_li, vector_ls, vector_fo, vector_fe, vector_chi, valor_chi)
            ),
            columns=head)
        return df

"""def create_df_frecuencias(dict_data, tipo_dist):
    if tipo_dist == "Uniforme":
        head = ["limite inferior", "limite superior", "frecuencia obsevada", "frecuencia esperada", "Vector CHI"]
        df = pd.DataFrame(
            list(
                zip(dict_data["vector_li"], dict_data["vector_ls"], dict_data["vector_fo"],
                    dict_data["vector_fe"], dict_data["vector_chi"])
            ),
            columns=head
        )
        return df
    else:
        head = ["limite inferior", "limite superior", "frecuencia obsevada", "frecuencia esperada"]
        df = pd.DataFrame(
            list(
                zip(dict_data["vector_li"], dict_data["vector_ls"], dict_data["vector_fo"],
                    dict_data["vector_fe"])
            ),
            columns=head
        )
        return df"""


"""def create_df_chi(dict_data):
    head = ["Intervalos agrupados", "frecuencia observada agrupada", "frecuencia esperada agrupada", "(O - E)^2/2)"]
    df = pd.DataFrame(
        list(
            zip(dict_data["vector_int_ag"], dict_data["vector_fo_ag"], dict_data["vector_fe_ag"], dict_data["vector_chi"])
        ),
        columns=head
    )
    return df"""


def create_df_serie_aleatoria(dict_data):
    head = ["numeros random distribucion " + dict_data["tipo_distribucion"]]
    df = pd.DataFrame(
        list(
            zip(dict_data["vector_serie_nros_aleatorios"])
        ),
        columns=head
    )
    return df


