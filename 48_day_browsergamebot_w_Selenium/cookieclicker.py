from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprstuvwxyz-, '

def get_prices():
    prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    items = []
    for price in prices:
        items.append(price.text)
    shaped_items = []
    for item in items:
        temp = ""
        for ch in item:
            if ch not in SYMBOLS:
                temp += ch
        shaped_items.append(temp)
    shaped_items = [s for s in shaped_items if s]
    int_list = []
    for s in shaped_items:
        try:
            int_list.append(int(s))
        except ValueError:
            pass
    return int_list

def check_gold(gold, int_list):
    if gold > int_list[7]:
        driver.find_element(By.ID, "buyTime machine").click()
    elif gold > int_list[6]:
        driver.find_element(By.ID, "buyPortal").click()
    elif gold > int_list[5]:
        driver.find_element(By.ID, "buyAlchemy lab").click()
    elif gold > int_list[4]:
        driver.find_element(By.ID, "buyShipment").click()
    elif gold > int_list[3]:
        driver.find_element(By.ID, "buyMine").click()
    elif gold > int_list[2]:
        driver.find_element(By.ID, "buyFactory").click()
    elif gold > int_list[1]:
        driver.find_element(By.ID, "buyGrandma").click()
    elif gold > int_list[0]:
        driver.find_element(By.ID, "buyCursor").click()
cps = driver.find_element(By.ID, value="cps")
print(cps.text)
bot_is_on = True

time.sleep(10)
cookie = driver.find_element(By.ID, value="cookie")
next_check = time.time() + 5
timeout = time.time() + 60*5  

while bot_is_on:
    test = 0
    cookie.click()
    if test == 5 or time.time() > timeout:
        break
    test = test - 1
    if time.time() > next_check:
        money_text = driver.find_element(By.ID, "money").text.replace(",", "")
        if money_text.isdigit():
            money = int(money_text)
            int_list = get_prices()
            if len(int_list) >= 8:
                check_gold(money, int_list)
        next_check = time.time() + 5
print(driver.find_element(By.ID, value="cps").text)