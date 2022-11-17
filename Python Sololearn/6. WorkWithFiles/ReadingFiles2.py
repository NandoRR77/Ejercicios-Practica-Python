file = open("./nando.txt", "r")
cont = file.read(4) #el 4 corresponde al número de bytes que imprimirá la instruccion
cont = file.read(16)
cont = file.read() #aunque acá no pasamos el número de bytes que debería imprimir, como quedó al final de las lecturas anteriores, 
                    #solo escribe los bytes restantes luego de las lecturas anteriores
print(cont)
file.close()