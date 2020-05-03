import copy


class Gizmo:

    def __init__(self) -> None:
        print("Gizmo id %d " % id(self))


Gizmo()
# i = Gizmo() * 10 # throws axception as part of the learning

charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex == charles)
print(alex is not charles)

# Tuples are immutable but referenced objects are not
print("*" * 50)
t1 = (1, 2, 3, [1, 2])
t2 = (1, 2, 3, [1, 2])
print(t1 is t2)
print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(2)
print(t1)

print(t1 == t2)
print(t1 is t2)
print(id(t1[-1]))

print("*" * 50)

# copies are shallow by default

t2 = [1, 2, 3, [2, 3], (2, 3, 4)]
t3 = list(t2)
print(t3)
print(t2)
t4 = t2[:]
print(t3 == t2)
print(t3 is t2)


class Bus:

    def __init__(self, passanges=None) -> None:
        if passanges is None:
            self.passanges = []
        else:
            self.passanges = passanges

    def pick(self, name):
        self.passanges.append(name)

    def drop(self, name):
        self.passanges.remove(name)


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

buses = [bus1, bus2, bus3]
for bus in buses:
    print(id(bus), end=' ')

bus1.drop('Bill')
print(bus2.passanges)
print(bus3.passanges)

