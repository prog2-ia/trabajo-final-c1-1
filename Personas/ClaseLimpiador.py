from Personas.ClaseEmpleado import Empleado
from ClaseRefugio import Refugio

class Limpiador(Empleado):
    def __init__(self, nombre: str, edad: int, genero: str, dni: str, salario: int, refugio: Refugio=None):
        super().__init__(nombre, edad, genero, dni, 'Limpiador', refugio)
        self.salario = salario
        self.tiempo: int = 0

    def trabajar(self, horas: int):
        self.tiempo += horas

    def aumento(self):
        if self.tiempo // 4200 > 0:
            self.tiempo -= 4200
            self.salario *= 1.10
            return f"¡Aumento de sueldo para {self.nombre}! Nuevo salario: {self.salario}"
        else:
            return f"Desgraciadamente no cumpre los requisitos para el aumento"