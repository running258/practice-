from selenium import webdriver
from conf.envInit import envInit

class loginEle(envInit):

    # def __init__(self):
    #     self.browser = envInit()

    def userName(self):

        return webdriver.DesiredCapabilities.Chrome().find_element_by_xpath("//input[@id='viewhigh-login-username-input']")

    def passWord(self):
        self.browser.find_element_by_xpath("//input[@id='viewhigh-login-pwd-input']")

    def loginButton(self):
        self.browser.find_element_by_xpath("//input[@id='viewhigh-login-login-btn']")

