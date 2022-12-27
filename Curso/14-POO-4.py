# Declaración de la clase
class Restaurant:

    # El constructor se ejecuta automáticamente
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria
        # Se aplica encapsulamiento
        self.__precio = precio # Default: Public, PROTECTED, PRIVATE

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre} \r\n Categoría: {self.categoria} \r\n Precio: ${self.__precio}')

    # GETTERS Y SETTERS - Get = Obtiene un valor, Set = Agrega un valor.
         # Permiten acceder a atributos privados de una clase

    def get_precio(self):
        # print(self.__precio)
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

# Herencia

# Declaración de una clase hijo de Restaurant

class Hotel(Restaurant):
    def __init__(self,nombre, categoria, precio):
        # Referencia la clase padre
        super().__init__(nombre,categoria,precio)

hotel = Hotel('Hotel POO','5 Estrellas', 500)
hotel.mostrar_datos()