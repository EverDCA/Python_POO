#definir clase

class Celular:
    #Metodo constructor
    def __init__(self,marca,bateria,nombre,imei,camara):
        self.marca = marca
        self.bateria = bateria
        self.nombre = nombre
        self.imei = imei
        self.camara = camara
    
    #Metodo para mostrar detalles de cada objeto:
    def mostrarDetalles(self):
        print("Informacion del celular:\n")
        print(f"Marca: {self.marca}")
        print(f"bateria: {self.bateria}")
        print(f"nombre: {self.nombre}")
        print(f"imei: {self.imei}")
        print(f"camara: {self.camara}\n")
    
    def encender(self):
        self.carga = int(input("Ingrese la carga del celular : "))
        
        if self.carga>0:
            self.encendido=True
            print(f"--{self.carga}--")
            print(f"El celular {self.nombre} se puede encender\n")
        else:
            print(f"El celular {self.nombre} NO se puede encender\n")
            
        
    def apagar(self):
        self.validar = input(f"Quiere apagar el celular {self.nombre}?(y/n): ")
        if self.validar == "y":
            if self.encendido == True:
                print(f"El celular {self.nombre} se apago correctamente\n")
                
        else:
            ""
    def cargar(self):
        print(f"El celular esta cargando\n Carga Actual: {self.carga}%\n")
    
#Creamos Los objetos apartir de instanciar la clase Celular
celular1 = Celular("Huawei","4500mAh","Huawei p30","302212191","98px") 
celular2= Celular("Samsung","5000mAh","Samsung S22+","198393891","64mpx")
celular3=Celular("Samsung","3000mAh","Samsung J2","1922389264","12px")

#Mostrar los detalles de cada objeto:
celular1.mostrarDetalles()
celular1.encender()
celular1.apagar()
celular1.cargar()
celular2.mostrarDetalles()
celular3.mostrarDetalles()