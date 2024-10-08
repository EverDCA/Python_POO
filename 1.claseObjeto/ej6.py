#definir clase
import time
class Moto:
    #Metodo constructor
    def __init__(self,marca,modelo,peso,vmax,torque):
        self.marca = marca
        self.modelo = modelo
        self.peso = peso
        self.vmax = vmax
        self.torque = torque
    
    #Metodo para mostrar detalles de cada objeto:
    def mostrarDetalles(self):
        print("Informacion de la moto:\n")
        print(f"marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"peso: {self.peso}")
        print(f"Velocidad maximan: {self.vmax}")
        print(f"Torque: {self.torque}\n")
        
    def encender(self):
        print(f"La moto {self.marca} esta Encendiendo!..")
        time.sleep(2)
        print("-----------")
        time.sleep(1)
        print("La moto esta encendida\n")
        
    def Apagar(self):
        print(f"la moto {self.marca} esta Apagandose!..")
        time.sleep(2)
        print("-----------")
        time.sleep(1)
        print("la moto esta apagada\n")
        

        
#Creamos Los objetos apartir de instanciar la clase Celular
moto1=Moto("Biwi","2016","98kg","80kh","8.2Nm") 
moto2=Moto("Yamaha","2022","99kg","120kh","12Nm")
moto3=Moto("Honda","2008","69kg","70kh","8Nm")

#Mostrar los detalles de cada objeto:
moto1.mostrarDetalles()
moto1.encender()
moto1.Apagar()
moto2.mostrarDetalles()
moto3.mostrarDetalles()