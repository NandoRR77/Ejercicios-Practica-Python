'''
Declara una función llamada reverse_list. 
Toma una matriz como parámetro y devuelve el inverso de la matriz (usa bucles).
'''

def reverse_list(list):

    reverse_list1 = []
    
    for i in range(len(list)-1,-1,-1):
        reverse_list1.append(list[i])       
    return reverse_list1

print(reverse_list(['a','b','c']))