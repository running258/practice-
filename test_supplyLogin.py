from selenium import webdriver
import pytest
from conf.envInit import envInit
from common.readYaml import yamlFile

loginEle = yamlFile().readYamlFile('\\supply\\ele_loginPage.yaml')

@pytest.fixture(scope='function')
def browserLogin():
    browser = envInit().openBrowser()
    userName = browser.find_element_by_xpath(loginEle['supply_loginPage']['userName'])
    passWord = browser.find_element_by_xpath(loginEle['supply_loginPage']['password'])
    loginButton = browser.find_element_by_xpath(loginEle['supply_loginPage']['loginButton'])
    userName.send_keys("zhangleyuan")
    passWord.send_keys("zhangleyuan")
    loginButton.click()
    yield browser
    browser.close()

# TODO   *
def test_loginSuccess(browserLogin):
    browserLogin.implicitly_wait(5)
    assert browserLogin.find_element_by_xpath(
        "//*[@class='icon icon-caidan']").is_enabled()

