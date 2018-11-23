from selenium import webdriver


class browserConf(object):
    
    def openBrowser(self):
        browser = webdriver.Chrome()
        browser.get('https://vhsupply.test.viewchain.net/')
        browser.maximize_window()



