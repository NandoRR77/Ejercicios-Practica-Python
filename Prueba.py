razon_social_bd = 'BELTRAN BENAVIDES MARTHA GUILLERMINA'
Primer_Apellido = 'BELTRAN'
Segundo_Apellido = 'BENAVIDES'
Primer_Nombre = 'MARTHA'
Segundo_Nombre = 'GUILLERMINA'

for i in range (3):
    if Primer_Apellido in razon_social_bd:
        print(f'{Primer_Apellido} encontrado en {razon_social_bd}')
        if Segundo_Apellido in razon_social_bd:
           print(f'{Segundo_Apellido} encontrado en {razon_social_bd}')
        else:
            print(f'{Segundo_Apellido} no encontrado en {razon_social_bd}')
    if Primer_Nombre in razon_social_bd:
            print(f'{Primer_Nombre} encontrado en {razon_social_bd}')
    else:
        print(f'{Primer_Nombre} no encontrado en {razon_social_bd}')  
        if Segundo_Nombre in razon_social_bd:
            print(f'{Segundo_Nombre} encontrado en {razon_social_bd}')
        else:
            print(f'{Primer_Nombre} no encontrado en {razon_social_bd}')  