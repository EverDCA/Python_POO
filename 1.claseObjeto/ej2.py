#definir clase

class Animal:
    #Metodo constructor
    def __init__(self,peso,nombre,escosistema,patas,tamaño):
        self.peso = peso
        self.nombre = nombre
        self.ecosistema = escosistema
        self.patas = patas
        self.tamaño = tamaño
    
    #Metodo para mostrar detalles de cada objeto:
    def mostrarDetalles(self):
        print("Informacion del Animal:\n")
        print(f"Peso: {self.peso}")
        print(f"Nombre: {self.nombre}")
        print(f"Ecosistema: {self.ecosistema}")
        print(f"# Patas: {self.patas}")
        print(f"Tamaño: {self.tamaño}\n")
        
    def comer(self):
        print(f"El {self.nombre} esta comiendo!...\n")
        
    def correr(self):
        print(f"El {self.nombre} esta corriendo!...\n")

        
#Creamos Los objetos apartir de instanciar la clase Celular
Animal1=Animal("8kg-18kg","Perro","Terrestre","4","Pequeño") 
Animal2=Animal("8kg","Conejo","Terrestre","4","Mediano")
Animal3=Animal("3kg","Pez","Acuatico","0","Pequeño")

#Mostrar los detalles de cada objeto:
Animal1.mostrarDetalles()
Animal1.correr()
Animal1.comer()
Animal2.mostrarDetalles()
Animal3.mostrarDetalles()