from ClaseAnimales import Animales

class Perro(Animales):
    def __init__(self, nombre, edad, tiempo, codigo, raza, refugio = None): #Añadir que dependiendo de la raza tenga unas condiciones especificas u otras

        super().__init__(nombre, edad, 'perro', tiempo, codigo, refugio)
        self.raza = raza

    def caracteristicas(self, caract):
        print(f'Este perro de la raza {self.raza} tiene estas características: {caract}')

    def inspeccion(self):
        estado_dentadura = input('¿La dentadura del animal tiene algun problema? (s/n) ')
        if estado_dentadura == 's':
            estado_dentadura = input('¿Que enfermedad tiene en la dentadura? ')
            self.enfermedad.append(estado_dentadura)

            tratamiento = input('¿Que tratamiento necesita para curarlo? ')
            self.necesidades.append(tratamiento)

        comida = input('¿Que comida requiere este animal? ')
        self.comida = comida

        chequeo = input('¿El perro tiene alguna otra patologia? (s/n) ')
        if chequeo == 's':
            num = int(input('¿Cuantas patologias tiene? '))

            for i in range(num):
                enfermedad = input('¿Que enfermedad padece? ')
                self.enfermedad.append(enfermedad)

                cura = input('¿Tiene algún tratamiento? (s/n) ')
                if cura == 's':
                    tratamiento = input('¿Cual es el tratamiento a llevar a cabo? ')
                    self.necesidades.append(tratamiento)