pregunta = 'Agrega un número y te diré si es par o impar: \r\n'
pregunta += '(Escribe "cerrar" para salir de la aplicación)\r\n '

# Variable condicional para el while
preguntar = True
while preguntar:
    numero = input(pregunta)
    numero = numero.lower()
    if numero == 'cerrar':
        preguntar = False
    else:
        #Se convierte a int para que no falle la ejecución
        numero = int(numero) 
        if numero % 2 == 0:
            print(f'El numero {numero} es par \r\n') 
        else:
            print(f'El numero {numero} es impar \r\n')
