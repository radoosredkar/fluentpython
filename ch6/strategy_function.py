import inspect
from abc import ABC, abstractmethod
from collections import namedtuple
import ch6.promos
from ch6.promos import fidelity_promo, large_order_promo, bulk_item_promo

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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self) -> str:
        fmt = "<Order Total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


promos = [
    func for name, func in
    inspect.getmembers(ch6.promos, inspect.isfunction)
]


def best_promo(order):
    """Select best discount avaliable"""
    return max(promo(order) for promo in promos)


def main():
    joe = Customer("John Doe", 0)
    ann = Customer("Ann Smith", 1100)
    cart = [
        LineItem("Banana", 4, .5),
        LineItem("Apple", 10, 1.5),
        LineItem("Watermelon", 5, 5.0)
    ]
    print(Order(joe, cart, fidelity_promo))
    print(Order(ann, cart, fidelity_promo))

    large_order = [
        LineItem(str(item), 1, 1) for item in range(20)
    ]

    print(Order(joe, large_order, large_order_promo))
    print(Order(joe, large_order, best_promo))


if __name__ == '__main__':
    main()
