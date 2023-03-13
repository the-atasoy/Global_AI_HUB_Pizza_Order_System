from Product.Product import Product

class Ingredient(Product):
    def __init__(self, description, cost):
        super().__init__(description, cost)