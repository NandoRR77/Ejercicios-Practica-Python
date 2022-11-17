#digitar caracter e identificar si es vocal o consonante

letra = input("Digite un caracter: ") .lower() #.lower() convierte la mayúscula en minúscula, esto porque las comparaciones están en minúscula, esto por si el usuario ingresa mayúsculas. Si comparo en mayusculas hago el upper()

if (letra == "a" or letra == "e" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print(f"El caracter {letra} es una vocal")
else:
    print(f"El caracter {letra} es una consonante")