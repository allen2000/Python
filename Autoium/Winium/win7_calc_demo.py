# coding: utf-8
from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://localhost:9999',
    desired_capabilities={
        "debugConnectToRunningApp": 'false',
        "app": r"C:/windows/system32/calc.exe"
    })

window = driver.find_element_by_class_name('CalcFrame')

window.find_element_by_id('137').click()
window.find_element_by_id('93').click()
window.find_element_by_id('138').click()
window.find_element_by_id('121').click()

result = window.find_element_by_id('150')

print(result.get_attribute('Name'))
assert result.get_attribute('Name')=='15'

driver.close()