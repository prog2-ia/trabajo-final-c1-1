from Personas.ClaseUsuario import Usuario
from Personas.ClaseEmpleado import Empleado
from Refugio.ClaseRefugio import Refugio


class Voluntario(Usuario, Empleado):
    #el tiempo se queda por defecto en 0, si el usuario quiere especificar el tiempo, basta con que lo especifíque
    def __init__(self, nombre: str, edad: int, genero: str, dni: str, contacto: int, residencia: str, tiempo: int = 0, refugio: Refugio=None):
        Usuario.__init__(self, nombre, dni, contacto, residencia, genero)
        Empleado.__init__(self, nombre, edad, genero, dni, tiempo, refugio)

        # Atributo específico de voluntario
        self.misiones_completadas = 0

    #lo mismo que con el tiempo, pero con ayuda
    def trabajar(self, horas: int, tarea="ayuda general"):
        self.HorasTrabajadas(horas)
        puntos_ganados = horas // 10
        #usamos la sobrecarga del operador +=
        self += puntos_ganados
        print (f"Voluntario {self.nombre} realizó: {tarea}. Ganó {puntos_ganados} puntos de lealtad.")
        return puntos_ganados

    def realizar_mision(self):
        self.misiones_completadas += 1
        return f"Misión finalizada. Total: {self.misiones_completadas}"