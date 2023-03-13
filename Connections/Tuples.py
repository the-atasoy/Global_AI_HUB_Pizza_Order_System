# These functions are used for adding selected items to add the basket.
# Last element of every tuple checks if product selected or not.

from Connections.Objects import *

def pizza_tuple(self):
    pizzas = [
        (classic.get_description(), classic.get_cost(), self.main_page.classic_pizza_check.isChecked()),
        (margherita.get_description(), margherita.get_cost(), self.main_page.margherita_pizza_check.isChecked()),
        (turk.get_description(), turk.get_cost(), self.main_page.turk_pizza_check.isChecked()),
        (dominos.get_description(), dominos.get_cost(), self.main_page.dominos_pizza_check.isChecked())
    ]
    return pizzas

def ingredient_tuple(self):
    ingredients = [
        (olive.get_description(), olive.get_cost(), self.main_page.zeytin_check.isChecked()),
        (mushroom.get_description(), mushroom.get_cost(), self.main_page.mantar_check.isChecked()),
        (goat_cheese.get_description(), goat_cheese.get_cost(), self.main_page.keci_peyniri_check.isChecked()),
        (meat.get_description(), meat.get_cost(), self.main_page.et_check.isChecked()),
        (onion.get_description(), onion.get_cost(), self.main_page.sogan_check.isChecked()),
        (corn.get_description(), corn.get_cost(), self.main_page.misir_check.isChecked())
    ]
    return ingredients

def sauce_tuple(self):
    sauces = [
        (ketchup.get_description(), ketchup.get_cost() * self.main_page.spinBox_ketchup_4.value(),
         self.main_page.ketchup_check.isChecked()),
        (mayo.get_description(), mayo.get_cost() * self.main_page.spinBox_mayo_4.value(),
         self.main_page.mayo_check.isChecked()),
        (mustard.get_description(), mustard.get_cost() * self.main_page.spinBox_mustard_4.value(),
         self.main_page.mustard_check.isChecked()),
        (bbq.get_description(), bbq.get_cost() * self.main_page.spinBox_bbq_4.value(),
         self.main_page.bbq_check.isChecked()),
        (hot_sauce.get_description(), hot_sauce.get_cost() * self.main_page.spinBox_hot_sauce_4.value(),
         self.main_page.hot_sauce_check.isChecked()),
        (ranch.get_description(), ranch.get_cost() * self.main_page.spinBox_ranch_4.value(),
         self.main_page.ranch_check.isChecked())
    ]
    return sauces

def beverage_tuple(self):
    drinks = [
        (coke.get_description(), coke.get_cost() * self.main_page.spinBox_coke.value(), self.main_page.coke_check.isChecked()),
        (fanta.get_description(), fanta.get_cost() * self.main_page.spinBox_fanta.value(), self.main_page.fanta_check.isChecked()),
        (pop_soda.get_description(), pop_soda.get_cost() * self.main_page.spinBox_pop_soda.value(),
         self.main_page.pop_soda_check.isChecked()),
        (lemonade.get_description(), lemonade.get_cost() * self.main_page.spinBox_lemonade.value(),
         self.main_page.lemonade_check.isChecked()),
        (ayran.get_description(), ayran.get_cost() * self.main_page.spinBox_ayran.value(), self.main_page.ayran_check.isChecked())
    ]

    return drinks
