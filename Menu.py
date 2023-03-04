import pandas as pd

# Pizzalar
class Costs:
    @staticmethod
    def klasik_pizza_cost():
        pizza = pd.read_csv("pizzas.csv")
        return pizza.iloc[0, 1]

    @staticmethod
    def margarita_pizza_cost():
        pizza = pd.read_csv("pizzas.csv")
        return pizza.iloc[1, 1]

    @staticmethod
    def turk_pizza_cost():
        pizza = pd.read_csv("pizzas.csv")
        return pizza.iloc[2, 1]

    @staticmethod
    def dominos_pizza_cost():
        pizza = pd.read_csv("pizzas.csv")
        return pizza.iloc[3, 1]


    # Soslar
    @staticmethod
    def ketcap_cost():
        sauce = pd.read_csv("sauces.csv")
        return sauce.iloc[0, 1]

    @staticmethod
    def mayonez_cost():
        sauce = pd.read_csv("sauces.csv")
        return sauce.iloc[1, 1]

    @staticmethod
    def hardal_cost():
        sauce = pd.read_csv("sauces.csv")
        return sauce.iloc[2, 1]

    @staticmethod
    def ranch_cost():
        sauce = pd.read_csv("sauces.csv")
        return sauce.iloc[3, 1]

    @staticmethod
    def bbq_cost():
        sauce = pd.read_csv("sauces.csv")
        return sauce.iloc[4, 1]

    @staticmethod
    def aci_sos_cost():
        sauce = pd.read_csv("sauces.csv")
        return sauce.iloc[5, 1]

    #ingredients

    @staticmethod
    def zeytin_cost():
        ingredients = pd.read_csv("ingredients.csv")
        return ingredients.iloc[0, 1]

    @staticmethod
    def mantar_cost():
        ingredients = pd.read_csv("ingredients.csv")
        return ingredients.iloc[1, 1]

    @staticmethod
    def keci_peyniri_cost():
        ingredients = pd.read_csv("ingredients.csv")
        return ingredients.iloc[2, 1]

    @staticmethod
    def et_cost():
        ingredients = pd.read_csv("ingredients.csv")
        return ingredients.iloc[3, 1]

    @staticmethod
    def sogan_cost():
        ingredients = pd.read_csv("ingredients.csv")
        return ingredients.iloc[4, 1]

    @staticmethod
    def misir_cost():
        ingredients = pd.read_csv("ingredients.csv")
        return ingredients.iloc[5, 1]

    @staticmethod
    #beverages
    def kola_cost():
        beverages = pd.read_csv("ingredients.csv")
        return beverages.iloc[0, 1]

    @staticmethod
    def fanta_cost():
        beverages = pd.read_csv("ingredients.csv")
        return beverages.iloc[1, 1]

    @staticmethod
    def gazoz_cost():
        beverages = pd.read_csv("ingredients.csv")
        return beverages.iloc[2, 1]

    @staticmethod
    def limonata_cost():
        beverages = pd.read_csv("ingredients.csv")
        return beverages.iloc[3, 1]

    @staticmethod
    def ayran_cost():
        beverages = pd.read_csv("ingredients.csv")
        return beverages.iloc[4, 1]


