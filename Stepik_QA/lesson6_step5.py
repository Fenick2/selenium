import math
import time
from selenium import webdriver

url = 'http://suninjuly.github.io/find_link_text'
browser = webdriver.Chrome()
browser.get(url)
link = str(math.ceil(math.pow(math.pi, math.e) * 10000))
browser.find_element_by_link_text(link).click()
try:
    input1 = browser.find_element_by_name('first_name').send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name').send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city').send_keys("Smolensk")
    input4 = browser.find_element_by_id('country').send_keys("Russia")
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(20)
    browser.quit()
