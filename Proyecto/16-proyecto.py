# Proyecto crear directorio de contactos

import os

CARPETA = 'Proyecto/Contactos/' # Carpeta de contactos -> Constante
EXTENSION = '.txt' # Extensión del archivo

class Contacto():
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():
    #Revisa si la carpeta existe o no
    crear_directorio()

    # Mostrar menú de opciones
    mostrar_menu()

    # Preguntar la acción que desea realizar
    preguntar = True

    while preguntar:
        opcion = int (input('Seleccione una opción: \r\n'))
        
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no valida, intente de nuevo')


def eliminar_contacto():
    nombre = input('Seleccione el Contacto que desea eliminar \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado correctamente\r\n')
    except:
        print('\r\nNo existe este contacto\r\n')

    # Reiniciar la app
    app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe \r\n')

    # Reiniciar App
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # Imprime los contenidos
                print(linea.rstrip())
            # Imprime un separador entre contactos
            print('\r\n')
    

    # Reiniciar app
    app()

def editar_contacto():
    nombre_anterior = input('\r\nNombre del contacto que desea editar: \r\n')

    # Validar si el archivo existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            # Resto de los campos
            nombre_contacto = input('Agrega el Nueva nombre: \r\n')
            telefono_contacto = input('Agrega el Nuevo teléfono: \r\n')
            categoria_contacto = input('Agrega la Nueva categoria: \r\n')

            # Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')

            #Pediente de correción
            
            # Renombrar el archivo
            # os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            # Mostrar mensaje de exito
            print('\r\n Contacto editado correctamente \r\n')
    else:
        print('Ese contacto no existe')

    # Reiniciar la aplicación
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del Contacto \r\n')

    # Validar si el nombre ya existe
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            # Resto de los campos
            telefono_contacto = input('Telefono del contacto \r\n')
            categoria_contacto = input('Categoria del contacto \r\n')

            # Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir el contacto 
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Nombre: ' + contacto.telefono + '\r\n')
            archivo.write('Nombre: ' + contacto.categoria + '\r\n')

            # Mostrar mensaje de exito
            print('\r\n Contacto creado correctamente \r\n ')
    else:
        print('\r\nEse contacto ya existe \r\n')
    
    # Reiniciar la app
    app()

def mostrar_menu():
    print('Seleccione del menú lo que desea hacer: ')
    print('1) Crear nuevo contacto')
    print('2) Modificar contacto')
    print('3) Mostrar contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA):
        # crear la carpeta
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()