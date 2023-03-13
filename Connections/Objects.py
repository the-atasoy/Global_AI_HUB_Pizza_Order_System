# Objects are created in this file using datas in database via files "Costs.py" and "Descriptions.py".

from Connections.Costs import *
from Connections.Descriptions import *

from Product.Beverage.Beverage import Beverage
from Product.Ingredient.Ingredient import Ingredient
from Product.Pizza.Pizza import Pizza
from Product.Sauce.Sauce import Sauce

# Pizza objects
dominos = Pizza(Descriptions.dominos_description(), Costs.dominos_cost())
turk = Pizza(Descriptions.turk_description(), Costs.turk_cost())
margherita = Pizza(Descriptions.margherita_description(), Costs.margherita_cost())
classic = Pizza(Descriptions.classic_description(), Costs.classic_cost())

# Ingredient objects
olive = Ingredient(Descriptions.olive_description(), Costs.olive_cost())
mushroom = Ingredient(Descriptions.mushroom_description(), Costs.mushroom_cost())
goat_cheese = Ingredient(Descriptions.goat_cheese_description(), Costs.goat_cheese_cost())
meat = Ingredient(Descriptions.meat_description(), Costs.meat_cost())
onion = Ingredient(Descriptions.onion_description(), Costs.onion_cost())
corn = Ingredient(Descriptions.corn_description(), Costs.corn_cost())

# Sauce objects
ketchup = Sauce(Descriptions.ketchup_description(), Costs.ketchup_cost())
mayo = Sauce(Descriptions.mayo_description(), Costs.mayo_cost())
mustard = Sauce(Descriptions.mustard_description(), Costs.mustard_cost())
bbq = Sauce(Descriptions.bbq_description(), Costs.bbq_cost())
hot_sauce = Sauce(Descriptions.hot_sauce_description(), Costs.hot_sauce_cost())
ranch = Sauce(Descriptions.ranch_description(), Costs.ranch_cost())

# Beverage objects
coke = Beverage(Descriptions.coke_description(), Costs.coke_cost())
fanta = Beverage(Descriptions.fanta_description(), Costs.fanta_cost())
pop_soda = Beverage(Descriptions.pop_soda_description(), Costs.pop_soda_cost())
lemonade = Beverage(Descriptions.lemonade_description(), Costs.lemonade_cost())
ayran = Beverage(Descriptions.ayran_description(), Costs.ayran_cost())
