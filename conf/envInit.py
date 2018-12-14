from selenium import webdriver

class envInit(object):

    # def __init__(self,browserName='Chrome'):
    #     if browserName != "Chrome" :
    #         raise Exception("the browser should be Chrome",type)
    #     else:
    #         self.browser = webdriver.Chrome()


    def initBrowser(self,browserName='Chrome'):
        if browserName != "Chrome" :
            raise Exception("the browser should be Chrome",type)
        else:
            return webdriver.Chrome()
        # return 

    def openBrowser(self,env='staging'):
        self.initBrowser()
        # if env == 'staging':
        #     _url = 'https://vhsupply.staging.viewchain.net/#/login'
        # elif env == 'test':
        #     _url = 'https://vhsupply.test.viewchain.net/#/login'
        # elif env == 'demo':
        #     _url = 'https://vhsupply.demo.viewchain.net/#/login'
        # browser.get(_url)
        # browser.maximize_window()
        # return browser