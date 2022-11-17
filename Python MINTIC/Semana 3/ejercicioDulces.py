''' Una empresa ha decidido asignarle la tarea de desarrollar  un programa que permita gestionar la venta de dulces.
Se le pide ingresar la siguiente información: cantidad de dulces a comprar, el tipo de dulce (1,2 o 3) y muestre
como salida el tipo de dulce, el precio unitario, la cantidad y el monto de la venta, teniendo en cuenta la siguiente política de descuento

Tipo dulce 1:   precio unitario $3
                hasta 5 dulces $0.5 de descuento
                de 5 hasta 10 7% de descuento
                
Tipo dulce 2:   precio unitario $4
                hasta 7 dulces sin descuento
                mas de 7 5% de descuento
                
Tipo dulce 3:   precio unitario $5
                1 a 4 sin descuento
                Mas de 4 15%
 '''
tipo = int(input("Ingrese el tipo de dulces a comprar (1 - 2 - 3 ): "))
if tipo > 3:
    print("Tipo de dulce no disponible")
else:
    cant = int(input("Ingrese la cantidad de dulces a comprar: "))
    
    dulceria = {"Cantidad":cant, "Tipo":tipo, "Precio":0, "Monto":0}

    if dulceria["Tipo"] == 1:
        dulceria["Precio"] = 3
        dulceria["Monto"] = dulceria["Precio"]*dulceria["Cantidad"]
        
        if dulceria["Cantidad"] <= 5:
            descuento = dulceria["Monto"] - 0.5 #calculo el descuento del 0.5
            dulceria["Monto"] -= descuento #hago el descuento
        elif dulceria["Cantidad"] <= 10:
            descuento = dulceria["Monto"] * 0.07 #calculo el descuento del 7%
            dulceria["Monto"] -= descuento #hago el descuento

    elif dulceria["Tipo"] == 2:
        dulceria["Precio"] = 4
        dulceria["Monto"] = dulceria["Precio"]*dulceria["Cantidad"]
        if dulceria["Cantidad"] > 7:
            descuento = dulceria["Monto"] * 0.05 #calculo el descuento del 5%
            dulceria["Monto"] -= descuento #hago el descuento
            
    elif dulceria["Tipo"] == 3:
        dulceria["Precio"] = 5
        dulceria["Monto"] = dulceria["Precio"]*dulceria["Cantidad"]
        if dulceria["Cantidad"] > 4:
            descuento = dulceria["Monto"] * 0.15 #calculo el descuento del 15%
            dulceria["Monto"] -= descuento #hago el descuento

    print("El tipo de dulce: ", dulceria["Tipo"], 
        "\ntiene un costo unitario de: $" , dulceria["Precio"],
        "\ny usted compró un total de: " , dulceria["Cantidad"], 
        "\npor un valor de: $", dulceria["Monto"])