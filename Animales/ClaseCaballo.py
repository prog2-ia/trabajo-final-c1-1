from Animales.ClaseAnimales import Animales
from ClaseRefugio import Refugio

class Caballo(Animales):
    def __init__(self, nombre: str, edad: int, raza: str, refugio: Refugio = None):

        super().__init__(nombre, edad, 'caballo', refugio)
        self.raza = raza
        self.patologia: list = []

    def inspeccion(self, comida: str, estado_pezunyas: str = None, enfermedad: str = None, cura: str = None):
        self.comida = comida

        if estado_pezunyas:
            self.estado_pezunyas = estado_pezunyas

        if enfermedad and cura:
            dic_pat = {'enfermedad': enfermedad, 'cura': cura}
            self.patologia.append(dic_pat)

        informe = f'===== INFORME VETERINARIO =====\n'
        informe += f'Paciente: {self.nombre} | Código: {self.codigo}\n'
        informe += f'Raza del caballo: {self.raza}\n '
        informe += f'Edad: {self.edad} | Tiempo en el refugio: {self.tiempo}\n'
        informe += f'------------------------------\n'
        informe += f'RESULTADOS DE LA REVISIÓN\n'
        informe += f'Dieta asignada: {self.comida}\n'

        if estado_pezunyas:
            informe += f'Estado Pezuñas: {self.estado_pezunyas}\n'
        else:
            informe += f'Estado Pezuñas: Sin revisar\n'

        informe += f'------------------------------\n'
        informe += f'PATOLOGIAS:\n'

        if len(self.patologia) == 0:
            informe += f'El animal no está enfermo\n'

        else:
            for pat in self.patologia:
                informe += f'El animal tiene {pat['enfermedad']} y se cura con {pat['cura']}\n'

        self.informe = informe

        return self.informe