from scripts.prueba_chi_cuadrado import *
from graficos.prueba_graficos import *
from scripts.soporte import *


# cantidad de numeros a generar, A, B, cantidad de intervalos
def generar_distribucion_uniforme(params):

    valor_a = params["valoar_a"]
    valor_b = params["valor_b"]
    cantidad_nros = params["cantidad_nros"]
    cantidad_intervalos = params["cantidad_intervalos"]

    vector_nros_aleatorios_uniforme = generar_vector_uniforme(valor_a, valor_b, cantidad_nros)
    data = {
        "vector_nros_aleatorios_uniforme": vector_nros_aleatorios_uniforme
    }
    data.update(prueba_chi_cuadrdado_uniforme(vector_nros_aleatorios_uniforme, cantidad_intervalos))

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
    vector_nros_aleatorios_expo = generador_vector_exponencial(params["opcion_dist"],
                                                     params["valor_op_dist"], params["cantidad_nros"])
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
    cantidad_nros = params["cantidad_nros"]
    vector_nros_aleatorios_normal = generar_vector_normal(cantidad_nros,
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


