from abc import ABC, abstractmethod
from xmlrpc.client import escape


class Empleado:
    def __init__(self, nombre, edad, genero, dni, ofcicio, refugio = None):
        self.oficio = ofcicio
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.__dni = dni
        self.tiempo = 0
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
            return f"Error: El DNI debe tener 9 caracteres."

    @abstractmethod
    def trabajar(self):
        pass

    def HorasTrabajadas(self, horas):
        self.tiempo += horas
        return f"{self.nombre} ha registrado {horas} horas nuevas. Total: {self.tiempo}"

    def __str__(self): #definimos el str, para que muestre el nombre y el DNI del epmleado
        return f"Empleado: {self.nombre} | DNI: {self.dni}"

    def __len__(self): #implementacioçon del método len
        return self.tiempo

    def __eq__(self, otro):
        # Primero comprobamos si el 'otro' objeto es de la misma clase
        if not isinstance(otro, Empleado):
            return False

        return self.__dni == otro.__dni

    def __repr__(self): #Implementación del método repr
        return f"Empleado(nombre='{self.nombre}', dni='{self.dni}')"