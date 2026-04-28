from Animales.ClaseAnimales import Animales
from Animales.ClaseNecesidad import Necesidad

class Gato(Animales):
    def __init__(self, nombre, edad, raza, refugio = None):

        super().__init__(nombre, edad, 'Gato', refugio)
        self.raza = raza

    def inspeccion(self, comida, estado_garras = None):
        self.comida = comida
        informe = f'===== INFORME VETERINARIO ====='
        informe += f'Paciente: {self.nombre} | Código: {self.codigo}\n'
        informe += f'Raza del gato: {self.raza}\n '
        informe += f'Edad: {self.edad} | Tiempo en el refugio: {self.tiempo}\n'
        informe += f'------------------------------\n'
        informe += f'RESULTADOS DE LA REVISIÓN\n'
        informe += f'Dieta asignada: {self.comida}\n'

        if estado_garras:
            informe += f'Estado Garras: {estado_garras}\n'
        else:
            informe += f'Estado Garras: Sin revisar\n'

        informe += f'------------------------------\n'
        informe += f'PATOLOGIAS:\n'

        if len(self.necesidades) > 0:
            for patologia in self.necesidades:
                informe += f'Patología: {patologia.problema}\n'
                informe += f'Necesita: {patologia.solucion}\n'

        else:
            informe += f'El gato no tiene ninguna patología\n'