import pandas as pd


def get_menu():
    pizza = pd.read_csv("pizzas.cvs")
    print(pizza[["Pizzas", "Price"]].to_string(index=False))

    ingredients = pd.read_csv("ingredients.cvs")
    print(ingredients[["Ingredients", "Price"]].to_string(index=False))

    beverages = pd.read_csv("beverages.cvs")
    print(beverages[["Beverages", "Price"]].to_string(index=False, justify="left"))

    sauces = pd.read_csv("sauces.cvs")
    print(sauces[["Sauces", "Price"]].to_string(index=False, justify="left"))


get_menu()
