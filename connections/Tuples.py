# These tuples codes add products to selected items to menu in GUI
from Connections.Objects import *
def pizza_tuple(self):
    pizzas = [
        (classic.get_description(), classic.get_cost(), self.ui.klas_pizza_check.isChecked()),
        (margherita.get_description(), margherita.get_cost(), self.ui.Mar_pizza_check.isChecked()),
        (turk.get_description(), turk.get_cost(), self.ui.turk_pizza_check.isChecked()),
        (dominos.get_description(), dominos.get_cost(), self.ui.s_pizza_check.isChecked())
    ]
    return pizzas

def ingredient_tuple(self):
    ingredients = [
        (olive.get_description(), olive.get_cost(), self.ui.zeytin_check.isChecked()),
        (mushroom.get_description(), mushroom.get_cost(), self.ui.mantar_check.isChecked()),
        (goat_cheese.get_description(), goat_cheese.get_cost(), self.ui.keci_peyniri_check.isChecked()),
        (meat.get_description(), meat.get_cost(), self.ui.et_check.isChecked()),
        (onion.get_description(), onion.get_cost(), self.ui.sogan_check.isChecked()),
        (corn.get_description(), corn.get_cost(), self.ui.misir_check.isChecked())
    ]
    return ingredients

def sauce_tuple(self):
    sauces = [
        (ketchup.get_description(), ketchup.get_cost() * self.ui.spinBox_ketcap_4.value(),
         self.ui.ketcap_check.isChecked()),
        (mayo.get_description(), mayo.get_cost() * self.ui.spinBox_mayonez_4.value(),
         self.ui.mayonez_check.isChecked()),
        (mustard.get_description(), mustard.get_cost() * self.ui.spinBox_hardal_4.value(),
         self.ui.hardal_check.isChecked()),
        (bbq.get_description(), bbq.get_cost() * self.ui.spinBox_bbq_4.value(),
         self.ui.bbq_check.isChecked()),
        (hot_sauce.get_description(), hot_sauce.get_cost() * self.ui.spinBox_aci_sos_4.value(),
         self.ui.aci_sos_check.isChecked()),
        (ranch.get_description(), ranch.get_cost() * self.ui.spinBox_ranch_4.value(),
         self.ui.ranch_check.isChecked())
    ]
    return sauces

def drinks_tuple(self):
    drinks = [
        (coke.get_description(), coke.get_cost() * self.ui.spinBox_KOLA.value(), self.ui.kola_check.isChecked()),
        (fanta.get_description(), fanta.get_cost() * self.ui.spinBox_FANTA.value(), self.ui.fanta_check.isChecked()),
        (pop_soda.get_description(), pop_soda.get_cost() * self.ui.spinBox_GAZOZ.value(),
         self.ui.gazoz_check.isChecked()),
        (lemonade.get_description(), lemonade.get_cost() * self.ui.spinBox_LMONATA.value(),
         self.ui.limonata_check.isChecked()),
        (ayran.get_description(), ayran.get_cost() * self.ui.spinBox_AYRAN.value(), self.ui.ayran_check.isChecked())
    ]

    return drinks
