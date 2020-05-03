l = list(range(10, 70, 10))
print(l)
print(l[:2])
print(l[1:3])
print(l[3:])
print(l[:-3])
print(l[-2:])
print("*" * 100)
# split at 2
print(l[2:], l[:2])

s = 'bycicle'
print(s[::-1])  # reverse
print(s[::-2])  # reverse every sec char

l = list(range(10))
START = slice(0, 3)
MIDDLE = slice(3, 7)
END = slice(7, 10)
print(l, l[START], l[MIDDLE], l[END])
del l[MIDDLE]
print(l, l[START], l[MIDDLE], l[END])

# + and * with sequences
print(l[START] * 5)

#  List of lists

board = [['_'] * 3 for i in range(3)]
board[1][1] = 'X'
board[2][1] = 'o'
print(board)

# *= +=

lst = list(range(3))
print(id(lst))
lst *= 2
print(id(lst))

print(lst)

lst = tuple(range(3))
print(id(lst))
lst *= 2
print(id(lst))
print(lst)

# sorting
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits, reverse=True)) # create new object and sort it desc
print(sorted(fruits, reverse=False, key=len)) # create new object and sort it by length

print(list.sort(fruits)) # changes object and returns none
print(fruits) # sorted object
