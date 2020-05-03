import random
from typing import Mapping, overload, Iterable, Tuple

from log import logger
import collections

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'), ]

country_code = {country: code for country, code in DIAL_CODES}
logger.info(country_code.pop(81, '-999'))
for k, v in sorted(country_code.items()):
    print("%s=>%s" % (v, k))
    

country_code = {code: country for code, country in country_code.items() if code > 55}
logger.info(country_code)
for k, v in sorted(country_code.items()):
    print("%s=>%s" % (v, k))

logger.info(country_code.popitem())

# count words
# not so beautiful updating with get
words = "And now I will do it and then I will not".split()
index = dict()
for word in words:
    occurances = index.get(word, [])
    occurances.append(word)
    index[word.lower()] = occurances
logger.info(index)

# better updating with setdefault
index = dict()
for word in words:
    index.setdefault(word.lower(), []).append(word)
logger.info(index)

# better updating with defaultdict
index = collections.defaultdict(list)
for word in words:
    index[word.lower()].append(word)
logger.info(index)


# __missing__ method and create key when not existing


class UserDIct(dict):
    def __missing__(self, key):
        self[key] = "def%s" % random.randint(1, 10000)
        return self[key]


user_dict = UserDIct()
user_dict["1"] = 123
logger.info(user_dict)
logger.info(user_dict["test"])
logger.info(user_dict)