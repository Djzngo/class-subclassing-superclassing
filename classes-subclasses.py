"""
This program is an example of the use of classes within Python.
"""
class Items():
    """
    Creates an instance of items. 
    """
    #Instance attributes
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    #Returns the value of the items.
    def value(self):
        return self.price * self.quantity

class Game(Items):
    """
    Creates an instance of a game item.
    """
    #Instance attributes
    def __init__(self, name, price, quantity, platform):
        #Superclass (Items)
        super().__init__(name, price, quantity)
        self.platform = platform

    #Returns a description of the game item.
    def describe(self):
        return f"Name: {self.name}, Platform: {self.platform}, Price: £{self.price}, Quantity: {self.quantity}, Total value: £{self.value()}"

class Clothing(Items):
    """
    Creates an instance of a clothing item.
    """
    #Instance attributes
    def __init__(self, name, price, quantity, category, size):
        #Superclass (Items)
        super().__init__(name, price, quantity)
        self.category = category
        self.size = size

    def describe(self):
        return f"Name: {self.name}, Category: {self.category}, Size: {self.size}, Price: £{self.price}, Quantity: {self.quantity}, Total value: £{self.value()}"

game_one = Game("Nubby's Number Factory", 4.29, 250, "PC")

clothing_one = Clothing("Goku T-shirt", 24.99, 25, "T-shirts", "Large")

print(game_one.describe())
print(clothing_one.describe())