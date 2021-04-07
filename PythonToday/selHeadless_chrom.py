import time
import pickle
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PythonToday.vk_auth import login, pwd


useragent = UserAgent()
option = webdriver.ChromeOptions()
option.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/88.0.4324.96 Safari/537.36")
option.add_argument('--disable-blink-features=AutomationControlled')

# headless mode
option.headless = True
# option.add_argument('--headless')

driver = webdriver.Chrome(options=option)

url = 'https://vk.com'

try:
    driver.get(url=url)
    time.sleep(3)

    email_input = driver.find_element_by_id('index_email')
    email_input.clear()
    email_input.send_keys(login)
    time.sleep(2)

    pwd_input = driver.find_element_by_id('index_pass')
    pwd_input.clear()
    pwd_input.send_keys(pwd)
    time.sleep(1)
    # pwd_input.send_keys(Keys.ENTER)

    login_button = driver.find_element_by_id('index_login_button').click()
    time.sleep(3)

    profile_link = driver.find_element_by_id('l_pr').click()
    time.sleep(5)

    video_block = driver.find_element_by_class_name('VideoPreview__thumbWrap').click()


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
