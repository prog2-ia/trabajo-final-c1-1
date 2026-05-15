from Personas.ClaseEmpleado import Empleado

class Limpiador(Empleado):
    def __init__(self, nombre, edad, genero, dni, salario, refugio=None):
        super().__init__(nombre, edad, genero, dni, 'Limpiador', refugio)
        self.salario = salario
        self.tiempo = 0

    def trabajar(self, horas):
        self.tiempo += horas

    def aumento(self, horas):
        if self.tiempo // 4200 > 0:
            self.tiempo = 0
            self.salario *= 1.10
            return f"¡Aumento de sueldo para {self.nombre}! Nuevo salario: {self.salario}"