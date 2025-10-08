'''
Día 4 – Condicionales más complejos

- Pide tres números e imprime el mayor de ellos.

- Verifica si un año es bisiesto.

- Crea un programa que pida una contraseña y valide si coincide con la guardada
'''
print('#Pide tres números e imprime el mayor de ellos')

num1 = int(input('Ingrese el número 1 => '))
num2 = int(input('Ingrese el número 2 => '))
num3 = int(input('Ingrese el número 3 => '))

#Con función
'''
def num_mayor(num1, num2, num3):
    if num1 == num2 and num1 == num3:
        return print(f'Los números {num1}, {num2} y {num3}son iguales')
    elif num1 > num2 and num1 > num3:
        return print(f'El número {num1} es mayor')
    elif num2 > num1 and num2 > num3:
        return print(f'El número {num2} es mayor')
    else:
        return print(f'El número {num3} es mayor')

num_mayor(num1, num2, num3)
'''

#Con función lambda
num_mayor2 = lambda num1, num2, num3 : 'Los números son iguales' if num1 == num2 and num1 == num3 else 'El número 1 es mayor' if num1 > num2 and num1 > num3 else ('El número 2 es mayor' if num2 > num1 and num2 > num3 else 'El número 3 es mayor')
print(num_mayor2(num1, num2, num3))

print('****************************************************\n')


#Verifica si un año es bisiesto
'''
el año debe ser divisible por 4, 
excepto si es divisible por 100, 
en cuyo caso solo será bisiesto si también es divisible por 400
'''
print('#Verifica si un año es bisiesto')

anio = int(input('Ingrese un año en formato AAAA => '))

#Con if
'''
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f'El año {anio} es bisiesto')
else:
    print(f'El año {anio} no es bisiesto')
'''

#Con función
'''
def validar_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return 'es bisiesto'
    else:
        return 'no es bisiesto'

print(f'El año {anio} ' + validar_bisiesto(anio))
'''

#Con función lambda
valida_bisiesto = (lambda anio: 'es bisiesto' if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) else 'no es bisiesto')
print(f'El año {anio} ' + valida_bisiesto(anio))

print('****************************************************\n')

#Crea un programa que pida una contraseña y valide si coincide con la guardada
print('#Validar contraseñas iguales')

passw = input('Ingrese su contraseña => ')
passw_2 = input('Repita su contraseña => ') 


#Con función
'''
def valida_password(passw, passw_2):
    if passw == passw_2:
        return 'Las contraseñas coinciden'
    else:
        return 'Las contraseñas no coinciden'

print(valida_password(passw, passw_2))
'''

#Con función lambda
valida_password2 = (lambda passw, passw_2 : 'Las contraseñas coinciden' if passw == passw_2 else 'Las contraseñas no coinciden')
print(valida_password2(passw, passw_2))

print('****************************************************\n')
