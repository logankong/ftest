from BaseAction import *
from elements.JianceElement import *
import time


class JianceAction(BaseAction, JianceElement):
    def test_top10(self, num=10):
        driver = JianceElement(self.driver)
        driver.get(self.base_url + "/")
        tbody = driver.find_element(*self.tbodyTag)
        i = 1
        while ('Loading...' in tbody.text) or ('' == tbody.text):
            time.sleep(1)
            if i == 30:
                break
            i += 1

        trs = tbody.find_elements(*self.lineTag)
        try:
            for line_tbody in trs:
                value = line_tbody.find_element(*self.valueTag).get_attribute('value')
                host_id, group_id = value.split('_')
                text = line_tbody.text.split()
                data = self.getSql(group_id, host_id)

                try:
                    self.assertEqual(text[3:10], data)
                except AssertionError as e:
                    self.log(e)
                num -= 1
                if num < 1:
                    break
        except AssertionError as e:
            self.log('tbody.text', tbody.text)


if __name__ == "__main__":
    testsuite = unittest.TestSuite()
    testsuite = unittest.TestLoader().loadTestsFromTestCase(JianceAction)
    unittest.TextTestRunner(verbosity=2).run(testsuite)
