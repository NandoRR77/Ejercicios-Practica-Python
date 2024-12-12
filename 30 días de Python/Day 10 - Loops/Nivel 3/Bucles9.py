'''
Esta es una lista de frutas, ['banana', 'naranja', 'mango', 'limón'] invierte el orden usando un bucle.

#Solución no óptima
frutas = ['banana', 'naranja', 'mango', 'limón']
for fruta in range(1):
    print(f'Frutas en orden normal {frutas}')

for fruta in range(1):
    frutas.reverse()
    print(f'Frutas en orden normal {frutas}')
'''

frutas = ['banana', 'naranja', 'mango', 'limón']

print('Orden normal =>')
for fruta in frutas:
    print(fruta)
print(f'Lista frutas orden normal =>{frutas}')
   
print('\nOrden inverso =>')
tam = len(frutas)
frutas_inver = []

for i in range(tam-1,-1,-1):
    #print(frutas[i])
    frutas_inver.append(frutas[i])
print(f'Lista frutas invertidas =>{frutas_inver}')