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


def exponencial_calculos(vector_exponencial, intervalo, lambd):
    maximo = max(vector_exponencial)
    minimo = min(vector_exponencial)
    vector_li, vector_ls = limites(minimo, maximo, intervalo)
    vector_fo_expo = frecuencia_obs(vector_exponencial, vector_li, vector_ls, maximo)
    vector_fe_expo = frecuencia_esp_expo(vector_li, vector_ls, lambd, len(vector_exponencial))
    funcion_chi_vector = funcion_chi(vector_fo_expo, vector_fe_expo)
    funcion_chi_valor = calcular_chi(funcion_chi_vector)
    matriz = [vector_exponencial, vector_li, vector_ls, vector_fo_expo, vector_fe_expo, funcion_chi_vector]
    print(funcion_chi_valor)
    return matriz


def punto_3(vector, variable, opcion):
    if opcion == 1:
        vector_exponencial = exponencial_calculadora_land(vector, variable)
        intervalos = intervalo_valido()
        matriz = exponencial_calculos(vector_exponencial, intervalos, variable)
        print(matriz)

    if opcion == 2:
        vector_exponencial = exponencial_calculadora_expon(vector, variable)
        intervalos = intervalo_valido()
        exponencial = exponencial_calculos(vector_exponencial, intervalos)

