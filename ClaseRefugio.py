class Refugio:
    def __init__(self, nombre: str, tamanyo: int):
        self.nombre = nombre
        self.tamanyo = tamanyo #Capacidad del refugio
        self.animales: list = []
        self.empleados: list = []

    def __str__(self):
        return f'Refugio "{self.nombre}" (Animales: {len(self.animales)}/{self.tamanyo})'

    def anyadir_animal(self, animal: object):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)

    def anyadir_empleado(self, empleado: object):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado)

    def adoptar(self, codigo: str):
        for animal in self.animales:
            if animal.codigo == codigo:
                self.animales.remove(animal)
                return animal

        return None