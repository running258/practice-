from selenium import webdriver
import pytest




class TestLogin(object):

    @pytest.fixture
    def login(object):
        browser = webdriver.Chrome()
        browser.get("https://vhsupply.staging.viewchain.net/#/login")
        browser.maximize_window()

        userName = browser.find_element_by_xpath("//input[@id='viewhigh-login-username-input']")
        passWord = browser.find_element_by_xpath("//input[@id='viewhigh-login-pwd-input']")
        loginButton = browser.find_element_by_xpath("//button[@id='viewhigh-login-login-btn']")

        userName.send_keys("zhangleyuan")
        passWord.send_keys("zhangleyuan")
        loginButton.click()
        return browser
    
    def test_loginSuccess(login):
        login().implicitly_wait(5)
        assert login().find_element_by_xpath("//div[@class='header el-row']").is_enabled()
        # browser.close()

