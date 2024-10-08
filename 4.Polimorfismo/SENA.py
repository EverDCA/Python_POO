class  Aprendiz:
    def __init__(self,nombres,apellidos,cedula,sexo):
        self.nombres=nombres
        self.apellidos=apellidos
        self.cedula=cedula
        self.sexo = sexo
        self.formacion=input("Programa de formacion: ")
        self.regional = input("Regional: ")
        
    def show_Info(self):
        print(f"Hola soy un aprendiz SENA!:\n"
            f"{self.nombres}  {self.apellidos}\n"
            f"CC: {self.cedula}\n"
            f"Sexo:  {self.sexo}\n"
            f"Estudiante del programa: {self.formacion} de la regional {self.regional}\n")
        
class Instructor:
    def __init__(self,nombres,apellidos,cedula,area):
        self.nombres=nombres
        self.apellidos=apellidos
        self.cedula=cedula
        self.area = area
        
    def show_Info(self):
        print(f"Hola soy un Intructor SENA!:\n"
            f"{self.nombres}  {self.apellidos}\n"
            f"CC: {self.cedula}\n"
            f"Area de instruccion:  {self.area}\n"
            )
        
class Coordinador:
    def __init__(self,nombres,apellidos,cedula,departamento):
        self.nombres=nombres
        self.apellidos=apellidos
        self.cedula=cedula
        self.departamento = departamento
        
    def show_Info(self):
        print(f"Hola soy un Coordinador SENA!:\n"
            f"{self.nombres}  {self.apellidos}\n"
            f"CC: {self.cedula}\n"
            f"Departamento:  {self.departamento}\n"
            )
        
def show_information(persona):
    persona.show_Info()
    
    
Aprendiz1 = Aprendiz("Samuel Elias","Lastre Paternina","2313546548","Masculino")
Instructor1= Instructor("Stefania","Tamara","65564823","Ingles")
Coordinador1=Coordinador("Carlos","Martinez","13246598","Recursos Humanos")

show_information(Aprendiz1)
show_information(Instructor1)
show_information(Coordinador1)