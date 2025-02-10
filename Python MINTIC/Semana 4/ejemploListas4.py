numeros = []

for i in range(6):
    numeros.append(int(input(f"Digite el número {i + 1} de la loterìa que desea comprar: ")))
    numeros.sort() #organiza los numeros de la lista numeros de menor a mayor
print(f"Los números comprados, ordenados de menor a mayor son: {numeros}")
numeros.reverse() #ordena los números de mayor a menor, ojo que primero hay que hacer el sort
# numeros.sort(reverse = True) esta instruccion aplica en una misma linea el ordenado asc y desc
print(f"Los números comprados, ordenados de mayor a menor son: {numeros}")