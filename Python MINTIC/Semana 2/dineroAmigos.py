#Función dinero amigos

def funcionDineroAmigos(dineroGuillermo: float):
    dineroLuis = dineroGuillermo / 2
    dineroJuan = (dineroGuillermo + dineroLuis)/2
    dineroTotal = dineroGuillermo + dineroLuis + dineroJuan
    
    return "\nGuillermo tiene = ${}\nLuis tiene = ${}\nJuan tiene = ${}\n\nEl total del dinero es = ${}\n" .format(dineroGuillermo,dineroLuis,dineroJuan,dineroTotal)

dineroGuillermo = float(input("\nIngrese el dinero que tiene Guillermo:$"))
print(funcionDineroAmigos(dineroGuillermo))
