# Exercise: Demonstrate encapsulation using a BankAccount class.
# Create a BankAccount class with a private attribute __balance.
# Implement deposit() method that adds money with validation (amount must be positive).
# Implement withdraw() method that subtracts money with validation
# (amount must be positive and not exceed current balance).
# Implement get_balance() method to safely access the private balance.
# Test all methods and try to access __balance directly to see encapsulation in action.

# Exercise: Demonstrate encapsulation using a BankAccount class.
# Create a BankAccount class with a private attribute __balance.
# Implement deposit() method that adds money with validation (amount must be positive).
# Implement withdraw() method that subtracts money with validation
# (amount must be positive and not exceed current balance).
# Implement get_balance() method to safely access the private balance.
# Test all methods and try to access __balance directly to see encapsulation in action.

class BankAccount: # class with a private attribute to demonstrate encapsulation
    def __init__(self, balance): # initialize account with starting balance
        self.__balance = balance # private attribute — not accessible from outside the class

    def deposit(self, amount): # controlled method to add funds
        if amount > 0:
            self.__balance += amount # modify private attribute from inside the class
        else:
            print("Error: deposit amount must be positive")

    def withdraw(self, amount): # controlled method to subtract funds
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount # modify private attribute from inside the class
        elif amount > self.__balance:
            print("Declined: insufficient balance")
        else:
            print("Error: withdraw amount must be positive")

    def get_balance(self): # getter — safe way to read the private attribute
        print(f"Balance: {self.__balance}")


account = BankAccount(100) # instantiate object with balance of 100
account.get_balance()
account.deposit(0)         # invalid — triggers error
account.get_balance()
account.deposit(50)        # valid — balance becomes 150
account.get_balance()
account.withdraw(0)        # invalid — triggers error
account.get_balance()
account.withdraw(50)       # valid — balance becomes 100
account.get_balance()
account.withdraw(150)      # invalid — insufficient balance
account.get_balance()
print(account.__balance)   # AttributeError — private attribute not accessible from outside