class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f"{self.name} - {self.price} so'm")


product1 = Product("Telefon", 3500000, "Elektronika")
product2 = Product("Noutbuk", 8500000, "Elektronika")
product3 = Product("Smart-soat", 1200000, "Aksessuar")
product4 = Product("Televizor", 5000000, "Maishiy texnika")
product5 = Product("Kiryuvish mashinasi", 6000000, "Maishiy texnika")
product6 = Product("Naushnik", 400000, "Aksessuar")

products = [product1, product2, product3, product4, product5, product6]

expensive = max(products, key=lambda p: p.price)

print("Eng qimmat mahsulot:")
expensive.info()