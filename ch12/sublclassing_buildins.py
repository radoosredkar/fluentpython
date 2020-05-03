import collections


class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


DD = DoppelDict(one=1)
print(DD)
DD["two"] = 2
print(DD)
DD.update(three=3)
print(DD)
print("*" * 20)
DD = DoppelDict2(one=1)
print(DD)
DD["two"] = 2
print(DD)
DD.update(three=3)
print(DD)


class AnswerDict(dict):
    def __getitem__(self, key):
        return 42

class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict(a="foo")
print(ad)
d = {}
d.update(ad)
print(ad)
d["a"] = "foo"
print(ad)

print("*" * 20)
ad = AnswerDict2(a="foo")
print(ad)
d = {}
d.update(ad)
print(ad)
d["a"] = "foo"
print(ad)
