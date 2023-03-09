import pandas as pd


class Costs:

    # Pizzas
    @staticmethod
    def classic_cost():
        pizza = pd.read_csv("Costs/pizzas.csv")
        return pizza.iloc[0, 1]

    @staticmethod
    def margherita_cost():
        pizza = pd.read_csv("Costs/pizzas.csv")
        return pizza.iloc[1, 1]

    @staticmethod
    def turk_cost():
        pizza = pd.read_csv("Costs/pizzas.csv")
        return pizza.iloc[2, 1]

    @staticmethod
    def dominos_cost():
        pizza = pd.read_csv("Costs/pizzas.csv")
        return pizza.iloc[3, 1]

    # Sauces
    @staticmethod
    def ketchup_cost():
        sauce = pd.read_csv("Costs/sauces.csv")
        return sauce.iloc[0, 1]

    @staticmethod
    def mayo_cost():
        sauce = pd.read_csv("Costs/sauces.csv")
        return sauce.iloc[1, 1]

    @staticmethod
    def mustard_cost():
        sauce = pd.read_csv("Costs/sauces.csv")
        return sauce.iloc[2, 1]

    @staticmethod
    def ranch_cost():
        sauce = pd.read_csv("Costs/sauces.csv")
        return sauce.iloc[3, 1]

    @staticmethod
    def bbq_cost():
        sauce = pd.read_csv("Costs/sauces.csv")
        return sauce.iloc[4, 1]

    @staticmethod
    def hot_sauce_cost():
        sauce = pd.read_csv("Costs/sauces.csv")
        return sauce.iloc[5, 1]

    # Ingredients
    @staticmethod
    def olive_cost():
        ingredients = pd.read_csv("Costs/ingredients.csv")
        return ingredients.iloc[0, 1]

    @staticmethod
    def mushroom_cost():
        ingredients = pd.read_csv("Costs/ingredients.csv")
        return ingredients.iloc[1, 1]

    @staticmethod
    def goat_cheese_cost():
        ingredients = pd.read_csv("Costs/ingredients.csv")
        return ingredients.iloc[2, 1]

    @staticmethod
    def meat_cost():
        ingredients = pd.read_csv("Costs/ingredients.csv")
        return ingredients.iloc[3, 1]

    @staticmethod
    def onion_cost():
        ingredients = pd.read_csv("Costs/ingredients.csv")
        return ingredients.iloc[4, 1]

    @staticmethod
    def corn_cost():
        ingredients = pd.read_csv("Costs/ingredients.csv")
        return ingredients.iloc[5, 1]

    # Beverages
    @staticmethod
    def coke_cost():
        beverages = pd.read_csv("Costs/beverages.csv")
        return beverages.iloc[0, 1]

    @staticmethod
    def fanta_cost():
        beverages = pd.read_csv("Costs/beverages.csv")
        return beverages.iloc[1, 1]

    @staticmethod
    def pop_soda_cost():
        beverages = pd.read_csv("Costs/beverages.csv")
        return beverages.iloc[2, 1]

    @staticmethod
    def lemonade_cost():
        beverages = pd.read_csv("Costs/beverages.csv")
        return beverages.iloc[3, 1]

    @staticmethod
    def ayran_cost():
        beverages = pd.read_csv("Costs/beverages.csv")
        return beverages.iloc[4, 1]
