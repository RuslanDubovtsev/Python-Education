import time
import random
import asyncio
import requests
import bs4
from bs4 import BeautifulSoup
import aiohttp
from urllib.parse import urljoin
from collections import deque
import aiofiles
import json


def req(URL):
    to_visited = [URL]
    for x in range(10):
        url = to_visited.pop(0)
        response = requests.get(url)
        soap = bs4.BeautifulSoup(response.text, 'lxml')

        for teg in soap.find_all("a", href=True):
            full_url = urljoin(url, teg(['href']))
            to_visited.append(full_url)
    return to_visited



async def request(url, session):
    visited = []
    if url not in visited:
        async with session.get(url) as response:
            if response.status == 200 and 'text/html' in response.headers.get("Content-Type", ''):
                print(f"{url} - {response.status}")
                visited.append(url)
                return await response.text()


# async def test(url, link):
#     full_url = urljoin(url, link)
#     return await full_url


async def fetch(max_pages=2):
    urls = deque(["https://www.google.com/", "https://web.whatsapp.com/"])
    # to_visit = deque([urls])
    storage = []
    visited = set()

    while len(visited) < max_pages:
        # url = urls.popleft()

        async with aiohttp.ClientSession() as session:
            tasks = [request(elem, session) for elem in urls]
            res = await asyncio.gather(*tasks)
            for i in urls:
                visited.add(i)

    for elem in res:
        soap = BeautifulSoup(elem, 'lxml')
        for link in soap.find_all("a"):
            full_url = urljoin(urls[0], link['href'])
            storage.append({link.get_text(): full_url})
    return  storage


    # print(visited)
    # async with aiofiles.open('file.json', 'w') as response:
    #     await response.write(storage)
    # async with aiofiles.open('file.txt', 'r') as file:
    #      file.read()



# async def json_converter():
#     res = await fetch()
#     return await res
#     # print(type(res))





if __name__ == "__main__":
    print(asyncio.run(fetch()))
    # print(req('https://quotes.toscrape.com/'))