from bs4 import BeautifulSoup
import re
import requests
URL = 'https://store.naver.com/restaurants/detail?id=1872451543'

def extract_indeed_jobs():
    result = requests.get(URL)
    soup = BeautifulSoup(result.content, 'html.parser')
    title = soup.find("strong", {"class": "name"})
    title = str(title.string).strip()
    print(title)

    category = soup.find("span", {"class": "category"})
    category = str(category.string).strip()
    print(category)

    location = soup.find("span", {"class": "addr"})
    location = str(location.string).strip()
    print(location)

    time = soup.find("span", {"class": "time"})
    if time is not None:
        time = str(time.string).strip()
        print(time)
    else:
        time = " "
        print(time)

    description = soup.find("div", {"class": "info"})
    desc = description.find("span", {"class": "txt"})
    if desc is not None:
        tag = soup.find("span", {"class": "kwd"})
        if tag is not None:
            desc = " "
            print(description)
        else:
            desc = str(description.string).strip()
            print(description)
    else:
        desc = " "
        print(desc)

    URL_IMG = 'https://store.naver.com/restaurants/detail?id'
    result_IMG = requests.get(f'{URL_IMG}=1872451543&tab=photo')

    soups = BeautifulSoup(result_IMG.content, 'html.parser')

    area = soups.find("div", {"class": "list_photo"})
    a = area.find("a")
    if a is not None:
        img = a.find("img").get("src")
        print(img)
    else:
        a = area.find("div")
        img = a.find("img").get("src")
        print(img)

    list_menu = soup.find("ul", {"class": "list_menu"})
    menu = list_menu.find_all("span", {"class": "name"})
    menu_result = []
    for item in menu:
        menu_result.append(item.get_text())
    print(menu_result)


    price = soup.find_all("em", {"class": "price"})
    print(price)
    price_result = []
    for item in price:
        price_result.append(item.get_text())
    print(price_result)


    return {
        'title': title,
        'category': category,
        'location': location,
        'time': time,
        'description': description,
        'menu': menu_result,
        'price': price_result,
    }
