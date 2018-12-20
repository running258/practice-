import logging
from selenium import webdriver
from common.readYaml import yamlFile
from ele.hospital.hospitalLoginEle import hospitalLoginEle

class hospitalLogin(object):
    
    def __init__(self,folder='yamlTestData'):
        #init the browser and login env
        loginData = yamlFile(folder).readYamlFile('\\hospitalTestData.yaml')
        self._browser = str(loginData['hospital_loginPage']['browser'])
        self._env = str(loginData['hospital_loginPage']['env'])
        self._userName = str(loginData['hospital_loginPage']['userName'])
        self._passWord = str(loginData['hospital_loginPage']['passWord'])

    def login(self):

        if self._browser.lower() == 'chrome':
            browser = webdriver.Chrome()
        else:
            logging.error("the browser shouldn't be %s" % self._browser)
        if self._env == 'test':
            browser.get("https://hosp-cloud.test.viewchain.net/#/login")
        elif self._env == 'staging':
            browser.get("https://hosp-cloud.staging.viewchain.net/#/login")
        elif self._env == 'demo':
            browser.get("https://hosp-cloud.demo.viewchain.net/#/login")
        else:
            logging.error("the env shouldn't be %s" % self._env)
        browser.maximize_window()
        browser.find_element_by_xpath(hospitalLoginEle().userName()).send_keys(self._userName)
        browser.find_element_by_xpath(hospitalLoginEle().passWord()).send_keys(self._passWord)
        browser.find_element_by_xpath(hospitalLoginEle().loginButton()).click()
        return browser
    
