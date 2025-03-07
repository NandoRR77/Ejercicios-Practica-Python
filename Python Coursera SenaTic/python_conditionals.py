'''
Supongamos que quiere ofrecer un determinado descuento a los clientes si gastan más de $100. 
También proporcionará un descuento adicional si ese cliente forma parte de un programa de 
fidelización. Si el cliente no forma parte del programa de fidelización y no gastó más de $100, 
se aplica un cargo por servicio del 5 %.
'''

service = 0.05
discount1 = 0.05
discount2 = 0.10
gastado = float(input("Ingrese el valor gastado:"))
fidelizado = input("Hace parte del programa de fidelización? \nIngrese True o False: \n")
total = 0


if gastado <= 100 and fidelizado == "False":
    total = gastado + (gastado * service)
    print("El total a pagar es: " , total)
elif gastado <= 100 and fidelizado == "True":
    total = gastado - (gastado * discount1)
    print("El total a pagar es: " , total)
elif gastado > 100 and fidelizado == "True":
    total = gastado - (gastado * discount1)
    print("El total a pagar es: " , total)
else:
    total = gastado - (gastado * discount2)
    print("El total a pagar es: " , total)