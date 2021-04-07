import time
from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/88.0.4324.96 Safari/537.36")
option.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=option)

url = 'https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty'

try:
    driver.get(url=url)
    # print(driver.window_handles)
    print(f"Currently URL is: {driver.current_url}")
    time.sleep(3)

    items = driver.find_elements_by_xpath("//div[@data-marker='item-photo']")
    items[0].click()
    # print(driver.window_handles)
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    print(f"Currently URL is: {driver.current_url}")

    seller = driver.find_element_by_class_name('seller-info-name')
    print(f"Seller name is: {seller.text}")
    print('#' * 20)
    time.sleep(3)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
    print(f"Currently URL is: {driver.current_url}")

    items[1].click()
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    print(f"Currently URL is: {driver.current_url}")
    seller = driver.find_element_by_xpath("//div[@data-marker='seller-info/name']")
    print(f"Seller name is: {seller.text}")
    print('-' * 20)

    ad_date = driver.find_element_by_class_name("title-info-metadata-item-redesign")
    print(f"An ad date is: {ad_date.text}")
    print('-' * 20)

    joined_date = driver.find_elements_by_class_name("seller-info-value")[1]
    print(f"Seller since: {joined_date.text}")
    print('#' * 20)
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
