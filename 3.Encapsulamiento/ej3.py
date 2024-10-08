class Libro:
    # Constructor
    def __init__(self, titulo, autor, isbn, cantidad, categoria):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.cantidad = cantidad
        self.categoria = categoria

    # Métodos para obtener los valores privados
    def obt_titulo(self):
        return self.__titulo

    def obt_autor(self):
        return self.__autor

    def obt_isbn(self):
        return self.__isbn

    # Métodos para establecer nuevos valores
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def establecer_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def establecer_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn

    # Método para mostrar detalles del libro
    def show_details(self):
        print(f"\nTítulo: {self.__titulo}"
            f"\nAutor: {self.__autor}"
            f"\nISBN: {self.__isbn}"
            f"\nCantidad: {self.cantidad}"
            f"\nCategoría: {self.categoria}")

# Crear una instancia de Libro
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978", 50, "Novela")
libro1.show_details()

# Establecer nuevos valores
libro1.establecer_titulo("El Amor en los Tiempos del Cólera")
libro1.establecer_autor("Gabriel García Márquez")
libro1.establecer_isbn("979")

# Mostrar los detalles nuevamente
print(f"\nTítulo: {libro1.obt_titulo()}"
        f"\nAutor: {libro1.obt_autor()}"
        f"\nISBN: {libro1.obt_isbn()}"
        f"\nCantidad: {libro1.cantidad}"
        f"\nCategoría: {libro1.categoria}")
