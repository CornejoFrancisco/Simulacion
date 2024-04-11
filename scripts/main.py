from scripts.prueba_chi_cuadrado import *
from graficos.graficos import *
from scripts.soporte import *


def generar_distribucion_uniforme(params):

    valor_a = params["valor_a"]
    valor_b = params["valor_b"]
    cantidad_nros = params["cantidad_nros"]
    cantidad_intervalos = params["cantidad_intervalos"]

    vector_nros_aleatorios_uniforme = generar_vector_uniforme(valor_a, valor_b, cantidad_nros)

    data = prueba_chi_cuadrdado_uniforme(vector_nros_aleatorios_uniforme, cantidad_intervalos)

    vector_li_ls = data["vector_li"].copy()
    vector_li_ls.append(data["maximo"])

    dict_df_serie_unif = {
        "tipo_distribucion": "uniforme",
        "vector_serie_nros_aleatorios": vector_nros_aleatorios_uniforme
    }

    df_serie_unif = create_df_serie_aleatoria(dict_df_serie_unif)
    tabla_nros_aleatorios(df_serie_unif, "uniforme")

    df_frecuencias = create_df_frecuencias(data)

    table_frecuencias(df_frecuencias)
    grafico_histograma_frecuencias(vector_nros_aleatorios_uniforme, data["minimo"], data["maximo"],
                                   data["amplitud"], vector_li_ls)


def generar_distribucion_exponencial(params):
    vector_nros_aleatorios_expo = generador_vector_exponencial(params["opcion_dist"],
                                                     params["valor_op_dist"], params["cantidad_nros"])
    data = prueba_chi_cuadrado_exponencal(vector_nros_aleatorios_expo, params["cantidad_intervalos"],
                                          params["opcion_dist"], params["valor_op_dist"])
    vector_li_ls = data["vector_li"].copy()
    vector_li_ls.append(data["maximo"])

    dict_df_serie_expo = {
        "tipo_distribucion": "exponencial",
        "vector_serie_nros_aleatorios": vector_nros_aleatorios_expo
    }
    df_serie_expo = create_df_serie_aleatoria(dict_df_serie_expo)
    tabla_nros_aleatorios(df_serie_expo, "exponencial")

    df_frecuencias_expo = create_df_frecuencias(data)
    table_frecuencias(df_frecuencias_expo)
    grafico_histograma_frecuencias(vector_nros_aleatorios_expo, data["minimo"], data["maximo"],
                                   data["amplitud"], vector_li_ls)


def generar_distribucion_normal(params):
    cantidad_nros = params["cantidad_nros"]
    vector_nros_aleatorios_normal = generar_vector_normal(cantidad_nros,
                                  params["desviacion"], params["media"])
    data = prueba_chi_cuadrado_normal(vector_nros_aleatorios_normal, params["cantidad_intervalos"],
                                      params["media"], params["desviacion"])
    vector_li_ls = data["vector_li"].copy()
    vector_li_ls.append(data["maximo"])

    dict_df_serie_norm = {
        "tipo_distribucion": "normal",
        "vector_serie_nros_aleatorios": vector_nros_aleatorios_normal
    }

    df_df_serie_norm = create_df_serie_aleatoria(dict_df_serie_norm)
    tabla_nros_aleatorios(df_df_serie_norm, "normal")

    df_frecuencias_norm = create_df_frecuencias(data)
    table_frecuencias(df_frecuencias_norm)
    grafico_histograma_frecuencias(vector_nros_aleatorios_normal, data["minimo"], data["maximo"],
                                   data["amplitud"], vector_li_ls)


