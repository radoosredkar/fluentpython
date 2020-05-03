from collections import namedtuple
from functools import reduce, partial


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


print(fact(10))

from operator import mul, attrgetter


def simpler_fac(n):
    return reduce(mul, range(1, n + 1))


print(simpler_fac(10))

metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
              ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
              ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
              ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)), ]

# sort by name
from operator import itemgetter

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

LatLing = namedtuple('LatLing', 'lat lng')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLing(lat, lng))
               for name, cc, pop, (lat, lng) in metro_data]
print(metro_areas)
print(metro_areas[0].name, metro_areas[0].coord.lat, metro_areas[0].coord.lng)

name_lat = attrgetter('name', 'coord.lat')
for city in metro_areas:
    print(name_lat(city))

from operator import methodcaller

s = 'the time has come'
upper = methodcaller('upper')
print(upper(s))

# Freeze arguments
print(mul(10, 4))
triple = partial(mul, 3)
print(triple(10))
print(list(map(triple, range(1, 8))))
