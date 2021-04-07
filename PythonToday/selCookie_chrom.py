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

    news_link = driver.find_element_by_id('l_nwsf').click()
    time.sleep(5)

    # cookies
    pickle.dump(driver.get_cookies(), open(f'{login}_cookies', 'wb'))

    # for cookie in pickle.load(open(f'{login}_cookies', 'rb')):
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
