from log import logger

import array

numbers = array.array('h', list(range(-2, 3)))
logger.info("numbers %s", numbers)

memview = memoryview(numbers)
logger.info("memview len=>%s, [0]=>%s", len(memview), memview[0])
