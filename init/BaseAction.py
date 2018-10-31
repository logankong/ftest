import unittest
import ddt
import HTMLTestRunner
from selenium import webdriver
from ftest.utils.DbUtils import DB
from ftest.utils.ExcelUtil import ExcelUtil
from ftest.projects.{projectName}.config import *


class BaseAction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS(service_args=SERVICE_ARGS)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.base_url = BASE_URL
        self.verificationErrors = []
        self.accept_next_alert = True
        self.login(TOKEN)
        self.db = DB(DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME)

    def tearDown(self):
        self.db.closeMysql()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def login(self, cookie):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.delete_all_cookies()
        driver.add_cookie({
            'name': 'PHPSESSID',
            'value': cookie,
            'session': 'true',
            'domain': 'jiance.360.cn',
            'path': '/',
            'httponly': 'fasle',
            'secure': 'false'})
        driver.get(self.base_url + "/")
        try:
            self.assertEqual("360网站云监测", driver.title)
        except AssertionError as e:
            self.log(e)
