import Costs
import Descriptions
from Product.Drink.SubDrink import *
from Product.Ingredient.SubIngredient import *
from Product.Pizza.SubPizza import *
from Product.Sauce.SubSauce import *

# pizza objects
dominos = Dominos(Descriptions.Descriptions.dominos_description(), Costs.Costs.dominos_cost())
turk = Turk(Descriptions.Descriptions.turk_description(), Costs.Costs.turk_cost())
margherita = Margherita(Descriptions.Descriptions.margherita_description(), Costs.Costs.margherita_cost())
classic = Classic(Descriptions.Descriptions.classic_description(), Costs.Costs.classic_cost())

# ingredient objects
olive = Olive(Descriptions.Descriptions.olive_description(), Costs.Costs.olive_cost())
mushroom = Mushroom(Descriptions.Descriptions.mushroom_description(), Costs.Costs.mushroom_cost())
goat_cheese = GoatCheese(Descriptions.Descriptions.goat_cheese_description(), Costs.Costs.goat_cheese_cost())
meat = Meat(Descriptions.Descriptions.meat_description(), Costs.Costs.meat_cost())
onion = Onion(Descriptions.Descriptions.onion_description(), Costs.Costs.onion_cost())
corn = Corn(Descriptions.Descriptions.corn_description(), Costs.Costs.corn_cost())

# sauce objects
ketchup = Ketchup(Descriptions.Descriptions.ketchup_description(), Costs.Costs.ketchup_cost())
mayo = Mayo(Descriptions.Descriptions.mayo_description(), Costs.Costs.mayo_cost())
mustard = Mustard(Descriptions.Descriptions.mustard_description(), Costs.Costs.mustard_cost())
bbq = BBQ(Descriptions.Descriptions.bbq_description(), Costs.Costs.bbq_cost())
hot_sauce = Hot(Descriptions.Descriptions.hot_sauce_description(), Costs.Costs.hot_sauce_cost())
ranch = Ranch(Descriptions.Descriptions.ranch_description(), Costs.Costs.ranch_cost())

# drink objects
coke = Coke(Descriptions.Descriptions.coke_description(), Costs.Costs.coke_cost())
fanta = Fanta(Descriptions.Descriptions.fanta_description(), Costs.Costs.fanta_cost())
pop_soda = SodaPop(Descriptions.Descriptions.pop_soda_description(), Costs.Costs.pop_soda_cost())
lemonade = Lemonade(Descriptions.Descriptions.lemonade_description(), Costs.Costs.lemonade_cost())
ayran = Ayran(Descriptions.Descriptions.ayran_description(), Costs.Costs.ayran_cost())
