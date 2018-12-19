import logging
from selenium import webdriver
from ele.supply.supplyLoginEle import supplyLoginEle
# from common.readYaml import yamlFile

# class supplyLogin(object):
    
#     def __init__(self,folder='yamTestData'):
#         #init the browser and login env
#         loginData = yamlFile(folder).readYamlFile('\\supplyTestData.yaml')
#         self._browser = str(loginData['supply_loginPage']['browser'])
#         self._env = str(loginData['supply_loginPage']['env'])
#         self._userName = str(loginData['supply_loginPage']['userName'])
#         self._passWord = str(loginData['supply_loginPage']['passWord'])

#     def login(self):

#         if self._browser.lower() == 'chrome':
#             browser = webdriver.Chrome()
#         else:
#             logging.error("the browser shouldn't be %s" % self._browser)

#         if self._env == 'test':
#             browser.get("https://vhsupply.test.viewchain.net/#/login")
#         elif self._env == 'staging':
#             browser.get("https://vhsupply.staging.viewchain.net/#/login")
#         elif self._env == 'demo':
#             browser.get("https://vhsupply.demo.viewchain.net/#/login")
#         else:
#             logging.error("the env shouldn't be %s" % self._env)


#         return browser
    
