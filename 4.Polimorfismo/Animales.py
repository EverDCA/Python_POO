class Perro:
    def __init__(self, raza, edad,nombre):
        self.raza = raza
        self.edad = edad
        self.nombre=nombre
    
    def sonido(self):
        print(f"El perro {self.nombre} de raza {self.raza} hace: ¡Guau Guau!")

class Gato:
    def __init__(self, raza, edad,nombre):
        self.raza = raza
        self.edad = edad
        self.nombre=nombre
    def sonido(self):
        print(f"El gato {self.nombre} de raza {self.raza} hace: ¡Miau Miau!")

class Pajaro:
    def __init__(self, especie, edad,nombre):
        self.especie = especie
        self.edad = edad
        self.nombre=nombre
    def sonido(self):
        print(f"El pájaro {self.nombre} de especie {self.especie} hace: ¡Pío Pío!")

def emitir_sonido(animal):
    animal.sonido()

# Ejemplo de uso
perro1 = Perro("FreshPuddle", 3,"Milo")
gato1 = Gato("Siamés", 2,"Megatron")
pajaro1 = Pajaro("Perico", 1,"Insano")

emitir_sonido(perro1)
emitir_sonido(gato1)
emitir_sonido(pajaro1)
