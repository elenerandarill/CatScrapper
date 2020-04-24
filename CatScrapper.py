#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


URL = "https://allegro.pl/kategoria/zywe-zwierzeta-koty-15998?bmatch=baseline-al-product-eyesa2-engag-dict43-com-1-2-0318"

html_doc = requests.get(URL)
# print(html_doc.status_code)   #200
html_doc = html_doc.text

soup = BeautifulSoup(html_doc, "html.parser")

all_offers = soup.find_all('div', class_="_9c44d_2H7Kt")
# print(all_sells)


"""For finding titles."""

def title_find(sell):
    sell_objs = sell('h2')
    for obj_h in sell_objs:
        link = obj_h.find('a')
        link_cat = link.get('href')
        file_name = str(link_cat).split('/')[-1]
        return file_name


"""For finding prices."""

def price_find(sell):
    span_price = sell('span', class_="_9c44d_1zemI")
    price00_zl = span_price[0].get_text()
    price00 = price00_zl.replace(' zł', '')
    price0 = price00.replace(' ', '')
    price = price0.replace(',00', '')
    return price


"""For finding jpgs."""

for sell in all_offers:
    price = price_find(sell)
    title = title_find(sell)
    sell_img = sell.find('img')
    cat_img = sell_img.get('data-src')
    if not cat_img:
        cat_img = sell_img.get('src')
    r = requests.get(cat_img)
    with open(f"D:\\OneDrive\\code\\python\\CatScrapper\\cats_img\\cat_{title}_Cena_{price}zl.jpg", "wb") as f:
        f.write(r.content)



