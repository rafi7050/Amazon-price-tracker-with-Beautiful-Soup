import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.amazon.com/dp/B07PTMKYS7/'
# url = 'https://www.amazon.com/FIFA-21-Xbox-One/dp/B08BGPPJ1R/'
# url = "https://www.amazon.com/PlayStation-VR-Marvels-Iron-Bundle-4/dp/B08CD34NZH/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Accept-Language": "en",
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")
# print(soup.prettify())

name = soup.select_one(selector="#productTitle").getText()
name = name.strip()
# print(name)

price = soup.select_one(selector="#priceblock_ourprice").getText()
price = float(price[1:])
# print(price)

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Accept-Language": "en",
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = float(price[1:])

    return name, price

print(get_link_data(url))