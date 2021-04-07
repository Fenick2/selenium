import time
from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/88.0.4324.96 Safari/537.36")
# disable webdriver mode
option.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=option)

url = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'

try:
    driver.get(url)
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
