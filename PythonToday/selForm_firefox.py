import time
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PythonToday.vk_auth import login_inst, pwd_inst


useragent = UserAgent()
option = webdriver.FirefoxOptions()
option.set_preference('general.useragent.override', f"{useragent.random}")

driver = webdriver.Firefox(options=option)

try:
    driver.get(url='https://instagram.com')
    time.sleep(3)

    username_input = driver.find_element_by_name('username')
    username_input.clear()
    username_input.send_keys(login_inst)
    time.sleep(3)

    password_input = driver.find_element_by_name('password')
    password_input.send_keys(pwd_inst)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
