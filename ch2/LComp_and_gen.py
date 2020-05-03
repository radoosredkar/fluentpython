# List Comprehensions
from pprint import pprint

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

codes = [ord(symbol) for symbol in symbols]

print(codes)

# filter

remove = list(filter(lambda c: c != '$', symbols))
print(remove)

# comprehension
remove = [symbol for symbol in symbols if symbol != '$']
print(remove)

# T Shirts
sizes = list('MSL')
colors = 'black white'.split(' ')
tshirts = [(color, size) for size in sizes
           for color in colors]

pprint(tshirts)

# Generators
codes = [ord(symbol) for symbol in symbols]

print(codes)

sizes = list('MSL')
colors = 'black white'.split(' ')
for tshirt in ('%s %s' % (color, size) for size in sizes for color in colors):
    print(tshirt)
