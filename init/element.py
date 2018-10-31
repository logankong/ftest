from selenium.webdriver.common.by import By
from ftest.utils.BaseUtil import Base


class {scriptName}Element(Base):
    searchInput = (By.NAME, 'search')
    searchButton = (By.XPATH, "//div[@id='app']/div[3]/div/div/div[3]/div[2]/div[3]/div/a")

    def getTotalNum(self):
        res = self.db.query('select * from test limit 1')
        return str(res[1])
