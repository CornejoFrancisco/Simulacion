from soporte import*

def exponencial_calculadora_land(vector, variable):
    vector_exponencial = []
    for i in vector:
        rnd_expo = -(1/variable)*(math.log(1-i))
        vector_exponencial.append(round(rnd_expo, 4))
    return vector_exponencial


def exponencial_calculadora_expon(vector, variable):
    vector_exponencial = []
    for i in vector:
        rnd_expo = -(variable)*(math.log(1-i))
        vector_exponencial.append(round(rnd_expo, 4))
    return vector_exponencial


def exponencial_calculos(vector_exponencial, intervalo, lambd):
    maximo = round(max(vector_exponencial),4)
    minimo = round(min(vector_exponencial),4)
    vector_li, vector_ls = limites(minimo, maximo, intervalo)
    vector_fo_expo = frecuencia_obs(vector_exponencial, vector_li, vector_ls, maximo)
    vector_fe_expo = frecuencia_esp_expo(vector_li, vector_ls, lambd, len(vector_exponencial))
    funcion_chi_vector = funcion_chi(vector_fo_expo, vector_fe_expo)
    funcion_chi_valor = calcular_chi(funcion_chi_vector)
    matriz = [vector_exponencial, vector_li, vector_ls, vector_fo_expo, vector_fe_expo, funcion_chi_vector,
              funcion_chi_valor, intervalo]
    print(funcion_chi_valor)
    return matriz


def punto_3(vector, variable, opcion):
    if opcion == 1:
        vector_exponencial = exponencial_calculadora_land(vector, variable)
        intervalos = intervalo_valido()
        matriz = exponencial_calculos(vector_exponencial, intervalos, variable)
        return matriz

    if opcion == 2:
        vector_exponencial = exponencial_calculadora_expon(vector, variable)
        intervalos = intervalo_valido()
        exponencial = exponencial_calculos(vector_exponencial, intervalos)

