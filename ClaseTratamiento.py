class Tratamiento:
    def __init__(self, tipo, utilidad):
        self.tipo = tipo #El tipo de tratamiento que es
        self.tipo.append(tipo)
        self.utilidad = utilidad #Para que sirve ese tratamiento

    def descripcion(self):
        print(f'El tratamiento es del tipo {self.tipo} y su utilidad es {self.utilidad}')