'''
Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y 
muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde 
<mes> es el nombre del mes.

'''
meses = {
    '01': 'enero',
    '02': 'febrero',
    '03': 'marzo',
    '04': 'abril',
    '05': 'mayo',
    '06': 'junio',
    '07': 'julio',
    '08': 'agosto',
    '09': 'septiembre',
    '10': 'octubre',
    '11': 'noviembre',
    '12': 'diciembre',
}

fecha = input('Ingrese una fecha en formato dd/mm/aaaa =>')
fecha = fecha.split('/')

print(f'{fecha[0]} de {meses[fecha[1]]} {fecha[2]}')

