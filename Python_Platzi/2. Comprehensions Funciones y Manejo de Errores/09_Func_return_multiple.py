def find_volume(length=1, width=1, depth=1): #Le defino valores por defecto si no me envían parámetros
    return length * width * depth, width, 'hola' #Al separar con comas, devuelvo multiples valores en una tupla

result = find_volume(10,20,3)

print(result) #Imprimir todo lo que retorna la funcon
print(result[0]) #imprimir solo el cálculo, la posición de la tupla