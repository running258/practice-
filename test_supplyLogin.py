import pytest
# from conf.envInit import envInit
from ele.supply.supplyLoginEle import supplyLoginEle
from common.readYaml import yamlFile

testData = yamlFile('yamlTestData').readYamlFile('\\supplyTestData.yaml')

@pytest.fixture(scope='function')
def supply():
    browser = envInit().openBrowser()
    userName = browser.find_element_by_xpath(suppleLoginEle().userName())
    passWord = browser.find_element_by_xpath(suppleLoginEle().passWord())
    loginButton = browser.find_element_by_xpath(suppleLoginEle().loginButton())
    userName.send_keys(testData['supply_loginPage']['userName'])
    passWord.send_keys(testData['supply_loginPage']['passWord'])
    loginButton.click()
    yield browser
    browser.close()

def test_loginSuccess(supply):
    supply.implicitly_wait(5)
    assert supply.find_element_by_xpath(
        "//*[@class='icon icon-caidan']").is_enabled()

