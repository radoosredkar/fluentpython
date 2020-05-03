
from tombola import Tombola


class Bingo(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            # return self._items.pop() # too slow so replaced
            position = random.randrange(len(self._balls))
        except IndexError:
            raise LookupError("pick from empty item BingoCage")
        return self._balls[position]

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))

    def __call__(self):
        self.pick()

bingo = Bingo(range(1,30))
print(str(bingo))
for i in range(12):
    print(bingo.pick())

class LoterryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except:
            raise LookupError("Pick from empty BingoCage")
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))

lottery = LoterryBlower(range(39))
print(str(lottery))
for i in range(7):
    print(lottery.pick())


# Virtual subclass

@Tombola.register
class TombolaList(list):
    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
    
    load = list.extend

    def loaded(self):
        return bool(self)
    
    def inspect(self):
        return tuple(sorted(self))


print(issubclass(TombolaList, Tombola))
t = TombolaList(range(100))
print(isinstance(t, Tombola))
