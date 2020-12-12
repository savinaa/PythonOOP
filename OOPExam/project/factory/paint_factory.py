from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    @property
    def products(self):
        return self.ingredients

    @products.setter
    def products(self, value):
        self.ingredients = value

    def add_ingredient(self,ingredient_type: str, quantity: int):
        if ingredient_type in ["white", "yellow", "blue", "green", "red"]   and self.can_add(quantity):
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = quantity
            else:
                self.ingredients[ingredient_type] += quantity
        elif not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        elif ingredient_type not in ["white", "yellow", "blue", "green", "red"] :
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self,ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients and self.ingredients[ingredient_type]>=quantity:
            #TODO
            # what if final result is 0??? Remove from dictionary?
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = quantity
            else:
                self.ingredients[ingredient_type] -= quantity
        elif self.ingredients[ingredient_type]<quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")
        elif ingredient_type not in self.ingredients:
            #TODO
            #ingredient or product???
            raise KeyError("No such ingredient in the factory")