import os
import logging

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

HOST = '0.0.0.0'
PORT = '8000'

REDIS_CON = 'localhost', 6379

DEBUG = True

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.addHandler(console)
