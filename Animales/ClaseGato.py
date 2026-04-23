from Animales.ClaseAnimales import Animales

class Gato(Animales):
    def __init__(self, nombre, edad, codigo, raza, refugio = None):

        super().__init__(nombre, edad, 'gato', codigo, refugio)
        self.raza = raza

    def caracteristicas(self, caract):
        print(f'La raza de este gato es: {self.raza}, y tiene estas características: {caract}')

    def inspeccion(self):
        pass