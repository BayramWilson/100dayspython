from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
cookie.click()

money = driver.find_element(By.CSS_SELECTOR, value="#money")
#print(money.text)

prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
items = []
for price in prices:
    print(price.text)
    items.append(price.text)
print(items)
items = items.strip("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprstuvwxyz-")
print(items)
# item1 = driver.find_element(By.XPATH, value='//*[@id="buyCursor"]/b/text()[2]')
# print(item1.text)
# item2 = driver.find_element(By.XPATH, value='')
# item3 = driver.find_element(By.XPATH, value='')
# item4 = driver.find_element(By.XPATH, value='')
# item5 = driver.find_element(By.XPATH, value='')
# item6 = driver.find_element(By.XPATH, value='')
# item7 = driver.find_element(By.XPATH, value='')
# item8 = driver.find_element(By.XPATH, value='')

# store = {
#     "item":"",
#         "price":""
# }
#while True: