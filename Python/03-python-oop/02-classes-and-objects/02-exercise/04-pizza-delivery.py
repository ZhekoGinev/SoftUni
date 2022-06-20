class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False
        self.warning = f"Pizza {self.name} already prepared, and we can't make any changes!"

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return self.warning
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += price_per_quantity * quantity

    def remove_ingredient(
        self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return self.warning
        if ingredient not in self.ingredients:
            return (f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!")
        elif ingredient in self.ingredients and quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= price_per_quantity * quantity

    def make_order(self):
        if self.ordered:
            return self.warning
        else:
            self.ordered = True
            ingredients = ', '.join(f'{k}: {v}' for k,v in self.ingredients.items())
            return f"You've ordered pizza {self.name} prepared with {ingredients} and the price will be {self.price}lv."
        
