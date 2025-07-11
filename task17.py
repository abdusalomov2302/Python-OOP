class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner} balansi: {self.balance} so'm")

    def get_balance(self):
        return self.balance


account1 = BankAccount("Sevara", 1500000)
account2 = BankAccount("Ali", 2300000)
account3 = BankAccount("Laylo", 1850000)
account4 = BankAccount("Javohir", 1200000)
account5 = BankAccount("Dilnoza", 950000)

accounts = [account1, account2, account3, account4, account5]

balance = 0
for account in accounts:
    balance += account.get_balance()

print(f"Bankdagi jami balans: {balance} so'm")