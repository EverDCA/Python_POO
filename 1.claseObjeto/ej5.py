#definir clase
class FigurasGeo:
    #Metodo constructor
    def __init__(self,lados,base,altura,nombre,color):
        self.lados = lados
        self.base = base
        self.altura = altura
        self.nombre = nombre
        self.color = color
    
    #Metodo para mostrar detalles de cada objeto:
    def mostrarDetalles(self):
        print("Informacion de la figura:\n")
        print(f"lados: {self.lados}")
        print(f"base: {self.base}")
        print(f"altura: {self.altura}")
        print(f"nombre: {self.nombre}")
        print(f"color: {self.color}\n")
        
    def Area(self):
        if self.nombre == "Triangulo":
            self.resultado= (self.base*self.altura)/2
            print(f"El area del triangulo es: {self.resultado}")
        elif self.nombre == "Rectangulo":
            self.resultado= (self.base*self.altura)
            print(f"El area del Rectangulo es: {self.resultado}")
        elif self.nombre == "Circulo":
            self.radio = int(input("Ingrese el radio del circulo: "))
            self.resultado= 3.1416*(self.radio**2)
            print(f"El area del Circulo es: {self.resultado}")
            
    def perimetro(self):
        if self.nombre == "Triangulo":
            self.lado1= int(input("Ingrese el primer lado del triangulo: "))
            self.lado2= int(input("Ingrese el primer lado del triangulo: "))
            self.lado3= int(input("Ingrese el primer lado del triangulo: "))
            
            self.resultado= (self.lado1+self.lado2+self.lado3)
            print(f"El Perimetro del triangulo es: {self.resultado}")
        elif self.nombre == "Rectangulo":
            self.resultado= (self.base+self.altura)*2
            print(f"El Perimetro del Rectangulo es: {self.resultado}")
        elif self.nombre == "Circulo":
            self.diametro = int(input("Ingrese el diametro del circulo: "))
            self.resultado= 3.1416*(self.diametro**2)
            print(f"El area del Circulo es: {self.resultado}")
        
        

        
#Creamos Los objetos apartir de instanciar la clase Celular
Figura1=FigurasGeo(0,0,0,"Circulo","Rojo") 
Figura2=FigurasGeo(3,21,21,"Triangulo","Azul")
Figura3=FigurasGeo(4,22,14,"Rectangulo","Negro")

#Mostrar los detalles de cada objeto:
Figura1.mostrarDetalles()
Figura1.Area()
Figura1.perimetro()
Figura2.mostrarDetalles()
Figura2.Area()
Figura3.mostrarDetalles()
Figura3.Area()
