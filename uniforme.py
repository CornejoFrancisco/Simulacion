from soporte import *

def punto_2(vector, variable_a, variable_b):
    if variable_a > variable_b:
        cantidad_intervalo = intervalo_valido()

        simulador_uniforme = uniforme_calculadora(vector, variable_a, variable_b, cantidad_intervalo)
        print(simulador_uniforme)

    if variable_b > variable_a:
        cantidad_intervalo = intervalo_valido()
        simulacdor_uniforme = uniforme_calculadora(vector, variable_b, variable_a, cantidad_intervalo)


def uniforme_calculadora(vector, variable_a, variable_b, cantidad_intervalo):

    vector_uniform = vector_uniforme(vector, variable_a, variable_b)

    minimo = min(vector_uniform)
    maximo = max(vector_uniform)
    limites_li_lf, vector_li, vector_ls = limites(minimo, maximo, cantidad_intervalo)
    cantidad_apareciones = contador_elementos(vector_uniform, limites_li_lf, vector_li, vector_ls, maximo)

    frecuencia_apareciones = [(len(vector)/cantidad_intervalo) for _ in range(cantidad_intervalo)]

    funcion_chi_vector = funcion_chi(cantidad_apareciones, frecuencia_apareciones)
    funcion_chi_valor = calcular_chi(funcion_chi_vector)
    print(funcion_chi_valor)
    matriz = [vector_uniform, cantidad_intervalo, vector_li, vector_ls, cantidad_apareciones ,frecuencia_apareciones, funcion_chi_vector]
    print(matriz)
    return matriz



