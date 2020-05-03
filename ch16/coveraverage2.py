from coroutil import coroutine
from collections import namedtuple

Result = namedtuple("Result", "count average")

@coroutine
def average():
    print("started")
    total = 0
    count = 0
    average = None
    while True:
        term = yield average
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)


aver = average()
# print(next(aver))
for i in range(0, 100, 13):
    print(aver.send(i))

print(aver.send(40))
print(aver.send(50))
print(aver.send(None))
