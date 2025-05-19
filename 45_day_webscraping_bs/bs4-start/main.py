import requests
from bs4 import BeautifulSoup

# Get the Hacker News front page
response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

# List to store all post data
posts_data = []

# Find all posts
posts = soup.find_all("tr", class_="athing")

for post in posts:
    titleline = post.find("span", class_="titleline")
    if titleline:
        a_tag = titleline.find("a")
        title = a_tag.get_text()
        link = a_tag.get("href")

        # Get the upvote info from the next row
        subtext_row = post.find_next_sibling("tr")
        score_span = subtext_row.find("span", class_="score")
        if score_span:
            upvote_text = score_span.get_text()
            upvotes = int(upvote_text.split()[0])
        else:
            upvotes = 0

        posts_data.append((title, link, upvotes))

# Sort posts by upvotes descending
sorted_posts = sorted(posts_data, key=lambda x: x[2], reverse=True)

# Print sorted results
for i, (title, link, upvotes) in enumerate(sorted_posts, start=1):
    print(f"{i}. {title}")
    print(f"   Link: {link}")
    print(f"   Upvotes: {upvotes}")
