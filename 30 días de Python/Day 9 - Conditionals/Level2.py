'''
Exercises: Day 8

Exercises: Level 2

1. Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F

2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: 
September, October or November, the season is Autumn. December, January or February, 
the season is Winter. March, April or May, the season is Spring June, July or August, 
the season is Summer

3. The following list contains some fruits:

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
'''


# 1. Write a code which gives grade to students according to theirs scores
print('# 1. Write a code which gives grade to students according to theirs scores')

note = int(input('Ingrese su nota ==> '))

'''
# Con condicionales
if note < 0 or note > 100:
    print(f'La nota ingresada no es válida')
elif note <= 49:
    print(f'Para la nota {note} la calificación es F')
elif note <= 59:
    print(f'Para la nota {note} la calificación es D')
elif note <= 69:
    print(f'Para la nota {note} la calificación es C')
elif note <= 89:
    print(f'Para la nota {note} la calificación es B')
else:
    print(f'Para la nota {note} la calificación es A')
'''    
    
#Con función
#Defino listas con los rangos usando list comprenhesion
A = [i for i in range(90,101)]
B = [i for i in range(70,90)]
C = [i for i in range(60,70)]
D = [i for i in range(50,60)]
F = [i for i in range(50)]

#Defino el diccionario con la calificación y las notas
grades = {
    'Grade A': A,
    'Grade B': B,
    'Grade C': C,
    'Grade D': D,
    'Grade F': F, 
}

def calcular_calificacion(note):
    for calificacion, notas in grades.items():
        if note in notas:
            return f'Para la nota {note}, la calificacion es {calificacion}'
    return 'Nota no valida'

print(calcular_calificacion(note))

print('****************************************************\n')


# 2. Check if the season is Autumn, Winter, Spring or Summer
print('2. Check if the season is Autumn, Winter, Spring or Summer')

#Defino un diccionario con los meses y las estaciones
estaciones = {
    'Autumn':['September', 'October', 'November'],
    'Winter':['December', 'January', 'February'],
    'Spring':['March', 'April', 'May'],
    'Summer':['June', 'July', 'August'],
}

#Defino lista de meses para que solo seleccionen un válido
meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

mes_buscado = input(f'Ingrese un mes de la siguiente lista \n =>{meses}\n')


def valida_estacion(mes_buscado):
    for estacion, meses in estaciones.items():
        if mes_buscado in meses:
            print(f'La estación que corresponde según el mes ingresado es => {estacion}')
    print(f'El mes {mes_buscado} no es válido')

valida_estacion(mes_buscado)
          
print('****************************************************\n')



# 3. Validate fruits
print(' 3. Validate fruits')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input(f'Ingrese una fruta =>  ')

def valida_fruta(fruit):
    if fruit in fruits:
        return f'That fruit already exist in the list {fruits}'
    else:
        fruits.append(fruit)
    return f'The friuit {fruit} was added to list {fruits}' 

print(valida_fruta(fruit))

print('****************************************************\n')
