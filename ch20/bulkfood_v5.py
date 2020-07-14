import model_v5 as model


class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def __str__(self):
        return f"{self.description}:{self.subtotal()}"

coconuts = LineItem("Brazilian coconut", 20, 17.95)
print(coconuts)
# truffle = LineItem("White Truffle", 100, 0)
truffle = LineItem("Truffle", 100, 1)
print(truffle)
