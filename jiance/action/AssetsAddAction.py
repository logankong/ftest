from BaseAction import *
from elements.AssetsElement import *
import time
excel = Excel(APP_DIR + '/data/assets.xls', 'assets')


@ddt.ddt
class AssetsAddAction(BaseAction, AssetsElement):
    @ddt.data(*excel.next())
    def test_add_assets(self, data):
        driver = AssetsElement(self.driver)
        driver.get(self.base_url + "/")
        try:
            driver.find_element(*self.guanlizhongxinInput).click()
            driver.find_element(*self.zichanguanliInput).click()
            driver.find_element(*self.tianjiazichanInput).click()
            driver.find_element(*self.domainInput).send_keys(data['domain'])
            driver.find_element(*self.jigouInput).send_keys(data['jigou'])
            driver.find_element(*self.nameInput).send_keys(data['name'])
            driver.find_element(*self.telInput).send_keys(data['tel'])
            driver.find_element(*self.mailInput).send_keys(data['mail'])
            driver.find_element(*self.saveButton).click()
            time.sleep(1)
            driver.find_element(*self.searchInput).send_keys(data['domain'])
            driver.find_element(*self.searchInput).send_keys(Keys.ENTER)
            tbody = driver.find_element(*self.searchName)
            i = 1
            while ('Loading...' in tbody.text) or ('' == tbody.text):
                time.sleep(1)
                if i == 30:
                    break
                i += 1
            self.assertIn(data['domain'], tbody.text)
        except AssertionError as e:
            self.log(e)


if __name__ == "__main__":
    testsuite = unittest.TestSuite()
    testsuite = unittest.TestLoader().loadTestsFromTestCase(AssetsAction)
    unittest.TextTestRunner(verbosity=2).run(testsuite)
