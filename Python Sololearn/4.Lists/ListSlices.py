#List slices allow you to get a part of the list using two colon-separated indices. This returns a new list containing all the values between the indices.

print("ejemplo fragmentos de una lista")
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])


#If the first number in a slice is omitted, it’s taken to be the start of the list.

print("ejemplo omitiendo primer valor del list slide")
squares2 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares2[:7])


#If the second number is omitted, it’s taken to be the end.
print("ejemplo omitiendo segundo valor del list slide")
squares3 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares3[7:])

#Just like with ranges, your list slices can include a third number, representing the step, to include only alternate values in the slice. Like this:
print("ejemplo list slides con 3 argumentos")
squares4 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares4[::2])
print(squares4[2:8:3])

'''Negative values can also be used in list slicing (as well as normal list indexing). 
Which means that when negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list. Like this:'''
print("ejemplo list slides con indice negativo, imprimirá hasta la ultima posición -1, o sea el 64")
squares4 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares4[1:-1])

#imprimirá desde la posición 7 (49) hasta la 5+1 (36). En este caso 
print('#imprimirá desde la posición 7 (49) hasta la 5-1 (36). En este caso ')
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs)
print(sqs[7:5:-1])

#Using [::-1] as a slice is a common and idiomatic way to reverse a list.
nums = [5, 42, 7, 1, 0]
res = nums[::-1]
print(res)

names=[0,1,2,3,4]
print(names)
print(names[1:-1])
