#definir clase
import time
class Empleado:
    #Metodo constructor
    def __init__(self,trabajo,horario,edad,sexo,tiempo):
        self.trabajo = trabajo
        self.horario = horario
        self.edad = edad
        self.sexo = sexo
        self.tiempo = tiempo
    
    #Metodo para mostrar detalles de cada objeto:
    def mostrarDetalles(self):
        print("Informacion del Empleado:\n")
        print(f"trabajo: {self.trabajo}")
        print(f"horario: {self.horario}")
        print(f"edad: {self.edad}")
        print(f"sexo: {self.sexo}")
        print(f"Tiempo en la empresa: {self.tiempo}\n")
        
    def trabajar(self):
        print(f"El empleado con la ocupacion de {self.trabajo} va a empezar a trabajar!..")
        time.sleep(2)
        print("-----------")
        time.sleep(1)
        print("el empleado esta trabajando\n")
        
    def descansar(self):
        print(f"El empleado con la ocupacion de {self.trabajo} va a empezar a descansar!..")
        time.sleep(2)
        print("-----------")
        time.sleep(1)
        print("el empleado esta descansando\n")
        

        
#Creamos Los objetos apartir de instanciar la clase Celular
Empleado1=Empleado("Contador","Normal","34 años","Hombre","4 años") 
Empleado2=Empleado("Diseñadora","Normal","22 años","Mujer","3 meses")
Empleado3=Empleado("Guardia","Nocturno","32 años","Hombre","10 años")

#Mostrar los detalles de cada objeto:
Empleado1.mostrarDetalles()
Empleado1.trabajar()
Empleado1.descansar()
Empleado2.mostrarDetalles()
Empleado3.mostrarDetalles()