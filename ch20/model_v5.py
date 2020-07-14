import abc


class AutoStorage:
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
            return getattr(instance, self.storage_name)

    def __set__(self, instace, value):
        setattr(instace, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):
    def __set__(self, instace, value):
        value = self.validate(instace, value)
        super().__set__(instace, value)

    @abc.abstractmethod
    def validate(self, instace, value):
        """return validated or raise ValueError"""


class Quantity(Validated):
    """A number greater than zero"""

    def validate(self, instace, value):
        if value < 0:
            raise ValueError("value must be > 0")
        return value


class NonBlank(Validated):
    """a string with at least one non-space character"""

    def validate(self, instace, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError("value cannot be empty or blank")
        return value
