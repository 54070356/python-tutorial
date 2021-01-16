import logging
import sys

from flask import Flask

console_handler = logging.StreamHandler(sys.stdout)
# https://youtrack.jetbrains.com/issue/PY-39762
# noinspection PyArgumentList
logging.basicConfig(
    level=logging.INFO,
    #format="%(asctime)s.%(msecs)03d %(levelname)s %(process)d --- [%(threadName)s] %(filename)s : %(message)s",
    format="%(asctime)s.%(msecs)03d [%(threadName)s] %(levelname)s %(filename)s:%(lineno)d - %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[console_handler]
)

log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)
app = Flask(__name__)


@app.route('/service', methods=['POST'])
def serve():
    logging.info('handle request')
    return {'msg': 'hello'}
