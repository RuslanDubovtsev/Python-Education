import requests
import inspect
import time
from bs4 import BeautifulSoup


def URL_prepare(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    }

    habr_news = requests.get(URL, headers=headers)
    habr_news_text = habr_news.text
    bs = BeautifulSoup(habr_news_text, 'lxml')
    # type_log = bs.find_all("span", class_='publication-type-label__label publication-type-label__label_type-article')
    links = bs.find_all("a", class_='tm-title__link')
    # print(links)
    return links


def parser(URL):
    flag = yield

    if flag == "True":
        sorted_dict = {}
        links = URL_prepare(URL)
        for new in links:
            # sorted_dict["Тип"] = new[type_log.]
            sorted_dict[new.text] = new['href']
            # print(new)
        for key, value in sorted_dict.items():
            print(f"{key}: {'https://habr.com' + value}")
            time.sleep(0.5)
    else:
        return "The bool value is False"


def generator():
    p = parser('https://habr.com/ru/feed/')
    print(f"parser: {inspect.getgeneratorstate(p)}")
    yield from p


def flag(gen):
    next(gen)
    while True:
        flag = input("True/False?: ")
        print(f"generator: {inspect.getgeneratorstate(gen)}")
        gen.send(flag)

while True:
    try:
        flag(generator())
    except StopIteration:
        print("The operation is stopped")