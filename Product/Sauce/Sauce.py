from Product.Product import Product

class Sauce(Product):
    def __init__(self, description, cost):
        super().__init__(description, cost)