class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} hisobiga {amount}  so'm qo'shildi. Sizning hisobingiz {self.balance} so'm")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} hisobidan {amount}  so'm yechildi! Balansingiz {self.balance} so'm")
        else:
            print(f"{self.owner},balansingizni to'ldiring!")
    def show_balance(self):
        print(f"{self.owner} hisobida {self.balance} so'm bor.")


account1 = BankAccount("Sevara", 20000000)
account2 = BankAccount("Sevinch", 10000000)
account3 = BankAccount("Farzona", 13000000)

account1.deposit(12000000)
account1.withdraw(1000000)

account2.deposit(9000000)
account2.withdraw(3000000)

account3.deposit(12000000)
account3.withdraw(8000000)

account1.show_balance()
account2.show_balance()
account3.show_balance()