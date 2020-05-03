import random

from log import logger

needles = [random.randint(1, 1000) for i in range(1, 100)]
haystack = [random.randint(1, 1000) for i in range(1, 100000)]
needles_found = len(set(needles) & set(haystack))

print("Found %s needles" % (needles_found))

needles_found = len(set(needles).intersection(haystack))

print("Found %s needles" % (needles_found))

lst = [random.randint(1, 100) for i in range(30)]
logger.info("len list %s", len(lst))

st = {i for i in lst}
logger.info("len set %s", len(st))
