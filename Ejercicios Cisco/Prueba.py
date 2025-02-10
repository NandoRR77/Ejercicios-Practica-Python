var = 0
while var < 6:
    var += 1
    if var % 2 ==0:
        continue
    print("#")
    
    
lista = [1, 2, 3]
for v in range (len(lista)):
    lista.insert(1,lista[v])
print(lista)


vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

t = [[3-i for i in range (3)] for j in range (3)]
s= 0
for i in range(3):
    s+= t[i][i]
print(s)

