list = []
number = 0

for i in range(1,11):
    number = int(input(f'Ingrese un número {i}: '))
    if number > 0 and number <= 11:
        list.append(number)
    else:
        print(f'El número {number} ingresado no es válido \n Fin del programa.')
        break
print(f'Los números ingresados fueron: {list}')


#Lista generada con list comprehesion
numbers_2 = {i for i in range(1,11) if i > 0 and i <= 11}
print(f'Lista creada con List Comprehesion {numbers_2}')