class DemoException(Exception):
    """An Exception Type for demonstration"""

def demo_exc_handling():
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except DemoException:
            print("*** DemoException Handled. Continuing,...")
        else:
            print("-> coroutine received:{!r}".format(x))
    raise RuntimeError("This line should never run")

exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.send(22)
exc_coro.close()
from inspect import getgeneratorstate
print(getgeneratorstate(exc_coro))
exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException())
print(getgeneratorstate(exc_coro))
exc_coro.send(11)
# exc_coro.throw(ZeroDivisionError())

def demo_exc_handling_finally():
    print("-> coroutine started")
    while True:
        try:
            x = yield
        except DemoException:
            print("*** DemoException Handled. Continuing,...")
        else:
            print("-> coroutine received:{!r}".format(x))
        finally:
            print("-> coroutine ending")
    raise RuntimeError("This line should never run")

print("*" * 100)
exc_coro = demo_exc_handling_finally()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException())
print(getgeneratorstate(exc_coro))
