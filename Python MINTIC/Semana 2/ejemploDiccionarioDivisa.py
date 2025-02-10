''' Ejercicio 1: escribir un programa que guarde en una variable el diccionario 
{"Euro" : "€" , "Dollar": "$" , "Yen":"￥"}, 
pregunte al usuario por una divisa y muestre su símbolo
o un mensaje de aviso si la divisa no está en el diccionario '''

from tokenize import PseudoExtras


divisas = {"Euro":"€" , "Dollar":"$" , "Yen":"￥"} #el nombre de la clave siempre empieza por Mayuscula cuando es texto, no espacios entre clave:valor

opcionUsuario = input("Por favor ingrese una divisa: ")

if opcionUsuario.title() in divisas:                     # .tittle() captura si es mayúscula o minúscula lo ingresado y devuelve el resultado
    print(divisas[opcionUsuario.title()]) 
else:
    print("La divisa no se encuentra registrada")
    print(f"Las divisas registradas son  {divisas}") 
        

