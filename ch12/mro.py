class A:
    def ping(self):
        print("ping", self)


class B:
    def pong(self):
        print("pong", self)


class C(A):
    def pong(self):
        print(self)


class D(B, C):
    def ping(self):
        super().ping()  # or A.ping(self)
        print("post-ping", self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


d = D()
print(d.pong())
print(C.pong(d))
print(D.__mro__)
print(f"pingpong {'*' * 50}")
print(d.pingpong())
print(d.pingpong())


def print_mro(cls):
    print(", ".join((c.__name__ for c in cls.__mro__)))


print_mro(bool)

import io

print_mro(io.BytesIO)
