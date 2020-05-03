class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]

foo = Foo()

print(foo[1])

for i in foo: print(i)
print(20 in foo)
print(15 in foo)

from random import shuffle

l = list(range(10))
print(l)
shuffle(l)
print(l)

import os
print (os.getcwd())
import sys
sys.path.append(".")

from ch1.cart_deck import FrenchDeck
deck = FrenchDeck()

def set_card(self, key, value):
    deck._cards[key] = value

FrenchDeck.__setitem__ = set_card

print(deck[:5])
shuffle(deck)
print(deck[:5])