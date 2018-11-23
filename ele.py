from selenium import webdriver
from browserDefine import browserConf




    # class LoginEle(browserConf):
    #     pass


# browserConf().openBrowser()

class LoginPage(browserConf):
    userName = "//input[@id='viewhigh-login-username-input']"
    def LoginPage_UserName(self):
        pass



print(LoginPage().userName)



browser.element.action