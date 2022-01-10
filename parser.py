import json

from bs4 import BeautifulSoup as BS
import requests
from hyphen import Hyphenator
from hyphen.textwrap2 import fill

h_en = Hyphenator('en_US')
URL = "https://www.timberland.com/shop/mens-boots"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
}


def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r

def get_content(html,image = False):
    soup = BS(html, "lxml")
    catalog_items = (soup.find("div", {"id": "catalog-results"})).findAll("script")
    for item in catalog_items:
        i_json = json.loads(item.text)
        description = i_json["description"]
        name = i_json["name"]
        article = f'article: {i_json["sku"]}'
        url = f'url: {i_json["url"]}'
        price = f'{i_json["offers"]["price"]} {i_json["offers"]["priceCurrency"]}'
        list_for_write = [description, name, article, url, price]
        list_for_write.append(f'image: {i_json["image"]}') if image else None

        with open('example.txt', 'a') as f:
            [f.write(fill(f"{i}", width=30) + '\n') for i in list_for_write]
            f.write('\n')

html = get_html(URL)
get_content(html.text, image=True)