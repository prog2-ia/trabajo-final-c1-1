from ClaseAnimales import Animales

class Gato(Animales):
    def __init__(self, nombre, edad, tiempo, codigo, raza, refugio = None):

        super().__init__(nombre, edad, 'gato', tiempo, codigo, refugio)
        self.raza = raza

    def caracteristicas(self, caract):
        print(f'Este perro de la raza {self.raza} tiene estas características: {caract}')

    def inspeccion(self):
        comida = input('¿Que comida requiere este gato? ')
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


        estado_garras = input('¿Sufre algún problema en las garras? (s/n) ')
        if estado_garras == 's':
            estado_garras = input('¿Que problema tiene en las garras? ')
            self.enfermedad.append(estado_garras)

            tratamiento = input('¿Existe algún tratamiento para esto? ')
            self.necesidades.append(tratamiento)
