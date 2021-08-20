import requests
from bs4 import BeautifulSoup
from PriceTracker.configs import HEADERS


def get_ids(URL):
    if 'amazon' in URL:
        return {"website": "amazon", "price_id": "priceblock_ourprice", "title_id": "productTitle"}
    elif 'flipkart' in URL:
        return {"website": "flipkart", "price_class": "_30jeq3 _16Jk6d", "title_class": "B_NuCI"}
    else:
        return {"website": "other"}


def check_price(URL):
    web_page = requests.get(URL, headers=HEADERS)

    soup = BeautifulSoup(web_page.content, 'html.parser')
    price = None
    ids = get_ids(URL)
    if ids["website"] == "amazon":
        price = soup.find(id=ids["price_id"])
        # print(soup)
    elif ids["website"] == "flipkart":
        price = soup.find("div", {"class": ids["price_class"]})
    else:
        return price

    if price != None:
        price = float(price.get_text().strip().replace(
            ',', '').replace(' ', '')[1:])
        return price


def get_price_title(URL):
    web_page = requests.get(URL, headers=HEADERS)

    soup = BeautifulSoup(web_page.content, 'html.parser')
    price = None
    title = None
    ids = get_ids(URL)
    if ids["website"] == "amazon":
        price = soup.find(id=ids["price_id"])
        title = soup.find(id=ids["title_id"])
    elif ids["website"] == "flipkart":
        price = soup.find("div", {"class": ids["price_class"]})
        title = soup.find("span", {"class": ids["title_class"]})
    else:
        return price, title

    if price != None:
        price = float(price.get_text().strip().replace(
            ',', '').replace(' ', '')[1:])
        title = title.get_text().strip().replace('<!-- -->', '').replace('&nbsp', '')
        return price, title
