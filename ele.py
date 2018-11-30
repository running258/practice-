from selenium import webdriver
from browserDefine import browserConf




    # class LoginEle(browserConf):
    #     pass


# browserConf().openBrowser()

class LoginPage(browserConf):

    def __init__(self):
        self.browser = webdriver.Chrome()

    def LoginPage_UserName(self):
        self.browser.find_element_by_xpath("//input[@id='viewhigh-login-username-input']").send_keys("zhangleyuantest")
        return self
    def LoginPage_Password(self):
        return self



# print(LoginPage().LoginPage_UserName())
browserConf().openBrowser()
LoginPage().LoginPage_UserName()


