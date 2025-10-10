'''
Exercises: Day 8

Exercises: Level 1

1. Get user input using input(“Enter your age: ”). If user is 18 or older, 
give feedback: You are old enough to drive. If below 18 give feedback to wait 
for the missing amount of years. 

Output:
Enter your age: 30
You are old enough to learn to drive.

Output:
Enter your age: 15
You need 3 more years to learn to drive.

2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
Use input(“Enter your age: ”) to get the age as input. You can use a nested condition 
to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom 
text if my_age = your_age. 

Output:
Enter your age: 30
You are 5 years older than me.

3. Get two numbers from the user using input prompt. If a is greater than b return a is 
greater than b, if a is less b return a is smaller than b, else a is equal to b. 

Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3

'''

#1. Calcular edad para conducir
print('\n#1. Calcular edad para conducir\n')

edad = int(input('Ingrese su edad >= '))

def calcular_edad_conduccion(edad):
    if edad >= 18:
        print('\nUsted tiene la edad suficiente para conducir.')
    else:
        restante = 18 - edad
        print(f'\nUsted necesita {restante} años más para conducir.')

calcular_edad_conduccion(edad)

print('****************************************************\n')


#2. Comparar mi edad con tu edad y la diferencia en años
print('#2. Comparar mi edad con tu edad y la diferencia en años\n')

tu_edad = int(input('Ingrese su edad >= '))
mi_edad = 42
print(f'Mi edad es {mi_edad} años')

def comparar_edad(tu_edad, mi_edad):
    if mi_edad == tu_edad:
        print('Tenemos la misma edad\n')
    elif mi_edad > tu_edad:
        diferencia = mi_edad - tu_edad
        if diferencia == 1:
            print(f'Yo soy {diferencia} año mayor que tu\n')
        else:
            print(f'Yo soy {diferencia} años mayor que tu\n')
    else:
        diferencia = tu_edad - mi_edad
        if diferencia == 1:
            print(f'Tu eres {diferencia} año mayor que yo\n')
        else:
            print(f'Tu eres {diferencia} años mayor que yo\n')

comparar_edad(tu_edad,mi_edad)

print('****************************************************\n')


#3. Comparar 2 números y decir cual es mayor
print('#3. Comparar 2 números y decir cual es mayor\n')

num1 = int(input('Ingrese el número 1 => '))
num2 = int(input('Ingrese el número 2 => '))

def num_mayor(num1, num2):
    if num1 == num2:
        return print(f'Los números ingresados son iguales')
    elif num1 > num2: 
        return print(f'El número {num1} es mayor que el número {num2}')
    else: 
        return print(f'El número {num2} es mayor que el número {num1}')

num_mayor(num1, num2)

print('****************************************************\n')