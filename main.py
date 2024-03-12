def convert_recipe(servings, desired_servings, ingredients):
    conversion_factor = desired_servings / servings
    adjusted_ingredients = {}

    for ingredient, details in ingredients.items():
        quantity = details['quantity']
        unit = details['unit']
        adjusted_quantity = quantity * conversion_factor
        adjusted_ingredients[ingredient] = {'quantity': adjusted_quantity, 'unit': unit}

    return adjusted_ingredients

def main():
    servings = int(input("Enter the original number of servings: "))
    desired_servings = int(input("Enter the desired number of servings: "))

    ingredients = {}
    num_ingredients = int(input("Enter the number of ingredients: "))

    for i in range(num_ingredients):
        ingredient = input("Enter the name of ingredient {}: ".format(i+1))
        quantity = float(input("Enter the quantity of ingredient {} (in original recipe): ".format(i+1)))
        unit = input("Enter the unit of ingredient {} (e.g. cups, grams): ".format(i+1))
        ingredients[ingredient] = {'quantity': quantity, 'unit': unit}

    adjusted_ingredients = convert_recipe(servings, desired_servings, ingredients)

    print("\nAdjusted quantities for {} servings:".format(desired_servings))
    for ingredient, details in adjusted_ingredients.items():
        quantity = details['quantity']
        unit = details['unit']
        print("{}: {:.2f} {}".format(ingredient, quantity, unit))

if __name__ == "__main__":
    main()
