import collections
from random import shuffle

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrencDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 12)] + list('JQKA')
    suits = 'spades diamonds clubs hears'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]    
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, key, value):
        self._cards.insert(key, value)

deck = FrencDeck2()

print(deck[:5])
shuffle(deck)
print(deck[:5])