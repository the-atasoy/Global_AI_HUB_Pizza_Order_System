import pandas as pd

class Descriptions:

    # Pizzas
    @staticmethod
    def classic_description():
        pizza = pd.read_csv("Data/pizzas.csv")
        return pizza.iloc[0, 0]

    @staticmethod
    def margherita_description():
        pizza = pd.read_csv("Data/pizzas.csv")
        return pizza.iloc[1, 0]

    @staticmethod
    def turk_description():
        pizza = pd.read_csv("Data/pizzas.csv")
        return pizza.iloc[2, 0]

    @staticmethod
    def dominos_description():
        pizza = pd.read_csv("Data/pizzas.csv")
        return pizza.iloc[3, 0]

    # Sauces
    @staticmethod
    def ketchup_description():
        sauce = pd.read_csv("Data/sauces.csv")
        return sauce.iloc[0, 0]

    @staticmethod
    def mayo_description():
        sauce = pd.read_csv("Data/sauces.csv")
        return sauce.iloc[1, 0]

    @staticmethod
    def mustard_description():
        sauce = pd.read_csv("Data/sauces.csv")
        return sauce.iloc[2, 0]

    @staticmethod
    def ranch_description():
        sauce = pd.read_csv("Data/sauces.csv")
        return sauce.iloc[3, 0]

    @staticmethod
    def bbq_description():
        sauce = pd.read_csv("Data/sauces.csv")
        return sauce.iloc[4, 0]

    @staticmethod
    def hot_sauce_description():
        sauce = pd.read_csv("Data/sauces.csv")
        return sauce.iloc[5, 0]

    # Ingredients
    @staticmethod
    def olive_description():
        ingredients = pd.read_csv("Data/ingredients.csv")
        return ingredients.iloc[0, 0]

    @staticmethod
    def mushroom_description():
        ingredients = pd.read_csv("Data/ingredients.csv")
        return ingredients.iloc[1, 0]

    @staticmethod
    def goat_cheese_description():
        ingredients = pd.read_csv("Data/ingredients.csv")
        return ingredients.iloc[2, 0]

    @staticmethod
    def meat_description():
        ingredients = pd.read_csv("Data/ingredients.csv")
        return ingredients.iloc[3, 0]

    @staticmethod
    def onion_description():
        ingredients = pd.read_csv("Data/ingredients.csv")
        return ingredients.iloc[4, 0]

    @staticmethod
    def corn_description():
        ingredients = pd.read_csv("Data/ingredients.csv")
        return ingredients.iloc[5, 0]

    # Beverages
    @staticmethod
    def coke_description():
        beverages = pd.read_csv("Data/beverages.csv")
        return beverages.iloc[0, 0]

    @staticmethod
    def fanta_description():
        beverages = pd.read_csv("Data/beverages.csv")
        return beverages.iloc[1, 0]

    @staticmethod
    def pop_soda_description():
        beverages = pd.read_csv("Data/beverages.csv")
        return beverages.iloc[2, 0]

    @staticmethod
    def lemonade_description():
        beverages = pd.read_csv("Data/beverages.csv")
        return beverages.iloc[3, 0]

    @staticmethod
    def ayran_description():
        beverages = pd.read_csv("Data/beverages.csv")
        return beverages.iloc[4, 0]
