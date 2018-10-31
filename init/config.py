# 配置文件
from ftest.config import *

SERVICE_ARGS = ['--webdriver-logfile=' + BASE_DIR + '/logs/ghostdriver.log', '--disk-cache=true']
BASE_URL = 'https://jiance.360.cn/'
TOKEN = 'desc3u68p4cdgt5emufgieulm7'
IMPLICITLY_WAIT = 2

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PWD = '123456'
DB_NAME = 'world'
