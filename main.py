from ClaseRefugio import *
from Animales.ClaseGato import *
from Animales.ClasePerro import *
from Animales.ClaseCaballo import *
from Personas.ClaseUsuario import *
from Personas.ClaseCuidador import *
from Personas.ClaseLimpiador import *
from Personas.ClaseU_Prioritario import *
from Personas.ClaseVoluntario import *
import os
import pickle
from datetime import datetime



def pedir_entero(entrada):
    entero = False
    while not entero:
        try:
            valor = int(input(entrada))
            return valor
        except ValueError:
            print('Error: Debe introducir un número entero válido')



def seleccionar_refugio(mis_refugios): #Para siempre que haya que seleccionar un refugio y mostrar todos sus nombres
    if len(mis_refugios) == 0:
        print('ERROR: No hay ningún refugio creado.')
        return None

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



def anyadir_animal(mis_refugios): #Elección 2 en la función animales
    seleccion = pedir_entero('Elija un animal a añadir: ')

    while seleccion < 1 or seleccion > 3:
        seleccion = pedir_entero('Error: Introduzca un valor dentro del rango')

    if seleccion == 1:  # Añadir perro
        print('\n--- AÑADIR PERRO A UN REFUGIO ---')
        print('Puedes añadir el perro a los siguientes refugios:')
        refugio_seleccionado = seleccionar_refugio(mis_refugios)
        if refugio_seleccionado == None:
            return

        if len(refugio_seleccionado.animales) >= refugio_seleccionado.tamanyo:
            print('Este refugio ya está lleno\n')

        else:
            print('Ahora introduzca los datos del perro:')
            nombre = input('Nombre: ')
            edad = pedir_entero('Edad: ')
            raza = input('Raza: ')

            nuevo_perro = Perro(nombre, edad, raza, refugio_seleccionado)
            print('Se ha introducido correctamente al perro en la base de datos\n')

    elif seleccion == 2:
        print('--- AÑADIR GATO A UN REFUGIO ---\n')
        print('Puedes añadir el gato a los siguientes refugios:')
        refugio_seleccionado = seleccionar_refugio(mis_refugios)
        if refugio_seleccionado == None:
            return

        if len(refugio_seleccionado.animales) >= refugio_seleccionado.tamanyo:
            print('Este refugio ya está lleno\n')

        else:
            print('Ahora introduzca los datos del gato:')
            nombre = input('Nombre: ')
            edad = pedir_entero('Edad: ')
            raza = input('Raza: ')

            nuevo_gato = Gato(nombre, edad, raza, refugio_seleccionado)
            print('Se ha introducido correctamente al gato en la base de datos\n')

    elif seleccion == 3:
        print('--- AÑADIR CABALLO A UN REFUGIO ---\n')
        print('Puedes añadir el caballo a los siguientes refugios:')
        refugio_seleccionado = seleccionar_refugio(mis_refugios)
        if refugio_seleccionado == None:
            return

        if len(refugio_seleccionado.animales) >= refugio_seleccionado.tamanyo:
            print('Este refugio ya está lleno\n')

        else:
            print('Ahora introduzca los datos del caballo:')
            nombre = input('Nombre: ')
            edad = pedir_entero('Edad: ')
            raza = input('Raza: ')

            nuevo_caballo = Caballo(nombre, edad, raza, refugio_seleccionado)
            print('Se ha introducido correctamente al caballo en la base de datos\n')



