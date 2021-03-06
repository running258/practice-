import pytest
from common.readYaml import yamlFile
from func.supply.supplyLogin import supplyLogin


@pytest.fixture(scope='function')
def supply():
    supplyPage = supplyLogin().login()
    yield supplyPage
    supplyPage.close()

def test_loginSuccess(supply):
    supply.implicitly_wait(5)
    assert supply.find_element_by_xpath(
        "//*[@class='icon icon-caidan']").is_enabled()



