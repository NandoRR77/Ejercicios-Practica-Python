'''
# syntax
# Declaring a function
def function_name():
    #codes
    pass
# Calling a function
function_name()
'''
print('Función sin parámetros y sin return')
#Función sin parametros y sin return
def function_fullName():
    name = 'Fernando'
    last_name = 'Ramírez'
    print('El nombre completo es' , name, last_name )
function_fullName()

print('\nFunción sin parámetros y con return')
#Función sin parametros y con return
def function_fullName2():
    name = 'Camila'
    last_name = 'Ramírez'
    full_name = name + ' ' +last_name
    return full_name
print(function_fullName2())


print('\nFunción con parámetro')
#Función con parametro 
def function_imprime_mensaje(edad):
    message = 'Hola, esta es una función con parametros. La edad ingresada es: ' + str(edad)
    return message
print(function_imprime_mensaje(35))


def square_number(x):
    return x * x
print('El cuadrado del número es: ' , square_number(2))


print('\nFunción con 2 parámetros')
#Función con 2 parámetros 
def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

print('\nFuncion con mas de un parámetro sin importar el orden en que los pasemos')
#Funcion con mas de un paramatros sin importar el orden en que los pasemos
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter

print('\nFunción con parámetros predeterminados')
#Función con parámetros predeterminados.
#A veces, pasamos valores predeterminados a los parámetros cuando invocamos la función. 
#Si no pasamos argumentos al llamar a la función, se utilizarán sus valores predeterminados.

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))


print('\nFuncion con argumentos arbitrarios')
#Funcion con argumentos arbitrarios (si no conocemos el número de argumentos, 
#agregando * antes del nombre del parámetro.)

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10