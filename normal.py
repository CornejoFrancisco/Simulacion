import math
from soporte import*


def vector_normalizado(cantidad, media, desviacion):
    vector_normal = []
    vueltas = cantidad // 2
    if cantidad % 2 == 0:
        for i in range(vueltas):
            rnd1, rnd2 = random(), random()
            n1 = (math.sqrt(-2 * math.log(1 - rnd1)) * math.cos(2 * math.pi * rnd2)) * desviacion + media
            n2 = (math.sqrt(-2 * math.log(1 - rnd1)) * math.sin(2 * math.pi * rnd2)) * desviacion + media
            vector_normal.append(round(n1, 4))
            vector_normal.append(round(n2, 4))

    if cantidad % 2 != 0:
        for i in range(vueltas):
            rnd1, rnd2 = random(), random()
            if i == vueltas - 1:
                n1 = (math.sqrt(-2 * math.log(rnd1)) * math.cos(2 * math.pi * rnd2)) * desviacion + media
                n2 = (math.sqrt(-2 * math.log(rnd1)) * math.sin(2 * math.pi * rnd2)) * desviacion + media
                vector_normal.append(round(n1, 4))
                vector_normal.append(round(n2, 4))
                n1 = (math.sqrt(-2 * math.log(rnd1)) * math.cos(2 * math.pi * rnd2)) * desviacion + media
                vector_normal.append(round(n1, 4))
                break
            n1 = (math.sqrt(-2 * math.log(rnd1)) * math.cos(2 * math.pi * rnd2)) * desviacion + media
            n2 = (math.sqrt(-2 * math.log(rnd1)) * math.sin(2 * math.pi * rnd2)) * desviacion + media
            vector_normal.append(round(n1, 4))
            vector_normal.append(round(n2, 4))
    print(len(vector_normal))
    return vector_normal



def normal_calculos(vector_normal, intervalo, media, desviacion):
    maximo = max(vector_normal)
    minimo = min(vector_normal)
    vector_li, vector_ls, amplitud = limites(minimo, maximo, intervalo)
    vector_fo_norm = frecuencia_obs(vector_normal, vector_li, vector_ls, maximo)
    vector_fe_norm = frecuencia_esp_norm(vector_li, vector_ls, media, desviacion, len(vector_normal))
    funcion_chi_vector = funcion_chi(vector_fo_norm, vector_fe_norm)
    funcion_chi_valor = calcular_chi(funcion_chi_vector)
    matriz = [vector, vector_uniform, vector_li, vector_ls, vector_fo_unif, vector_fe_unif, funcion_chi_vector,
              funcion_chi_valor, cantidad_intervalo, minimo, maximo, amplitud]
    print(funcion_chi_valor)
    return matriz_normal

def punto_4(cantidad, media, desviacion):
    vector_normal = vector_normalizado(cantidad, media, desviacion)
    intervalo = intervalo_valido()
    normal = normal_calculos(vector_normal, intervalo, media, desviacion)
    return normal
