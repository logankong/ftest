from ftest.projects.{projectName}.action.BaseAction import *
from ftest.projects.{projectName}.elements.{scriptNameU}Element import *


class {scriptNameU}Action(BaseAction, {scriptNameU}Element):
    def test_{scriptName}(self):
        driver = {scriptNameU}Element(self.driver)
        driver.get(self.base_url + "/")

        driver.find_element(*self.xxx).send_keys('xxx')
        driver.find_element(*self.xxx).click()

        expect = data['xxx']  # expect = self.getSql()
        actual = driver.find_element(By.xxx, 'xxx')

        try:
            self.assertEqual(expect, actual.text)
        except AssertionError as e:
            self.log(e)

if __name__ == "__main__":
    testsuite = unittest.TestSuite()
    testsuite = unittest.TestLoader().loadTestsFromTestCase({scriptNameU}Action)
    unittest.TextTestRunner(verbosity=2).run(testsuite)
