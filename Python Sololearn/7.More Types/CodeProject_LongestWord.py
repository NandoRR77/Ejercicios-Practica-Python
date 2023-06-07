'''Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
'''

txt = input('Ingrese el texto: ')
words = txt.split(" ")

max = ""
for i in words:
    if len(max) > len(i):
        continue
    else:
        max = i

print(max)    
