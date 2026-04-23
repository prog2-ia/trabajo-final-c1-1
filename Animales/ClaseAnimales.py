from abc import ABC, abstractmethod

class Animales(ABC):
    total_animales = 0 #Lista para saber la cantidad de animales que llevamos creados

    def __init__(self, nombre, edad, especie, codigo, refugio = None):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.comida = None
        self.tiempo = 0
        self.__codigo = codigo #Codigo privado

        Animales.total_animales += 1

        if refugio:
            refugio.añadir_animal(self)

    @property
    def codigo(self):
        return self.__codigo

    @classmethod
    def mostrar_censo(cls):
        return f"Total histórico de animales registrados: {cls.total_animales}"

    def añadir_tiempo(self, tiempo):
        self.tiempo += tiempo

    def curar(self, enfermedad):
    # Para comprobar si la enfermedad de la que se ha curado el animal la sufria
        sufre = False
        for enf in self.enfermedad:
            if enf == enfermedad:
                self.enfermedad.remove(enfermedad)
                sufre = True


        if sufre == True:
            print(f'{self.nombre} se ha curado de {enfermedad}')

        else:
            print(f'{self.nombre} no sufre de {enfermedad}')


    def enfermar(self, enfermedad):
    #Para comprobar que no se introduzca dos veces la misma enfermedad
        sufre = False
        for enf in self.enfermedad:
            if enf == enfermedad:
                sufre = True

        if sufre == False:
            self.enfermedad.append(enfermedad)
            print(f'{self.nombre} ahora sufre de {enfermedad}')

        else:
            print(f'{self.nombre} ya tiene {enfermedad}')


    @abstractmethod
    def inspeccion(self):
        pass


