from collections import defaultdict
class EasterShop:
    def __init__(self, name, chocolate_factory, egg_factory, paint_factory):
        self.__name = name
        self.__chocolate_factory = chocolate_factory
        self.__egg_factory = egg_factory
        self.__paint_factory = paint_factory
        #self._storage=defaultdict(int) #(product name as key and quantity of the product as value)
        self.__storage= {} #(product name as key and quantity of the product as value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name=value

    @property
    def chocolate_factory(self):
        return self.__chocolate_factory

    @chocolate_factory.setter
    def chocolate_factory(self, value):
        self.__chocolate_factory=value

    @property
    def egg_factory(self):
        return self.__egg_factory

    @egg_factory.setter
    def egg_factory(self, value):
        self.__egg_factory = value

    @property
    def paint_factory(self):
        return self.__paint_factory

    @paint_factory.setter
    def paint_factory(self, value):
        self.__paint_factory = value

    @property
    def storage(self):
        return self.__storage

    @storage.setter
    def storage(self, value):
        self.__storage=value



    def add_chocolate_ingredient(self,type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type,quantity)

    def add_egg_ingredient(self,type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self,type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self,recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        #TODO
        #be careful here
        if recipe not in self.storage:
            self.storage[recipe] = 1
        else:
            self.storage[recipe] += 1

    def paint_egg(self,color: str, egg_type: str):
        if egg_type in self.egg_factory.products and color in self.paint_factory.products:
            if self.egg_factory.products[egg_type]>=1 and self.paint_factory.products[color]>=1:
                product_name = f"{color} {egg_type}"
                if product_name not in self.storage:
                    self.storage[product_name] = 1
                else:
                    self.storage[product_name]+=1
                self.egg_factory.remove_ingredient(egg_type,1)
                self.paint_factory.remove_ingredient(color,1)
            else:
                raise ValueError("Invalid commands")
        else:
            raise ValueError("Invalid commands")

    def __repr__(self):
        output=f"Shop name: {self.name}\n"
        output+=f"Shop storage:\n"
        for name, quantity in self.storage.items():
            output+=f"{name}: {quantity}\n"
        return output