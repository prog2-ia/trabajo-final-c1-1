from Animales.ClaseAnimales import Animales

class Perro(Animales):
    def __init__(self, nombre, edad, raza, refugio = None):

        super().__init__(nombre, edad, 'perro', refugio)
        self.raza = raza
        self.patologia = []

    def caracteristicas(self, caract):
        print(f'Este perro de la raza {self.raza} tiene estas características: {caract}')

    def inspeccion(self, comida, estado_dientes=None, enfermedad=None, cura=None):
        self.comida = comida

        if estado_dientes:
            self.estado_dientes = estado_dientes

        if enfermedad and cura:
            dic_pat = {'enfermedad': enfermedad, 'cura': cura}
            self.patologia.append(dic_pat)

        informe = f'===== INFORME VETERINARIO =====\n'
        informe += f'Paciente: {self.nombre} | Código: {self.codigo}\n'
        informe += f'Raza del perro: {self.raza}\n '
        informe += f'Edad: {self.edad} | Tiempo en el refugio: {self.tiempo}\n'
        informe += f'------------------------------\n'
        informe += f'RESULTADOS DE LA REVISIÓN\n'
        informe += f'Dieta asignada: {self.comida}\n'

        if estado_dientes:
            informe += f'Estado Dientes: {self.estado_dientes}\n'
        else:
            informe += f'Estado Dientes: Sin revisar\n'

        informe += f'------------------------------\n'
        informe += f'PATOLOGIAS:\n'

        if len(self.patologia) == 0:
            informe += f'El animal no está enfermo\n'

        else:
            for pat in self.patologia:
                informe += f'El animal tiene {pat['enfermedad']} y se cura con {pat['cura']}\n'

        self.informe = informe

        return self.informe