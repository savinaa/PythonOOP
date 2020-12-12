
#from collections import defaultdict
from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        #recipes: dict - empty upon initialization (recipe name as key and dictionary of needed ingredients to make the recipe)
        #products: dict - empty upon initialization (made recipes; recipe name as key and quantity as value)
        self.recipes={}
        #self.products=defaultdict(int)
        self.products= {}

    def add_ingredient (self,ingredient_type: str, quantity: int):
        if ingredient_type in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"] and self.can_add(quantity):
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = quantity
            else:
                self.ingredients[ingredient_type]+=quantity
        elif not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        elif ingredient_type not in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"] :
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient (self,ingredient_type: str, quantity: int):
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
            raise KeyError("No such product in the factory")

    def add_recipe(self,recipe_name: str, recipe: dict):
        if recipe_name not in self.recipes:
            self.recipes[recipe_name]=recipe
        else:
            #TODO
            #What means update? Add/remove ingredients or replace the recipe?
            self.recipes[recipe_name] = recipe

    def make_chocolate(self,recipe_name: str):
        if recipe_name in self.recipes:
            if recipe_name not in self.products:
                self.products[recipe_name] = 1
            else:
                self.products[recipe_name]+=1
            recipe=self.recipes[recipe_name]
            for ingredient, quantity in recipe.items():
                self.remove_ingredient(ingredient,quantity)
        else:
            raise TypeError("No such recipe")



