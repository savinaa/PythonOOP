from abc import ABC, abstractmethod
#from collections import defaultdict
class Factory(ABC):
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
        self._ingredients= {}#(name of the ingredient for key and quantity of the ingredient as a value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name=value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity=value

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients=value


    @abstractmethod
    def add_ingredient (self,ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient (self,ingredient_type: str, quantity: int):
        pass

    def can_add(self,value: int):
        # TODO
        return len(self.ingredients)+value<=self.capacity
