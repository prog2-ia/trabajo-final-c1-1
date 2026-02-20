class Cuidador:
    def __init__(self, nombre, edad, especialidad, genero, dni, animal, tiempo):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad #lista de razas con las que ha pasado más de 150h
        self.genero = genero
        self.dni = dni
        self.animal = animal #animal del cual se encarga en este momento
        self.tiempo = tiempo #timepo dedicado al animal con el que está ahora
    def Especializacion (self):
        if self.tiempo >= 150:
            if """razaAnimal""" not in self.especialidad:
                self.especialidad.append(#razaAnimal)
            else:
                print(f"{self.nombre} ya estaba especializado en la raza: {"""razaAnimal"""}")
    def HorasTrabajadas (self, horas):
        self.tiempo += horas
    def CambiarAnimal(self, animal):
        self.animal = animal
        self.tiempo = 0