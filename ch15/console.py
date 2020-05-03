from mirror_gen import looking_glass
from mirror import LookingGlass

with LookingGlass() as what:
    print("Alice, Kitty and SnowDrop")
    print(what)

with LookingGlass() as what:
    print(1/0)
    print(what)

print("*" * 100)

with looking_glass() as what:
    print("Alice, Kitty and SnowDrop")
    print(what)

with looking_glass() as what:
    print(1/0)
    print(what)
print("*" * 100)
