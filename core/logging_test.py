import logging
import os
from logging.handlers import RotatingFileHandler

print('jell')
logging.info("hello %s, %s", 'a', 'b')

if not os.path.exists('logs'):
    os.makedirs('logs')

#rotating_file_handler = RotatingFileHandler('logs/log.txt', maxBytes=20, backupCount=10)

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s.%(msecs)03d %(levelname)s %(process)d --- [%(threadName)s] %(filename)s : %(message)s",
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers=[rotating_file_handler]
# )

person = {
    "id":'id1',
    "name": 'Jack'
}

