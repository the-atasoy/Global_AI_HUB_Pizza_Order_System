from Product.Product import Product
class Pizza(Product):
    def __init__(self, description, cost):
        super().__init__(description, cost)

    