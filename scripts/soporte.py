from decimal import Decimal, ROUND_HALF_UP
from random import *
from scipy.stats import expon, norm
import pandas as pd
import math



def calc_media(vector):
    return sum(vector) / len(vector)


def calc_desviacion(vector, media):
    suma_dif_cuadrados = 0
    for x in vector:
        suma_dif_cuadrados += pow((x - media), 2)
    var_s = suma_dif_cuadrados / (len(vector) - 1)
    return math.sqrt(var_s)


# LIMITES
def limites(min, maxim, intervalo):
    vector_li = []
    vector_ls = []
    vector_nro_intervalo = []
    rango = maxim - min
    amplitud = rango / intervalo

    for i in range(intervalo):
        vector_nro_intervalo.append(i + 1)
        if i == 0:
            vector_li.append(min)
            vector_ls.append(min + amplitud)
        elif 0 < i < intervalo - 1:
            vector_li.append(vector_ls[-1])
            vector_ls.append(vector_li[-1] + amplitud)
        else:
            vector_li.append(vector_ls[-1])
            vector_ls.append(maxim)
    return vector_li, vector_ls, amplitud, vector_nro_intervalo, rango


# FRECUENCIAS
def frecuencia_obs(vector, vector_li, vector_ls):
    contador_apariciones = []
    for i in range(len(vector_li)):
        li = vector_li[i]
        ls = vector_ls[i]
        contador = 0

        for x in vector:
            if x <= ls and x > li:
                contador += 1
            if i == 0 and x == li:
                contador += 1
        contador_apariciones.append(contador)
    return contador_apariciones


def frecuencia_esp_unif(cantidad_nros, cantidad_intervalos):
    fe = cantidad_nros / cantidad_intervalos
    fe_menor_5 = False
    if fe < 5:
        fe_menor_5 = True
    vector_fe = cantidad_intervalos * [fe]
    return vector_fe, fe_menor_5


def frecuencia_esp_expo(vector_li, vector_ls, lambd, n):
    vector_fe = []
    fe_menor_5 = False
    for i in range(len(vector_li)):
        li = vector_li[i]
        ls = vector_ls[i]
        lambd = float(lambd)
        fe = (expon.cdf(ls, scale=1 / lambd) - (expon.cdf(li, scale=1 / lambd))) * n
        vector_fe.append(fe)
        if fe < 5:
            fe_menor_5 = True
    return vector_fe, fe_menor_5


def frecuencia_esp_norm(vector_li, vector_ls, media, desviacion, n):
    vector_fe = []
    fe_menor_5 = False
    for i in range(len(vector_li)):

        li = vector_li[i]
        ls = vector_ls[i]

        fe = (norm.cdf(ls, loc=media, scale=desviacion) - norm.cdf(li, loc=media, scale=desviacion)) * n
        vector_fe.append(fe)
        if fe < 5:
            fe_menor_5 = True
    return vector_fe, fe_menor_5


def agrupamiento_fe(vec_fe, vec_fo):
    vector_fe_ag = []
    vector_fo_ag = []
    vec_int_i = []
    vec_int_s = []
    vec_int_agrupados = []
    fe_acum = 0
    fo_acum = 0
    primero = True

    for i in range(len(vec_fe)):
        x = vec_fe[i]
        fe_acum += x
        fo_acum += vec_fo[i]

        if primero:
            vec_int_i.append(i)
            primero = False

        if fe_acum >= 5:
            vector_fe_ag.append(fe_acum)
            vector_fo_ag.append(fo_acum)
            fe_acum = 0
            fo_acum = 0
            vec_int_s.append(i)
            primero = True

        elif 0 < fe_acum < 5 and i == len(vec_fe) - 1:
            vector_fe_ag[-1] += fe_acum
            vector_fo_ag[-1] += fo_acum
            del vec_int_i[-1]
            vec_int_s[-1] = i

    for i in range(len(vec_int_s)):
        inicial = vec_int_i[i]
        final = vec_int_s[i]
        if inicial != final:
            intervalo = f"{inicial + 1} - {final + 1}"
            vec_int_agrupados.append(intervalo)
        else:
            intervalo = f"{inicial + 1}"
            vec_int_agrupados.append(intervalo)

    return vector_fe_ag, vector_fo_ag, vec_int_agrupados


