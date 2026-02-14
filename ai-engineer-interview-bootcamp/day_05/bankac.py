class BankAccount:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"deposit {amount} to {self.owner_name}'s account")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Not enough money!")

    def get_balance(self):
        return self.balance

account = BankAccount("Jack")
account.deposit(1000)
account.withdraw(502)
print(f"Account balance: {account.get_balance()}")