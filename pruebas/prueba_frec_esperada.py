from random import *
from decimal import Decimal, ROUND_HALF_UP
import pandas as pd

vec_fe = [49.1918, 24.8965, 12.6004, 6.3772, 3.2276, 2.4852, 3.5485, 2.3361, 1.6335, 0.8267, 0.4184, 0.2118, 0.1072]
vec_fo = [1, 6, 8, 1, 6, 9, 5, 1, 7, 6, 1, 3, 4]
vec_fe_2 = [0.2144, 0.3254, 0.1563, 0.02, 15.5621, 36.1523, 5.3623, 3.2512, 0.2641, 0.2361, 0.0054]
vec_fo_2 = [1, 6, 8, 1, 6, 9, 5, 1, 7, 6, 1]
#vec_fe_3 = [0.2144, 0.3254, 0.1563, 4.4125, 1, 15.5621, 36.1523, 5.3623, 3.2512]
#vec_fo_3 = [1, 6, 8, 1, 6, 9, 5, 1, 7]
vec_fe_3 = [0.2144, 0.3254, 0.1563, 4.4125, 1, 15.5621, 36.1523, 5.3623, 3.2512, 0.2641, 2.25, 4.88, 1, 4.9999, 0.025, 0.002, 0.001]
vec_fo_3 = [1, 6, 8, 1, 6, 9, 5, 1, 7, 6, 1, 3, 3, 6, 8, 7, 6]


def frec_esp2(vec_f, vec_o):
    vec_agrupados = []
    vec_oac = []
    vec_li = []
    vec_ls = []
    suma = 0
    acum = 0

    primero = True
    for i in range(len(vec_f)):
        x = vec_f[i]
        if x < 5:
            suma += x
            acum += vec_o[i]

            if primero:
                primero = False
                vec_li.append(i)

            if suma >= 5:
                vec_agrupados.append(round(suma, 4))
                vec_oac.append(round(acum, 4))
                suma = 0
                acum = 0
                vec_ls.append(i)
                primero = True

            elif i == len(vec_f) - 1 and suma < 5:
                vec_agrupados[-1] += round(suma, 4)
                vec_oac[-1] += round(acum, 4)

                if suma != x:
                    vec_ls[-1] = i
                    del vec_li[-1]
                elif suma == x:
                    vec_ls.append(i)
                    vec_li[-1] = vec_li[-1] - 1

                suma = 0
                acum = 0

        else:
            if 0 < suma < 5:
                vec_agrupados.append(round(x + suma, 4))
                vec_oac.append(round(acum + vec_o[i], 4))
                vec_ls.append(i)

            else:
                vec_agrupados.append(x)
                vec_oac.append(vec_o[i])
            primero = True
            suma = 0
            acum = 0

    vector_relleno = ["" for i in range(len(vec_f) - len(vec_agrupados))]
    vec_agrupados += vector_relleno
    vec_oac += vector_relleno

    df = pd.DataFrame({"Vector_fo": vec_o, "Vector_fe": vec_f, "vector_fo_ag": vec_oac, "vector_fe_ag": vec_agrupados})
    print(df)
    print(vec_li)
    print(vec_ls)


def frec_esp(vec_f, vec_o):
    vec_agrupados = []
    vec_oac = []
    vec_li = []
    vec_ls = []
    vec_intervalos = []
    suma = 0
    acum = 0
    primero = True

    for i in range(len(vec_f)):
        x = vec_f[i]
        suma += x
        acum += vec_o[i]
        if primero:
            vec_li.append(i)
            primero = False

        if suma >= 5:
            vec_agrupados.append(round(suma, 4))
            vec_oac.append(acum)
            suma = 0
            acum = 0
            vec_ls.append(i)
            primero = True
        elif 0 < suma < 5 and i == len(vec_f) - 1:
            vec_agrupados[-1] += round(suma, 4)
            vec_oac[-1] += acum
            del vec_li[-1]
            vec_ls[-1] = i

    for i in range(len(vec_ls)):
        inicial = vec_li[i]
        final = vec_ls[i]
        if inicial != final:
            intervalo = f"{inicial} - {final}"
            vec_intervalos.append(intervalo)
        elif inicial == final:
            intervalo = f"{inicial}"
            vec_intervalos.append(intervalo)

    vector_relleno = ["" for i in range(len(vec_f) - len(vec_agrupados))]
    vec_agrupados += vector_relleno
    vec_oac += vector_relleno
    vec_intervalos += vector_relleno

    df = pd.DataFrame({"Vector_fo": vec_o, "Vector_fe": vec_f,"intervalos agrupados": vec_intervalos,
                       "vector_fo_ag": vec_oac, "vector_fe_ag": vec_agrupados})
    print(df)

#frec_esp(vec_fe_3, vec_fo_3)
#frec_esp2(vec_fe_2, vec_fo_2)
#print(round(random.uniform(0,1),4))

numero = (Decimal(3.15255)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
#print(numero)

def intervalos():
    min = (Decimal(str(1.2252))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    max = (Decimal(str(9.9514))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    nro_i = 10
    rango = (Decimal(str(max - min))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    amplotud = (Decimal(str(rango / nro_i))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    vec_li = []
    vec_ls = []
    for i in range(nro_i):
        if i == 0:
            vec_li.append(min)
        else:
            li = vec_ls[i - 1]  # Usar el límite superior del intervalo anterior
            vec_li.append(li)

        ls = min + amplotud * (i + 1) # Calcular ls directamente
        #ls = ls.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
        vec_ls.append(ls)

    print(vec_li)
    print(vec_ls)

#intervalos()

"""x = 12.12355
a = 2.9704
b = 0.8726
#print(random())
#print((Decimal(str(a + b))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))

print(list(map(lambda x: (Decimal(str(x))).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP), [-0.6140493547080164, 0.4299944755018261, 1.4740383057116686, 2.518082135921511, 3.5621259661313536, 4.606169796341196, 5.6502136265510385, 6.694257456760881, 7.7383012869707235, 8.782345117180565, 9.826388947390425])))

def redondeo_manual(x):
    x = str(x)"""

