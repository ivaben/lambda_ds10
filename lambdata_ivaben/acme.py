
from random import randint

class Product():
    
    def __init__(self, name = "", price = 10, weight = 20, flammability = 0.5, identifier = randint (1000000, 9999999)):


        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        val_stealability = self.price / self.weight
        
        if val_stealability < 0.5:
            return print("Not so stealabel...")

        elif val_stealability >= 0.5 and val_stealability < 1:
            return print("Kinda stealable")

        else:
            return print("Very stealable!")


    def explode(self):
        val_explode = self.flammability * self.weight

        if val_explode < 10:
            return print("...fizzle.")

        elif val_explode >= 10 and self.explode < 50:
            return print("...boom!")

        else:
            return print("...BABOOM!!")


class BoxingGlove(Product):
    def __init__(self, name = " ", price = 10, weight = 10, flammability = 0.5, 
    identifier = randint (1000000, 9999999)):


        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        return print("...it's a glove")

    def punch(self):
        if self.weight < 5:
            return print("That tickles")

        elif self.weight >= 5 and self.weight < 15:
            return print("Hey that hurt!")

        else:
            return print("OUCH!")


