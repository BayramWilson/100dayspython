import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/news")
website = response.text

soup = BeautifulSoup(website, "html.parser")




# print(soup.select(".title a"))
# anchor_tag = soup.select(".title a")
# print(soup.getText(anchor_tag))
# anchor_tag = soup.find_all(name="a", )
# anchor_text = soup.getText(anchor_tag)

# Find the first <span> with class "titleline"
titleline = soup.find('span', class_='titleline')

# Find the <a> tag within it and get the text
a_text = titleline.find('a').get_text()

a_link = titleline.find("a").get("href")

a_upvote = soup.find("span", class_="score")
a_upvote = a_upvote.getText()
# <span class="score" id="score_43982777">40 points</span>
print(a_text)
print(a_link)
print(a_upvote)













# import lxml

# with open("website.html") as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)
# print(soup.find_all("a"))

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")
# print(company_url)
# print(soup.select(".heading"))

