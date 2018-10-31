import unittest
import HTMLTestRunner
import time
from ftest.config import *
from ftest.projects.{projectName}.action.{scriptNameU}Action import {scriptNameU}Action


class {projectNameU}():
    def __init__(self):
        self.testsuite = unittest.TestSuite()

    def testAll(self):
        self.testsuite.addTest(unittest.makeSuite({scriptNameU}Action))

        return self.testsuite

if __name__ == "__main__":
    {projectName} = {projectNameU}()
    filename = BASE_DIR + '/projects/{projectName}/reports/html/' + time.strftime("%Y%m%d-%H%M%S") + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试执行情况')
    runner.run({projectName}.testAll())
    fp.close()
