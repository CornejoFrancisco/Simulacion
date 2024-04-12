vec_fe = [49.1918, 24.8965, 12.6004, 6.3772, 3.2276, 2.4852, 3.5485, 2.3361, 1.6335, 0.8267, 0.4184, 0.2118, 0.1072]
vec_fo = [1, 6, 8, 1, 6, 9, 5, 1, 7, 6, 1, 3, 4]
vec_fe_2 = [0.2144, 0.3254, 0.1563, 0.02, 15.5621, 36.1523, 5.3623, 3.2512, 0.2641, 0.2361, 0.0054]
vec_fo_2 = [1, 6, 8, 1, 6, 9, 5, 1, 7, 6, 1]
vec_fe_3 = [0.2144, 0.3254, 0.1563, 4.4125, 1, 15.5621, 36.1523, 5.3623, 3.2512, 0.2641, 2.25, 4.88, 0.2361, 0.0054]
vec_fo_3 = [1, 6, 8, 1, 6, 9, 5, 1, 7, 6, 1, 3, 4, 6]

def frec_esp(vec_f, vec_o):
    vec_agrupados = []
    vec_oac = []
    suma = 0
    acum = 0
    for x in vec_f:
        if x < 5:
            suma += x
            ind_x = vec_f.index(x)
            acum += vec_o[ind_x]

            if suma >= 5:
                print("ultimo sumado: ", x)
                vec_agrupados.append(round(suma, 4))
                vec_oac.append(round(acum, 4))
                suma = 0
                acum = 0
            if vec_f.index(x) == len(vec_f) - 1 and suma < 5:
                vec_agrupados[-1] += round(suma, 4)
                vec_oac[-1] += round(acum, 4)
                suma = 0
                acum = 0

        else:
            ind_x = vec_f.index(x)
            if suma < 5:
                vec_agrupados.append(round(x + suma, 4))
                vec_oac.append(round(acum + vec_o[ind_x], 4))
            else:
                vec_agrupados.append(x)
                vec_oac.append(vec_o[ind_x])
            suma = 0
            acum = 0
    print(vec_f)
    print(vec_agrupados)
    print(vec_o)
    print(vec_oac)

"""    for x in vec_agrupados:
        if x < 5:
            indice = vec_agrupados.index(x)
            vec_agrupados[indice - 1] += x
            vec_agrupados.pop(indice)
    print(vec_agrupados)"""

frec_esp(vec_fe_3, vec_fo_3)
