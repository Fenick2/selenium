import time
import pyperclip as pyperclip
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


try:
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element_by_tag_name('button').click()
    time.sleep(2)
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)

    x_el = browser.find_element_by_id('input_value').text
    y = calc(x_el)
    browser.find_element_by_id('answer').send_keys(y)
    time.sleep(1)
    browser.find_element_by_tag_name('button').click()
    time.sleep(2)

    alert = browser.switch_to.alert
    al_txt = alert.text
    pyperclip.copy(al_txt.split(': ')[-1])
    alert.accept()

finally:
    browser.quit()
