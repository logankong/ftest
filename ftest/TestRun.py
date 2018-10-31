import sys
import time
sys.path.append('../ftest')
import HTMLTestRunner
from ftest.config import *


class TestRun():
    def __init__(self, testCase, title='测试报告', description='测试执行情况'):
        APP_DIR = app_path
        filename = APP_DIR + '/reports/' + time.strftime("%Y%m%d-%H%M%S") + '.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=title, description=description)
        runner.run(testCase)
        fp.close()
