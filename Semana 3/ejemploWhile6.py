#Escribir dos contraseñas y comprobar que sean la misma

def main():
    print("CONFIRME SU CONTRASEÑA")
    password = input("Por favor ingrese su contraseña: ")
    password2 = input("Por favor repita su contraseña: ")
    
    while password != password2:
        print("Las contraseñas no coinciden")
        password = input("Por favor ingrese su contraseña: ")
        password2 = input("Por favor repita su contraseña: ")
    
    print("La contraseñas coinciden, se ha guardado ")
    
if __name__ == "__main__":
    main()