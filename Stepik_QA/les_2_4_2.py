from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin
import time
import pyperclip as pyperclip

browser = webdriver.Chrome()


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
my_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
browser.find_element_by_id('book').click()

x_el = browser.find_element_by_id('input_value').text
y = calc(x_el)
message = browser.find_element_by_id("answer")
message.send_keys(y)
browser.find_element_by_id('solve').click()
time.sleep(1)

alert = browser.switch_to.alert
al_txt = alert.text
pyperclip.copy(al_txt.split(': ')[-1])
alert.accept()

browser.quit()
