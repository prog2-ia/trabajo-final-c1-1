from Animales.ClaseAnimales import Animales

class Gato(Animales):
    def __init__(self, nombre, edad, codigo, raza, refugio = None):

        super().__init__(nombre, edad, 'Gato', codigo, refugio)
        self.raza = raza

    def inspeccion(self, comida, nueva_necesidad = None, estado_garras = None):
        self.comida = comida
        informe = f'===== INFORME VETERINARIO ====='
        informe += f'Paciente: {self.nombre} | Código: {self.codigo}\n'
        informe += f'Raza del gato: {self.raza}\n '
        informe += f'Edad: {self.edad} | Tiempo en el refugio: {self.tiempo}\n'
        informe += f'------------------------------'
        informe += f'RESULTADOS DE LA REVISIÓN'
        informe += f'Dieta asignada: {self.comida}'

        if estado_garras:
            informe += f'Estado Garras: {estado_garras}'
        else:
            informe += f'Estado Garras: Sin revisar'


        if nueva_necesidad:
            self += nueva_necesidad  # Guardamos la necesidad en el historial
            informe += f'Se ha diagnosticado con {nueva_necesidad.problema}\n'
            informe += f'Tratamiento a seguir: {nueva_necesidad.solucion}\n'

        informe += f'------------------------------'