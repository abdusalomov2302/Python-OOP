class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

product1 = Product("Telefon", 1200000, "electronics", True)
product2 = Product("Komyuter", 1300000, "electronics", False)

print(f"Mahsulot nomi: {product1.name}, Maxsulot narxi: {product1.price}, Mahsulot turi: {product1.category}, Mahsulot omborda bormi yo'qmi: {product1.in_stock}")
print(f"Mahsulot nomi: {product2.name}, Maxsulot narxi: {product2.price}, Mahsulot turi: {product2.category}, Mahsulot omborda bormi yo'qmi: {product2.in_stock}")