# GENERADORES
def generar_vector_uniforme(a, b, cantidad_nros):
    vector_uniforme = []
    for i in range(cantidad_nros):
        rnd = random()
        rnd_uniforme = a + rnd * (b - a)
        vector_uniforme.append(rnd_uniforme)
    return vector_uniforme


def generador_vector_exponencial(variable_select, valor_variable, cantidad_nros):
    vector_exponencial = []
    if variable_select == 1:
        for i in range(cantidad_nros):
            rnd = random()
            rnd_expo = -(1 / valor_variable) * (math.log(1 - rnd))
            vector_exponencial.append(rnd_expo)
    elif variable_select == 2:
        for i in range(cantidad_nros):
            rnd = random()
            rnd_expo = -valor_variable * (math.log(1 - rnd))
            vector_exponencial.append(rnd_expo)
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
        vector_normal.append(n1)
        vector_normal.append(n2)

        if i == vueltas - 1 and cantidad_nros_aleatorios % 2 != 0:
            n1 = (math.sqrt(-2 * math.log(rnd1)) *
                  math.cos(2 * math.pi * rnd2)) * desviacion + media
            vector_normal.append(n1)

    return vector_normal


# CALCULOS CHI
def funcion_chi(frecuencia_observada, frecuencia_esperada):
    vector = []

    for i in range(len(frecuencia_observada)):
        fo = frecuencia_observada[i]
        fe = frecuencia_esperada[i]
        chi_calc = pow((fo - fe), 2) / fe
        vector.append(chi_calc)

    return vector


def calcular_chi(vector_chi):

    return sum(vector_chi)


# OTROS


