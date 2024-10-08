class Producto:
    # Constructor
    def __init__(self,nombre,precio,cantidad,categoria):
        self.__nombre=nombre  
        self.__precio=precio  
        self.cantidad=cantidad  
        self.categoria=categoria 
        
    # Métodos para obtener los valores privados
    def obt_nombre(self):
        return self.__nombre
    
    def obt_precio(self):
        return self.__precio   
    
    # Métodos para establecer nuevos valores para los atributos privados
    def establecer_nombre(self,new_name):
        self.__nombre= new_name
    
    def establecer_precio(self,new_price):
        self.__precio=new_price
            
    # Método para mostrar los detalles del producto
    def show_details(self):
        print(f"\nNombre: {self.__nombre}"
            f"\nPrecio: {self.__precio}"
            f"\nCantidad: {self.cantidad}"
            f"\nCategoría: {self.categoria}")
        
# Creación de un objeto Producto y muestra de detalles iniciales
producto1 = Producto("Laptop", 1200000, 10, "Pc")
producto1.show_details()

# Se establecen nuevos valores para el nombre y el precio
producto1.establecer_nombre("Laptop Gaming")
producto1.establecer_precio(2200000)

# Se muestran los detalles nuevamente con los nuevos valores
print(f"\nNombre: {producto1.obt_nombre()}"
      f"\nPrecio: {producto1.obt_precio()}"
      f"\nCantidad: {producto1.cantidad}"
      f"\nCategoría: {producto1.categoria}")
