from abc import ABC, abstractmethod
class Product(ABC):
    @abstractmethod
    def __init__(self, description, cost):
        self.__description = description
        self.__cost = cost

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        self.__cost = cost
