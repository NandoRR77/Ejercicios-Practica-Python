#Saldo inicial $1000 
#Menú de Ingresar - retirar - Mostrar - Salir

saldoInicial = float(1000)
print("\t : Menú")
print("1 .:: Ingresar dinero a la cuenta   ::.")
print("2 .:: Retirar dinero de la cuenta   ::.")
print("3 .:: Mostrar saldo disponible      ::.")
print("4 .:: Salir                         ::.")
accion = int(input("Por favor digite la opción del menú: "))
print()

if accion == 1:
    ingreso = float(input("Indique la cantidad de dinero a ingresar = $"))
    saldoInicial += ingreso  # es lo mismo que poner saldoInicial = saldoInicial + ingreso 
    print(f"Ha realizado un ingreso de ${ingreso} .\nSu nuevo saldo es = ${saldoInicial} .")

elif accion == 2:
    egreso = float(input("Indique la cantidad de dinero a retirar = $"))
    if egreso > saldoInicial:
        print(f"El valor a retirar ${egreso} supera su saldo actual ${saldoInicial}")
    else:
        saldoInicial -= egreso
        print(f"Ha realizado un retiro de ${egreso} .\nSu nuevo saldo es = ${saldoInicial} .")

elif accion == 3:
    print(f"Su saldo actual es de = ${saldoInicial} .")

elif accion ==4:
    print(f"Ha seleccionado SALIR.\n¡Gracias por contar con nuestros servicios!")
    
else:
    print("ERROR: Opción seleccionada no válida")