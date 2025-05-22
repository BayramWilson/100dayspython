from bs4 import BeautifulSoup
import requests

TARGETPRICE=99.95
URL="https://appbrewery.github.io/instant_pot/"
html_doc = requests.get(URL)
html_doc = html_doc.text
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)