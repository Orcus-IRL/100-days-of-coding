import lxml.html
import requests
from bs4 import BeautifulSoup
from lxml import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ta;q=0.8",
    "Cookie": "PHPSESSID=0add8dc288dc087775dd9e50fa7b6bde; _ga=GA1.2.1083484957.1707392799; _gid=GA1.2.1735823321.1707392799; _ga_VL41109FEB=GS1.2.1707392799.1.0.1707392799.0.0.0",
    "Accept-Encoding": "gzip, deflate, br",
    "sec-fetch-mode":"navigate"
}

response = requests.get(url="https://amzn.eu/d/4c4kL9k", headers=headers)
lxml_parser = lxml.html.HTMLParser
soup = BeautifulSoup(response.text,parser=lxml_parser)
# print(soup.find(attrs={"class":"a-price-whole"}))
print(soup)

# mail

import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )