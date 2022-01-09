import json

from bs4 import BeautifulSoup as BS
import requests

URL = "https://www.timberland.com/shop/mens-boots"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
}

def get_html(url):
    r = requests.get(url, headers=HEADERS)
    return r

def get_content(html):
    soup = BS(html, "lxml")
    catalog_items = (soup.find("div", {"id": "catalog-results"})).findAll("script")
    for item in catalog_items:
        i_json = json.loads(item.text)
        item_to_write = f'{i_json["description"]}\n{i_json["name"]}\n{i_json["sku"]}\n{i_json["url"]}\n' \
                        f'{i_json["offers"]["price"]} {i_json["offers"]["priceCurrency"]}\n\n'
        with open('example.txt', 'a') as f:
            f.write(str(item_to_write))


html = get_html(URL)
get_content(html.text)