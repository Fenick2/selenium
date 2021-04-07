from selenium import webdriver
import fake_useragent


user = fake_useragent.UserAgent().random
option = webdriver.FirefoxOptions()
option.set_preference('general.useragent.override', user)
browser = webdriver.Firefox(options=option)
browser.get('https://юзерагент.рф/')
