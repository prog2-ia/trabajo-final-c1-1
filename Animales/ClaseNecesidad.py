class Necesidad:
    def __init__(self, problema, solucion):
        self.problema = problema
        self.solucion = solucion


    def __str__(self):
        return f"{self.problema} (Tratamiento: {self.solucion})"

    def __repr__(self):
        return self.__str__()