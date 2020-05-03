# create, save and load big array of numbers
import bisect
from sys import stdout
from array import array
from random import randrange, random
from log import logger

# sort array
nums = array('d', (randrange(1, 1000) for i in range(1000)))
logger.info('unsorted array %s', nums)
snums = array(nums.typecode, sorted(nums))
logger.info('sorted array %s', snums)

# insert sorted
bisect.insort(snums, -1)
logger.info('sorted array %s', snums)


logger.info('remove exit to exec whole file')
exit() # too long execution after that


floats = array('d', (random() for i in range(10 ** 7)))
logger.info('Array created %s %s', floats[-3:-1], len(floats))

logger.info('Array to file start')
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
logger.info('Array to file end')

floats = array('d')

logger.info('Reading cleared len=%s', len(floats))
logger.info('Reading Array from file start')
fp = open('floats.bin', 'rb')
floats.fromfile(fp, 10 ** 7)
logger.info('Reading Array from file end %s %s', floats[-3:-1], len(floats))

