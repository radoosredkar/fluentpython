import itertools
from decimal import Decimal
from fractions import Fraction


def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen


ap = aritprog_gen(0, 1, 2)
print(list(ap))
ap = aritprog_gen(1, 0.5, 3)
print(list(ap))
ap = aritprog_gen(0, 1 / 3, 1)
print(list(ap))
ap = aritprog_gen(0, Fraction(1, 3), 1)
print(list(ap))
ap = aritprog_gen(0, Decimal(".1"), 0.3)
print(list(ap))
