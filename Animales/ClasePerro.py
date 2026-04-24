from Animales.ClaseAnimales import Animales

class Perro(Animales):
    def __init__(self, nombre, edad, raza, refugio = None):

        super().__init__(nombre, edad, 'perro', refugio)
        self.raza = raza

    def caracteristicas(self, caract):
        print(f'Este perro de la raza {self.raza} tiene estas características: {caract}')

    def inspeccion(self):
        pass