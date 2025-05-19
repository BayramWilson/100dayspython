import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all("h3", class_="title")
shaped_movies = []
# movies = soup.find("h3", class_="title")
for i in movies:
    # print(i.get_text())

    shaped_movies.append(i.get_text())
    



file = open('Movies.txt','w')
for item in shaped_movies:
	file.write(item+"\n")
file.close()


# movie = movies.get_text()

# print(movie)