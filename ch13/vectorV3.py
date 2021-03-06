import math
import reprlib
from array import array
import numbers
import functools
import operator
import itertools


class Vector3d:
    typecode = "d"

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __init__(self, components) -> None:
        self.components = array(self.typecode, components)

    def __iter__(self):
        return iter(self.components)

    def __repr__(self) -> str:
        components = reprlib.repr(self.components)
        components = components[components.find("[") : -1]
        return "Vector3d({})".format(components)

    def __str__(self) -> str:
        return str(tuple(self))

    def __eq__(self, other):
        # return len(self) == len(other) and all(a == b for a, b in zip(self, other))
        if isinstance(other, Vector3d):
            return (len(self) == len(other)) and all(
                a == b for a, b in zip(self, other)
            )
        else:
            return NotImplemented

    def __hash__(self):
        # hashes = (hash(x) for x in self.components)
        hashes = map(hash, self.components)
        return functools.reduce(operator.xor, hashes, 0)

    def __bool__(self):
        return bool(abs(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self.components))

    def __len__(self):
        return len(self.components)

    def __pos__(self):
        return Vector3d(self)

    def __neg__(self):
        return Vector3d(-x for x in self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector3d(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector3d([x * scalar for x in self])
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self.components[index])
        elif isinstance(index, numbers.Integral):
            return self.components[index]
        else:
            msg = f"{cls.__name_} indices must me integers"
            raise TypeError(msg)

        return self.components[index]

    shortcut_names = "xyzt"

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self.components):
                return self.components[pos]
        msg = "{.__name__!r} object has no attribute {!r}"
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = "readonly attribute {arrt_name!r}"
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name}"
            else:
                error = ""
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith("h"):  # hyperspherical coordinates
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = "<{}>"
        else:
            coords = self
            outer_fmt = "({})"
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(", ".join(components))
