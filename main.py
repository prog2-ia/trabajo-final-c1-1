from ClaseRefugio import *
from Animales.ClaseGato import *
from Animales.ClasePerro import *
from Animales.ClaseCaballo import *
from Personas.ClaseUsuario import *
from Personas.ClaseCuidador import *
from Personas.ClaseLimpiador import *
from Personas.ClaseU_Prioritario import *
import os



def pedir_entero(entrada):
    entero = False
    while not entero:
        try:
            valor = int(input(entrada))
            return valor
        except ValueError:
            print('Error: Debe introducir un número entero válido')



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



def añadir_animal(): #Elección 2 en la función animales
    seleccion = pedir_entero('Elija un animal a añadir: ')

    while seleccion < 1 or seleccion > 3:
        seleccion = pedir_entero('Error: Introduzca un valor dentro del rango')

    if seleccion == 1:  # Añadir perro
        print('\n--- AÑADIR PERRO A UN REFUGIO ---')
        print('Puedes añadir el perro a los siguientes refugios:')
        refugio_seleccionado = seleccionar_refugio()

        if len(refugio_seleccionado.animales) >= refugio_seleccionado.tamaño:
            print('Este refugio ya está lleno\n')

        else:
            print('Ahora introduzca los datos del perro:')
            nombre = input('Nombre: ')
            edad = pedir_entero('Edad: ')
            raza = input('Raza: ')

            Perro(nombre, edad, raza, refugio_seleccionado)
            print('Se ha introducido correctamente al perro en la base de datos\n')

    elif seleccion == 2:
        print('--- AÑADIR GATO A UN REFUGIO ---\n')
        print('Puedes añadir el gato a los siguientes refugios:')
        refugio_seleccionado = seleccionar_refugio()

        if len(refugio_seleccionado.animales) >= refugio_seleccionado.tamaño:
            print('Este refugio ya está lleno\n')

        else:
            print('Ahora introduzca los datos del gato:')
            nombre = input('Nombre: ')
            edad = pedir_entero('Edad: ')
            raza = input('Raza: ')

            Gato(nombre, edad, raza, refugio_seleccionado)
            print('Se ha introducido correctamente al gato en la base de datos\n')

    elif seleccion == 3:
        print('--- AÑADIR CABALLO A UN REFUGIO ---\n')
        print('Puedes añadir el caballo a los siguientes refugios:')
        refugio_seleccionado = seleccionar_refugio()

        if len(refugio_seleccionado.animales) >= refugio_seleccionado.tamaño:
            print('Este refugio ya está lleno\n')

        else:
            print('Ahora introduzca los datos del caballo:')
            nombre = input('Nombre: ')
            edad = pedir_entero('Edad: ')
            raza = input('Raza: ')

            Caballo(nombre, edad, raza, refugio_seleccionado)
            print('Se ha introducido correctamente al caballo en la base de datos\n')



def animales():

    seguir = True
    while seguir:
        print('Bienvenido al apartado animales, estas son las opciones:')
        print('1: Añadir un nuevo Animal')
        print('2: Buscar animales por código')
        print('3: Pasar la inspección de un animal') #Clase abstracta
        print('4: Adopción de animal')
        print('5: Volver al inicio')

        seleccion = pedir_entero('Elija un apartado (1/2/3/4/5): ')
        print()

        while seleccion < 1 or seleccion > 5:  # Obliga a seleccionar bien
            print('Elija un valor válido')
            seleccion = pedir_entero('Elija un apartado (1/2/3/4/5): ')


        if seleccion == 1:  # Añadir animal
            print('Puedes añadir uno de los siguientes animales: ')
            print('1: Perro')
            print('2: Gato')
            print('3: Caballo')

            añadir_animal()


        elif seleccion == 2:  # Ver todos los animales
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


        elif seleccion == 3:  # Llamar a la función necesidad e inspección
            print('Vamos a pasar una inspección')
            print('De que refugio?')

            refugio_seleccionado = seleccionar_refugio()

            if len(refugio_seleccionado.animales) == 0:
                print('En este refugio no tiene animales por el momento\n')

            elif len(refugio_seleccionado.animales) > 0:
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
                    estado_dientes = input('¿En que estado se encuentran los dientes del perro?: ')
                    enfermo = input('¿El perro está enfermo? (s/n) ')
                    if enfermo == 's':
                        enfermedad = input('¿Que enfermedad padece? ')
                        cura = input('¿Cual es la cura de la enfermedad? ')
                        informe = nombre_final.inspeccion(comida, estado_dientes, enfermedad, cura)
                    else:
                        informe = nombre_final.inspeccion(comida, estado_dientes)


                elif nombre_final.especie == 'caballo':
                    estado_pezuñas = input('¿En que estado se encuentran las pezuñas del caballo?: ')
                    enfermo = input('¿El caballo está enfermo? (s/n) ')
                    if enfermo == 's':
                        enfermedad = input('¿Que enfermedad padece? ')
                        cura = input('¿Cual es la cura de la enfermedad? ')
                        informe = nombre_final.inspeccion(comida, estado_pezuñas, enfermedad, cura)
                    else:
                        informe = nombre_final.inspeccion(comida, estado_pezuñas)

                print()
                print(informe)

                nombre_carpeta = 'Informes'

                if not os.path.exists(nombre_carpeta):
                    os.makedirs(nombre_carpeta)

                nombre_archivo = f"{nombre_carpeta}/Informe_{nombre_final.codigo}_{nombre_final.nombre}.txt"
                with open(nombre_archivo, "w", encoding="utf-8") as fichero:
                    fichero.write(informe)

                print(f'Informe guardado en {nombre_archivo}')
                input('Pulse [Enter] para continuar')


        elif seleccion == 4:  #Animal adoptado
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


        elif seleccion == 5:  #Volver para atrás
            seguir = False



