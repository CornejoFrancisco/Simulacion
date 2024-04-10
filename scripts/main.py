from scripts.prueba_chi_cuadrado import *
from graficos.prueba_graficos import *
from soporte import *


# cantidad de numeros a generar, A, B, cantidad de intervalos
def generar_distribucion_uniforme(params):
    print(params)
    vector_nros_aleatorios = vector_cargado(params["cantidad_nros"])
    vector_nros_aleatorios_uniforme = vector_uniforme(vector_nros_aleatorios, params["valor_a"], params["valor_b"])
    data = prueba_chi_cuadrdado_uniforme(vector_nros_aleatorios_uniforme, params["cantidad_intervalos"])
    vector_li_ls = data[1]
    vector_li_ls.append(data[9])
    print(vector_li_ls)
    df = create_data_frame(data)
    print(df)
    table(df)
    grafico_histograma_frecuencias(data[0], data[7], data[8], data[9], data[10], vector_li_ls)


# cantidad de numeros a generar, opcion lambda o media, valor de opcion anterior, cantidad de intervalos
def generar_distribucion_exponencial(params):
    print(params)
    vector_nros_aleatorios = vector_cargado(params["cantidad_nros"])
    print(params["valor_op_dist"], params["opcion_dist"])
    vector_nros_aleatorios_expo = vector_exponencial(vector_nros_aleatorios,
                                                     params["opcion_dist"], params["valor_op_dist"])
    print(vector_nros_aleatorios_expo)
    print("pasa vector exponencial")
    data = prueba_chi_cuadrado_exponencal(vector_nros_aleatorios_expo, params["cantidad_intervalos"],
                                          params["opcion_dist"], params["valor_op_dist"])
    print("sale de prueba chi cuadrado ")
    vector_li_ls = data[1]
    vector_li_ls.append(data[9])
    print(vector_li_ls)
    df = create_data_frame(data)
    print(df)
    table(df)
    grafico_histograma_frecuencias(data[0], data[7], data[8], data[9], data[10], vector_li_ls)


# cantidad de numeros a generar, media, desviacion, cantidad de intervalos
def generar_distribucion_normal(params):
    print(params)
    vector_nros_aleatorios_1 = []
    vector_nros_aleatorios_2 = []

    cantidad_nros = params["cantidad_nros"]
    if cantidad_nros % 2 == 0:
        vector_nros_aleatorios_1 = vector_cargado(cantidad_nros // 2)
        vector_nros_aleatorios_2 = vector_cargado(cantidad_nros // 2)
    elif cantidad_nros % 2 != 0:
        vector_nros_aleatorios_1 = vector_cargado((cantidad_nros // 2) + 1)
        vector_nros_aleatorios_2 = vector_cargado((cantidad_nros // 2) + 1)
    print("llega aca")
    vector_nros_aleatorios_normal = vector_normal(vector_nros_aleatorios_1, vector_nros_aleatorios_2, cantidad_nros,
                                  params["desviacion"], params["media"])
    data = prueba_chi_cuadrado_normal(vector_nros_aleatorios_normal, params["cantidad_intervalos"],
                                      params["media"], params["desviacion"])
    vector_li_ls = data[1]
    vector_li_ls.append(data[9])
    print(vector_li_ls)
    df = create_data_frame(data)
    print(df)
    table(df)
    grafico_histograma_frecuencias(data[0], data[7], data[8], data[9], data[10], vector_li_ls)


