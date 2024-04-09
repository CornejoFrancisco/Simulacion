from soporte import *


def prueba_chi_cuadrdado_uniforme(vector_nros_aleatorios_x_distribucion, cantidad_intervalos):
    minimo = min(vector_nros_aleatorios_x_distribucion)
    maximo = max(vector_nros_aleatorios_x_distribucion)
    vector_li, vector_ls, amplitud = limites(minimo, maximo, cantidad_intervalos)
    vector_fo = frecuencia_obs(vector_nros_aleatorios_x_distribucion, vector_li, vector_ls, maximo)
    vector_fe = [(len(vector_nros_aleatorios_x_distribucion)/cantidad_intervalos) for _ in range(cantidad_intervalos)]
    vector_chi = funcion_chi(vector_fo, vector_fe)
    valor_chi = calcular_chi(vector_chi)
    matriz = [vector_nros_aleatorios_x_distribucion, vector_li, vector_ls, vector_fo, vector_fe, vector_chi, valor_chi,
              cantidad_intervalos, minimo, maximo, amplitud]
    return matriz

