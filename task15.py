class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock


product1 = Product("Non", 3_000, True)
product2 = Product("Sut", 8_000, False)
product3 = Product("Yog'", 18_000, True)
product4 = Product("Un", 12_500, True)
product5 = Product("Tuz", 1_500, False)

products = [product1, product2, product3, product4, product5]

prices = sum(p.price for p in products if p.in_stock)

print(f"Ombordagi mahsulotlar narxi: {prices} so'm")