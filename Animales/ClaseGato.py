from Animales.ClaseAnimales import Animales

class Gato(Animales):
    def __init__(self, nombre, edad, raza, refugio = None):

        super().__init__(nombre, edad, 'Gato', refugio)
        self.raza = raza
        self.patologia = []

    def inspeccion(self, comida, estado_garras = None, enfermedad = None, cura = None):
        self.comida = comida

        if estado_garras:
            self.estado_garras = estado_garras

        if enfermedad and cura:
            dic_pat = {'enfermedad': enfermedad, 'cura': cura}
            self.patologia.append(dic_pat)

        informe = f'===== INFORME VETERINARIO ====='
        informe += f'Paciente: {self.nombre} | Código: {self.codigo}\n'
        informe += f'Raza del gato: {self.raza}\n '
        informe += f'Edad: {self.edad} | Tiempo en el refugio: {self.tiempo}\n'
        informe += f'------------------------------\n'
        informe += f'RESULTADOS DE LA REVISIÓN\n'
        informe += f'Dieta asignada: {self.comida}\n'

        if estado_garras:
            informe += f'Estado Garras: {self.estado_garras}\n'
        else:
            informe += f'Estado Garras: Sin revisar\n'

        informe += f'------------------------------\n'
        informe += f'PATOLOGIAS:\n'

        if len(self.patologia) == 0:
            informe += f'El animal no está enfermo\n'

        else:
            for pat in self.patologia:
                informe += f'El animal tiene {pat['enfermedad']} y se cura con {pat['cura']}'

        return informe