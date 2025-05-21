import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import os
from dotenv import load_dotenv
import pprint
load_dotenv()


# -----------------SPOTIFY PART------------------------- # 
# auth_manager = SpotifyClientCredentials()
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
username= os.getenv("SPOTIFY_USERNAME")

scope = "user-library-read"
scope1 = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               username=username,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               redirect_uri="https://spotify.com",
                                               scope=scope1))
user_id = sp.current_user()["id"]



user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
URL = "https://www.billboard.com/charts/hot-100/" + user_input
headers = {"USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


chart_result_list = soup.find_all("li", class_="o-chart-results-list__item")

titles=[]
for item in chart_result_list:
    title_tag = item.find("h3", id="title-of-a-story")
    if title_tag:
        title = title_tag.get_text(strip=True)
        titles.append(title)
# print(type(titles))
# print(titles) # all listed
# print(len(titles))  # 100
year = user_input[:4]

q = f"track:\"{titles[0]}\" year:{year}"
# print(q)
research = sp.search(q=q, limit=1, offset=0, type="track", market=None)

track_uri = research["tracks"]["items"][0]["uri"]

track_uri_list = []

for i in range(0, 101):
    try:
        q = f"track:\"{titles[i]}\" year:{year}"
        research = sp.search(q=q, limit=1, offset=0, type="track", market=None)
        track_uri = research["tracks"]["items"][0]["uri"]
        track_uri_list.append(track_uri)
    except IndexError:
        track_uri_list.append(None)
print(track_uri_list)


# for i in q:
#     f"track:\"{titles[0]}\" year:{year}"
print()





def create_playlist():

    pass