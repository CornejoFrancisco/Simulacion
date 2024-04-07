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
            vector_normal.append(n1)
            vector_normal.append(n2)

    if cantidad % 2 != 0:
        for i in range(vueltas):
            rnd1, rnd2 = random(), random()
            if i == vueltas - 1:
                n1 = (math.sqrt(-2 * math.log(rnd1)) * math.cos(2 * math.pi * rnd2)) * desviacion + media
                n2 = (math.sqrt(-2 * math.log(rnd1)) * math.sin(2 * math.pi * rnd2)) * desviacion + media
                vector_normal.append(n1)
                vector_normal.append(n2)
                n1 = (math.sqrt(-2 * math.log(rnd1)) * math.cos(2 * math.pi * rnd2)) * desviacion + media
                vector_normal.append(n1)
                break
            n1 = (math.sqrt(-2 * math.log(rnd1)) * math.cos(2 * math.pi * rnd2)) * desviacion + media
            n2 = (math.sqrt(-2 * math.log(rnd1)) * math.sin(2 * math.pi * rnd2)) * desviacion + media
            vector_normal.append(n1)
            vector_normal.append(n2)
    print(len(vector_normal))
    return vector_normal



def normal_calculos(vector_normal, intervalo):
    maximo = max(vector_normal)
    minimo = min(vector_normal)
    limites_li_lf = limites(minimo, maximo, intervalo)
    vector_fo_norm = frecuencia_obs(vector_normal, limites_li_lf, maximo)
    vector_fe_norm = frecuencia_fo_fe(cantidad_apariciones, intervalo)
    funcion_chi_vector = funcion_chi(frecuencia_apareciones)
    funcion_chi_valor = calcular_chi(funcion_chi_vector)
    normal = [vector_normal, limites_li_lf, cantidad_apariciones, frecuencia_apareciones, funcion_chi_vector, funcion_chi_valor]
    print(funcion_chi_valor)
    return normal

def punto_4(cantidad, media, desviacion):
    vector_normal = vector_normalizado(cantidad, media, desviacion)
    intervalo = intervalo_valido()
    normal = normal_calculos(vector_normal, intervalo)
    print(normal)
