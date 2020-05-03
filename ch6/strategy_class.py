from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.price = price
        self.quantity = quantity
        self.product = product

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer: Customer, cart, promotion=None) -> None:
        self.promotion = promotion
        self.cart = list(cart)
        self.customer = customer

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            return 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self) -> str:
        fmt = "<Order Total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


class Promotion(ABC):

    @abstractmethod
    def discount(self, order: Order):
        """Return discount as positive dollar amount"""


class FidelityPromo(Promotion):
    """5% discount for customers with 1000 or more fidelity points"""

    def discount(self, order: Order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """10 % discount for each LineItem with 20 or more units"""

    def discount(self, order: Order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount + item.total() * .1
        return discount


class LargeOrderPromo(Promotion):
    """7 % discount for orders with 10 or more distinct items"""

    def discount(self, order: Order):
        disitnct_items = {item.product for item in order.cart}
        if len(disitnct_items) >= 10:
            return order.total() * .07
        return 0


def main():
    joe = Customer("John Doe", 0)
    ann = Customer("Ann Smith", 1100)
    cart = [
        LineItem("Banana", 4, .5),
        LineItem("Apple", 10, 1.5),
        LineItem("Watermelon", 5, 5.0)
    ]
    print(Order(joe, cart, FidelityPromo()))
    print(Order(ann, cart, FidelityPromo()))

    large_order = [
        LineItem(str(item), 1, 1) for item in range(20)
    ]

    print(Order(joe, large_order, LargeOrderPromo()))


if __name__ == '__main__':
    main()
