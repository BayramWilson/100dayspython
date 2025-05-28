from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# total_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# # total_articles.click()
# print(total_articles.text)

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()
# search_button = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
# search_button.click()
# time.sleep(2)
# type_in_search_bar = driver.find_element(By.NAME, value="search")
# type_in_search_bar.send_keys("Python")
# type_in_search_bar.send_keys(Keys.ENTER)

driver.get(url="https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Bayram")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Wilson")

email = driver.find_element(By.NAME, value="email")
email.send_keys("bayram.wilson04@gmail.com")
email.send_keys(Keys.ENTER)