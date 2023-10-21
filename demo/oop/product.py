class Product:
    # class attribute or static attribute
    taxrate = 15

    def __init__(self, name, price=0):
        self.name = name
        self.price = price

    def getNetPrice(self):
        return self.price + self.price * Product.taxrate / 100

    @staticmethod   # decorator
    def getTaxrate():
        return  Product.taxrate


p1 = Product("iPhone 15", 100000)
print(p1.getNetPrice())
print(Product.getTaxrate())