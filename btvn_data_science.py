from bs4 import BeautifulSoup

import requests

web = "https://www.otofun.net/threads/bao-tri-va-nang-cap-trang-choxeotofun-net.1867324/?fbclid=IwAR3FrxY-_e-CjYI6RB16KbliNjarQafdn8M3y8j1C_iK4WAJQu9qB-UHKN8"
res = requests.get(web)
cont = res.text

soup = BeautifulSoup(cont, "lxml")

box = soup.find("div", class_ = "p-body-inner")

title = box.find("h1", class_ = "p-title-value").get_text()
date = box.find("div", class_ = "message-attribution-main").get_text()
content = box.find("div", class_ = "message-inner").get_text()






with open(f'{title}.txt', 'w', encoding = "utf-8") as file:
    file.write(content)