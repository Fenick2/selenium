import time
from selenium import webdriver

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')
option.headless = True  # запуск браузера без интерфейса

browser = webdriver.Firefox(options=option)

browser.get('https://nick-name.ru/generate/')

for i in range(10):
    button_xpath = '/html/body/div/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
    browser.find_element_by_xpath(button_xpath).click()

    link = browser.find_element_by_id('register').get_attribute('href')[36:]
    print(f'Nickname: {link}')
    time.sleep(1.0)

# browser.close()
