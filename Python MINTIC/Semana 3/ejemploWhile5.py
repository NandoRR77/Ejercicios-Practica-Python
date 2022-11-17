variable  = 10
while variable > 0:
    variable -=1
    if variable == 5:
        continue # continue salta al while, omite el print
    print("Actual valor de la variable: ", variable)