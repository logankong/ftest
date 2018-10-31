from ftest import *


class SearchElement(Base):
    searchInput = (By.NAME, 'search')
    searchButton = (By.XPATH, "//div[@id='app']/div[3]/div/div/div[3]/div[2]/div[3]/div/a")
    searchName = (By.TAG_NAME, 'tbody')
    searchLine = (By.TAG_NAME, 'tr')
    checkboxName = (By.CSS_SELECTOR, 'input.checkbox', 90)
    refreshJs = '''return  new DM.timer(function(){
                                vm.initData();
                            });'''
    tbodyTag = (By.TAG_NAME, 'tbody')
