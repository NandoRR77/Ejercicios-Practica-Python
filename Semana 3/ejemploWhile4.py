variable = 10

while variable > 0:
    print("El actual valor de la variable", variable)
    variable -= 1
    if variable == 5:
        print("La variable ha llegado a ", variable, "y se rompe el ciclo")
        break