from soporte import *

def punto_2(vector, variable_a, variable_b):
    if variable_a > variable_b:
        cantidad_intervalo = intervalo_valido()

        matriz = uniforme_calculadora(vector, variable_a, variable_b, cantidad_intervalo)
        return matriz

    if variable_b > variable_a:
        cantidad_intervalo = intervalo_valido()
        matriz = uniforme_calculadora(vector, variable_b, variable_a, cantidad_intervalo)
        return matriz

def uniforme_calculadora(vector, variable_a, variable_b, cantidad_intervalo):

    vector_uniform = vector_uniforme(vector, variable_a, variable_b)

    minimo = min(vector_uniform)
    maximo = max(vector_uniform)
    vector_li, vector_ls, amplitud = limites(minimo, maximo, cantidad_intervalo)
    vector_fo_unif = frecuencia_obs(vector_uniform, vector_li, vector_ls, maximo)

    vector_fe_unif = [(len(vector)/cantidad_intervalo) for _ in range(cantidad_intervalo)]

    funcion_chi_vector = funcion_chi(vector_fo_unif, vector_fe_unif)
    funcion_chi_valor = calcular_chi(funcion_chi_vector)
    matriz = [vector_uniform, vector_li, vector_ls, vector_fo_unif, vector_fe_unif, funcion_chi_vector,
              funcion_chi_valor, cantidad_intervalo, minimo, maximo, amplitud]
    return matriz



