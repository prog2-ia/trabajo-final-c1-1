from ClaseRefugio import *
from Animales.ClaseGato import *
from Animales.ClasePerro import *
from Personas.ClaseUsuario import *
from Personas.ClaseCuidador import *
from Personas.ClaseLimpiador import *
from Personas.ClaseU_Prioritario import *


def seleccionar_refugio(): #Para siempre que haya que seleccionar un refugio y mostrar todos sus nombres
    for refugio in mis_refugios:
        print(refugio)

    refugio_seleccionado = None

    while refugio_seleccionado == None:
        refu = input('¿Que refugio elijes?: ')
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
        print('5: Adopción de animal')
        print('6: Volver al inicio')

        seleccion = int(input('Elija un apartado (1/2/3/4/5/6): '))
        print()

        while seleccion < 1 or seleccion > 5:  # Obliga a seleccionar bien
            print('Elija un valor válido')
            seleccion = int(input('Elija un apartado (1/2/3/4/5/6): '))


        if seleccion == 1:  # Añadir perro
            print('Puedes añadir el perro a los siguientes refugios:')
            refugio_seleccionado = seleccionar_refugio()

            if len(refugio_seleccionado.animales) >= refugio_seleccionado.tamaño:
                print('Este refugio ya está lleno\n')

            else:
                print('Ahora introduzca los datos del perro:')
                nombre = input('Nombre: ')
                entrada = ''
                while not entrada.isdigit():
                    entrada = input('Edad: ')
                    if entrada.isdigit():
                        edad = int(entrada)
                    else:
                        print('Debe introducir un número')

                raza = input('Raza: ')

                Perro(nombre, edad, raza, refugio_seleccionado)
                print('Se ha introducido correctamente al perro en la base de datos\n')


        elif seleccion == 2:  # Añadir gato
            print('Puedes añadir el gato a los siguientes refugios:')
            refugio_seleccionado = seleccionar_refugio()

            if len(refugio_seleccionado.animales) >= refugio_seleccionado.tamaño:
                print('Este refugio ya está lleno\n')

            else:
                print('Ahora introduzca los datos del gato:')
                nombre = input('Nombre: ')
                entrada = ''
                while not entrada.isdigit():
                    entrada = input('Edad: ')
                    if entrada.isdigit():
                        edad = int(entrada)
                    else:
                        print('Debe introducir un número')

                raza = input('Raza: ')

                Gato(nombre, edad, raza, refugio_seleccionado)
                print('Se ha introducido correctamente al gato en la base de datos\n')


        elif seleccion == 3:  # Ver todos los animales
            print('¿En que refugio se encuentra el animal que buscas?: ')
            refugio_seleccionado = seleccionar_refugio()
            if len(refugio_seleccionado.animales) == 0:
                print('No hay animales en este refugio por el momento\n')

            else:
                refugio_seleccionado.mostrar_animales()

            elegido = False
            while not elegido:
                seleccion_codigo = input('Seleccione el código de un animal: ')
                for animal in refugio_seleccionado.animales:
                    if seleccion_codigo == animal.codigo:
                        elegido = True
                        nombre_final = animal

                if not elegido:
                    print('El animal seleccionado no está en el refugio elegido')

            print(f'Ha elegido a {nombre_final}')
            print(f'{nombre_final.informe}\n')


        elif seleccion == 4:  # Llamar a la función necesidad e inspección
            print('Vamos a pasar una inspección')
            print('De que refugio?')

            refugio_seleccionado = seleccionar_refugio()
            print('De que animal vamos a pasar la inspección?')

            refugio_seleccionado.mostrar_animales()

            elegido = False
            while not elegido:
                seleccion_codigo = input('Seleccione el código de un animal: ')
                for animal in refugio_seleccionado.animales:
                    if seleccion_codigo == animal.codigo:
                        elegido = True
                        nombre_final = animal

                if not elegido:
                    print('El animal seleccionado no está en el refugio elegido')

            comida = input('¿Que comida debe tomar el animal? ')

            if nombre_final.especie == 'gato':
                estado_garras = input('¿En que estado se encuentran las garras del gato?: ')
                enfermo = input('¿El gato está enfermo? (s/n) ')
                if enfermo == 's':
                    enfermedad = input('¿Que enfermedad padece? ')
                    cura = input('¿Cual es la cura de la enfermedad? ')
                    informe = nombre_final.inspeccion(comida, estado_garras, enfermedad, cura)
                else:
                    informe = nombre_final.inspeccion(comida, estado_garras)

            elif nombre_final.especie == 'perro':
                estado_dientes = input('¿En que estado se encuentran las garras del gato?: ')
                enfermo = input('¿El gato está enfermo? (s/n) ')
                if enfermo == 's':
                    enfermedad = input('¿Que enfermedad padece? ')
                    cura = input('¿Cual es la cura de la enfermedad? ')
                    informe = nombre_final.inspeccion(comida, estado_dientes, enfermedad, cura)
                else:
                    informe = nombre_final.inspeccion(comida, estado_dientes)

            print(informe)


        elif seleccion == 5:  #Animal adoptado
            print('--- TRÁMITE DE ADOPCIÓN ---')
            refugio_seleccionado = seleccionar_refugio()

            if len(refugio_seleccionado.animales) == 0:
                print('No hay animales en este refugio.\n')

            else:
                refugio_seleccionado.mostrar_animales()
                codigo = input('Introduce el código del animal a adoptar: ')

                exito = refugio_seleccionado.adoptar(codigo)

                if exito:
                    print(f'¡Felicidades! el animal con código {codigo} ha sido adoptado')

                else:
                    print(f'Error: No existe ningún animal con código {codigo} en el refugio {refugio_seleccionado.nombre}')


        elif seleccion == 6:  #Volver para atrás
            seguir = False



