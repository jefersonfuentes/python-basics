# Creando un diccionario simple

cancion = {
    'artista' : 'Metallica', # llave y valor
    'cancion' : 'Enter Sandman',
    'lanzamiento' : 1992,
    'likes' : 3000
}

# Acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

# Mezclar con un string
artista = cancion['artista']
print(f'Estoy escuchando a {artista}')

# Agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

# Remplazar valor existente
cancion['cancion'] = 'One'
print(cancion)

# Eliminar valor
del cancion['lanzamiento']
print(cancion)