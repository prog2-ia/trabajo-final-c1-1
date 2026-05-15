from Personas.ClaseEmpleado import Empleado

class Cuidador(Empleado):
    def __init__(self, nombre, edad, genero, dni, refugio=None):
        super().__init__(nombre, edad, genero, dni, 'Cuidador', refugio)
        self.seguimiento_animales = {}  # Diccionario: {animal: horas}
        self.lista_experto = []

    def trabajar(self, animal, horas):
        self.HorasTrabajadas(horas)

        if animal not in self.seguimiento_animales:
            self.seguimiento_animales[animal] = 0

        self.seguimiento_animales[animal] += horas

        if self.seguimiento_animales[animal] >= 150:
            if animal.especie not in self.lista_experto:
                self.lista_experto.append(animal.especie)
                return f"Enhorabuena {self.nombre}, ahora eres experto en la especie: {animal.especie}"

        return f"Horas acumuládas con {animal.nombre}: {self.seguimiento_animales[animal]}"

    def __getitem__(self, indice):
        # Permite acceder a la lista de especies expertas usando corchetes.
        return self.lista_experto[indice]