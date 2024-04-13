import pandas as pd

vec_fe = [49.1918, 24.8965, 12.6004, 6.3772, 3.2276, 2.4852, 3.5485, 2.3361, 1.6335, 0.8267, 0.4184, 0.2118, 0.1072]
vec_fo = [1, 6, 8, 1, 6, 9, 5, 1, 7, 6, 1, 3, 4]
vec_fe_2 = [0.2144, 0.3254, 0.1563, 0.02, 15.5621, 36.1523, 5.3623, 3.2512, 0.2641, 0.2361, 0.0054]
vec_fo_2 = [1, 6, 8, 1, 6, 9, 5, 1, 7, 6, 1]
vec_fe_3 = [0.2144, 0.3254, 0.1563, 4.4125, 1, 15.5621, 36.1523, 5.3623, 3.2512, 0.2641, 2.25, 4.88, 1, 4.9999, 0.025]
vec_fo_3 = [1, 6, 8, 1, 6, 9, 5, 1, 7, 6, 1, 3, 3, 6, 7]

def frec_esp(vec_f, vec_o):
    vec_agrupados = []
    vec_oac = []
    vec_ind_ag = []
    vec_li = []
    vec_ls = []
    indice_li = 0
    indice_ls = 0
    suma = 0
    acum = 0

    primero = True
    for x in vec_f:
        ind_x = vec_f.index(x)
        if x < 5:
            suma += x
            acum += vec_o[ind_x]

            if primero:
                indice_li = ind_x
                primero = False
                vec_li.append(ind_x)
                print("li zona primero:", indice_li)

            if suma >= 5:
                vec_agrupados.append(round(suma, 4))
                vec_oac.append(round(acum, 4))
                suma = 0
                acum = 0

                indice_ls = ind_x
                ind_x_1 = vec_f.index(x)
                print(ind_x_1)
                vec_ls.append(ind_x)
                print("ls zona suma >= 5:", indice_ls)

                primero = True

            if vec_f.index(x) == len(vec_f) - 1 and suma < 5:
                vec_agrupados[-1] += round(suma, 4)
                vec_oac[-1] += round(acum, 4)
                suma = 0
                acum = 0

                indice_ls = ind_x
                print("ls zona ultimo elemento:", indice_ls)

                primero = True

        else:
            if 0 < suma < 5:
                vec_agrupados.append(round(x + suma, 4))
                vec_oac.append(round(acum + vec_o[ind_x], 4))

                indice_ls = ind_x
                vec_ls.append(ind_x)
                print("ls zona suma < 5 y estas en un > 5:", indice_ls)

            else:
                vec_agrupados.append(x)
                vec_oac.append(vec_o[ind_x])
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


frec_esp(vec_fe_3, vec_fo_3)
