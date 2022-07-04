#Solución Reto Semana 1
usuario = str(input("\nPor favor ingrese su usuario: "))
capital = float(input("\nPor favor ingrese el capital aportado: $"))
tiempo = float(input("\nPor favor ingrese el tiempo transcurrido: "))

#Funcion Interes Ganado
def funcionTotalGanado(usuario: str, capital: float, tiempo: int):
    interesGanado = (capital * 0.03 * tiempo)/12
    valorTotal = interesGanado + capital
    return "\nPara el usuario {} la cantidad de dinero a recibir, según el capital inicial de ${} para un tiempo de {} meses es: {}\n" .format(usuario,capital,tiempo,valorTotal)

#Funcion Interes Perdido
def funcionTotalPerdido(usuario: str, capital: float, tiempo: int):
    interesPerdido = (capital * 0.02)
    valorTotal = capital - interesPerdido
    return "\nPara el usuario {} la cantidad de dinero a recibir, según el capital inicial de ${} para un tiempo de {} meses es: {}\n" .format(usuario,capital,tiempo,valorTotal)

#Valida el tiempo para saber cuál de los dois caminos tomar
if (tiempo<=2):
    print(funcionTotalPerdido(usuario,capital,tiempo))
else:
    print(funcionTotalGanado(usuario,capital,tiempo))

