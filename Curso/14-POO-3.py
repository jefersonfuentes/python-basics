# Declaración de la clase
class Restaurant:

    # El constructor se ejecuta automáticamente
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria
        # Se aplica encapsulamiento
        self.__precio = precio # Default: Public, PROTECTED, PRIVATE

    def mostrar_restaurant(self):
        print(f'Nombre: {self.nombre} \r\n Categoría: {self.categoria} \r\n Precio: ${self.__precio}')

    # GETTERS Y SETTERS - Get = Obtiene un valor, Set = Agrega un valor.
         # Permiten acceder a atributos privados de una clase

    def get_precio(self):
        # print(self.__precio)
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

# Instacia de la clase (Objeto)
restaurant = Restaurant('Pizzería Straker', 'Comida Italiana', 20)
# restaurant.__precio = 50 # No será posible modificarlo con PRIVATE __ 
restaurant.mostrar_restaurant()
restaurant.set_precio(80)
# restaurant.get_precio()
precio = restaurant.get_precio() # Getter por medio del return
print(precio)

# Instacia de la clase 2 (Objeto 2)
restaurant2 = Restaurant('Burger King', 'Comida rápida', 10)
restaurant2.mostrar_restaurant()
restaurant2.set_precio(40)
# restaurant2.get_precio() 
precio2 = restaurant2.get_precio() # Getter por medio del return
print(precio2)