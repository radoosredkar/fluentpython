from log import logger
from collections import deque

dq = deque(range(10), maxlen=10)
logger.info(dq)
dq.append(99)
logger.info(dq)
dq.append(99)
logger.info(dq)
dq.rotate(3)
logger.info(dq)
dq.rotate(-5)
logger.info(dq)
dq.rotate(2)
dq.extendleft(range(10, 40, 10))
logger.info(dq)
