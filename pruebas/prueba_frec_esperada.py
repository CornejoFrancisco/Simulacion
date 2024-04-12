vec_fe = [49.1918, 24.8965, 12.6004, 6.3772, 3.2276, 1.6335, 0.8267, 0.4184, 0.2118, 0.1072]

"""new_vec_fe = []
vec_elim = []
siguiente = 0
for i in range(len(vec_fe)):
    if vec_fe[i] < 5:
        nf = 0
        for j in range(siguiente, len(vec_fe) - 1):
            if nf < 5:
                nf += vec_fe[j]
                nf = round(nf, 4)
            elif nf >= 5:
                break

        new_vec_fe.append(nf)
    else:
        new_vec_fe.append(vec_fe[i])
        ultimo_sumado = i
        
print(vec_elim, siguiente)
print(vec_fe)
print(new_vec_fe)"""

vec_fe_new = []
print(vec_fe)
for x in vec_fe:
    if x < 5:
        indice_x = vec_fe.index(x)
        nf = 0
        print(indice_x)
        for i in range(indice_x, len(vec_fe) - 1):
            nf += vec_fe[i]
            if nf >= 5:
                vec_fe_new.append(round(nf, 4))
                break
    else:
        vec_fe_new.append(x)

print(vec_fe_new)