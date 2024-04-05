# This is a sample Python script.
import math

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from soporte import*

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
            cantidad = validad_positivo("Ingrese el numero de cantidad de datos deseado: ")
            vector = vector_cargado(cantidad)

            cargado_numero = True
            print(vector)
            uniforme_calculadora(vector, 0, 0, 10)


        elif op == 2:
            if cargado_numero:
                # Selecion del caso que sea uniforme
                variable_a = int(input("Ingrese la variable A: "))
                variable_b = int(input("Ingrese la variable B: "))

                punto_2(vector, variable_a, variable_b)

            else:
                print("No se cargo todavia el vector")
        elif op == 3:
            if cargado_numero:
                print("1 - lambda")
                print("2 - Media")
                opcion = validad_positivo("Ingrese la opcion deseada: ")
                if opcion == 1:
                    valor_lambda = validad_positivo("Ingrese el valor de lambda: ")
                    punto_3_media(vector, valor_lambda)
                if opcion == 2:
                    valor_lambda = validad_positivo("Ingrese el valor de media: ")
                    punto_3_lambda(vector)
            else:
                print("No se cargo todavia el vector")
        elif op == 4:
            if cargado_numero:
                punto_4(vector)
            else:
                print("No se cargo todavia el vector")
        elif( op != 1 or op != 2 or op != 3 or op != 4):
            print("Se cierra el programa!! ")
            break





if __name__ == '__main__':
    principal('__Simulacion__')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
