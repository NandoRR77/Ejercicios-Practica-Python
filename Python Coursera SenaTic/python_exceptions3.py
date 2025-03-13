FileNotFoundError

#El código siguiente busca un archivo que no existe. 
# Agregue la gestión de excepciones para detectar este error 
# y devolver el siguiente mensaje "No se pudo encontrar el archivo".

# Starter code - LOGRADO

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("No se pudo encontrar el archivo")


'''
Solución plataforma
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("Unable to locate file")  
'''