def animales(mis_refugios, lista_usuarios):

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

            anyadir_animal(mis_refugios)


        elif seleccion == 2:  # Ver todos los animales
            print('¿En que refugio se encuentra el animal que buscas?: ')
            refugio_seleccionado = seleccionar_refugio(mis_refugios)
            if refugio_seleccionado == None:
                return
            if len(refugio_seleccionado.animales) == 0:
                print('No hay animales en este refugio por el momento\n')

            else:
                refugio_seleccionado.mostrar_animales()

                elegido = False
                while not elegido:
                    seleccion_codigo = input('Seleccione el código de un animal: ').upper()
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

            refugio_seleccionado = seleccionar_refugio(mis_refugios)
            if refugio_seleccionado == None:
                return

            if len(refugio_seleccionado.animales) == 0:
                print('En este refugio no tiene animales por el momento\n')

            elif len(refugio_seleccionado.animales) > 0:
                print('De que animal vamos a pasar la inspección?')

                refugio_seleccionado.mostrar_animales()

                elegido = False
                while not elegido:
                    seleccion_codigo = input('Seleccione el código de un animal: ').upper()
                    for animal in refugio_seleccionado.animales:
                        if seleccion_codigo == animal.codigo:
                            elegido = True
                            nombre_final = animal

                    if not elegido:
                        print('El animal seleccionado no está en el refugio elegido')

                comida = input('¿Que comida debe tomar el animal? ')

                if nombre_final.especie == 'gato':
                    estado_garras = input('¿En que estado se encuentran las garras del gato?: ')
                    enfermo = input('¿El gato está enfermo? (s/n) ').lower()
                    if enfermo == 's':
                        enfermedad = input('¿Que enfermedad padece? ')
                        cura = input('¿Cual es la cura de la enfermedad? ')
                        informe = nombre_final.inspeccion(comida, estado_garras, enfermedad, cura)
                    else:
                        informe = nombre_final.inspeccion(comida, estado_garras)


                elif nombre_final.especie == 'perro':
                    estado_dientes = input('¿En que estado se encuentran los dientes del perro?: ')
                    enfermo = input('¿El perro está enfermo? (s/n) ').lower()
                    if enfermo == 's':
                        enfermedad = input('¿Que enfermedad padece? ')
                        cura = input('¿Cual es la cura de la enfermedad? ')
                        informe = nombre_final.inspeccion(comida, estado_dientes, enfermedad, cura)
                    else:
                        informe = nombre_final.inspeccion(comida, estado_dientes)


                elif nombre_final.especie == 'caballo':
                    estado_pezunyas = input('¿En que estado se encuentran las pezuñas del caballo?: ')
                    enfermo = input('¿El caballo está enfermo? (s/n) ').lower()
                    if enfermo == 's':
                        enfermedad = input('¿Que enfermedad padece? ')
                        cura = input('¿Cual es la cura de la enfermedad? ')
                        informe = nombre_final.inspeccion(comida, estado_pezunyas, enfermedad, cura)
                    else:
                        informe = nombre_final.inspeccion(comida, estado_pezunyas)

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
            if len(lista_usuarios) == 0:
                print('No hay usuarios que puedan adoptar.\n')
                return

            print('¿Quien va a adoptar al animal?')
            for persona in lista_usuarios:
                print(persona.dni)

            dni = pedir_dni()
            cliente = buscar_usuario(dni, lista_usuarios)
            while cliente == None:
                print('Este usuario no existe')
                dni = pedir_dni()
                cliente = buscar_usuario(dni, lista_usuarios)

            print('Posibles refugios a elegir:')
            refugio_seleccionado = seleccionar_refugio(mis_refugios)
            if refugio_seleccionado == None:
                return

            if len(refugio_seleccionado.animales) == 0:
                print('No hay animales en este refugio.\n')

            else:
                refugio_seleccionado.mostrar_animales()
                codigo = input('Introduce el código del animal a adoptar: ')

                exito = refugio_seleccionado.adoptar(codigo, cliente.dni)

                if exito:
                    print(f'¡Felicidades! el animal con código {codigo} ha sido adoptado por {cliente.nombre} con DNI: {cliente.dni}.\n ')
                    carpeta_historial = 'Historial'

                    if not os.path.exists(carpeta_historial):
                        os.makedirs(carpeta_historial)

                    try:
                        ruta_txt = os.path.join(carpeta_historial, 'Historial_Adopción.txt')
                        fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

                        with open(ruta_txt, "a", encoding="utf-8") as fichero:
                            fichero.write(f"[{fecha}] El animal con código {codigo} del refugio '{refugio_seleccionado.nombre}' ha sido adoptado por {cliente.nombre} con DNI: {cliente.dni}.\n")

                    except Exception as e:
                        print(f"Error al escribir el historial: {e}")

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
                if len(refugio.animales) == refugio.tamanyo:
                    print(f'\033[1m{refugio.nombre.upper()}\033[0m: Está al máximo de su capacidad, deberá crear otro refugio para seguir acogiendo animales')

                elif len(refugio.animales) == 0:
                    print(f'\033[1m{refugio.nombre.upper()}\033[0m: No tiene ningún animal todavía')

                else:
                    print (f'\033[1m{refugio.nombre.upper()}\033[0m: Ahora mismo tiene {refugio.animales} en el, por lo que caben {len(refugio.animales) - refugio.tamanyo} animales más')

                print()


        elif seleccion == 2:  # Añadir un refugio
            print('Vamos a añadir un nuevo refugio: ')
            nombre = input('Nombre del refugio: ').lower()
            tamanyo = pedir_entero('Espacio máximo del refugio: ')
            print()

            mi_refugio = Refugio(nombre, tamanyo)
            mis_refugios.append(mi_refugio)


        elif seleccion == 3:  # Volver para atrás
            seguir = False

    return mis_refugios


