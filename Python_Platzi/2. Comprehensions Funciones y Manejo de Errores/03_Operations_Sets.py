set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

#Unión (todos sin repetidos)
set_c = set_a.union(set_b) #Unión a con b
print(set_c)
print(set_a | set_b) #Unión de a con b con operador |

#Intersección (sólo los comunes)
set_c = set_a.intersection(set_b) #Intersección a con b
print(set_c)
print(set_a & set_b) #Intersección de a con b con operador &

#Diferencia (Deja los elementos del primer conjunto - los elementos del segundo sin mostrar tampoco repetidos)
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b) #Set a - elementos de b

#Diferencia simétrica (unión sin los elementos en común)
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)