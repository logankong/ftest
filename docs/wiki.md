from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))
try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

# 获取tle
    driver.title

# 输入
    inputElement.send_keys("cheese!")

# 获取控件
    | :------                           | -----:        | :-------:         |
    | find_element_by_id                | find_element  | ID                |
    | find_element_by_tag_name          | find_element  | TAG_NAME          |
    | find_element_by_name              | find_element  | NAME              |
    | find_element_by_link_text         | find_element  | LINK_TEXT         |
    | find_element_by_partial_link_text | find_element  | PARTIAL_LINK_TEXT |
    | find_element_by_css_selector      | find_element  | CSS_SELECTOR      |
    | find_elements_by_xpath            | find_elements | XPATH             |
    | find_elements_by_class_name       | find_elements | CLASS_NAME        |
    | find_elements_by_tag_name         |               |                   |

## ID
    element = driver.find_element_by_id("coolestWidgetEvah")
    element = driver.find_element(by=By.ID, value="coolestWidgetEvah")

## class_name
    cheeses = driver.find_elements_by_class_name("cheese")
    cheeses = driver.find_elements(By.CLASS_NAME, "cheese")

## tag_name
    frame = driver.find_element_by_tag_name("iframe")
    frame = driver.find_element(By.TAG_NAME, "iframe")

## name
    cheese = driver.find_element_by_name("cheese")
    cheese = driver.find_element(By.NAME, "cheese")

## link
    cheese = driver.find_element_by_link_text("cheese")
    cheese = driver.find_element(By.LINK_TEXT, "cheese")

## partial_link
    cheese = driver.find_element_by_partial_link_text("cheese")
    cheese = driver.find_element(By.PARTIAL_LINK_TEXT, "cheese")

## css
    cheese = driver.find_element_by_css_selector("#food span.dairy.aged")
    cheese = driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")

## xpath
    inputs = driver.find_elements_by_xpath("//input")
    inputs = driver.find_elements(By.XPATH, "//input")

# 使用JS
    labels = driver.find_elements_by_tag_name("label")
    inputs = driver.execute_script(
        "var labels = arguments[0], inputs = []; for (var i=0; i < labels.length; i++){" +
        "inputs.push(document.getElementById(labels[i].getAttribute('for'))); } return inputs;", labels)

# 获取text
    element = driver.find_element_by_id("element_id")
    element.text

# 表单操作
    select = driver.find_element_by_tag_name("select")
    allOptions = select.find_elements_by_tag_name("option")
    for option in allOptions:
        print "Value is: " + option.get_attribute("value")
        option.click()


## available since 2.12
    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element_by_tag_name("select"))
    select. ()
    select.select_by_visible_text("Edam")

    driver.find_element_by_id("submit").click()

    element.submit()

# 窗口切换
    driver.switch_to.window("windowName")

    for handle in driver.window_handles:
        driver.switch_to.window(handle)

# frame切换
    driver.switch_to.frame("frameName")

# 对话框操作
    alert = driver.switch_to.alert
>usage: alert.dismiss(), etc.

# 跳转
    driver.forward()
    driver.back()

# 打开URL
    driver.get("http://www.example.com")

# Cookie操作
    driver.add_cookie({'name':'key', 'value':'value', 'path':'/'})
>additional keys that can be passed in are:
'domain' -> String,
'secure' -> Boolean,
'expiry' -> Milliseconds since the Epoch it should expire.

## 打印所有cookie
    for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])

## 删除Cookies
### 通过名字
    driver.delete_cookie("CookieName")
### 全部删除
    driver.delete_all_cookies()


# 拖拽
    from selenium.webdriver.common.action_chains import ActionChains
    element = driver.find_element_by_name("source")
    target =  driver.find_element_by_name("target")
    ActionChains(driver).drag_and_drop(element, target).perform()

# PhantJS参数设置
    from selenium import webdriver
    from selenium.webdriver import DesiredCapabilities
    driver=webdriver.PhantomJS(executable_path='存放路径\phantomjs.exe')

    desired_capabilities= DesiredCapabilities.PHANTOMJS.copy()
    headers = {'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',#这种修改 UA 也有效
    'Connection': 'keep-alive'
    'Referer':'http://www.baidu.com/'}

    for key, value in headers.iteritems():
        desired_capabilities['phantomjs.page.customHeaders.{}'.format(key)] = value
    desired_capabilities['phantomjs.page.customHeaders.User-Agent'] ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    driver= webdriver.PhantomJS(desired_capabilities=desired_capabilities)

    driver.get("http://www.myip.cn/judge.php")
    print driver.page_source
