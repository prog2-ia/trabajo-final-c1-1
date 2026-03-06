class Empleado:
    def __init__(self, nombre, edad, genero, dni, refugio = None):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.dni = dni
    def HorasTrabajadas (self, horas):
        self.tiempo += horas

    if refugio:
        refugio.añadir_empleado(self)