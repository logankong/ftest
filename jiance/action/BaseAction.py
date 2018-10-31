import sys
sys.path.append('..')
sys.path.append('../../')
from ftest import *
from config import *


class BaseAction(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(command_executor, desired_capabilities)
        # self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.base_url = BASE_URL
        self.verificationErrors = []
        self.accept_next_alert = True
        self.login(TOKEN)

    def tearDown(self):
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
            'domain': DOMAIN,
            'path': '/',
            'httponly': 'fasle',
            'secure': 'false'})
        driver.get(self.base_url + "/")
        try:
            self.assertEqual("网站云监测", driver.title)
        except AssertionError as e:
            self.log(e)
