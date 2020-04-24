#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup


URL = "https://allegro.pl/kategoria/zywe-zwierzeta-koty-15998?bmatch=baseline-al-product-eyesa2-engag-dict43-com-1-2-0318"

html_doc = requests.get(URL)
# print(html_doc.status_code)   #200
html_doc = html_doc.text

soup = BeautifulSoup(html_doc, "html.parser")

all_sells = soup.find_all('div', class_="_9c44d_2H7Kt")
# print(all_sells)

"""For finding titles."""
# for sell in all_sells:
#     sell_objs = sell('h2')
#     for obj_h in sell_objs:
#         link = obj_h.find('a')
#         link_cat = link.get('href')
#         file_name = str(link_cat).split('/')[-1]
#         print(file_name)

"""For finding prices."""
for sell in all_sells:
    span_price = sell('span', class_="_9c44d_1zemI")
    price_zl = span_price[0].get_text()
    price = price_zl.replace(' zł', '')
    price = price.replace(' ', '')
    price = price.replace(',00', '')
    print(price)

"""For finding jpgs."""
# numb = 0
# for sell in all_sells:
#     sell_img = sell.find('img')
#     cat_img = sell_img.get('data-src')
#     if not cat_img:
#         cat_img = sell_img.get('src')
#     r = requests.get(cat_img)
#     with open(f"D:\\OneDrive\\code\\python\\CatScrapper\\cats_img\\cat{numb}.jpg", "wb") as f:
#         f.write(r.content)
#         numb += 1



