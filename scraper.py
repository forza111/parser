import json
import re
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup as BS
import requests
from hyphen import Hyphenator
from hyphen.textwrap2 import fill

h_en = Hyphenator('en_US')
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
}

def get_filename(url: str, save_file=False) -> str:
    """
    Create filename with .txt extension based on url and current date

    :param url: str
    url address for name generation
    :param save_file: bool (default=False)
    Save file. If False, the filename ends in _deleted

    :return: str
    Path content/filename
    """

    _, pathname = re.split(r'/shop/', url)
    deleted = '_deleted' if not save_file else ''
    filename = f"{pathname}-{date.today()}{deleted}.txt"
    path = Path.cwd() / 'content' / filename
    create_empty_file(path) if save_file else None
    return path

def create_empty_file(filename):
    """
    Creates an empty file in the specified directory or overwrites an existing one.

    :param filename: str
    File Path

    :return: None
    """

    with open(filename, 'w'):
        pass

def get_content(url, width=60, image_url=False, save_file=False):
    """
    Performing page parsing at the given URL.

    :param url: str
    A get request is made at this URL
    :param width: int (default=60)
    The "Hyphenator" library is used to generate text of a given width and word wrap. This parameter is passed to the
    "fill" function and based on it the text width is formed.
    :param image_url: bool (default=False)
    Display image url
    :param save_file: bool (default=False)
    Save file

    :return: str
    Path to generated file
    """

    html = requests.get(url, headers=HEADERS).text
    soup = BS(html, "lxml")
    catalog_items = (soup.find("div", {"id": "catalog-results"})).findAll("script")
    filename = get_filename(url, save_file)

    for item in catalog_items:
        i_json = json.loads(item.text)
        description = i_json["description"]
        name = i_json["name"]
        article = f'article: {i_json["sku"]}'
        url = f'url: {i_json["url"]}'
        price = f'price: {i_json["offers"]["price"]} {i_json["offers"]["priceCurrency"]}'
        list_for_write = [description, name, article, price, url]
        list_for_write.append(f'image: {i_json["image"]}') if image_url else None

        with open(filename, 'a') as f:
            [f.write(fill(f"{i}", width=width) + '\n') for i in list_for_write]
            f.write('\n')
    return filename