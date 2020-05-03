def f(a, b):
    a += b
    return a


a = 1
b = 2
print(a, b)
print(f(a, b))
print(a, b)

a = [1, 2]
b = [5, 6]

print(a, b)
print(f(a, b))
print(a, b)

a = (1, 2, 3)
b = (4, 5)

print(a, b)
print(f(a, b))
print(a, b)


class HauntedBus:

    def __init__(self, passanges=[]) -> None:
        self.passanges = passanges

    def pick(self, name):
        self.passanges.append(name)

    def drop(self, name):
        self.passanges.remove(name)

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passanges)
bus1.pick('Chalie')
bus1.pick('Alice')

print(bus1.passanges)
bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passanges)

bus3 = HauntedBus()
print(bus3.passanges)
bus3.pick('Dave')
print(bus2.passanges)

print(bus3.passanges is bus2.passanges)
print(bus1.passanges)
