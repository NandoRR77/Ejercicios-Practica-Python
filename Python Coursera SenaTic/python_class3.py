class Payslips:
    def __init__(self, name, payment, amount):
        self.name = name
        self.payment = payment
        self.amount = amount
    
    def pay(self): #Método para pagarle al empleado
        self.payment = 'yes'
        
    def status(self): #Método para comprobar el estado del pago al empleado
        if self.payment == 'yes':
            return self.name + ' is paid: $' + str(self.amount)
        else:
            return self.name + ' is no paid yet '

#instancio 2 objetos
nando = Payslips('Fernando Ramirez','no',5400000)
camila = Payslips('Camila Ramirez', 'no', 8700000)

#Invoco el método que comprueba el estado
print('\nValidación:')
print(nando.status(), '\n', camila.status())


#realizo el pago a un empleado
camila.pay()

#Invoco nuevamente el método que comprueba el estado
print('\nActualización:')
print(nando.status(), '\n', camila.status())
