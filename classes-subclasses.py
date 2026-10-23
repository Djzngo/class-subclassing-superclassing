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

test = Items("test", 2, 4)

print(test.name)