'''
1. Check the data type of all your variables using type() built-in function
2. Using the len() built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4 .Declare 5 as num_one and 4 as num_two
    a. Add num_one and num_two and assign the value to a variable total
    b. Subtract num_two from num_one and assign the value to a variable diff
    c. Multiply num_two and num_one and assign the value to a variable product
    d. Divide num_one by num_two and assign the value to a variable division
    e. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    f. Calculate num_one to the power of num_two and assign the value to a variable exp
    g. Find floor division of num_one by num_two and assign the value to a variable floor_division
5. The radius of a circle is 30 meters.
    a. Calculate the area of a circle and assign the value to a variable name of area_of_circle
    b. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    c. Take radius as user input and calculate the area.
6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords'''

#1
first_name = 'Fernando'
last_name = 'Ramirez'
full_name = 'Fernando Ramirez'
country = 'Colombia'
city = 'Bello'
age = 39
year = 1983
is_married = True
is_true = False
is_light_on = True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#2
print(len(first_name))

#3
print(len(first_name) == len(last_name))

#4
num_one = 4
num_two = 5

#Add
total = print(num_one + num_two)

#substraction
diff = print(num_one - num_two)

#multiplication
product = print(num_one * num_two)

#division
division = print(num_one / num_two)

#remainder
remainder = print(num_two % num_one)

#power
exp = print(num_one ** num_two)

#floor_division
floor_division = print(num_one // num_two)

#5. 
#a. Area
radius = 30
pi = 3.14159265359
area_of_circle = round(pi*(radius ** 2),3)
print("El área del circulo es: " , area_of_circle)

#b. circum of circle
circum_of_circle = round((2 * pi * radius),3)
print("La circunferencia del circulo es: " , circum_of_circle)

#c. 
radius = float(input("Ingrese el radio: "))

#6
first_name = input("Ingrese su primer nombre: ")
last_name = input("Ingrese su apellido: ")
country = input("Ingrese su país de nacimiento: ")
age = int(input("Ingrese su edad: "))

print("Su nombre es: ", first_name, "y su apellido es ", last_name, ".\nUsted vive en ", country, "y tiene ", age, "años.")