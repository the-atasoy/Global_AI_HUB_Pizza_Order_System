import Menu
from Product.Drink.SubDrink import *
from Product.Ingredient.SubIngredient import *
from Product.Pizza.SubPizza import *
from Product.Sauce.SubSauce import *

# pizza objects
dominos = Dominos("Domino's pizza tabanı", Menu.Costs.dominos_pizza_cost())
turk = Turk("Türk pizza tabanı", Menu.Costs.turk_pizza_cost())
margherita = Margherita("Margarita pizza tabanı", Menu.Costs.margarita_pizza_cost())
classic = Classic("Klasik pizza tabanı", Menu.Costs.klasik_pizza_cost())

# ingredient objects
olive = Olive("Zeytin", Menu.Costs.zeytin_cost())
mushroom = Mushroom("Mantar", Menu.Costs.mantar_cost())
goat_cheese = GoatCheese("Keçi Peyniri", Menu.Costs.keci_peyniri_cost())
meat = Meat("Et", Menu.Costs.et_cost())
onion = Onion("Soğan", Menu.Costs.sogan_cost())
corn = Corn("Mısır", Menu.Costs.misir_cost())

# sauce objects
ketchup = Ketchup("Ketçap", Menu.Costs.ketcap_cost())
mayo = Mayo("Mayonez", Menu.Costs.mayonez_cost())
mustard = Mustard("Hardal", Menu.Costs.hardal_cost())
bbq = BBQ("BBQ Sos", Menu.Costs.bbq_cost())
hot_sauce = Hot("Acı Sos", Menu.Costs.aci_sos_cost())
ranch = Ranch("Ranch Sos", Menu.Costs.ranch_cost())

# drink objects
coke = Coke("Kola", Menu.Costs.kola_cost())
fanta = Fanta("Fanta", Menu.Costs.fanta_cost())
pop_soda = SodaPop("Gazoz", Menu.Costs.gazoz_cost())
lemonade = Lemonade("Limonata", Menu.Costs.limonata_cost())
ayran = Ayran("Ayran", Menu.Costs.ayran_cost())
