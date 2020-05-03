import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it

        This method should return LookupError when instance is empty
        """

    def loaded(self):
        """Return True if at least 1 item False otherwise"""
        return bool(self.inspect)

    def test(self):
        pass

    def inspect(self):
        """Return a sorted touple with the items currently inside"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
