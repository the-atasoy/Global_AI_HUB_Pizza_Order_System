from Product.Product import Product

class Beverage(Product):
    def __init__(self, description, cost):
        super().__init__(description, cost)