'''
#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
y = -2
x = (2 - y) / 2
slope8 = 2
print(f'The slope = {slope8}, the y = {y} and x = {x}')
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
#Distancia euclidiana
from math import dist

punto1=(2, 2)
punto2 = (6, 10)

slope9 = ((punto2[1]-punto1[1]) / (punto2[0]-punto1[0]))

distancia = round(dist(punto1, punto2),3)
print(f'Euclidean distance = {distancia}, the slope = {slope9}')
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

#10. Compare the slopes in tasks 8 and 9.
print(f"The comparision between slope1 and slope2 is" , slope8 == slope9)

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = float(input('Please enter a value for x: '))
y = ((x**2) + (6*x) + 9)
print(f'The y value = {y}')

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') != len('dragon'))

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('Check if on is found in both python and dragon.', 'The result is', 'on' in 'python' and 'on' in 'dragon')

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('Use in operator to check if jargon is in the sentence "I hope this course is not full of jargon".','The result is', 'jargon' in 'I hope this course is not full of jargon')

#15. There is no 'on' in both dragon and python
print('There is no "on" in both dragon and python','The result is', 'on' not in 'python' and 'on' not in 'dragon')

#16. Find the length of the text python and convert the value to float and convert it to string
convert_to_float = float(len('python'))
convert_to_string = str(convert_to_float)
print(convert_to_string)
#metodo 2
print(str(float(len('python'))))

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input('Please, enter a num to validate if is even or no: '))
if num % 2 ==0:
    print(f'Number {num} is even')
else:
    print(f'Number {num} is not even')
    
#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7//3 == int(2.7))

#19. Check if type of '10' is equal to type of 10
a = '10'
b = 10
print(a == b)  

#20. Check if int('9.8') is equal to 10
a = int('9.8')
b = 10
print(a == b)  

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
try:
    hours = int(input('Please enter hours: '))
    rate_per_hour = float(input('Please value per hour: '))
    pay = hours * rate_per_hour
    print(f'Your pay is: ${pay}')
except (ValueError, TypeError):
    print('Value type no valid')
    print('Program finished')

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
number_years = int(input('Enter your lived years: '))
if number_years < 1:
    print('Please enter a number grather than 1')
else:    
    seconds_lived = number_years * 31536000
    print(f'You have lived for {seconds_lived} seconds')
    
#23. Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125

'''
#23. Write a Python script that displays the following table
for i in range(1,6): # imprime filas
    for j in range(1,6): # imprime columnas
        if(j == 2): 
            print(1, end = '   ') #la segunda columna es de 1
        elif(j == 3):
            print(i*1, end = '   ') #la tercera columna es la primera * 1
        elif(j == 4):
            print(i**2, end = '   ') #la cuarta columna es la primera al cuadrado
        elif(j == 5):
            print(i**3, end = '   ') #la quinta columna es la primera al cubo
        else:   
            print(i, end = '   ') #imprime cada fila con el valor que tenga i
    print('')#con esto deja un espacio cada que imprime una fila

