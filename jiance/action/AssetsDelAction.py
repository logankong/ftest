from BaseAction import *
from elements.AssetsElement import *
import time
excel = Excel(APP_DIR + '/data/assets.xls', 'assets')


@ddt.ddt
class AssetsDelAction(BaseAction, AssetsElement):
    @ddt.data(*excel.next())
    def test_del_assets(self, data):
        driver = AssetsElement(self.driver)
        driver.get(self.base_url + "/")
        try:
            driver.find_element(*self.guanlizhongxinInput).click()
            driver.find_element(*self.zichanguanliInput).click()
            time.sleep(2)
            driver.find_element(*self.searchInput).send_keys(data['domain'])
            driver.find_element(*self.searchInput).send_keys(Keys.ENTER)
            time.sleep(1)
            driver.find_element(*self.checkboxInput).click()    # 选择需要删除的列
            time.sleep(1)
            driver.find_element(*self.deleteButton).click()  # 点击删除
            time.sleep(1)
            driver.find_element(*self.btnButton).click()  # 确认删除
            time.sleep(1)
            driver.find_element(*self.searchInput).clear()
            driver.find_element(*self.searchInput).send_keys(data['domain'])
            driver.find_element(*self.searchInput).send_keys(Keys.ENTER)
            tbody = driver.find_element(*self.searchName)
            i = 1
            while ('Loading...' in tbody.text) or ('' == tbody.text):
                time.sleep(1)
                if i == 30:
                    break
                i += 1
            self.assertNotIn(data['domain'], tbody.text)
        except AssertionError as e:
            self.log(e)


if __name__ == "__main__":
    testsuite = unittest.TestSuite()
    testsuite = unittest.TestLoader().loadTestsFromTestCase(AssetsDelAction)
    unittest.TextTestRunner(verbosity=2).run(testsuite)
