import itertools
import operator
import random

gen = itertools.count(1, 0.5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, 0.5))
print(list(gen))

# accumulate
print(list(itertools.compress(data=[1, 2, 3, 4, 5], selectors=[1, 0, 0, 2, 2])))
print(list(itertools.dropwhile((lambda x: x < 10), range(20))))
print(list(itertools.filterfalse((lambda x: x < 10), range(20))))
print(list(itertools.takewhile((lambda x: x < 10), range(20))))
print(list(itertools.islice(range(20), 17)))
print(list(itertools.islice(range(20), 12, 17, 2)))

# Mapping iterators

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample, min)))
print(list(itertools.accumulate(sample, max)))

print(list(itertools.accumulate(range(1, 11), operator.mul)))
print(list(itertools.accumulate(range(1, 11), operator.add)))

print(list(enumerate("albatroz")))
print(list(map(operator.mul, range(11), range(11))))
print(list(map((lambda a, b: (a, b)), range(10), list(range(4)))))
print(list(itertools.starmap(operator.mul, enumerate("albaroz", 1))))
print(
    list(
        itertools.starmap(
            (lambda n, m: str(m) + "=>" + str(n)), enumerate("albaroz", 1)
        )
    )
)

# Chaining iterators
print("*" * 50)
print(list(itertools.chain(range(12), "albatroz")))
print("*" * 50)
print(list(itertools.chain(enumerate("albatroz"))))
print("*" * 50)
print(list(itertools.chain.from_iterable(enumerate("albatroz"))))
print("*" * 50)
print(list(itertools.product(range(2), "RO")))
print("*" * 50)
print(list(zip(range(3), "test")))
print("*" * 50)
print(list(zip(range(3), "test", range(100, 200, 10))))
print("*" * 50)
print(list(itertools.zip_longest(range(3), "albabtroz")))
print("*" * 50)
print(list(itertools.zip_longest(range(3), "albabtroz", fillvalue="?")))

# product
print("*" * 50)
print(list(itertools.product("ABC", range(2))))

suits = "hearts,spades,diamonds,clubs".split(",")
cards = "QKBA"
print("*" * 50)
for card in itertools.product(cards, suits):
    print(card)
print("*" * 50)
print(list(itertools.product(cards, repeat=2)))

# Generato items
print("*" * 50)
ct = itertools.count()
print(next(ct))
print(next(ct))
print(next(ct))

print(list(itertools.islice(ct, 3)))
print("*" * 50)
cy = itertools.cycle("123456")
print(next(cy))
print(list(itertools.islice(cy, 7)))

# Rearanging
print("*" * 50)
print(list(itertools.groupby("AAABBBBCCGGGGGGG")))
for char, group in itertools.groupby("AAABBBBCCGGGGGGG"):
    print(char, list(group))

print("*" * 50)
animals = ["duck", "eagle", "rat", "giraffe", "bear", "bat", "dolphin", "shark", "lion"]
animals.sort()
print(animals)
animals.sort(key=len)
print(animals)
print("*" * 50)
for length, group in itertools.groupby(animals, len):
    print(f"{length}=>{list(group)}")

print("*" * 50)
for length, group in itertools.groupby(reversed(animals), len):
    print(f"{length}=>{list(group)}")

print("***************YIELD FROM******************************")


def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


print(list(chain("ABC", "GHF")))


def chain1(*iterables):
    for it in iterables:
        yield from it


print(list(chain1("ABC", "GHF")))

print("*" * 50)


def d6():
    return random.randint(1, 6)


print(d6())

d6_iter = iter(d6, 1)
for roll in d6_iter:
    print(roll)

print("*" * 100)
