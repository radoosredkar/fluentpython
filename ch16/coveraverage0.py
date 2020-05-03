from coroutil import coroutine

@coroutine
def average():
    print("started")
    total = 0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


aver = average()
# print(next(aver))
for i in range(0, 100, 13):
    print(aver.send(i))

aver = average()
print(aver.send(40))
print(aver.send(50))
print(aver.send('spam'))
