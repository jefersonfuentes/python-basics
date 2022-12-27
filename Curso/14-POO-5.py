# Declaración de la clase
class Restaurant:

    # El constructor se ejecuta automáticamente
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria
        # Se aplica encapsulamiento
        self.precio = precio # Default: Public, PROTECTED, PRIVATE

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre} \r\n Categoría: {self.categoria} \r\n Precio: ${self.precio}')

    # GETTERS Y SETTERS - Get = Obtiene un valor, Set = Agrega un valor.
         # Permiten acceder a atributos privados de una clase

    def get_precio(self):
        # print(self.precio)
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

# Herencia

# Declaración de una clase hijo de Restaurant

class Hotel(Restaurant):
    def __init__(self,nombre, categoria, precio, alberca):
        # Referencia al constructor del padre
        super().__init__(nombre,categoria,precio)
        self.alberca = alberca

    # Reescribir método (debe llamarse igual)
    def mostrar_datos(self):
        print(f'Nombre: {self.nombre} \r\n Categoría: {self.categoria} \r\n Precio: ${self.precio} \r\n Alberca: {self.alberca}')

    def get_alberca(self):
        return self.alberca

hotel = Hotel('Hotel POO','5 Estrellas', 500, 'Si')
hotel.mostrar_datos()

# alberca = hotel.get_alberca()
# print(alberca)