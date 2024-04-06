from soporte import*

def punto_2(vector, variable_a, variable_b):
    if variable_a > variable_b:
        cantidad_intervalo = intervalo_valido()

        simulador_uniforme = uniforme_calculadora(vector, variable_a, variable_b, cantidad_intervalo)

    if variable_b > variable_a:
        cantidad_intervalo = intervalo_valido()
        simulacdor_uniforme = uniforme_calculadora(vector, variable_b, variable_a, cantidad_intervalo)


def uniforme_calculadora(vector, variable_a, variable_b, cantidad_intervalo):

    vector_uniform = vector_uniforme(vector, variable_a, variable_b)

    minimo = min(vector_uniform)
    maximo = max(vector_uniform)
    limites_li_lf = limites(minimo, maximo, cantidad_intervalo)
    cantidad_apareciones = contador_elementos(vector_uniform, limites_li_lf, maximo)

    frecuencia_apareciones = frecuencia_fo_fe(cantidad_apareciones, cantidad_intervalo)

    funcion_chi_vector = funcion_chi_uniforme(frecuencia_apareciones)
    funcion_chi_valor = calcular_chi(funcion_chi_vector)
    print(funcion_chi_valor)
    matriz = [vector_uniform, cantidad_intervalo, limites_li_lf, frecuencia_apareciones, funcion_chi_vector]
    return matriz


