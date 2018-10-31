from BaseAction import *
from elements.SearchElement import *
import time
excel = Excel(APP_DIR + '/data/search.xls', 'search')


@ddt.ddt
class SearchAction(BaseAction, SearchElement):
    @ddt.data(*excel.next())
    def test_search(self, data):
        driver = SearchElement(self.driver)
        driver.get(self.base_url + "/")

        tbody = driver.find_element(*self.tbodyTag)
        i = 1
        while ('Loading...' in tbody.text) or ('' == tbody.text):
            time.sleep(1)
            if i == 30:
                break
            i += 1

        driver.find_element(*self.searchInput).send_keys(data['content'])
        driver.find_element(*self.searchButton).click()
        time.sleep(2)
        driver.find_element(*self.checkboxName)
        tbody = driver.find_element(*self.searchName)
        tbody_trs = tbody.find_elements(*self.searchLine)
        for tbody_tr in tbody_trs:
            try:
                self.assertTrue(data['content'] in tbody_tr.text)
            except AssertionError as e:
                self.log(e)


if __name__ == "__main__":
    testsuite = unittest.TestSuite()
    testsuite = unittest.TestLoader().loadTestsFromTestCase(SearchAction)
    unittest.TextTestRunner(verbosity=2).run(testsuite)
