'''
Día 6 – Bucles prácticos

- Dibuja un triángulo de asteriscos de altura 5.

- Pide una palabra y muestra cada letra en una línea.

- Pide un número y calcula el factorial.
'''

#Dibuja un triángulo de asteriscos de altura 5
print('\nDibuja un triángulo de asteriscos de altura 5\n')

#Con ciclo for
print('Con ciclo for')
for i in range (6):
    print('*'*i)

#Con Lamda
print('\n\nCon función lambda')
triangle = list(map(lambda i: print('*'*i), range(6)))

print('\n****************************************************\n')


#Pide una palabra y muestra cada letra en una línea
print('\nPide una palabra y muestra cada letra en una línea\n')

#Con ciclo for
print('Con ciclo for')
palabra = input('Ingrese una palabra >= ')
for i in palabra:
    print(i)

#Con Lamda
print('\n\nCon función lambda')
palabra_linea = list(map(lambda i: print(i), palabra))

print('\n****************************************************\n')


#Pide un número y calcula el factorial
print('\nPide un número y calcula el factorial\n')

#Con función normal
print('Con función normal')

num = int(input('Ingrese un número >= '))
def factorial(num):
    fact = 1    
    for i in range(1,num+1):
        #fact = fact*i
        fact *= i
    return fact

print(f'el factorial de {num} es {factorial(num)}')

print('\n****************************************************\n')