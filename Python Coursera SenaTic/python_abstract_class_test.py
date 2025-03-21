# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):
    ### YOUR CODE HERE
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"
    
    @abstractmethod
    def withdraw(self, cantidad):
        pass

# Class Swiss
class Swiss(Bank):
    """ A specific type of bank than derives from class Bank

    [IMPLEMENT ME]
        1. This class must derive from class Bank
        2. Create a constructor for this class that initializes a class
           variable `bal` to 1000
        3. Implement the basicinfo() function so that it prints "This is the 
           Swiss Bank" and returns a string with "Swiss Bank: " (don't forget
           the space after the colon) followed by the current bank balance.

           For example, if self.bal = 80, then it would return "Swiss Bank: 80"

        4. Implement withdraw so that it takes one argument (in addition to
           self) that is an integer which represents the amount to be withdrawn
           from the bank. Deduct the withdrawn amount from the bank bal, print 
           the withdrawn amount ("Withdrawn amount: {amount}"), print the new
           balance ("New Balance: {self.bal}"), and return the new balance.

           Note: Make sure to verify that there is enough money to withdraw!  
                 If amount is greater than balance, then do not deduct any 
                 money from the class variable `bal`. Instead, print a 
                 statement saying `"Insufficient funds"`, and return the 
                 original account balance instead.
    """
    ### YOUR CODE HERE
    def __init__(self):
        self.bal = 1000
    
    def basicinfo(self):
        print("This is the Swiss Bank: ")
        return f"Swiss Bank: {self.bal}"
    
    def withdraw(self, cantidad):
        if cantidad > self.bal:
            print("Fondos insuficientes")
        else:        
            self.bal -= cantidad
            print(f"Withdrawn amount: {cantidad}")
        print(f"New balance: {self.bal}")
        return self.bal
         


# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()