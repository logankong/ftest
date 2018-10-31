from ftest import *


class AssetsElement(Base):
    guanlizhongxinInput = (By.LINK_TEXT, '管理中心')
    zichanguanliInput = (By.LINK_TEXT, '资产管理')
    tianjiazichanInput = (By.LINK_TEXT, '添加资产')
    domainInput = (By.ID, 'domain')      # 网站域名或IP
    jigouInput = (By.XPATH, "(//input[@type='text'])[2]")    # 机构名称
    nameInput = (By.XPATH, "(//input[@type='text'])[3]")    # 负责人姓名
    telInput = (By.XPATH, "(//input[@type='text'])[4]")  # 负责人手机
    mailInput = (By.XPATH, "(//input[@type='text'])[5]")  # 负责人邮箱
    saveButton = (By.LINK_TEXT, '保存资产')
    searchInput = (By.NAME, 'search')
    searchButton = (By.XPATH, '//*[@id="app"]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/a')
    searchCheckbox = (By.CLASS_NAME, 'checkbox')
    searchName = (By.TAG_NAME, 'tbody')
    searchLine = (By.NAME, 'tr')
    checkboxInput = (By.CSS_SELECTOR, 'input.checkbox')
    deleteButton = (By.CSS_SELECTOR, 'a.batch-btn.red')
    btnButton = (By.CSS_SELECTOR, 'button.btn.btn-default')


