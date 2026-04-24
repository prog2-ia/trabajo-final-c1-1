class Necesidad:
    def __init__(self, problema, solucion):
        self.problema = problema
        self.solucion = solucion


    def __str__(self): #En caso de que alguien quiera hacer print(necesidad)
        return f'Problema: {self.problema}. Tratamiento: {self.solucion}'

    def __repr__(self):
        return self.__str__()