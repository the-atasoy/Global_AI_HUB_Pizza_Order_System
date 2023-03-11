from Connections.Costs import *
from Connections.Descriptions import *

from Product.Drink.SubDrink import *
from Product.Ingredient.SubIngredient import *
from Product.Pizza.SubPizza import *
from Product.Sauce.SubSauce import *

# pizza objects
dominos = Dominos(Descriptions.dominos_description(), Costs.dominos_cost())
turk = Turk(Descriptions.turk_description(), Costs.turk_cost())
margherita = Margherita(Descriptions.margherita_description(), Costs.margherita_cost())
classic = Classic(Descriptions.classic_description(), Costs.classic_cost())

# ingredient objects
olive = Olive(Descriptions.olive_description(), Costs.olive_cost())
mushroom = Mushroom(Descriptions.mushroom_description(), Costs.mushroom_cost())
goat_cheese = GoatCheese(Descriptions.goat_cheese_description(), Costs.goat_cheese_cost())
meat = Meat(Descriptions.meat_description(), Costs.meat_cost())
onion = Onion(Descriptions.onion_description(), Costs.onion_cost())
corn = Corn(Descriptions.corn_description(), Costs.corn_cost())

# sauce objects
ketchup = Ketchup(Descriptions.ketchup_description(), Costs.ketchup_cost())
mayo = Mayo(Descriptions.mayo_description(), Costs.mayo_cost())
mustard = Mustard(Descriptions.mustard_description(), Costs.mustard_cost())
bbq = BBQ(Descriptions.bbq_description(), Costs.bbq_cost())
hot_sauce = Hot(Descriptions.hot_sauce_description(), Costs.hot_sauce_cost())
ranch = Ranch(Descriptions.ranch_description(), Costs.ranch_cost())

# drink objects
coke = Coke(Descriptions.coke_description(), Costs.coke_cost())
fanta = Fanta(Descriptions.fanta_description(), Costs.fanta_cost())
pop_soda = SodaPop(Descriptions.pop_soda_description(), Costs.pop_soda_cost())
lemonade = Lemonade(Descriptions.lemonade_description(), Costs.lemonade_cost())
ayran = Ayran(Descriptions.ayran_description(), Costs.ayran_cost())
