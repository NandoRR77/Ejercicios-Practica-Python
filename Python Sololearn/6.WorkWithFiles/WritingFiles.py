file = open("/Users/nandoramirez/PythonMinTic/Ejercicios/Ejercicios-Practica-Python/Python Sololearn/6.WorkWithFiles/nando.txt" , "w") #tenemos que dar permisos de escritura con "w"
                                                #When a file is opened in write mode, the file's existing content is deleted.
file.write("Agregando nueva linea desde python. \n Esta será la segunda línea que agreguemos")
file.close()


#vamos a ver lo que le agregamos al archivo
file = open("/Users/nandoramirez/PythonMinTic/Ejercicios/Ejercicios-Practica-Python/Python Sololearn/6.WorkWithFiles/nando.txt" , "r")
print(file.read())
file.close()