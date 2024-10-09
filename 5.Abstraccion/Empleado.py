from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcularSalario(self):
        pass
    def show_details(self):
        pass
    
class empleadoPorTiempoCompleto:
    def __init__(self,nombre,apellido,faltas):
        self.nombre=nombre
        self.apellido=apellido
        self.__cargo=input(f"Ingrese Su Cargo:\n"
                        f"1. Manager\n"
                        f"2. Empleado\n"
                        f"3. Admin\n").upper()
        self.__faltas=faltas
        
    def calcularSalario(self):
        if self.__cargo != "MANAGER" and self.__cargo != "EMPLEADO" and self.__cargo != "ADMIN":
            print("Error, Valor no valido...")
        else:
            if self.__cargo == "MANAGER":
                self.salario=5000000*(self.__faltas/100)
                self.salariofinal=5000000-self.salario
                print(f"Cargo:Administrador\nSu salario es de:{self.salariofinal} se desconto {self.salario} por sus {self.__faltas} faltas")
                
            elif self.__cargo == "EMPLEADO":
                self.salario=2000000*(self.__faltas/100)
                self.salariofinal=2000000-self.salario
                print(f"Cargo:Administrador\nSu salario es de:{self.salariofinal} se desconto {self.salario} por sus {self.__faltas} faltas")
                
            elif self.__cargo=="ADMIN":
                self.salario=(4000000*(self.__faltas/100))
                self.salariofinal=4000000-self.salario
                print(f"Cargo:Administrador\nSu salario es de:{self.salariofinal} se desconto {self.salario} por sus {self.__faltas} faltas")
                
            
    def show_details(self):
        print(f"\nNombre: {self.nombre}"
            f"\nApellido: {self.apellido}"
            f"\nCargo: {self.__cargo}"
            f"\nFaltas: {self.__faltas}") 
        
class empleadoPorHoras:
    def __init__(self,nombre,apellido,faltas):
        self.nombre=nombre
        self.apellido=apellido
        self.__faltas=faltas
    def show_details(self):
        print(f"\nNombre: {self.nombre}"
            f"\nApellido: {self.apellido}"
            f"\nFaltas: {self.__faltas}")     
        
    def calcularSalario(self):
        self.horas= 0
        for i in range(4):
            i=i+1
            self.hsemanales = int(input(f"Ingrese las horas trabajadas en la {i} semana: "))
            self.horas+=self.hsemanales
    
        self.salario=7000*self.horas
        self.descuento=self.salario*(self.__faltas/100)
        self.salariofinal=self.salario-self.descuento
        print(f"Su salario es de: {self.salariofinal} $pesos\n"
            f"Se descontaron {self.descuento} por sus {self.__faltas} faltas")
        
        
empleadoPorTiempoCompleto1=empleadoPorTiempoCompleto("Ever","Canchano",2)   
empleadoPorTiempoCompleto1.calcularSalario()
empleadoPorTiempoCompleto1.show_details()

empleadoPorHoras1=empleadoPorHoras("Samuel","Lastre",4)
empleadoPorHoras1.calcularSalario()
empleadoPorHoras1.show_details()
