
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


car = Car("BMW", "X5", 2022)

print(car.brand)
print(car.model)
print(car.year)