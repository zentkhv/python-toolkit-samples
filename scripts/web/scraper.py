# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string, [a['href'] for a in soup.find_all('a', href=True)]

if __name__ == '__main__':
    title, links = scrape_page('https://example.com')
    print(f"Title: {title}, Links: {links}")
