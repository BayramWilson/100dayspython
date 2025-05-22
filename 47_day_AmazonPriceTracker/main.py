from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib
import datetime

load_dotenv()


TARGETPRICE=100
SMTP_ADDRESS="smtp.gmail.com"
EMAIL = os.getenv("CRYPTOUSER_EMAIL")
# print(EMAIL)
# PASSWORD = os.getenv("CRYPTOUSER_EMAIL_PASSWORD")
# print(PASSWORD)
AUTH_TOKEN=os.getenv("CRYPTOUSER_AUTH_TOKEN")
URL="https://appbrewery.github.io/instant_pot/"
html_doc = requests.get(URL)
html_doc = html_doc.text
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)

current_price = soup.find("div", id="corePriceDisplay_desktop_feature_div")
current_price = current_price.find("span", class_="aok-offscreen").get_text()
# print(type(current_price))
current_price = current_price[2:]
# print(current_price)
current_price = float(current_price)


if current_price < TARGETPRICE:
    server = smtplib.SMTP(SMTP_ADDRESS, 587)
    server.set_debuglevel(debuglevel=0)
    
    server.connect(SMTP_ADDRESS, port=587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL, AUTH_TOKEN)

    from_addr = f"Crypto User <{EMAIL}>"
    to_addr = EMAIL

    subj = "Amazon Price Alert"
    date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

    message_text = f"Hello,\nyour Price Alert for {URL} has been triggered, the current price for {URL} is ${current_price}!"
    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s"% ( from_addr, to_addr, subj, date, message_text )

    server.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg)
    server.quit()




