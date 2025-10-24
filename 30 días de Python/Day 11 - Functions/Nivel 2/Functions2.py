'''
Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número
'''

def factorial(num):
    
    if num <= 0:
        fact = 0
        print(f'El factorial de {num} es {fact}')
    else:
        fact = 1
        for i in range(1, num+1):
            fact *= i
        print(f'El factorial de {num} es {fact}')

factorial(7)