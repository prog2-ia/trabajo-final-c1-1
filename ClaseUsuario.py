class Usuario:
    def __init__(self, nombre, dni, contacto, residencia, genero):
        self.nombre = nombre
        self.dni = dni
        self.contacto = contacto
        self.residencia = residencia
        self.animales_adoptados = []
        self.genero = genero
        self.puntos_lealtad = 0 #son puntos que se acumulan para un sistema de beneficios y de la posibilidad de adopción
    def RegistrarAdopcion(self, animal):
        if animal not in self.animales_adoptados:
            self.animales_adoptados.append(animal)
            print(f"Registro exitoso: {self.nombre} ha adoptado a {animal}.")
        else:
            print(f"{self.nombre} ya tiene a ese animal adoptado")
    def ActualizarContacto(self, nuevo_contacto):
        if nuevo_contacto != self.contacto:
            self.contacto = nuevo_contacto
            print("Se ha actualizado con éxito el contácto")
        else:
            print(f"{nuevo_contacto} es el contacto que tiene actualmente señor/a {self.nombre}")
    def SumarPuntos(self, cantidad):
        self.puntos_lealtad += cantidad