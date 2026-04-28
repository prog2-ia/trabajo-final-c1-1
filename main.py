from ClaseRefugio import *
from Animales.ClaseAnimales import *
from Animales.ClaseGato import *
from Animales.ClasePerro import *
from Animales.ClaseNecesidad import *


def seleccionar_refugio(): #Para siempre que haya que seleccionar un refugio y mostrar todos sus nombres
    for refugio in mis_refugios:
        print(refugio)

    refu = input('¿A que refugio quieres añadirlo?: ')
    refugio_seleccionado = None

    for refugio in mis_refugios:
        if refugio.nombre.lower() == refu.lower():
            refugio_seleccionado = refugio

    if refugio_seleccionado == None:
        print('Este refugio no está en tú lista de refugios\n')

    else:
        print(f'El refugio seleccionado es: {refugio_seleccionado.nombre}')

    return refugio_seleccionado



def animales():

    seguir = True
    while seguir:
        print('Bienvenido al apartado animales, estas son las opciones:')
        print('1: Añadir un nuevo Perro')
        print('2: Añadir un nuevo Gato')
        print('3: Buscar animales por código')
        print('4: Pasar la inspección de un animal') #Clase abstracta
        print('5: Volver al inicio')

        seleccion = int(input('Elija un apartado (1/2/3/4/5): '))
        print()

        while seleccion < 1 or seleccion > 5:  # Obliga a seleccionar bien
            print('Elija un valor válido')
            seleccion = int(input('Elija un apartado (1/2/3/4): '))

        if seleccion == 1:  # Añadir perro
            pass

        elif seleccion == 2:  # Añadir gato
            print('Puedes añadir el gato a los siguientes refugios:')
            refugio_seleccionado = seleccionar_refugio()

            if len(refugio_seleccionado.animales) >= refugio_seleccionado.tamaño:
                print('Este refugio ya está lleno\n')

            else:
                print('Ahora introduzca los datos del gato:')
                nombre = input('Nombre: ')
                edad = int(input('Edad: '))
                raza = input('Raza: ')

                Gato(nombre, edad, raza, refugio_seleccionado)
                print('Se ha introducido correctamente al gato en la base de datos\n')


        elif seleccion == 3:  # Ver todos los animales
            pass

        elif seleccion == 4:  # Llamar a la función necesidad e inspección
            print('Vamos a pasar una inspección')
            print('De que refugio?')

            refugio_seleccionado = seleccionar_refugio()
            print('De que animal vamos a pasar la inspección?')

            for animal in refugio_seleccionado.animales:
                print(f'{animal.codigo}: {animal.nombre}, {animal.especie}')

            seleccion_codigo = input('Seleccione el código de un animal: ')

            #Falta hacer que se seleccione el código del animal y se pase la inspección de ese animal



        elif seleccion == 5:  #Volver para atrás
            seguir = False



if __name__ == '__main__':
    ejecutando = True
    while ejecutando:

        mis_refugios = []
        print('Bienvenido al sistema, primero introduzca los datos necesaríos')
        nombre = input('Nombre del refugio: ').lower()
        capacidad = int(input('Espacio máximo del refugio: '))
        print()

        mi_refugio = Refugio(nombre, capacidad)
        mis_refugios.append(mi_refugio)

        inicio = True
        while inicio:

            print('-' * 50)
            print('Base de datos del refugio de animales')
            print('-' * 50)
            print('Deberá seleccionar uno de los siguientes apartados:')
            print('1: Apartado Animales')
            print('2: Apartado Trabajadores')
            print('3: Apartado Clientes')
            print('4: Apartado Refugios')
            print('5: Crear un nuevo refugio')
            print('6: Salir')

            seleccion = int(input('Elija un apartado (1/2/3/4/5/6): '))
            print()


            if seleccion == 1:#Apartado animales
                animales()

            elif seleccion == 2: #Apartado Trabajadores
                pass

            elif seleccion == 3: #Apartado Clientes
                pass

            elif seleccion == 5:
                pass

            elif seleccion == 5: #Crear nuevo refugio
                pass

            elif seleccion == 6: #Salir del programa
                inicio = False
                ejecutando = False

            else:
                print('Opción no valida')
                print()