a = {1,2,3}
b = {3,4,5}

#imprime la comparación entre a y b e imprime true or false
print(a == b)

#unión de conjuntos imprime los elementos que no esten repetidos
c = a | b
print(c)

#intersección de conjuntos imprime elementos comunes entre ambos conjuntos
c = a & b
print(c)

#diferencia de conjuntos
c = a - b #los que estàn en A y no en B
print(c)

c = b - a #los que estàn en B y no en A
print(c)

#diferencia simetrica de conjuntos (la suma de A y B menos la interseccion de A y B)
c = b ^ a
print(c)