from ClaseEmpleado import Empleado
class Limpiador(Empleado):
    def __init__(self, nombre, edad, genero, dni, tiempo, salario, refugio=None):
        super().__init__(nombre, edad, genero, dni, tiempo, refugio)
        self.salario = salario

    def trabajar(self, horas):
        self.HorasTrabajadas(horas)
        if self.tiempo // 4200 > (self.tiempo - horas) // 4200:
            self.salario *= 1.10
            print(f"¡Aumento de sueldo para {self.nombre}! Nuevo salario: {self.salario}")