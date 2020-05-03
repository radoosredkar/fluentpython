import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print("Gone with the wind")


ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
print(ender.alive)
s2 = "TEST"

print(ender.alive)

print(f"{'*' * 50} Weak References {'*' * 50}")

import weakref

a_set = {1, 2, 3}
wref = weakref.ref(a_set)
print(wref)
print(wref())
print(wref is None)
a_set = {4, 5, 6}
print(wref())
print(wref is None)


class Cheese:

    def __init__(self, kind) -> None:
        self.kind = kind

    def __repr__(self) -> str:
        return 'Cheese(%r)' % self.kind

    def __lt__(self, other):
        return self.kind < other.kind


stock = weakref.WeakKeyDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese] = cheese

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys()))

s1 = 'ABC'
s2 = 'ABC'
print(s1 is s2)

t1 = (1,2,3)
t2 = t1[:]
print(t1 is t2)
