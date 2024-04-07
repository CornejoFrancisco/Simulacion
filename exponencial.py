from soporte import*

def exponencial_calculadora_land(vector, variable):
    vector_exponencial = []
    for i in vector:
        vector_exponencial.append(-(1/variable)*(math.log(1-i)))
    return vector_exponencial


def exponencial_calculadora_expon(vector, variable):
    vector_exponencial = []
    for i in vector:
        vector_exponencial.append(-(variable) * (math.log(1 - i)))
    return vector_exponencial


def exponencial_calculos(vector_exponencial, intervalo):
    maximo = max(vector_exponencial)
    minimo = min(vector_exponencial)
    limites_li_lf = limites(minimo, maximo, intervalo)
    cantidad_apareciones = contador_elementos(vector_exponencial, limites_li_lf, maximo)
    frecuencia_apareciones = frecuencia_fo_fe(cantidad_apareciones, intervalo)
    funcion_chi_vector = funcion_chi(frecuencia_apareciones)
    funcion_chi_valor = calcular_chi(funcion_chi_vector)
    print(funcion_chi_valor)


def punto_3(vector, variable, opcion):
    if opcion == 1:
        vector_exponencial = exponencial_calculadora_land(vector, variable)
        intervalos = intervalo_valido()
        exponencial = exponencial_calculos(vector_exponencial, intervalos)

        print(vector_exponencial)
    if opcion == 2:
        vector_exponencial = exponencial_calculadora_expon(vector, variable)
        intervalos = intervalo_valido()
        exponencial = exponencial_calculos(vector_exponencial, intervalos)

