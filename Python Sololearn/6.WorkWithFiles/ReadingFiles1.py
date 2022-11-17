file = open("nando.txt","r")
a = file.read() #guardamos todo el contenido del archivo en una variable
print("el archivo nando.txt tiene",len(a), "caracteres")
file.close()