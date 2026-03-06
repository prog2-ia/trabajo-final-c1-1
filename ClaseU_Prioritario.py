from ClaseUsuario import Usuario
class Socio(Usuario):
    def __init__(self, nombre, dni, contacto, residencia, genero, cuota, prioridad):
        super().__init__(nombre, dni, contacto, residencia, genero)

        self.cuota_mensual = cuota
        self.prioridad = prioridad
        self.historial_adopciones = []
        self.membresia_activa = False

    def comprobar_socio(self):
        if self.cuota_mensual < 20:
            if self.genero == 'F':
                print(f"Doña {self.nombre}, su importe ha resultado insuficiente para mantener su membresía")
            else:
                print(f"Don {self.nombre}, su importe ha resultado insuficiente para mantener su membresía")
        else:
            self.membresia_activa = True
            print(f"Membresía activada con éxito para {self.nombre}.")
    def generar_certificado_donacion(self):
        if self.membresia_activa:
            print(f"Certificado emitido para {self.nombre} por su cuota de {self.cuota_mensual}€.")
        else:
            print(f"Error: {self.nombre} no tiene una membresía activa para generar certificados.")

    def calcular_descuento_veterinaria(self, precio_veterinario):
        if self.membresia_activa:
            return precio_veterinario * 0.8
        return precio_veterinario