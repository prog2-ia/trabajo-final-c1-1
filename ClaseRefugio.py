class Refugio:
    def __init__(self, direccion, tamaño, animal, empleados):
        self.direccion = direccion
        self.tamaño = tamaño
        self.animales = []
        self.empleados = []
    def añadir_animal(self, animal):
        self.animales.append(animal)
    def mostrar_animales(self):
        for animal in self.animales:
            print(f"{animal.nombre} ({animal.especie})")
    def añadir_empleado(self, empleado):
        self.empleados.append(empleado)
    def mostrar_empleados(self):
        for empleado in self.animales:
            print(f"{empleado.nombre} ({empleado.rol})")