# Declaración de la clase
class Restaurant:

    # El constructor se ejecuta automáticamente
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria
        self.precio = precio

    def mostrar_restaurant(self):
        print(f'Nombre: {self.nombre} \r\n Categoría: {self.categoria} \r\n Precio: ${self.precio}')

# Instacia de la clase (Objeto)
restaurant = Restaurant('Pizzería Straker', 'Comida Italiana', 20)
restaurant.mostrar_restaurant()

# Instacia de la clase 2 (Objeto 2)
restaurant2 = Restaurant('Burger King', 'Comida rápida', 10)
restaurant2.mostrar_restaurant()