# Ejemplo con elif

ocupacion = 'Jubilado'

if ocupacion == 'Estudiante':
    print('Tienes 50% de descueto')
elif ocupacion == 'Jubilado':
    print('Tienes 75% de descuento')
elif ocupacion == 'Desempleado':
    print('Tienes 10% de descuento')
else:
    print('Debe pagar el 100%')