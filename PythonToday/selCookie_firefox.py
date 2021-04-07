import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PythonToday.vk_auth import login_inst, pwd_inst


driver = webdriver.Firefox()

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

    # cookies
    pickle.dump(driver.get_cookies(), open(f'{login_inst}_cookies', 'wb'))

    # for cookie in pickle.load(open(f'{login_inst}_cookies', 'rb')):
    #     driver.add_cookie(cookie)
    #
    # time.sleep(5)
    # driver.refresh()
    # time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