def pedir_dni():
    seguir = True
    while seguir:
        dni = input('DNI: ')
        if len(str(dni)) == 9:
            return dni
        else:
            print("Error: El DNI debe tener 9 caracteres.")

def anyadir_empleado(mis_refugios): #
    seleccion = pedir_entero('¿Cuál es su futura ocupación? ')
    while seleccion < 1 or seleccion > 2:  # Obliga a seleccionar bien
        print('Elija un valor válido')
        seleccion = pedir_entero('Elija un apartado (1/2): ')

    if seleccion == 1:  #Añadirlo como cuidador
        print('\n--- NUEVO CUIDADOR EN EL REFUGIO ---')
        print('Puedes añadir al nuevo trabajador en los siguientes refugios:')
        refugio_seleccionado = seleccionar_refugio(mis_refugios)
        if refugio_seleccionado == None:
            return

        print('Ahora introduzca los datos del empleado:')
        nombre = input('Nombre: ')
        edad = pedir_entero('Edad: ')
        genero = input('Género(F/M): ').upper()
        dni = pedir_dni()


        Cuidador(nombre, edad, genero, dni, refugio_seleccionado)
        print('Se ha introducido correctamente al cuidador/a en la base de datos\n')

    elif seleccion == 2: #Añadirlo como limpiador
        print('--- NUEVO LIMPIADOR EN EL REFUGIO ---\n')
        print('Puedes añadir el nuevo trabajador en los siguientes refugios:')
        refugio_seleccionado = seleccionar_refugio(mis_refugios)
        if refugio_seleccionado == None:
            return

        print('Ahora introduzca los datos del empleado:')
        nombre = input('Nombre: ')
        edad = pedir_entero('Edad: ')
        genero = input('Género(F/M): ').upper()
        dni = pedir_dni()
        salario = pedir_entero('Introduzca el salario inicial acordado: ')

        Limpiador(nombre, edad, genero, dni, salario, refugio_seleccionado)
        print('Se ha introducido correctamente al limpiador/a en la base de datos\n')



