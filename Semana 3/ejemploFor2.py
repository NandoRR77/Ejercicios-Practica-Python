#tabla de multiplicar

respuesta = input("Digite S para si imprimir una tabla de multiplicar: ")
while respuesta == "s":
    numero = int(input("Por favor digite un número, se mostrará su tabla de multiplicar: "))

    for i in range (1,11): # el rango indica en que valor empieza la variable i y en cual valor termina, en este caso en 10
        resultado = i * numero
        print(f"{numero} X {i} = {resultado}")
    respuesta = input("Quiere imprimir otra tabla? Digite S para si: ")
    
print("Ha finalizado la sesión")