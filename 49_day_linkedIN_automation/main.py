from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)
sign_in = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in.click()

#LOGIN
EMAIL="cryptouser468@gmail.com"
PASSWORD="HalloWelt123!"
email = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
# driver.quit()