def refugios(mis_refugios):
    seguir = True
    while seguir:
        print('Bienvenido al apartado refugios, estas son las opciones:')
        print('1: Mirar tus refugios y su capacidad actual')
        print('2: Crear un nuevo refugio')
        print('3: Volver al inicio')

        seleccion = pedir_entero('Elija un apartado (1/2/3): ')
        print()

        while seleccion < 1 or seleccion > 5:  # Obliga a seleccionar bien
            print('Elija un valor válido')
            seleccion = pedir_entero('Elija un apartado (1/2/3): ')


        if seleccion == 1:# Mirar los refugios que tiene
            print('--- REFUGIOS ACTUALES ---\n')
            for refugio in mis_refugios:
                if len(refugio.animales) == refugio.tamaño:
                    print(f'\033[1m{refugio.nombre.upper()}\033[0m: Está al máximo de su capacidad, deberá crear otro refugio para seguir acogiendo animales')

                elif len(refugio.animales) == 0:
                    print(f'\033[1m{refugio.nombre.upper()}\033[0m: No tiene ningún animal todavía')

                else:
                    print (f'\033[1m{refugio.nombre.upper()}\033[0m: Ahora mismo tiene {refugio.animales} en el, por lo que caben {len(refugio.animales) - refugio.tamaño} animales más')

                print()


        elif seleccion == 2:  # Añadir un refugio
            print('Vamos a añadir un nuevo refugio: ')
            nombre = input('Nombre del refugio: ').lower()
            tamaño = pedir_entero('Espacio máximo del refugio: ')
            print()

            mi_refugio = Refugio(nombre, tamaño)
            mis_refugios.append(mi_refugio)


        elif seleccion == 3:  # Volver para atrás
            seguir = False

    return mis_refugios


def pedir_dni():
    while:
        dni = input('DNI: ')
        if len(str(nuevo_dni)) == 9:
            return dni
        else:
            return f"Error: El DNI debe tener 9 caracteres."

def añadir_empleado(): #Elección 2 en la función animales
    seleccion = pedir_entero('¿Cuál es su futura ocupación? ')
    while seleccion < 1 or seleccion > 2:  # Obliga a seleccionar bien
        print('Elija un valor válido')
        seleccion = int(input('Elija un apartado (1/2): '))

    if seleccion == 1:  # Añadir perro
        print('\n--- NUEVO CUIDADOR EN EL REFUGIO ---')
        print('Puedes añadir al nuevo trabajador en los siguientes refugios:')
        refugio_seleccionado = seleccionar_refugio()

        print('Ahora introduzca los datos del empleado:')
        nombre = input('Nombre: ')
        edad = pedir_entero('Edad: ')
        genero = input('Género: ')
        DNI = pedir_dni()


        Cuidador(nombre, edad, genero, DNI, refugio_seleccionado)
        print('Se ha introducido correctamente al cuidador/a en la base de datos\n')

    elif seleccion == 2:
        print('--- NUEVO LIMPIADOR EN EL REFUGIO ---\n')
        print('Puedes añadir el nuevo trabajador en los siguientes refugios:')
        refugio_seleccionado = seleccionar_refugio()

        print('Ahora introduzca los datos del empleado:')
        nombre = input('Nombre: ')
        edad = pedir_entero('Edad: ')
        genero = input('Género: ')
        DNI = pedir_dni()
        salario = pedir_entero('Introduzca el salario inicial acordado: ')

        Limpiador(nombre, edad, genero, DNI, salario, refugio_seleccionado)
        print('Se ha introducido correctamente al limpiador/a en la base de datos\n')



