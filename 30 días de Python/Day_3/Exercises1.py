#1. Declare your age as integer variable
age = 39

#2. Declare your height as a float variable
height = 1.78

#3 Declare a variable that store a complex number
a = (1 +1j)

''' 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100 '''
base = float(input("Please enter the triangle base: "))
height2 = float(input("Please enter the triangle height: "))
area = 0.5 * (base * height2)
print(f"The triangle area is {area}")
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

''' 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12'''

a = float(input('Please enter a valur for side a: '))
b = float(input('Please enter a valur for side b: '))
c = float(input('Please enter a valur for side c: '))
perimeter = a + b + c
print(f'The perimeter of triangle is {perimeter}')
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

'''6. Get length and width of a rectangle using prompt. 
Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))'''
length = int(input('Please enter length for a rectangule: '))
width = int(input('Please enter width for a rectangule: '))
area_triangle = length * width
perimeter_rectangle = 2 * (length + width)
print(f'The area of rectangle is {area_triangle} and its perimeter is {perimeter_rectangle}')
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

'''7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.'''
radius = float(input('Please enter de radius for circle: '))
pi = 3.14
area_of_circle = pi*(radius ** 2)
circum_of_circle = (2 * pi * radius)
print(f'The area of circle is {area_of_circle} and its circunference is {circum_of_circle}')
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')


