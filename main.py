from ClaseRefugio import *
from Animales.ClaseAnimales import *
from Animales.ClaseGato import *
from Animales.ClasePerro import *
from Animales.ClaseNecesidad import *


if __name__ == '__main__':

    ejecutando = True
    while ejecutando:

        mis_refugios = []
        print('Bienvenido al sistema, primero introduzca los datos necesaríos')
        nombre = input('Nombre del refugio: ').lower()
        capacidad = int(input('Espacio máximo del refugio: '))
        print()

        mi_refugio = Refugio(nombre, capacidad)  # Arreglar esto
        mis_refugios.append(mi_refugio)

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


        seleccion = int(input('Elija un apartado (1/2/3/4/5): '))
        print()


        if seleccion == 1: #Apartado animales
            print('Bienvenido al apartado animales, estas son las opciones:')
            print('1: Añadir un nuevo Perro')
            print('2: Añadir un nuevo Gato')
            print('3: Buscar animales por código')
            print('4: Hacer chequeo médico a un animal')
            #Falta hacer un volver para atrás

            seleccion_animales = int(input('Elija un apartado (1/2/3/4): '))
            print()

            if seleccion_animales < 1 or seleccion_animales > 4: #Obliga a seleccionar bien
                print('Elija un valor válido')
                seleccion_animales = int(input('Elija un apartado (1/2/3/4): '))


            if seleccion_animales == 1: #Añadir perro
                pass

            elif seleccion_animales == 2: #Añadir gato
                print('Puedes añadir el gato a los siguientes refugios:')
                for refugio in mis_refugios:
                    print(refugio)

                refu = input('¿A que refugio quieres añadirlo?: ')
                refugio_seleccionado = None

                for refugio in mis_refugios:
                    if refugio.nombre.lower() == refu.lower():
                        refugio_seleccionado = refugio

                if refugio_seleccionado == None:
                    print('Este refugio no está en tú lista de refugios')

                else:
                    print(f'El refugio seleccionado es: {refugio_seleccionado.nombre}')

                    if len(refugio_seleccionado.animales) >= refugio_seleccionado.tamaño:
                        print('Este refugio ya está lleno')

                    else:
                        print('Ahora introduzca los datos del gato:')
                        nombre = input('Nombre: ')
                        edad = int(input('Edad: '))
                        raza = input('Raza: ')

                        nuevo_animal = Gato(nombre, edad, raza, refugio_seleccionado)
                        print('Se ha introducido correctamente al gato en la base de datos')
                        #Falta hacer que no salte al inicio otra vez



            elif seleccion_animales == 3: #Ver todos los animales
                pass

            elif seleccion_animales == 4: #Llamada a la función necesidad para chequeo
                pass


        elif seleccion == 2: #Apartado Trabajadores
            pass

        elif seleccion == 3: #Apartado Clientes
            pass

        elif seleccion == 5:
            pass

        elif seleccion == 5: #Crear nuevo refugio
            pass

        elif seleccion == 6: #Salir del programa
            ejecutando = False

        # Falta hacer el error de un número mayor o menor

        else:
            print('Opción no valida')
            print()