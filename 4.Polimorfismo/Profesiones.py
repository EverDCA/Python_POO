class Medico:
    def __init__(self, especialidad, experiencia):
        self.especialidad = especialidad
        self.experiencia = experiencia
    
    def trabajar(self):
        print("\nInformacion Del/la Medico:")
        print(f"El médico especializado en {self.especialidad} con {self.experiencia} años de experiencia trata a sus pacientes con cuidado!.")

class Ingeniero:
    def __init__(self, ingenieria, experiencia):
        self.ingenieria =ingenieria
        self.experiencia = experiencia
    
    def trabajar(self):
        print("\nInformacion del/la Ingeniero/a:")
        print(f"El ingeniero de la rama {self.ingenieria} con {self.experiencia} años de experiencia es muy apto!.")

class Docente:
    def __init__(self, materia, experiencia):
        self.materia = materia
        self.experiencia = experiencia
    
    def trabajar(self):
        print("\nInformacion del/la Docente:")
        print(f"El docente de {self.materia} con {self.experiencia} años de experiencia enseña muy bien a sus aprendices.\n")

def trabajar_profesional(profesional):
    profesional.trabajar()


medico1 = Medico("Cardiologo", 10)
ingeniero1 = Ingeniero("Informatico", 5)
docente1 = Docente("Matemáticas", 8)

trabajar_profesional(medico1)
trabajar_profesional(ingeniero1)
trabajar_profesional(docente1)
