from selenium import webdriver
import pytest
from conf.envInit import envInit
# from ele.supply.login import loginEle


@pytest.fixture(scope='function')
def browserLogin():
    browser = envInit().openBrowser()
    userName = browser.find_element_by_xpath(
        "//input[@id='viewhigh-login-username-input']")
    passWord = browser.find_element_by_xpath(
        "//input[@id='viewhigh-login-pwd-input']")
    loginButton = browser.find_element_by_xpath(
        "//button[@id='viewhigh-login-login-btn']")
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
