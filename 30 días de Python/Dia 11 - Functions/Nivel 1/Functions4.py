'''
La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. 
Escriba una función que convierta °C a °F, convert_celsius_to-fahrenheit .
'''

def f_convert_celsius_to_fahrenheit(x):
    grades_f = (x * 9/5) + 32
    return grades_f
print(f_convert_celsius_to_fahrenheit(35))