def trabajadores(mis_refugios):
    seguir = True
    while seguir:
        print('Bienvenido al apartado trabajadores, estas son las opciones:')
        print('1: Añadir un nuevo Trabajador')
        print('2: Buscar trabajadores por DNI')
        print('3: Registro del trabajo de hoy')
        print('4: Acciones administrativas')
        print('5: Volver al inicio')

        seleccion = pedir_entero('Elija un apartado (1/2/3/4/5): ')
        print()

        while seleccion < 1 or seleccion > 5:  # Obliga a seleccionar bien
            print('Elija un valor válido')
            seleccion = pedir_entero('Elija un apartado (1/2/3/4/5): ')

        if seleccion == 1:  # Añadir empleado
            print('Opciones de empleo ')
            print('1: Cuidador')
            print('2: Limpiador')

            anyadir_empleado(mis_refugios)


        elif seleccion == 2:  # Ver todos los empleados
            print('¿En que refugio se encuentra el empleado que buscas?: ')
            refugio_seleccionado = seleccionar_refugio(mis_refugios)
            if refugio_seleccionado == None:
                return
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
                    nombre_final.dni = nuevo_dni


        elif seleccion == 3:  # Llamar a las funciones trabajo
            print('Momento de ver cuanti tiempo hemos trabajado hoy')
            print('De que refugio?')
            refugio_seleccionado = seleccionar_refugio(mis_refugios)
            if refugio_seleccionado == None:
                return

            if len(refugio_seleccionado.empleados) == 0:
                print('En este refugio no tiene animales por el momento\n')

            elif len(refugio_seleccionado.empleados) > 0:
                print('De que empleado vamos a pasar la inspección?')

                refugio_seleccionado.mostrar_empleados()

                elegido = False
                while not elegido:
                    seleccion_codigo = pedir_dni()
                    for empleado in refugio_seleccionado.empleados:
                        if seleccion_codigo == empleado.dni:
                            elegido = True
                            nombre_final = empleado

                    if not elegido:
                        print('El empleado seleccionado no está en el refugio elegido')

                if nombre_final.oficio == 'Cuidador':
                    animal = input('¿Con que animal ha estado trabajando? ')
                    horas = pedir_entero('¿Cuantas horas ha trabajado? ')
                    nombre_final.trabajar(animal, horas)

                elif nombre_final.oficio == 'Limpiador':
                    print('Buen trabajo hoy')
                    horas = pedir_entero('Cuantas horas has hecho hoy? ')
                    nombre_final.trabajar(horas)

        elif seleccion == 4:  # Opciones administrativas
            print('A continuación se le hará una serie de preguntas para saber cual proceso administrativo desea realizar')
            print('De que refugio forma parte?')

            refugio_seleccionado = seleccionar_refugio(mis_refugios)
            if refugio_seleccionado == None:
                return

            if len(refugio_seleccionado.empleados) == 0:
                print('En este refugio no tiene animales por el momento\n')

            elif len(refugio_seleccionado.empleados) > 0:
                print('A continuación se le pedirá el dni para llevarle al proceso administrativo que mejor se adecue a su situación')

                refugio_seleccionado.mostrar_empleados()

                elegido = False
                while not elegido:
                    seleccion_codigo = pedir_dni()
                    for empleado in refugio_seleccionado.empleados:
                        if seleccion_codigo == empleado.dni:
                            elegido = True
                            nombre_final = empleado

                    if not elegido:
                        print('El empleado seleccionado no está en el refugio elegido')

                if nombre_final.oficio == 'Cuidador':
                    print('Agradecemos mucho su trabajo voluntario')
                    print('Sin embargo no hay ningún proceso administrativo del cual puedas hacer uso')

                elif nombre_final.oficio == 'Limpiador':
                    print('Ahora es momento de solicitar su preciado aumento')
                    print('Antes de nada los recordatorios: ')
                    print('1. Puede solicitar su aumento de salario de forma indefinida, no hay penalización')
                    print('2. El mínimo de horas para solicitar el aumento son 4200h')
                    espera = input("si está usted de acuerdo con los téminos y condiciones pulse [ENTER]")
                    nombre_final.aumento()
                
        elif seleccion == 5:  #Volver para atrás
            seguir = False



def buscar_usuario(dni, lista_usuarios):
    for i in lista_usuarios:
        if i.dni == dni:
            return i
    return None



