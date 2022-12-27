# Realiza un examen con 3 preguntas que tu desees, el usuario deberá responder "SI" o "No" y al final otorgarle una calificación (La calificación se logra con una variable que inicia en 0 y por cada respuesta correcta incrementa en 1)


# Primera pregunta
def Examen():
    calificacion = 0
    Estado1 = False
    Estado2 = False
    Estado3 = False
    while Estado1 == False:
        Pregunta1 = input('El cielo es de color morado? responda Si o No \r\n')
        pregunta1 = Pregunta1.lower()
        if pregunta1 == 'no':
            calificacion += 10
            Estado1 = True
            print('Respuesta correcta \n')
        elif pregunta1 == 'si':
            print('Respuesta incorrecta \n')
            Estado1 = True
        else:
            print('Respuesta invalida, por favor responda Si o No \r\n')    

    # Segunda pregunta
    while Estado2 == False:
        Pregunta2 = input('Si hoy es Lunes mañana es viernes? responda Si o No \r\n')
        pregunta2 = Pregunta2.lower()
        if pregunta2 == 'no':
            calificacion += 10
            Estado2 = True
            print('Respuesta correcta \n')
        elif pregunta2 == 'si':
            Estado2 = True
            print('Respuesta incorrecta \n')
        else:
            print('Respuesta invalida, por favor responda Si o No \r\n')

    # Tercera pregunta
    while Estado3 == False:
        Pregunta3 = input('8 x 8 es igual a 64? responda Si o No \r\n')
        pregunta3 = Pregunta3.lower()
        if pregunta3 == 'si':
            calificacion +=10
            Estado3 = True
            print('Respuesta correcta \n')
        elif pregunta3 == 'no':
            Estado3 = True
            print('Respuesta incorrecta \n')
        else:
            print('Respuesta invalida, por favor responda Si o No \r\n')    

    print('Terminaste el examen \r\n')
    print(f'Tu calificación es de {calificacion}')

Examen()
