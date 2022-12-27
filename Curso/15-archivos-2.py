def app():

    # Por default viene en el modo read por ende no se le asigna modo
    with open('Curso/archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido)

app()