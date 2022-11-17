#El método de escritura devuelve el número de bytes escritos en un archivo, si tiene éxito.
nuevo_mensaje = "Hola mundo inmundo" #almacenamos lo que vamos a agregar en una variable
file = open("/Users/nandoramirez/PythonMinTic/Ejercicios/Ejercicios-Practica-Python/Python Sololearn/6.WorkWithFiles/nando.txt" , "w") 
cantidad_escrita = file.write(nuevo_mensaje) #creamos una variable para contar los bytes que hemos introducido
print(f"Se ha ingresado un texto con {cantidad_escrita} caracteres")     #imprimimos la variable
file.close
