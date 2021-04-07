from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
url = 'http://suninjuly.github.io/selects2.html'

try:
    driver.get(url=url)
    num1 = driver.find_element_by_id('num1').text
    num2 = driver.find_element_by_id('num2').text
    res = str(int(num1) + int(num2))

    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_value(res)

    driver.find_element_by_class_name('btn-default').click()
    time.sleep(5)
finally:
    driver.quit()
