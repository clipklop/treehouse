import random


from attributes import Sneaky, Agile
from characters import Character


class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        if self.sneaky:
            print(f'Called by {self}. So sneaky snake!')
            return bool(random.randint(0, 1))
        return "Soz, you aren't sneaky enough."
        # return self.sneaky and bool(random.randint(0, 1))