def clientes(mis_refugios, lista_usuarios):
    seguir = True
    while seguir:
        print('Bienvenido al apartado clientes, estas son las opciones:')
        print('1: Añadir un nuevo Usuario')
        print('2: Activar membresía por DNI')
        print('3: Registrarse como Voluntario')  
        print('4: Registrar trabajo voluntario')
        print('5: Ajustes de Usuario')
        print('6: Volver al inicio')

        seleccion = pedir_entero('Elija un apartado (1/2/3/4/5/6): ')
        print()

        while seleccion < 1 or seleccion > 6:  # Obliga a seleccionar bien
            print('Elija un valor válido')
            seleccion = pedir_entero('Elija un apartado (1/2/3/4/5/6): ')

        if seleccion == 1:  # Añadir Usuario
            print('\n--- NUEVO CLIENTE ---')
            nombre = input('Nombre: ')
            dni = pedir_dni()
            if buscar_usuario(dni, lista_usuarios):
                print("Error: Ya existe un usuario con ese DNI.")
            else:
                contacto = input('Número de contacto: ')
                genero = input('Género(F/M): ').upper()
                residencia = input('Dirección: ')
                nuevo_u = Usuario(nombre, dni, contacto, residencia, genero)
                lista_usuarios.append(nuevo_u)
                print(f'Usuario {nombre} registrado con éxito.\n')

        elif seleccion == 2: # Activar Socio (U_Prioritario)
            print('Para poder proceder por porfavor introduzca su DNI: ')
            dni = pedir_dni()
            cliente = buscar_usuario(dni, lista_usuarios)
            if cliente:
                print('Para convertirte en Usuario Prioritario, primero deberás pagar 20€')
                cuota = pedir_entero("Ingrese cuota mensual: ")
                
                # Convertimos o creamos el socio
                nuevo_socio = Socio(cliente.nombre, cliente.dni, cliente.contacto, cliente.residencia, cliente.genero, cuota)
                print(nuevo_socio.comprobar_socio())
                # Reemplazamos en la lista
                if nuevo_socio:
                    lista_usuarios.remove(cliente)
                    lista_usuarios.append(nuevo_socio)
                else:
                    print('Pruebe con otra cantidad')
            else:
                print("Primero registre al usuario como base (Opción 1).")

        elif seleccion == 3: # Registrar como Voluntario
            print('Para poder proceder por porfavor introduzca su DNI: ')
            dni = pedir_dni()
            cliente = buscar_usuario(dni, lista_usuarios)
            if cliente:
                edad = pedir_entero("Edad: ")
                refugio_asig = seleccionar_refugio(mis_refugios)
                if refugio_asig == None:
                    return
                nuevo_vol = Voluntario(cliente.nombre, edad, cliente.genero, cliente.dni, cliente.contacto, cliente.residencia, refugio_asig)
                lista_usuarios.remove(cliente)
                lista_usuarios.append(nuevo_vol)
                refugio_asig.anyadir_empleado(nuevo_vol)
                print(f"{cliente.nombre} ahora es voluntario en {refugio_asig.nombre}")
            else:
                print("Primero registre al usuario como base (Opción 1).")

        elif seleccion == 4: # Registrar trabajo voluntario
            dni = pedir_dni()
            cliente = buscar_usuario(dni, lista_usuarios)
            if isinstance(cliente, Voluntario):
                horas = pedir_entero("¿Cuántas horas ha trabajado hoy? ")
                tarea = input("Tarea realizada: ")
                cliente.trabajar(horas, tarea)
            else:
                print("Este usuario no está registrado como Voluntario.")

        elif seleccion == 5: # Ajustes
            dni = pedir_dni()
            cliente = buscar_usuario(dni, lista_usuarios)
            if cliente:
                nuevo_c = input("Nuevo contacto: ")
                print(cliente.actualizar_contacto(nuevo_c))
            else:
                print("Primero registre al usuario como base (Opción 1).")

        elif seleccion == 6:
            seguir = False
    
    return lista_usuarios



def guardar_datos(mis_refugios, lista_usuarios):
    carpeta_base_datos = 'BaseDatos'

    if not os.path.exists(carpeta_base_datos):
        os.makedirs(carpeta_base_datos)

    ruta_pkl = os.path.join(carpeta_base_datos, 'datos_sistema.pkl')
    try:
        with open(ruta_pkl, 'wb') as fichero:
            pickle.dump((mis_refugios, lista_usuarios), fichero)
        print('\nSe ha guardado todo de manera correcta')

    except Exception as e:
        print(f'Error al guardar los datos: {e}')



def cargar_datos():
    ruta_pkl = os.path.join('BaseDatos', 'datos_sistema.pkl')

    if os.path.exists(ruta_pkl):
        try:
            with open(ruta_pkl, 'rb') as fichero:
                mis_refugios, lista_usuarios = pickle.load(fichero)
            return mis_refugios, lista_usuarios
        except Exception as e:
            print(f"Error al leer el archivo: {e}. Iniciando sistema nuevo.\n")
            return [], []

    else:
        print('No se han encontrado datos previos. Iniciando sistema nuevo.\n')
        return [], []



if __name__ == '__main__':
    print('--- INICIANDO SISTEMA DEL REFUGIO ---')

    mis_refugios, lista_usuarios = cargar_datos()

    if len(mis_refugios) == 0:
        mis_refugios = []
        lista_usuarios = []
        print('Bienvenido al sistema, primero introduzca los datos necesaríos')
        nombre = input('Nombre del refugio: ').lower()
        tamanyo = pedir_entero('Espacio máximo del refugio: ')
        print()

        mi_refugio = Refugio(nombre, tamanyo)
        mis_refugios.append(mi_refugio)


    ejecutando = True
    while ejecutando:

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
            animales(mis_refugios, lista_usuarios)

        elif seleccion == 2: #Apartado Trabajadores
            trabajadores(mis_refugios)

        elif seleccion == 3: #Apartado Clientes
            lista_usuarios = clientes(mis_refugios, lista_usuarios)

        elif seleccion == 4: #Apartado Refugios
            mis_refugios = refugios(mis_refugios)

        elif seleccion == 5: #Salir del programa
            guardar_datos(mis_refugios, lista_usuarios)
            ejecutando = False

        else:
            print('Opción no valida')
            print()