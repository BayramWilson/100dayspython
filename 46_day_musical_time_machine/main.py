import requests
from bs4 import BeautifulSoup

user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
# URL = f"https://www.billboard.com/charts/hot-100/{user_input}"
URL = "https://www.billboard.com/charts/hot-100/" + user_input
headers = {"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# song_titles = soup.find_all(id="title-of-a-story")
# print(song_titles)
# for i in song_titles:
#     print(i.get_text())

chart_result_list = soup.find_all("li", class_="o-chart-results-list__item")

for item in chart_result_list:
    title_tag = item.find("h3", id="title-of-a-story")
    if title_tag:
        title = title_tag.get_text(strip=True)
        print(title)

