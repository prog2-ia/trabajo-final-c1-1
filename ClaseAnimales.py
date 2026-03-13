from abc import ABC, abstractmethod

class Animales(ABC):
    def __init__(self, nombre, edad, especie, tiempo, codigo, refugio = None):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.comida = ''
        self.necesidades = [] #Lista de necesidades (tratamientos y demás) que necesita el animal, se rellena al hacer la inspeción del animal
        self.tiempo = tiempo #Tiempo que lleva en el refugio
        self.enfermedad = [] #En caso de tener alguna, cuales son las enfermedades del animal (Lista), se rellena al hacer la inspeción del animal
        self.codigo = codigo #Para ser capaces de diferenciar a los animales por si dos tienen el mismo nombre

        #En caso de que hayamos añadido al refugio al que pertenece el animal lo añade directamente a ese refugio

        if refugio:
            refugio.añadir_animal(self)

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


    def adoptados(self):
        #Tenemos que hacer que se eliminen los animales del refugio cuando se adopten


    @abstractmethod
    def inspeccion(self):
        pass


