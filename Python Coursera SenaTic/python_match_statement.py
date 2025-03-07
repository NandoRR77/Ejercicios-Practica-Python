'''
Sirve para evaluar una variable que puede tomar muchos
valores
'''

http_request = int(input('Ingrese un valor 200, 201, 400, 500, 501:\n'))
    

match http_request:
    case 200:
        print('Bad Gateway')
    case 201:
        print('Bad URL')
    case 400:
        print('Timeout')
    case 500 | 501:
        print('No access')
    case _:
        ('Unknown')