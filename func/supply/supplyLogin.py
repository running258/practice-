import logging
from selenium import webdriver
from common.readYaml import yamlFile
from ele.supply.supplyLoginEle import supplyLoginEle

class supplyLogin(object):
    
    def __init__(self,folder='yamlTestData'):
        #init the browser and login env
        loginData = yamlFile(folder).readYamlFile('\\supplyTestData.yaml')
        self._browser = str(loginData['supply_loginPage']['browser'])
        self._env = str(loginData['supply_loginPage']['env'])
        self._userName = str(loginData['supply_loginPage']['userName'])
        self._passWord = str(loginData['supply_loginPage']['passWord'])

    def login(self):

        if self._browser.lower() == 'chrome':
            browser = webdriver.Chrome()
        else:
            logging.error("the browser shouldn't be %s" % self._browser)
        if self._env == 'test':
            browser.get("https://vhsupply.test.viewchain.net/#/login")
        elif self._env == 'staging':
            browser.get("https://vhsupply.staging.viewchain.net/#/login")
        elif self._env == 'demo':
            browser.get("https://vhsupply.demo.viewchain.net/#/login")
        else:
            logging.error("the env shouldn't be %s" % self._env)
        browser.maximize_window()
        browser.find_element_by_xpath(supplyLoginEle().userName()).send_keys(self._userName)
        browser.find_element_by_xpath(supplyLoginEle().passWord()).send_keys(self._passWord)
        browser.find_element_by_xpath(supplyLoginEle().loginButton()).click()
        return browser
    
