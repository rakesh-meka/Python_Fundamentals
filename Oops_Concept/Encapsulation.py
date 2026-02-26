class BankAccount:
    def __init__(self, name, balance):
        self.name = name              # Public variable
        self._account_type = "Savings" # Protected variable
        self.__balance = balance       # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Object creation
account = BankAccount("Rakesh", 5000)

account.deposit(2000)
print(account.name)                 # Accessible
print(account.get_balance())        # Access private data via method

# print(account.__balance)          # ❌ Error: Private variable not accessible