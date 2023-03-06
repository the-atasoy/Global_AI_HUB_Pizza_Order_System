from Objects import *


def pizza_menu(self):
    menu = (
            f"1. {classic.get_description()}          -----> {classic.get_cost()} $" + "\n" +
            f"2. {margherita.get_description()}   -----> {margherita.get_cost()} $" + "\n" +
            f"3. {turk.get_description()}            -----> {turk.get_cost()} $" + "\n" +
            f"4. {dominos.get_description()}    -----> {dominos.get_cost()} $")

    self.ui.pizza_menu.setText(menu)


def ingredient_menu(self):
    menu = (
            f"1. {olive.get_description()}           -----> {olive.get_cost()} $" + "\n" +
            f"2. {mushroom.get_description()}         -----> {mushroom.get_cost()} $" + "\n" +
            f"3. {goat_cheese.get_description()}   -----> {goat_cheese.get_cost()} $" + "\n" +
            f"4. {meat.get_description()}                 -----> {meat.get_cost()} $" + "\n" +
            f"5. {onion.get_description()}           -----> {onion.get_cost()} $" + "\n" +
            f"6. {corn.get_description()}             -----> {corn.get_cost()} $")

    self.ui.ingredient_menu.setText(menu)


def sauce_menu(self):
    menu = (
            f"1. {ketchup.get_description()}             -----> {ketchup.get_cost()} $" + "\n" +
            f"2. {mayo.get_description()}          -----> {mayo.get_cost()} $" + "\n" +
            f"3. {mustard.get_description()}              -----> {mustard.get_cost()} $" + "\n" +
            f"4. {ranch.get_description()}        -----> {ranch.get_cost()} $" + "\n" +
            f"5. {bbq.get_description()}            -----> {bbq.get_cost()} $" + "\n" +
            f"6. {hot_sauce.get_description()}             -----> {hot_sauce.get_cost()} $")

    self.ui.sauce_menu.setText(menu)


def drink_menu(self):
    menu = (
            f"1. {coke.get_description()}               -----> {coke.get_cost()} $" + "\n" +
            f"2. {fanta.get_description()}             -----> {fanta.get_cost()} $" + "\n" +
            f"3. {pop_soda.get_description()}            -----> {pop_soda.get_cost()} $" + "\n" +
            f"4. {lemonade.get_description()}       -----> {lemonade.get_cost()} $" + "\n" +
            f"5. {ayran.get_description()}            -----> {ayran.get_cost()} $")

    self.ui.drink_menu.setText(menu)