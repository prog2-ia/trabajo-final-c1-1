class Usuario:
    def __init__(self, nombre: str, dni: str, contacto: int, residencia: str, genero: str):
        self.nombre = nombre
        self.dni = dni
        self.contacto = contacto
        self.residencia = residencia
        self.animales_adoptados = []
        self.genero = genero
        self.puntos_lealtad = 0 #son puntos que se acumulan para un sistema de beneficios y de la posibilidad de adopción
    def registrar_adopcion(self, animal: str):
        if animal not in self.animales_adoptados:
            self.animales_adoptados.append(animal)
            return f"Registro exitoso: {self.nombre} ha adoptado a {animal}."
        else:
            return f"{self.nombre} ya tiene a ese animal adoptado"
    def actualizar_contacto(self, nuevo_contacto: int):
        if nuevo_contacto != self.contacto:
            self.contacto = nuevo_contacto
            return "Se ha actualizado con éxito el contácto"
        else:
            if self.genero == 'F':
                return f"{nuevo_contacto} es el contacto que tiene actualmente doña {self.nombre}"
            else:
                return f"{nuevo_contacto} es el contacto que tiene actualmente don {self.nombre}"

    def __iadd__(self, cantidad: int):
        self.puntos_lealtad += cantidad
        return self

    def __str__(self):
        return f"Usuario: {self.nombre}"

    def __eq__(self, otro):
        if not isinstance(otro, Usuario):
            return False

        return self.dni == otro.dni

    def __bool__(self):
        # Un usuario normal siempre se considera "activo" o válido
        return True

    def __getitem__(self, indice: int):
        # Permite acceder a los animales adoptados usando corchetes: usuario[0]
        return self.animales_adoptados[indice]