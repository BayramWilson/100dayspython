import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# Keep chromebrowser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)
driver.fullscreen_window()
driver.get("https://python.org")

# event_times = []
# events_list = []
# event_information={}

event_times = driver.find_elements(By.CSS_SELECTOR, value="div.medium-widget.event-widget.last time")
events_names = driver.find_elements(By.CSS_SELECTOR, value="div.medium-widget.event-widget.last li a")

for tim in event_times:
    print(tim.text)


# for event in events:
#     print(event.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
            "name": events_names[n].text
    }
print(events)

# driver.close()
driver.quit()
