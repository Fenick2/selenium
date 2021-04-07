import time
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.set_preference('dom.webdriver.enabled', False)

driver = webdriver.Firefox(options=options)

url = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'

try:
    driver.get(url)
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
