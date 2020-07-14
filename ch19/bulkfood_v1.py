class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError("value must be > 0")


def main():
    raisins = LineItem("Golden Raisins", 10, 6.95)
    walnuts = LineItem("walnuts", 0, 10.00)
    print(raisins.subtotal())
    raisins.weight = -20
    print(raisins.subtotal())


if __name__ == "__main__":
    main()
