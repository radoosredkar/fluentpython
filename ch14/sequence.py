import sentry_sdk

sentry_sdk.init("https://69883043d6624adbb1559896b537d714@sentry.io/5183667")
import re
import reprlib

RE_WORD = re.compile("\w+")


class Sequence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)


s = Sequence('"The time has come" the Valrus said')
print(s, len(s))
for word in s:
    print(word)
print(list(s))

it = iter(s)
for i in range(len(s) + 1):
    print(next(it))
