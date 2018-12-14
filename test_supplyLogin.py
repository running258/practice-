from selenium import webdriver
import pytest
from conf.envInit import envInit
from ele.supply.login import loginEle


@pytest.fixture(scope='function')
def browserLogin():
    browser = envInit().openBrowser()
    # loginEle().userName().send_keys("zhangleyuan")
    # loginEle().passWord().send_keys("zhangleyuan")
    # loginEle().loginButton().click()

    # userName = browser.find_element_by_xpath(
    #     "//input[@id='viewhigh-login-username-input']")
    # passWord = browser.find_element_by_xpath(
    #     "//input[@id='viewhigh-login-pwd-input']")
    # loginButton = browser.find_element_by_xpath(
    #     "//button[@id='viewhigh-login-login-btn']")

    # userName.send_keys("zhangleyuan")
    # passWord.send_keys("zhangleyuan")
    # loginButton.click()
    yield browser

# TODO   *
def test_loginSuccess(browserLogin):
    # browserLogin.implicitly_wait(5)
    # assert browserLogin.find_element_by_xpath(
    #     "//div[@class='header el-row2']").is_enabled()
    browserLogin.close()
