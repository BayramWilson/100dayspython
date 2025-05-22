from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# Path to correct ChromeDriver

options = Options()
options.binary_location = "/snap/bin/chromium" 

service = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome()
driver.get("https://www.amazon.com")
