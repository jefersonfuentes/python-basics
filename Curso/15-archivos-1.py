def app():
    # Crear un archivo
    archivo = open('Curso/archivo.txt', 'w') # w es permiso de escritura, sino existe lo creará

    for i in range(0, 20):
        archivo.write('Esta es la linea ' + str(i) + '\n')

    # Buena practica cerrar el archivo
    archivo.close()

app()