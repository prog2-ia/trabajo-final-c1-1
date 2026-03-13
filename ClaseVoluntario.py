from ClaseUsuario import Usuario
from ClaseEmpleado import Empleado


class Voluntario(Usuario, Empleado):
    #el tiempo se queda por defecto en 0, si el usuario quiere especificar el tiempo, basta con que lo especifíque
    def __init__(self, nombre, edad, genero, dni, contacto, residencia, tiempo=0, refugio=None):
        Usuario.__init__(self, nombre, dni, contacto, residencia, genero)
        Empleado.__init__(self, nombre, edad, genero, dni, tiempo, refugio)

        # Atributo específico de voluntario
        self.misiones_completadas = 0

    #lo mismo que con el tiempo, pero con ayuda
    def trabajar(self, horas, tarea="ayuda general"):
        self.HorasTrabajadas(horas)
        puntos_ganados = horas // 10
        self.SumarPuntos(puntos_ganados)
        print(f"Voluntario {self.nombre} realizó: {tarea}. Ganó {puntos_ganados} puntos de lealtad.")

    def realizar_mision(self):
        self.misiones_completadas += 1
        print(f"Misión finalizada. Total: {self.misiones_completadas}")