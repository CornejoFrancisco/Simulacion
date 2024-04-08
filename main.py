from uniforme import *
from exponencial import *
from normal import *
from graficos.prueba_graficos import *

def menu():
    print("1 - U[a,b]")
    print("2 - Exponencial negativo")
    print("3 - Normal media y desviacion")
    print("Cualquier otro numero es la salida")


def principal(param):
    op = -1
    while op:
        menu()
        op = int(input("Ingrese el numero de la opcion deseado: "))

        if op == 1:
            vector = insercion_cantidad()
            variable_a = int(input("Ingrese la variable A: "))
            variable_b = int(input("Ingrese la variable B: "))
            data = punto_2(vector, variable_a, variable_b)
            print(data)
            vector_li_ls = data[1].append((data[2])[-1])
            grafico_histograma_frecuencias(data[0], data[7], vector_li_ls)
        elif op == 2:
                vector = insercion_cantidad()
                opcion = menu_lambda_media()

                if opcion == 1:
                    valor_ingresado = validad_positivo("Ingrese el valor de lambda: ")
                    data = punto_3(vector, valor_ingresado, opcion)
                    vector_li_ls = data[1].append((data[2])[-1])
                    grafico_histograma_frecuencias(data[0], data[7], vector_li_ls)
                if opcion == 2:
                    valor_ingresado = validad_positivo("Ingrese el valor de media: ")
                    punto_3(vector, valor_ingresado, opcion)
        elif op == 3:
            cantidad = int(input("Ingrese la cantidad de numeros normalizados a generar: "))
            media = int(input("Ingrese el valor de la media: "))
            desviacion = int(input("Ingrese el valor de la desviacion: "))
            data = punto_4(cantidad, media, desviacion)
            vector_li_ls = data[1].append((data[2])[-1])
            grafico_histograma_frecuencias(data[0], data[7], vector_li_ls)

        elif( op != 1 or op != 2 or op != 3 or op != 4):
            print("Se cierra el programa!! ")
            break



if __name__ == '__main__':
    principal('__Simulacion__')

