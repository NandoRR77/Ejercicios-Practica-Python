import random

try:
    f = open("/Users/nandoramirez/Desktop/Ejercicios-Practica-Python/Python Coursera SenaTic/petnames.txt", "r")
    f_content = f.read()
    f_content_list = f_content.split("\n")
    print(random.choice(f_content_list))
except FileNotFoundError as e:
    print('ERROR' , e)
    
    
#Opción para que el usuario digite el nombre del archivo
import random
f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))