def trabajadores():
    seguir = True
    while seguir:
        print('Bienvenido al apartado trabajadores, estas son las opciones:')
        print('1: Añadir un nuevo Trabajador')
        print('2: Buscar trabajadores por DNI')
        print('3: Registro del trabajo de hoy')  # Clase abstracta
        print('4: (Cuidadores Only) Añadir animal con el que trabajar')
        print('5: Volver al inicio')

        seleccion = pedir_entero('Elija un apartado (1/2/3/4/5): ')
        print()

        while seleccion < 1 or seleccion > 5:  # Obliga a seleccionar bien
            print('Elija un valor válido')
            seleccion = pedir_entero('Elija un apartado (1/2/3/4/5): ')

        if seleccion == 1:  # Añadir animal
            print('Opciones de empleo ')
            print('1: Cuidador')
            print('2: Limpiador')

            añadir_empleado()


        elif seleccion == 2:  # Ver todos los animales
            print('¿En que refugio se encuentra el empleado que buscas?: ')
            refugio_seleccionado = seleccionar_refugio()
            if len(refugio_seleccionado.empleados) == 0:
                print('No hay empleados en este refugio por el momento\n')

            else:
                refugio_seleccionado.mostrar_empleados()

                elegido = False
                while not elegido:
                    print("A continución introduzca el DNI del empleado que busca.")
                    seleccion_codigo = pedir_dni()
                    for empleado in refugio_seleccionado.empleados:
                        if seleccion_codigo == empleado.dni:
                            elegido = True
                            nombre_final = empleado

                    if not elegido:
                        print('El animal seleccionado no está en el refugio elegido')

                print(f'Ha elegido a {nombre_final}')
                cambio = input('Desea cambiar el DNI?(S/N) ')
                if cambio.upper() == 'S':
                    nuevo_dni = pedir_dni()
                    empleado.dni = nuevo_dni


        elif seleccion == 3:  # Llamar a la función necesidad e inspección
            print('Momento de ver cuanti tiempo hemos trabajado hoy')
            print('De que refugio?')

            refugio_seleccionado = seleccionar_refugio()

            if len(refugio_seleccionado.empleados) == 0:
                print('En este refugio no tiene animales por el momento\n')

            elif len(refugio_seleccionado.empleados) > 0:
                print('De que empleado vamos a pasar la inspección?')

                refugio_seleccionado.mostrar_empleados()

                elegido = False
                while not elegido:
                    seleccion_codigo = pedir_dni()
                    for empleado in refugio_seleccionado.empleados:
                        if seleccion_codigo == empleado.codigo:
                            elegido = True
                            nombre_final = empleado

                    if not elegido:
                        print('El empleado seleccionado no está en el refugio elegido')

                if nombre_final.oficio == 'Cuidador':
                    animal = input('¿Con que animal está trabajando?: ')
                    horas = pedir_entero('¿Cuantas horas ha trabajado? ')

                elif nombre_final.especie == 'perro':
                    estado_dientes = input('¿En que estado se encuentran los dientes del perro?: ')
                    enfermo = input('¿El perro está enfermo? (s/n) ')
                    if enfermo == 's':
                        enfermedad = input('¿Que enfermedad padece? ')
                        cura = input('¿Cual es la cura de la enfermedad? ')
                        informe = nombre_final.inspeccion(comida, estado_dientes, enfermedad, cura)
                    else:
                        informe = nombre_final.inspeccion(comida, estado_dientes)

                print(informe)
                input('Pulse [Enter] para continuar')



def clientes():
    pass



if __name__ == '__main__':
    ejecutando = True
    while ejecutando:

        mis_refugios = []
        print('Bienvenido al sistema, primero introduzca los datos necesaríos')
        nombre = input('Nombre del refugio: ').lower()
        tamaño = pedir_entero('Espacio máximo del refugio: ')
        print()

        mi_refugio = Refugio(nombre, tamaño)
        mis_refugios.append(mi_refugio)

        inicio = True
        while inicio:

            print('-' * 50)
            print('Base de datos del refugio de animales')
            print('-' * 50)
            print()
            print('Deberá seleccionar uno de los siguientes apartados:')
            print('1: Apartado Animales')
            print('2: Apartado Trabajadores')
            print('3: Apartado Clientes')
            print('4: Apartado Refugios')
            print('5: Salir')

            seleccion = pedir_entero('Elija un apartado (1/2/3/4/5): ')
            print()


            if seleccion == 1:#Apartado animales
                animales()

            elif seleccion == 2: #Apartado Trabajadores
                trabajadores()

            elif seleccion == 3: #Apartado Clientes
                clientes()

            elif seleccion == 4: #Apartado Refugios
                mis_refugios = refugios(mis_refugios)

            elif seleccion == 5: #Salir del programa
                inicio = False
                ejecutando = False

            else:
                print('Opción no valida')
                print()