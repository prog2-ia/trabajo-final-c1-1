class Empleado:
    def __init__(self, nombre, edad, genero, dni, animal, tiempo):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.dni = dni
        self.animal = animal #animal del cual se encarga en este momento
        self.tiempo = tiempo #timepo dedicado al animal con el que está ahora
    def HorasTrabajadas (self, horas):
        self.tiempo += horas