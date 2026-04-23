from Animales.ClaseAnimales import *
from Animales.ClaseGato import *
from Animales.ClasePerro import *


if __name__ == '__main__':
    def menu():
        print('-'*50)
        print('Base de datos del refugio de animales')
        print('-'*50)

        ejecutando = True

        while (ejecutando):
            print('Deberá seleccionar uno de los siguientes apartados:')
            print('1: Apartado Animales')
            print('2: Apartado Trabajadores')
            print('3: Apartado Clientes')

            seleccion = int(input('Elija un apartado (1/2/3: )'))


            if seleccion == 1:
                pass

            elif seleccion == 2:
                pass

            elif seleccion == 3:
                pass

            else:
                print('Opción no valida')
