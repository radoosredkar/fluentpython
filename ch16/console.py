from inspect import getgeneratorstate


def simple_coroutine():
    print("->coroutine started")
    x = yield
    print("->coroutine received:", x)


try:
    my_coro = simple_coroutine()
    print(my_coro)
    next(my_coro)
    my_coro.send(42)
except StopIteration as e:
    print("error: StopIteration")


def simple_coroutine2(a):
    print("->coroutine started", a)
    b = yield a
    print("->coroutine received b", b)
    c = yield (a + b)
    print("->coroutine received c", c)


my_coro2 = simple_coroutine2(14)
print(getgeneratorstate(my_coro2))
print(next(my_coro2))
print(getgeneratorstate(my_coro2))
print(my_coro2.send(28))
# print(my_coro2.send('test'))

print("*" * 100)
def gen():
    yield from range(10)

print(list(gen()))

def chain(*iterables):
    for it in iterables:
        yield from it

s = "ABC"
t = tuple(range(3))
print(list(chain(s,t)))
