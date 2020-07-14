class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = f"_{prefix}#{index}"
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instace, self.storage_name)

    def __set__(self, instace, value):
        if value > 0:
            instace.__dict__[self.storage_name] = value
        else:
            raise ValueError("value must be > 0")


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtoral(self):
        return self.weight * self.price

    def __str__(self):
        return f"{self.description}"


coconuts = LineItem("Brazilian coconut", 20, 17.95)
print(coconuts)
print(LineItem.weight)
# truffle = LineItem("White Truffle", 100, 0)
truffle = LineItem("", 100, 1)
