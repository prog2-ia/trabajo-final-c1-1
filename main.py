from ClaseRefugio import *
from Animales.ClaseAnimales import *
from Animales.ClaseGato import *
from Animales.ClasePerro import *


if __name__ == '__main__':
    mis_refugios = []
    print('Bienvenido al sistema, primero introduzca los datos necesaríos')
    nombre = input('Nombre del refugio: ').lower()
    capacidad = int(input('Espacio máximo del refugio: '))

    nombre = Refugio(nombre, capacidad)
    mis_refugios.append(nombre)

    print('-'*50)
    print('Base de datos del refugio de animales')
    print('-'*50)

    ejecutando = True

    while ejecutando:
        print('Deberá seleccionar uno de los siguientes apartados:')
        print('1: Apartado Animales')
        print('2: Apartado Trabajadores')
        print('3: Apartado Clientes')
        print('4: Crear un nuevo refugio')

        seleccion = int(input('Elija un apartado (1/2/3/4): '))


        if seleccion == 1: #Apartado animales
            print('Bienvenido al apartado animales, estas son las opciones:')
            print('1: Añadir un nuevo Perro')
            print('2: Añadir un nuevo Gato')
            print('3: Buscar animales por código')
            print('4: Hacer chequeo médico a un animal')

            seleccion_animales = int(input('Elija un apartado (1/2/3/4): '))

            if seleccion_animales < 1 or seleccion_animales > 4: #Obliga a seleccionar bien
                print('Elija un valor válido')
                seleccion_animales = int(input('Elija un apartado (1/2/3/4): '))


            if seleccion_animales == 1: #Añadir perro
                pass

            elif seleccion_animales == 2: #Añadir gato
                print('Vamos a añadir el gato al refugio:')
                nombre = input('Nombre: ')
                edad = input('Edad: ')
                raza = input('Raza: ')
                print('Los refugios que tienes disponibles son:')
                for refugio in mis_refugios:
                    print(refugio)
                refu = input('A cual quieres añadirlo: ').lower()

                while refu not in mis_refugios:
                    print('Ese refugio no está en tú lista de refugios')
                    refu = input('A cual quieres añadirlo: ').lower()



            elif seleccion_animales == 3: #Ver todos los animales
                pass

            elif seleccion_animales == 4: #Llamada a la función necesidad para chequeo
                pass


        elif seleccion == 2: #Apartado Trabajadores
            pass

        elif seleccion == 3: #Apartado Clientes
            pass

        elif seleccion == 4: #Crear nuevo refugio
            pass

        else:
            print('Opción no valida')
