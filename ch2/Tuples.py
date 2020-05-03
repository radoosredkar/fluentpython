import os
from collections import namedtuple
from datetime import datetime

traveler_ids = [('Rado Osredkar', 1), ('Vladka Osredkar', 2)]
for traveler in traveler_ids:
    print('%s(id=%s)' % traveler)

ime, priimek, datum_rojstva = ('Rado', 'Osredkar', datetime(1977, 5, 6))

print('%s %s, Rojen: %s' % (ime, priimek, datum_rojstva))

_, ospath = os.path.split(os.path.realpath(__file__))

print(ospath)

first, second, *rest = range(10)
print(first, second, rest)

first, *rest, last = range(10)
print(first, rest, last)

# named tuples

City = namedtuple('City', 'name country populaton coordinates')
vrhnika = City('Vrhnika', 'Slovenia', 15000, (1, 2))
ljubljana = City('Ljubljana', 'Slovenia', 250000, (2, 2))
print(vrhnika, ljubljana)
print(vrhnika.country, vrhnika.coordinates, vrhnika[0])
print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
print(delhi_data)
print(*delhi_data)
delhi = City(*delhi_data)
print(delhi)
print("*" * 100)
print(delhi._asdict())

