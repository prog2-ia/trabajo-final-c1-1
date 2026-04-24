from abc import ABC, abstractmethod

class Animales(ABC):
    total_animales = 0 #Lista para saber la cantidad de animales que llevamos creados

    def __init__(self, nombre, edad, especie, codigo, refugio = None):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.necesidades = [] #Para cuando pase la inspección del veterinario
        self.comida = None
        self.tiempo = 0
        self.__codigo = codigo #Código privado

        Animales.total_animales += 1

        if refugio:
            refugio.añadir_animal(self)

    def __str__(self): #En caso de que alguien haga print(Nombre_Perro)
        return f'Código: {self.codigo}. Nombre: {self.nombre}. Especie: {self.especie}'

    def __iadd__(self, nueva_necesidad): #Permite hacer: animal += necesidad
        self.necesidades.append(nueva_necesidad)
        return self

    @property
    def codigo(self):
        return self.__codigo

    @classmethod
    def mostrar_censo(cls):
        return f'Total histórico de animales registrados: {cls.total_animales}'

    def añadir_tiempo(self, tiempo):
        self.tiempo += tiempo

    @abstractmethod
    def inspeccion(self, comida, nueva_necesidad = None):
        pass