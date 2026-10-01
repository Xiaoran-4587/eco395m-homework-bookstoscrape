import requests
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url)

    response.encoding = "utf-8"

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    return soup