from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://vhsupply.test.viewchain.net/')
browser.maximize_window()

userName = browser.find_element_by_xpath("//input[@id='viewhigh-login-username-input']")
password = browser.find_element_by_xpath("//input[@id='viewhigh-login-pwd-input']")
loginButton = browser.find_element_by_xpath("//button[@id='viewhigh-login-login-btn']")

userName.send_keys("zhangleyuantest")
password.send_keys("zhangleyuantest")
loginButton.click()

browser.implicitly_wait(5)
createPickUpButton = browser.find_element_by_xpath("//span[contains(text(),'生成拣货单')]")

assert createPickUpButton.is_enabled(), 'ele is not displayed'

browser.quit()


