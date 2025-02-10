
'''
while normal

counter = 0

while counter < 10:
    counter += 1
    print(counter)
'''

'''
While con break

counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break #romper el ciclo en 15 con el break
    print(counter)

'''

'''
While con continue
'''

counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue #salta a la siguiente la iteracción cuando se cumple la condición
    print(counter) #este print no se ejecuta hasta que counter no sea menor que 15