def create_df_final(dict_data):
    minimo = redondeo(dict_data["minimo"])
    maximo = redondeo(dict_data["maximo"])
    amplitud = redondeo(dict_data["amplitud"])
    vector_li = redondeo_vector(dict_data["vector_li"])
    vector_ls = redondeo_vector(dict_data["vector_ls"])
    vector_nro_intervalo = dict_data["vector_nro_intervalo"]
    vector_fo = redondeo_vector(dict_data["vector_fo"])
    vector_fe = redondeo_vector(dict_data["vector_fe"])
    vector_chi = redondeo_vector(dict_data["vector_chi"])
    valor_chi = redondeo(dict_data["valor_chi"])
    fe_menor_5 = dict_data["fe_menor_5"]
    cantidad_intervalos = dict_data["cantidad_intervalos"]
    rango = redondeo(dict_data["rango"])
    n = dict_data["n"]
    tipo_dist = dict_data["tipo_dist"]

    datos_entrada = [n, minimo, maximo, amplitud, rango, cantidad_intervalos]
    titulos_entrada = ["n", "Minimo", "Maximo", "Amplitud", "Rango", "n° intervalos"]

    if tipo_dist == "normal":
        media_param = dict_data["media_param"]
        desviacion_param = dict_data["desviacion_param"]
        media_calc = redondeo(dict_data["media_calc"])
        desviacion_calc = redondeo(dict_data["desviacion_calc"])
        datos_normal = [media_param, desviacion_param, media_calc, desviacion_calc]
        titulos_normal = ["media param", "desviacion param", "media calc", "desviacion calc"]
        datos_entrada = datos_entrada + datos_normal
        titulos_entrada = titulos_entrada + titulos_normal

    elif tipo_dist == "exponencial":
        media_calc = redondeo(dict_data["media_calc"])
        if "lambda" in dict_data:
            var_expo = "lambda"
            valor_var_expo = dict_data["lambda"]
        else:
            var_expo = "media expo"
            valor_var_expo = dict_data["media_expo"]
        datos_expo = [media_calc, valor_var_expo]
        titulos_expo = ["media calc", var_expo]
        datos_entrada += datos_expo
        titulos_entrada += titulos_expo

    elif tipo_dist == "uniforme":
        print(tipo_dist)
        valor_a = dict_data["A"]
        valor_b = dict_data["B"]
        datos_uniforme = [valor_a, valor_b]
        titulos_uniforme = ["A", "B"]
        print(len(datos_entrada))
        datos_entrada += datos_uniforme
        titulos_entrada += titulos_uniforme
        print(len(datos_entrada))

    vector_relleno_frecuencias = ["" for i in range(len(vector_li))]
    vector_relleno_datos_entrada = ["" for i in range(len(vector_li))]
    titulos_entrada_rell = titulos_entrada + vector_relleno_datos_entrada
    datos_entrada_rell = datos_entrada + vector_relleno_datos_entrada

    if fe_menor_5:
        vector_int_ag = dict_data["vector_int_ag"]
        vector_fo_ag = redondeo_vector(dict_data["vector_fo_ag"])
        vector_fe_ag = redondeo_vector(dict_data["vector_fe_ag"])
        vector_relleno_frecuencias_agrupadas = ["" for i in range(len(vector_li) - len(vector_int_ag))]
        vector_relleno_valor_una_fila = ["" for i in range(len(vector_li) - 1)]
        vector_int_ag += vector_relleno_frecuencias_agrupadas
        vector_fo_ag += vector_relleno_frecuencias_agrupadas
        vector_fe_ag += vector_relleno_frecuencias_agrupadas
        vector_chi += vector_relleno_frecuencias_agrupadas
        valor_chi = [valor_chi] + vector_relleno_valor_una_fila

        head = ["", "", "Numero intervalo", "limite inferior", "limite superior", "frecuencia obsevada",
                "frecuencia esperada", "intervalos agrupados", "frecuenia observada agrupada",
                "frecuencia esperada ag", "((O-E)^2)/ E", "valor chi"]
        df = pd.DataFrame(
            list(
                zip(titulos_entrada_rell, datos_entrada_rell, vector_nro_intervalo, vector_li, vector_ls, vector_fo,
                    vector_fe, vector_int_ag, vector_fo_ag, vector_fe_ag, vector_chi, valor_chi)
            ),
            columns=head)
        print("generar la tabla")
        return df

    else:
        valor_chi = [valor_chi] + vector_relleno_frecuencias

        head = ["", "", "Numero intervalo", "limite inferior", "limite superior", "frecuencia obsevada",
                "frecuencia esperada", "((O-E)^2)/ E", "valor chi"]
        df = pd.DataFrame(
            list(
                zip(titulos_entrada_rell, datos_entrada_rell, vector_nro_intervalo, vector_li, vector_ls, vector_fo, vector_fe,
                    vector_chi, valor_chi)
            ),
            columns=head)
        print("generar la tabla")
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
    datos = redondeo_vector(dict_data["vector_serie_nros_aleatorios"])
    df = pd.DataFrame(
        list(
            zip(datos)
        ),
        columns=head
    )
    return df


def gen_vector_li_ls(vector_li, vector_ls):
    vector_li_r = redondeo_vector(vector_li)
    vector_ls_r = redondeo_vector(vector_ls)
    vector_li_ls = []
    for i in range(len(vector_li)):
        if i == 0:
            li_ls = f"[{vector_li_r[i]}-{vector_ls_r[i]}]"
        else:
            li_ls = f"({vector_li_r[i]}\n-{vector_ls_r[i]}]"
        vector_li_ls.append(li_ls)
    return vector_li_ls


def redondeo_vector(vector):
    return list(map(lambda x: Decimal(str(x)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP), vector))


def redondeo_vector_text(vector):
    return list(map(lambda x: str((Decimal(str(x)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))), vector))

def redondeo(x):
    return Decimal(str(x)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
