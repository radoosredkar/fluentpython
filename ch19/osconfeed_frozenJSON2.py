from osconfeed import load
from collections import abc
import keyword
import warnings


class FrozenJSON:
    """A read-only facade for navigating a JSON-like objects
       using attribute notation
    """

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                msg = f"keyword found {key}"
                warnings.warn(msg)
                key += "_"
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg


def main():
    raw_feed = load()
    feed = FrozenJSON(raw_feed)
    print(feed.Schedule.keys())
    print(len(feed.Schedule.speakers))

    for key, value in sorted(feed.Schedule.items()):
            print(f"{len(value)} {key}")

    test = FrozenJSON({"name":"Rado", "lastname":"Osredkar", "class":"Rague"})
    print(test.name, test.lastname, test.class_)

if __name__ == "__main__":
    main()
