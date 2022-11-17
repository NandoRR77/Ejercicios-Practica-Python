file = open("/Users/nandoramirez/PythonMinTic/Ejercicios/Ejercicios-Practica-Python/Python Sololearn/6.WorkWithFiles/nando.txt","r")
a = file.read() #guardamos todo el contenido del archivo en una variable
print("el archivo nando.txt tiene",len(a), "caracteres")
file.close()