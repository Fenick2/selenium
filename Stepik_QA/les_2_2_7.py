from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname').send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname').send_keys("Petrov")
    input3 = browser.find_element_by_name('email').send_keys("a@m.ru")

    uploader = browser.find_element_by_id('file')
    open('test.txt', 'a').close()
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    uploader.send_keys(file_path)
    time.sleep(2)
    os.remove('test.txt')

    button = browser.find_element_by_class_name('btn-primary').click()

finally:
    time.sleep(5)
    browser.quit()
