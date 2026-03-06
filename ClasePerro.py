from ClaseAnimales import Animales

class Perro(Animales):
    def __init__(self, nombre, edad, necesidades, tiempo, comida, enfermedad, codigo, raza, refugio = None): #Añadir que dependiendo de la raza tenga unas condiciones especificas u otras

        super().__init__(nombre, edad, 'perro', necesidades, tiempo, comida, enfermedad, codigo, refugio)
        self.raza = raza

    def caracteristicas(self, caract):
        print(f'Este perro de la raza {self.raza} tiene estas características: {caract}')
