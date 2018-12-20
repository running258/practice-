import pytest
from common.readYaml import yamlFile
from func.supply.supplyLogin import supplyLogin
from func.hospital.hospitalLogin import hospitalLogin


def test_hospitalCreateOrder():
    hospitalPage = hospitalLogin().login()
    

def test_loginSuccess(supply):
    supply.implicitly_wait(5)
    assert supply.find_element_by_xpath(
        "//*[@class='icon icon-caidan']").is_enabled()


