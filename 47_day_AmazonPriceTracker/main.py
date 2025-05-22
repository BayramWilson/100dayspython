from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib
import datetime
import locale

load_dotenv()


TARGETPRICE=100
SMTP_ADDRESS="smtp.gmail.com"
EMAIL = os.getenv("CRYPTOUSER_EMAIL")
# print(EMAIL)
# PASSWORD = os.getenv("CRYPTOUSER_EMAIL_PASSWORD")
# print(PASSWORD)
AUTH_TOKEN=os.getenv("CRYPTOUSER_AUTH_TOKEN")
URL="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# headers = {
#     "Accept-Language":"de-DE,de;q=0.7",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
# }
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "de-DE,de;q=0.9", 
    # "Host": "httpbin.org", 
    "Priority": "u=0, i", 
    "Sec-Ch-Ua": "\"Chromium\";v=\"136\", \"Brave\";v=\"136\", \"Not.A/Brand\";v=\"99\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Sec-Gpc": "1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36", 
    # "X-Amzn-Trace-Id": "Root=1-682ee43a-2fab02355133b0fb0878fdbd"
    }

html_doc = requests.get(URL, headers=headers)
html_doc = html_doc.text
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)

# current_price = soup.find("div", id="corePriceDisplay_desktop_feature_div")
current_price = soup.find("div", id="corePrice_feature_div")
current_price = current_price.find("span", class_="a-offscreen").get_text()
# print(type(current_price))
current_price = current_price[:-1]

current_price = current_price.replace(",", ".")
current_price = float(current_price)

# print(current_price)


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




