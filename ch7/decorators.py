import functools
import html
import numbers
import time
from collections import abc


def deco(func: object) -> object:
    def inner():
        print("Running inner function")

    return inner


@deco
def target():
    print("Running target")


target()
print(target)


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


snooze(1)


@clock
def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)


factorial(10)


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@functools.lru_cache()
@clock
def fibonacci1(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(10)
print("*" * 40)
fibonacci1(10)


# Single dispatch
@functools.singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<pre>{0}</pre>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li></ul>'


print(htmlize('Rado Osredkar'))
print(htmlize(12))
print(htmlize({1, 2, 3, 4}))
print(htmlize(print))
print(htmlize(['alpha', {1, 2, 3}]))

print("*" * 50)


def decorator(active=False):
    def dec(func):
        if active:
            print(func)
        return func
    return dec


@decorator(active=True)
def test():
    print("From test")


test()
