from ClaseEmpleado import Empleado
class Cuidador(Empleado):
    def __init__(self, nombre, edad, genero, dni, tiempo, refugio=None):
        super().__init__(nombre, edad, genero, dni, tiempo, refugio)
        self.seguimiento_animales = {}  # Diccionario: {animal: horas}
        self.lista_experto = []

    def trabajar(self, animal, horas):
        self.HorasTrabajadas(horas)

        if animal not in self.seguimiento_animales:
            self.seguimiento_animales[animal] = 0

        self.seguimiento_animales[animal] += horas
        print(f"Horas acumuladas con {animal.nombre}: {self.seguimiento_animales[animal]}")

        if self.seguimiento_animales[animal] >= 150:
            if animal.especie not in self.lista_experto:
                self.lista_experto.append(animal.especie)
                print(f"Enhorabuena {self.nombre}, ahora eres experto en la raza: {animal.especie}")
