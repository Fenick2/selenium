import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

url = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser.get(url=url)
    x_element = browser.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(x_element)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn-default').click()
    time.sleep(10)

finally:
    browser.quit()