def refugios(mis_refugios):
    seguir = True
    while seguir:
        print('Bienvenido al apartado refugios, estas son las opciones:')
        print('1: Mirar tus refugios y su capacidad actual')
        print('2: Crear un nuevo refugio')
        print('3: Volver al inicio')

        seleccion = int(input('Elija un apartado (1/2/3): '))
        print()

        while seleccion < 1 or seleccion > 5:  # Obliga a seleccionar bien
            print('Elija un valor válido')
            seleccion = int(input('Elija un apartado (1/2/3): '))


        if seleccion == 1:  # Mirar los refugios que tiene
            for refugio in mis_refugios:
                if len(refugio.animales) == refugio.capacidad:
                    print(f'El refugio {refugio.nombre} está al máximo de su capacidad, deberá crear otro refugio para seguir acogiendo animales')

                elif len(refugio.animales) == 0:
                    print(f'El refugio {refugio.nombre} no tiene ningún animal todavía')

                else:
                    print (f'El refugio {refugio.nombre} ahora mismo tiene {refugio.animales} en el, por lo que caben {len(refugio.animales) - refugio.capacidad}')


        elif seleccion == 2:  # Añadir un refugio
            print('Vamos a añadir un nuevo refugio: ')
            nombre = input('Nombre del refugio: ').lower()
            capacidad = int(input('Espacio máximo del refugio: '))
            print()

            mi_refugio = Refugio(nombre, capacidad)
            mis_refugios.append(mi_refugio)


        elif seleccion == 3:  # Volver para atrás
            seguir = False

    return mis_refugios



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
            print('5: Salir')

            seleccion = int(input('Elija un apartado (1/2/3/4/5): '))
            print()


            if seleccion == 1:#Apartado animales
                animales()

            elif seleccion == 2: #Apartado Trabajadores
                pass

            elif seleccion == 3: #Apartado Clientes
                pass

            elif seleccion == 4: #Apartado Refugios
                mis_refugios = refugios(mis_refugios)

            elif seleccion == 5: #Salir del programa
                inicio = False
                ejecutando = False

            else:
                print('Opción no valida')
                print()