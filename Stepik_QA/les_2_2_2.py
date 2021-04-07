from selenium import webdriver
import time
from math import sin, log


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)
    x_el = browser.find_element_by_id('input_value').text
    print(x_el)
    x = calc(x_el)
    print(x)
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_id('robotCheckbox').click()
    rb = browser.find_element_by_id('robotsRule')
    _ = rb.location_once_scrolled_into_view
    rb.click()
    button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    _ = button.location_once_scrolled_into_view
    button.click()
    time.sleep(6)

finally:
    browser.quit()
