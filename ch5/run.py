#  FUnctions are 1st class objects
import random
from functools import reduce
from operator import add


def factorial(n):
    """Returns factorial of n"""
    return n if n < 2 else n * factorial(n - 1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

fact = factorial

print(fact, range(10))
print(list(map(fact, range(10))))


# High order funtions


def reverse(word):
    return word[::-1]


reverse.short_description = "Reverse"
print(dir(reverse))

# sort by reverserd words
fruit = ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
print(sorted(fruit))
print(sorted(fruit, key=reverse))

# map vs list compreh
print(list(map(fact, range(10))))
print([fact(n) for n in range(10)])

# filter vs list compreh
for n in (filter(lambda n: n % 2 == 0, range(10))):
    print(n)
print([n for n in range(n) if n%2 == 0])

print(reduce(add, range(100)))
print(sum(range(100)))

#  Lambda

print(sorted(fruit, key=lambda word : word[::-1]))


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("Cannot pick from empty bingocage")

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))
