import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from ftest.config import *


class Base():
    def __init__(self, webDriver):
        self.driver = webDriver
        self.driver.app_path = app_path
        self.operWait = 3

    def maximize_window(self):
        return self.driver.maximize_window

    def set_page_load_timeout(self, time_to_wait):
        return self.driver.set_page_load_timeout(time_to_wait)

    def set_script_timeout(self, time_to_wait):
        return self.driver.set_script_timeout(time_to_wait)

    def execute_script(self, locate, *args):
        self.driver.execute_script(locate, *args)

    def find_elements(self, *locate):
        wait = WAIT
        if len(locate) == 3:
            wait = locate[2]
            locate = (locate[0], locate[1])

        try:
            WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(locate))
            return self.driver.find_element(*locate)
        except:
            self.log(locate, True)

    def find_element(self, *locate):
        wait = WAIT
        if len(locate) == 3:
            wait = locate[2]
            locate = (locate[0], locate[1])

        try:
            WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(locate))
            return self.driver.find_element(*locate)
        except:
            self.log(locate, True)

    def screenShots(self):
        filePath = self.driver.app_path + '/reports/logs/'
        if not os.path.exists(filePath):
            os.makedirs(filePath)

        self.driver.maximize_window()
        imageName = time.strftime("%Y%m%d-%H%M%S") + '.png'
        self.driver.save_screenshot(filePath + imageName)

        return imageName

    def log(self, result, element=False):
        if not hasattr(self.driver, 'app_path'):
            self.driver.app_path = os.path.dirname(os.path.dirname(
                os.path.realpath(sys._getframe(1).f_code.co_filename)))

        self.verificationErrors = []
        self.verificationErrors.append(str(result))

        if element:
            selfStr = str(self).split(' ')[0].split('.')
            elementStr = selfStr[2]
            result = '%s 中未能匹配到: %s' % (elementStr, result)
        else:
            actionStr = str(self).split(' ')[1].split('.')[1].split(')')[0]
            result = actionStr + ' 中断言失败: ' + str(result)
        print(result)
        imageName = self.screenShots()

        filePath = self.driver.app_path + '/reports/logs/'
        if not os.path.exists(filePath):
            os.makedirs(filePath)

        filename = filePath + time.strftime("%Y%m%d") + '.log'
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write('[' + time.strftime("%Y-%m-%d %H:%M:%S") + '] ' + imageName + ' ' + result + '\n')
            f.close()

    def find_element_by_link_text(self, locate):
        return self.driver.find_element_by_link_text(locate)

    def find_element_by_tag_name(self, locate):
        return self.driver.find_element_by_tag_name(locate)

    def get(self, url):
        self.driver.get(url)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def add_cookie(self):
        self.driver.add_cookie()

    def checkUrl(self):
        pass

    def checkImg(self):
        pass

    def checkJs(self):
        pass

    def checkCss(self):
        pass

    def checkLoadTime(self):
        pass

    def checkConsoleError(self):
        pass

    def click(self, *locate):
        self.find_element(*locate).click()

    def clear(self, *locate):
        self.find_element(*locate).clear()

    def send(self, *locate):
        value = locate[2]
        locate = (locate[0], locate[1])
        self.clear(*locate)
        self.find_element(*locate).send_keys(value)
        sleep(self.operWait)

    def wait(self, secs):
        self.driver.implicitly_wait(secs)

    def set_window(self, wide, high):
        self.driver.set_window_size(wide, high)

    def right_click(self, *locate):
        element = self.find_element(*locate)
        ActionChains(self.driver).context_click(element).perform()

    def move_to_element(self, *locate):
        element = self.find_element(*locate)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, *locate):
        element = self.find_element(*locate)
        ActionChains(self.driver).double_click(element).perform()

    def drag_and_drop(self, *locate):
        locate1 = locate[0]
        locate2 = locate[1]

        element = self.find_element(*locate1)
        target = self.find_element(*locate2)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def get_display(self, *locate):
        return self.find_element(*locate).is_displayed()

    def refresh(self):
        self.driver.refresh()
        self.driver.implicitly_wait(10)

    def list_to_str(self, string):
        str_symptom = str(string).replace('u\'', '\'')
        return str_symptom.decode("unicode-escape")

    def get_text(self, *locate):
        return self.find(*locate).text

    def get_url(self, url):
        return self.driver.get(url)

    def get_title(self, url):
        self.driver.get(url)
        return self.driver.title
