from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

    def show_details(self):
        pass

class Ingeniero(TareaEmpleado):
    def __init__(self, nombre, apellido, proyecto):
        self.nombre = nombre
        self.apellido = apellido
        self.proyecto = proyecto

    def realizar_tarea(self):
        print(f"El Ingeniero {self.nombre} está diseñando el proyecto {self.proyecto}.")

    def show_details(self):
        super().show_details()
        print(f"Proyecto actual: {self.proyecto}")

class Doctor(TareaEmpleado):
    def __init__(self, nombre, apellido, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad

    def realizar_tarea(self):
        print(f"El Doctor {self.nombre} está tratando pacientes en la especialidad de {self.especialidad}.")

    def show_details(self):
        super().show_details()
        print(f"Especialidad: {self.especialidad}")

ingeniero1 = Ingeniero("Ana", "Gómez", "Puente Sincelejito")
ingeniero1.realizar_tarea()
ingeniero1.show_details()

doctor1 = Doctor("Carlos", "Ruiz", "Cardiología")
doctor1.realizar_tarea()
doctor1.show_details()
