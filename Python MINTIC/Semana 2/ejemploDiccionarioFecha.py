''' 
Escribir un programa que pida la fecha en un formato dd/mm/aaa y muestre por pantalla la misma fecha 
pero en formato dd de <mes> de aaaa, donde <mes> es el nombre del mes'''

mesesDicc = {1:"enero", 2:"febrero" , 3:"marzo" , 4:"abril" , 5:"mayo" , 6:"junio" , 7:"julio" , 8:"agosto" , 9:"septiembre" , 10:"octubre" , 11:"noviembre" , 12:"diciembre" }
fecha = input("Por favor ingrese la fecha en formato dd/mm/aaaa: ")
fecha = fecha.split("/") #a la fecha capturada la separo por el simbolo /, como encontró 3 / entonces los separa y se numeran desde la posición 0,1,2
print("Corresponde al día",fecha[0] , "del mes de",mesesDicc[int(fecha[1])],"del año",fecha[2]) #diccMeses[int(fecha[1])] acá la posición 1 del split lo transforma en entero, luego ubique ese numero en el diccionario y devuelva el valor literal de ese numero
