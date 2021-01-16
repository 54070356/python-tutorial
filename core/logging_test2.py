import logging
import os
from logging.handlers import RotatingFileHandler


if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(process)d --- [%(threadName)s] %(filename)s : %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("hello %s, %s", 'a', 'b')


