'''
with open('NewFile.txt', 'w') as file:
    #file.write('This is a new file created') #crea una sola linea en el nuevo archivo
    file.writelines(['This is a new file created', '\nThis is another line in the same file']) #writelines agrega mas lineas al archivo en formato lista
'''    

try:
    with open('Nando/NewFile.txt', 'a') as file: #a agrega las lineas al mismo archivo las veces que se ejecute
        file.writelines(['\nThis is a new file created', '\nThis is another line in the same file']) #writelines agrega mas lineas al archivo en formato lista
except FileNotFoundError as e:
    print('Error!', e)