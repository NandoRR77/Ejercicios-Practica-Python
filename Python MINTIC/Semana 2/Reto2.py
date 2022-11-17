id = int(input("Ingrese el ID del cliente: "))
nombre = str(input("Ingrese el nombre: "))
edad = int(input("Ingrese la edad: "))
primerIgreso = str(input("Si es primer ingreso digite S, sino N : ")) .upper()
informacion = {"idCliente":id , "nombre":nombre , "edad":edad , "primerIngreso":primerIgreso}

def validaCliente (informacion:dict)-> dict :
    dictResultado = {"nombre":informacion["nombre"], "edad":informacion["edad"],"atraccion" : "", "apto": False, "primeringreso":informacion["primerIngreso"], "totalBoleta":""}
           
    if (informacion["edad"] >= 7 and informacion["edad"] <15):         
        dictResultado["atraccion"] = "Sillas Voladoras"
        dictResultado["totalBoleta"] = 10000
        dictResultado["apto"] = True
        if (informacion["primerIngreso"] == "S"):
            descuento = dictResultado["totalBoleta"] * 0.05
            dictResultado["totalBoleta"] -= descuento
            dictResultado["primeringreso"] = True
        else: 
            dictResultado["primeringreso"] = False
    elif (informacion["edad"] >= 15 and informacion["edad"] <18):
        dictResultado["atraccion"] = "Carroschocones"
        dictResultado["totalBoleta"] = 5000
        dictResultado["apto"] = True
        if (informacion["primerIngreso"] == "S"):
            descuento = dictResultado["totalBoleta"] * 0.07
            dictResultado["totalBoleta"] -= descuento
            dictResultado["primeringreso"] = True
        else: 
            dictResultado["primeringreso"] = False
    
    elif informacion["edad"] > 18:
        dictResultado["atraccion"] = "X-Treme"
        dictResultado["totalBoleta"] = 20000
        dictResultado["apto"] = True
        if (informacion["primerIngreso"] == "S"):
            descuento = dictResultado["totalBoleta"] * 0.05
            dictResultado["totalBoleta"] -= descuento
            dictResultado["primeringreso"] = True
        else: 
            dictResultado["primeringreso"] = False
    else:
        dictResultado["atraccion"] = "N/A"
        dictResultado["totalBoleta"] = "N/A"
        if (informacion["primerIngreso"] == "S"):
            dictResultado["primeringreso"] = True
        else: 
            dictResultado["primeringreso"] = False

    return dictResultado
print(validaCliente(informacion))