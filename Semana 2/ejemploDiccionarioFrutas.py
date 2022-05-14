''' 
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un numero de kilos y muestre por pantalla el precio de ese numero de kilos de fruta
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello '''

frutasDicc = {"Guanabana":10.3 , "Mango":30.2 , "Banano":20.3 , "Naranja":5.5 }
fruta = input("¿Qué fruta desea comprar? : ") .title()
kilos = float(input("¿Cuántos kilos de fruta desea comprar? : "))

if fruta in frutasDicc:
   print(f"Para la fruta {fruta} el valor de {kilos} kilos es de: $" , frutasDicc[fruta]*kilos )
else:
    print(f"La fruta {fruta} no está registrada")