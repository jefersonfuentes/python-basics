lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

print(lenguajes)

# los arrays (lists) comienzan en la posición 0
print(lenguajes[0])

# Ordenador elementos A-Z
lenguajes.sort()
print(lenguajes)

# Acceder a un elemento en un string
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

# Modificar un elemento de un arreglo
lenguajes[2] = 'PHP'
print(lenguajes)

# Agregar elementos a un arreglo
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar elementos de un arreglo
del lenguajes[1]
print(lenguajes)

# Eliminar elementos de un arreglo 2
lenguajes.pop() #Eliminar último elemento
print(lenguajes)

# Eliminar con pop una posición especifica.
lenguajes.pop(0)
print(lenguajes)

# Eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)