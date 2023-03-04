from Product.Pizza.SubPizza import Dominos, Turk, Margherita, Classic
class Tuples:
    def pizza_tuple(self):
        dominos = Dominos("Domino's pizza plain", 20)
        turk = Turk("Turkish style pizza plain", 45)
        margherita = Margherita("Margherita pizza plain", 50)
        classic = Classic("Classic pizza plain", 35)
        pizzas_tuple = [
            (classic.get_description(), classic.get_cost(), self.ui.klas_pizza_check.isChecked()),
            (margherita.get_description(), margherita.get_cost(), self.ui.Mar_pizza_check.isChecked()),
            (turk.get_description(), turk.get_cost(), self.ui.turk_pizza_check.isChecked()),
            (dominos.get_description(), dominos.get_cost(), self.ui.s_pizza_check.isChecked())
        ]
        return print(pizzas_tuple)