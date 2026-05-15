class Refugio:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño #Capacidad del refugio
        self.animales = []
        self.empleados = []

    def __str__(self):
        return f'Refugio "{self.nombre}" (Animales: {len(self.animales)}/{self.tamaño})'

    def añadir_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)

    def añadir_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado)

    def adoptar(self, codigo):
        for animal in self.animales:
            if animal.codigo == codigo:
                self.animales.remove(animal)
                return True

        return False