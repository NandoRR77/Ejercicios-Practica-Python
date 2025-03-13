#Agregue la gestión de excepciones para evitar que se produzca el error y 
# se devuelva un mensaje más sencillo para el usuario, como "El elemento no existe en la lista".

# Starter code - Logrado
items = [1,2,3,4,5]

try:
    item = items[6]
except:
    print("El elemento no existe en la lista")
    
    
'''
Solución plataforma

try:
    item = items[6]
    print(item)
except: 
    print("The index does not exist in the list.")
'''