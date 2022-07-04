frutas = ("naranja","pera","kiwi","mango","banano") #Las tuplas se forman con () y despues de creadas no se pueden modificar, solo crar y leer
print(frutas)

#dimension de una tupla
print(len(frutas))

#acceder a un elemento de una tupla
print(frutas[2])

#navegacion inversa de una tupla
print(frutas[-2])

#modificar elemento de una tupla (no permitido)
#frutas[0] = "patilla"

#para modificar una tupla se tiene que convertir en lista, se modifica y luego se vuelve a convertir en tupla
frutaslista = list(frutas) #se convierte a lista
frutaslista[0]="patilla" #se cambia el elemento
frutas = tuple(frutaslista) #se convierte a tupla 
print(frutas)

#iterar con una tupla
for fruta in frutas:
    print(fruta, end=" - ") #se imprime el valor de fruta en forma horizontal y separado por guion y espacio