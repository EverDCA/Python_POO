#definir clase
import time
class Carro:
    #Metodo constructor
    def __init__(self,marca,traccion,modelo,peso,vmax):
        self.marca = marca
        self.traccion = traccion
        self.modelo = modelo
        self.peso = peso
        self.vmax = vmax
    
    #Metodo para mostrar detalles de cada objeto:
    def mostrarDetalles(self):
        print("Informacion del Carro:\n")
        print(f"marca: {self.marca}")
        print(f"traccion: {self.traccion}")
        print(f"Modelo: {self.modelo}")
        print(f"Peso: {self.peso}")
        print(f"Vmax: {self.vmax}\n")
        
    def encender(self):
        print(f"El carro {self.marca} esta Encendiendo!..")
        time.sleep(2)
        print("-----------")
        time.sleep(1)
        print("El carro esta encendido\n")
        
    def Apagar(self):
        print(f"El carro {self.marca} esta Apagandose!..")
        time.sleep(2)
        print("-----------")
        time.sleep(1)
        print("El carro esta apagado\n")
        

        
#Creamos Los objetos apartir de instanciar la clase Celular
Carro1=Carro("Toyota","Trasera","2018","1000kg","280kh") 
Carro2=Carro("Lamborghini","Trasera","2022","1200kg","300kh")
Carro3=Carro("Tesla","Ambas","2024","1400kg","200kh")

#Mostrar los detalles de cada objeto:
Carro1.mostrarDetalles()
Carro1.encender()
Carro1.Apagar()
Carro2.mostrarDetalles()
Carro3.mostrarDetalles()