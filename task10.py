class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Hisob to'ldirildi. Balansingiz {self.balance} so'm")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Pul yechildi! Balansingiz {self.balance} so'm")
        else:
            print("Mablag' yetarli emas. Hisobingizni to'ldiring!")

account = BankAccount("Sevara", 15000000)

account.deposit(10000000)

account.withdraw(7000000)
account.withdraw(2000000)