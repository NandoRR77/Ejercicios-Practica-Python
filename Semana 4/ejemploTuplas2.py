''' Almacenar en una lista, 5 tuplas que serán el paìs y su cantidad de habitantes. 
se deben crear tres funciones:
1. Cargar datos a la lista
2. Imprimir la lista
3. Ordenar la lista por cantidad de habitantes
'''

def cargarPaises(): #función para cargar los datos de los países
    paises = []
    for x in range(5):
        nombre = input(f"Por favor digite el nombre del país #{x + 1}: ")
        cant = int(input(f"Por favor ingrese la cantidad de habitantes del país #{x + 1}: "))
        paises.append((nombre,cant)) #con poner en () las variables, estoy convirtiendo esos elementos en una tupla
    return paises

def imprimir(paises):
    print("Los paises y su población son: ")
    for x in range(0, len(paises)): #recorro desde la posición 0 hasta la longitud de la lista paises
        print(paises[x][0], paises[x][1]) #imprimo el primer y segundo valor de cada tupla almacenado en cada posición de la lista
        
def paisMasPoblado(paises):
    pos = 0
    for x in range(0,len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print(f"el país con mayor cantidad de habitantes es: {paises[pos][0]} con {paises[pos][1]}")
    
paises = cargarPaises()
imprimir(paises)
paisMasPoblado(paises)