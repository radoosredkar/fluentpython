def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError("value must be > 0")

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity("weight")
    price = quantity("price")

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def main():
    raisins = LineItem("Golden Raisins", 10, 6.95)
    walnuts = LineItem("walnuts", 0, 10.00)
    print(raisins.subtotal())
    raisins.weight = -20
    print(raisins.subtotal())


if __name__ == "__main__":
    main()
