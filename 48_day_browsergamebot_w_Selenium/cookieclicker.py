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
    #print(price.text)
    items.append(price.text)
#print(items)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprstuvwxyz-, ' 
shaped_items = []
for item in items:
    temp = ""
    for ch in item:
        if ch not in SYMBOLS:
            temp += ch

    shaped_items.append(temp)
#print(shaped_items)
shaped_items.pop()
#print(shaped_items)
int_list = []
for str in shaped_items:
    int_list.append(int(str))
#print(int_list)    

print(int_list[0])
print(items[0])







    # item.strip("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprstuvwxyz-")
    # shaped_items.append(item)
# items = items.strip("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprstuvwxyz-")
# print(shaped_items)
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

# exList = ['JM = {12, 23, 34, 45, 56}', 'the quick brown fox', 'word ($(,))']


# results = []
# for element in exList:
#     temp = ""
#     for ch in element:
#         if ch not in SYMBOLS:
#             temp += ch

#     results.append(temp)

# print results