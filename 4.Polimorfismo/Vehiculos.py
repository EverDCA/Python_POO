class  Carro:
    def __init__(self,marca,vmax,modelo,color,tipo):
        self.marca=marca
        self.vmax=vmax
        self.modelo=modelo
        self.color=color
        self.tipo=tipo
        
    def show_Info(self):
        print(f"\nInformacion Del Carro!:\n"
            f"Marca: {self.marca}  Velocidad Maxima: {self.vmax}\n"
            f"Modelo: {self.modelo}\n"
            f"Color:  {self.color}\n"
            f"Tipo: {self.tipo}\n")

        
class Moto:
    def __init__(self,marca,vmax,modelo,color,tipo):
        self.marca=marca
        self.vmax=vmax
        self.modelo=modelo
        self.color=color
        self.tipo=tipo
        
    def show_Info(self):
        print(f"\nInformacion De la Moto!:\n"
            f"Marca: {self.marca}  Velocidad Maxima: {self.vmax}\n"
            f"Modelo: {self.modelo}\n"
            f"Color:  {self.color}\n"
            f"Tipo: {self.tipo}\n")
        
class Bicicleta:
    def __init__(self,marca,vmax,modelo,color,tipo):
        self.marca=marca
        self.vmax=vmax
        self.modelo=modelo
        self.color=color
        self.tipo=tipo
        
    def show_Info(self):
        print(f"\nInformacion De la Bicicleta!:\n"
            f"Marca: {self.marca}  Velocidad Maxima: {self.vmax}\n"
            f"Modelo: {self.modelo}\n"
            f"Color:  {self.color}\n"
            f"Tipo: {self.tipo}\n")
        
def show_information(vehiculo):
    vehiculo.show_Info()
    
    
Carro1 = Carro("Toyota","280kh","2018","Negro","Deportivo")
Moto1= Moto("Yamaha","240kh","2021","Azul","Naked")
Bicicleta1=Bicicleta("Mountain","100kh","2022","Amarillo","Montaña")

show_information(Carro1)
show_information(Moto1)
show_information(Bicicleta1)