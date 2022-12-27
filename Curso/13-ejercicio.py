playlist = {} #Diccionario vacio
playlist['canciones'] = [] #Lista vacia

# Función principal
def app():
  # Variable bandera
  agregar_playlist = True
  while agregar_playlist:
    nombre_playlist = input('Cómo desea nombrar la playlist?\r\n')
    if nombre_playlist:
        playlist['nombre'] = nombre_playlist
        #Al agregar un nombre se desactiva la variable bandera
        agregar_playlist = False

        #Llamar a la función para agregar canciones
        agregar_canciones()

def agregar_canciones():
    #Bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
        #Preguntar al usuario que canción desea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'Agrega canciones para la playlist {nombre_playlist} \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)

        if cancion == 'X':
            agregar_cancion = False

            #Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            #Agregar canciones
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist}\r\n')
    print('Canciones:\r\n')
    for i in playlist['canciones']:
        print(i)

app()