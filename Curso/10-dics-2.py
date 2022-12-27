# Iniciar un diccionario vacio

jugador = {}
print(jugador)

# Se une un jugador
jugador['nombre'] = 'Jeferson'
jugador['puntaje'] = 0
print(jugador)

# Incrementando el puntaje
jugador['puntaje'] = 100
print(jugador)

# Incrementando el puntaje
jugador['puntaje'] = 200
print(jugador)

#Acceder a un valor
print(jugador.get('Consola', 'No existe ese valor'))

# Iterar en el objeto
for llave, valor in jugador.items():
    print(valor)

# Eliminar jugador y puntaje

del jugador['nombre']
del jugador['puntaje']
print(jugador)
