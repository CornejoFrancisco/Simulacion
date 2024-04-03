# This is a sample Python script.
import math

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from Soporte import*

def menu():
    print("1 - Ingrese la cantidad de numero de datos deseado ")
    print("2 - U[a,b]")
    print("3 - Exponencial negativo")
    print("4 - Normal media y desviacion")
    print("Cualquier otro numero es la salida")





def principal(param):
    cargado_numero = False
    op = -1
    while op != 4:
        menu()
        op = int(input("Ingrese el numero de la opcion deseado: "))
        if op == 1:
            cantidad = validad_positivo()
            vector = vector_cargado(cantidad)
            mayor = max(vector)
            minimo = min(vector)

            rango = mayor-minimo
            intervalos = math.sqrt(cantidad)
            amplitud = rango/intervalos
            media = media_datos(vector)
            varianza = varianza_datos(vector)
            cargado_numero = True

        if op == 2:
            if cargado_numero:
                punto_2(vector)
            else:
                print("No se cargo todavia el vector")
        if op == 3:
            if cargado_numero:
                punto_3(vector)
            else:
                print("No se cargo todavia el vector")
        if op == 4:
            if cargado_numero:
                punto_4(vector)
            else:
                print("No se cargo todavia el vector")
        if( op != 1 or op != 2 or op != 3 or op != 4):
            print("Se cierra el programa!! ")
            break





if __name__ == '__main__':
    principal('__Simulacion__')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
