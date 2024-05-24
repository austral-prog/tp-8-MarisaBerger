rom sets_categories_data import ALCOHOLS


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))




def check_drinks(drink_name, drink_ingredients):
    drinkingredients = set(drink_ingredients)
    if len(drinkingredients.intersection(ALCOHOLS)) > 0:
        return drink_name + " Cocktail"
    else:
        return drink_name + " Mocktail"
