class Guitarra:
    def __init__(self, marca, cuerdas):
        self.marca = marca
        self.cuerdas = cuerdas
    
    def tocar(self):
        print("\nInformacion del instrumento: ")
        print(f"La guitarra de marca {self.marca} tiene {self.cuerdas} cuerdas y produce un sonido Metalicoo!.")

class Piano:
    def __init__(self, marca, teclas):
        self.marca = marca
        self.teclas = teclas
    
    def tocar(self):
        print("\nInformacion del instrumento: ")
        print(f"El piano de marca {self.marca} tiene {self.teclas} teclas y produce un sonido Armonioso.")

class Trompeta:
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
    
    def tocar(self):
        print("\nInformacion del instrumento: ")
        print(f"La trompeta de marca {self.marca} es del tipo {self.tipo} y produce un sonido Cultural.\n")

def tocar_instrumento(instrumento):
    instrumento.tocar()


guitarra1 = Guitarra("Fender", 6)
piano1 = Piano("Yamaha", 88)
trompeta1 = Trompeta("Bach", "Bb")

tocar_instrumento(guitarra1)
tocar_instrumento(piano1)
tocar_instrumento(trompeta1)
