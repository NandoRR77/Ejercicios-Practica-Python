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
 
diccionario = {"Cantidad":100, "Tipo":1, "Precio":3}

if diccionario["Tipo"] == 1:
    diccionario["Precio"] = 3
    monto = diccionario["Precio"]*diccionario["Cantidad"]
    if diccionario["Cantidad"] <= 5:
        descuento = monto - 0.5 #calculo el descuento del 0.5
        monto -= descuento #hago el descuento
    elif diccionario["Cantidad"] <= 10:
        descuento = monto * 0.07 #calculo el descuento del 7%
        monto -= descuento #hago el descuento

if diccionario["Tipo"] == 2:
    diccionario["Precio"] = 4
    monto = diccionario["Precio"]*diccionario["Cantidad"]
    if diccionario["Cantidad"] <= 7:
        monto = monto
    elif diccionario["Cantidad"] >= 7:
        descuento = monto * 0.05 #calculo el descuento del 5%
        monto -= descuento #hago el descuento
        
if diccionario["Tipo"] == 3:
    diccionario["Precio"] = 5
    monto = diccionario["Precio"]*diccionario["Cantidad"]
    if diccionario["Cantidad"] <= 7:
        monto = monto
    elif diccionario["Cantidad"] >= 4:
        descuento = monto * 0.15 #calculo el descuento del 15%
        monto -= descuento #hago el descuento
   