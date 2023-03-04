import pandas as pd

# Pizzalar
def klasik_pizza_cost():
    pizza = pd.read_csv("pizzas.csv")
    return pizza.iloc[0, 1]


def margarita_pizza_cost():
    pizza = pd.read_csv("pizzas.csv")
    return pizza.iloc[1, 1]


def turk_pizza_cost():
    pizza = pd.read_csv("pizzas.csv")
    return pizza.iloc[2, 1]


def sade_pizza_cost():
    pizza = pd.read_csv("pizzas.csv")
    return pizza.iloc[3, 1]


# Soslar
def ketcap_cost():
    sauce = pd.read_csv("sauces.csv")
    return sauce.iloc[0, 1]


def mayonez_cost():
    sauce = pd.read_csv("sauces.csv")
    return sauce.iloc[1, 1]


def hardal_cost():
    sauce = pd.read_csv("sauces.csv")
    return sauce.iloc[2, 1]


def ranch_cost():
    sauce = pd.read_csv("sauces.csv")
    return sauce.iloc[3, 1]


def bbq_cost():
    sauce = pd.read_csv("sauces.csv")
    return sauce.iloc[4, 1]


def aci_sos_cost():
    sauce = pd.read_csv("sauces.csv")
    return sauce.iloc[5, 1]

#ingredients

def zeytin_cost():
    ingredients = pd.read_csv("ingredients.csv")
    return ingredients.iloc[0, 1]

def mantar_cost():
    ingredients = pd.read_csv("ingredients.csv")
    return ingredients.iloc[1, 1]

def keci_peyniri_cost():
    ingredients = pd.read_csv("ingredients.csv")
    return ingredients.iloc[2, 1]

def et_cost():
    ingredients = pd.read_csv("ingredients.csv")
    return ingredients.iloc[3, 1]

def sogan_cost():
    ingredients = pd.read_csv("ingredients.csv")
    return ingredients.iloc[4, 1]

def misir_cost():
    ingredients = pd.read_csv("ingredients.csv")
    return ingredients.iloc[5, 1]

#beverages
def kola_cost():
    beverages = pd.read_csv("ingredients.csv")
    return beverages.iloc[0, 1]

def fanta_cost():
    beverages = pd.read_csv("ingredients.csv")
    return beverages.iloc[1, 1]

def gazoz_cost():
    beverages = pd.read_csv("ingredients.csv")
    return beverages.iloc[2, 1]

def limonata_cost():
    beverages = pd.read_csv("ingredients.csv")
    return beverages.iloc[3, 1]

def ayran_cost():
    beverages = pd.read_csv("ingredients.csv")
    return beverages.iloc[4, 1]

