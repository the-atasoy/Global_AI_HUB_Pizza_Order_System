from abc import ABC, abstractmethod
from Product.Product import Product

class Drink(Product, ABC):
    @abstractmethod
    def __init__(self, description, cost):
        super().__init__(description, cost)