from abc import ABC, abstractmethod

class Animales(ABC):
    total_animales = 0 #Lista para saber la cantidad de animales que llevamos creados

    def __init__(self, nombre: str, edad: int, especie: str, refugio = None):
        Animales.total_animales += 1

        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.necesidades = [] #Para cuando pase la inspección del veterinario
        self.comida = None
        self.tiempo = 0
        self.informe = 'No hay informe generado hasta que se realice la inspección'

        if especie == 'gato':
            letra = 'G'
        elif especie == 'perro':
            letra = 'P'
        elif especie == 'caballo':
            letra = 'C'
        else:
            letra = '?'

        self.codigo = f'{letra}{Animales.total_animales}'

        if refugio:
            refugio.anyadir_animal(self)

    def __str__(self): #En caso de que alguien haga print(Nombre_Perro)
        return f'Código: {self.codigo}. Nombre: {self.nombre}. Especie: {self.especie}'

    def __iadd__(self, nueva_necesidad: str): #Permite hacer: animal += necesidad
        self.necesidades.append(nueva_necesidad)
        return self

    @classmethod
    def mostrar_censo(cls):
        return f'Total histórico de animales registrados: {cls.total_animales}'

    def anyadir_tiempo(self, tiempo: int):
        self.tiempo += tiempo

    @abstractmethod
    def inspeccion(self, comida: str):
        pass