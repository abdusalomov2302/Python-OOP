class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def check_stock(self):
        if self.in_stock:
            print(f"{self.name} omborda mavjud ✅")

        else:
            print(f"{self.name} hozirda tugagan ❌")



product1 = Product("Telefon", 1200000, "electronics", True)
product1.check_stock()

print()

product2 = Product("Kompyuter", 1300000, "electronics", False)
product2.check_stock()