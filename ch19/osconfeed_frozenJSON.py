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
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


raw_feed = load()
feed = FrozenJSON(raw_feed)
print(feed.Schedule.keys())
print(len(feed.Schedule.speakers))

for key, value in sorted(feed.Schedule.items()):
        print(f"{len(value)} {key}")

test = FrozenJSON({"name":"Rado", "lastname":"Osredkar", "class":"Rague"})
print(test.name, test.lastname, test.class_)
