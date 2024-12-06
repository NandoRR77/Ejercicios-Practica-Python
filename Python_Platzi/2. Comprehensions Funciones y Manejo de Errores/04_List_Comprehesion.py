''' 
syntaxis = {element for element in iterable}
syntaxis = {element for element in iterable if condition} con condicionales

#Modo tradicional de generar una lista
 
numbers = []

for element in range(1,11):
    numbers.append(element * 2) #el elemento agregado lo multiplico * 2 antes de agregarlo
    
print(numbers)

#Con list comprehension
numbers_v2 = [element * 2 for element in range(1,11) ]
print(numbers_v2)

'''
#Crear lista de números del 1 al 10 agregando sólo los números pares 
#y multiplincando el número agregado * 2
numbers = []

for i in range (1 ,11):
    if i % 2 == 0:
        numbers.append(i * 2)
    else:
        continue
    
print(numbers)
#Con list comprehension + condicional
#Crear lista de números del 1 al 10 agregando sólo los números pares
#y multiplincando el número agregado * 2

numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)