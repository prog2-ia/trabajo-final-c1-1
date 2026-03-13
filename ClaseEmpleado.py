from abc import ABC, abstractmethod

class Empleado:
    def __init__(self, nombre, edad, genero, dni, tiempo, refugio = None):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.__dni = dni
        self.tiempo = tiempo
        if refugio:
            refugio.añadir_empleado(self)


    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevo_dni):
        if len(str(nuevo_dni)) == 9:
            self.__dni = nuevo_dni
        else:
            print("Error: El DNI debe tener 9 caracteres.")

    @abstractmethod
    def trabajar(self):
        pass

    def HorasTrabajadas(self, horas):
        self.tiempo += horas
        print(f"{self.nombre} ha registrado {horas} horas nuevas. Total: {self.tiempo}")