from Product.Drink.SubDrink import Coke
from Product.Drink.SuperDrink import Drink
from Product.Pizza.SubPizza import Classic
from Product.Product import Product


class Main:
    a = Classic("Classic Pizza", 3)

    print(a.get_cost())

    b = Coke("drink", 44)

    b.set_cost(55)
    print(b.get_cost())
    a=1

# try 222