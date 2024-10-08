class Personas:
    # Constructor 
    def __init__(self,nombres,apellidos,identidad,fNacimiento,sexo):
        self.__nombres=nombres  
        self.__apellidos=apellidos  
        self.__identidad=identidad  
        self.fnacimiento=fNacimiento 
        self.sexo=sexo  
        
    # Métodos para obtener los valores privados
    def obt_nombres(self):
        return self.__nombres
    
    def obt_apellidos(self):
        return self.__apellidos   
    
    def obt_identidad(self):
        return self.__identidad
    
    # Métodos para establecer nuevos valores para los atributos privados
    def establecer_nombres(self,new_name):
        self.__nombres= new_name
    
    def establecer_apellidos(self,new_apellido):
        self.__apellidos=new_apellido
            
    # Método para mostrar los detalles de la persona~
    def show_details(self):
        print(f"\nNombres: {self.__nombres}"
              f"\nApellidos: {self.__apellidos}"
              f"\nN° Identidad: {self.__identidad}"
              f"\nFecha De Nacimiento: {self.fnacimiento}"
              f"\nSexo: {self.sexo}")
        
# Creación de un objeto Persona y muestra de detalles iniciales
persona1 = Personas("Ever David", "Canchano Ariza", "1103740439", "18/08/2005", "Masculino")
persona1.show_details()

# Se establecen nuevos valores para los nombres y apellidos
persona1.establecer_nombres("Daniel Andres")
persona1.establecer_apellidos("Buelvas Perez")

# Se muestran los detalles nuevamente con los nuevos valores
print(f"\nNombres: {persona1.obt_nombres()}"
      f"\nApellidos: {persona1.obt_apellidos()}"
      f"\nN° Identidad: {persona1.obt_identidad()}"
      f"\nFecha De Nacimiento: {persona1.fnacimiento}"
      f"\nSexo: {persona1.sexo}")
