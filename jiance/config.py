import os
from selenium import webdriver

APP_DIR = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(APP_DIR + '/reports'):
    os.makedirs(APP_DIR + '/reports')

command_executor = 'http://192.168.99.100:8910'
desired_capabilities = webdriver.DesiredCapabilities.PHANTOMJS

BASE_URL = 'https://www.test.com/'
TOKEN = 'desc3u68p4cdgt5emufgieulm7'
IMPLICITLY_WAIT = 1
WAIT = 20
DOMAIN = 'www.test.com'

DB_HOST = '192.168.99.101'
DB_PORT = 3306
DB_USER = 'user'
DB_PWD = 'passowrd'
DB_NAME = 'test'

TUNNEL_FLAG = 1  # ssh远程跳转开关，0表示不跳转，默认值；1表示跳转

SSH_FORWARDER_HOST = '192.168.99.102'
SSH_FORWARDER_PORT = 22
SSH_FORWARDER_USER = 'user'
SSH_FORWARDER_PWD = 'passowrd'
