import time
from fake_useragent import UserAgent
from selenium import webdriver


useragent = UserAgent()
option = webdriver.ChromeOptions()
option.add_argument(f"user-agent={useragent.random}")

driver = webdriver.Chrome(options=option)

try:
    driver.get(url='https://юзер-агент.рф')

    # driver.refresh()
    # driver.get_screenshot_as_file('1.png')
    # driver.get(url='https://stackoverflow.com')
    # time.sleep(3)
    # driver.get_screenshot_as_file('2.png')
except Exception as ex:
    print(ex)
# finally:
#     driver.close()
#     driver.quit()
