# POO en Python

# Declaración de la clase
class Restaurant:

    # Self hace llamado al propio metodo al que pertenece.
    def agregar_restaurant(self, nombre): 
        self.nombre = nombre

    def mostrar_restaurant(self):
        print(f'Nombre: {self.nombre}')

# Instacia de la clase (Objeto)
restaurant = Restaurant()
restaurant.agregar_restaurant('Mc Donals')
restaurant.mostrar_restaurant()

# Instacia de la clase 2 (Objeto 2)
restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Burger King')
restaurant2.mostrar_restaurant()

# Mostrar información por fuera del metodo
print(f'Nombre restaurant: {restaurant.nombre}')
print(f'Nombre restaurant: {restaurant2.nombre}')