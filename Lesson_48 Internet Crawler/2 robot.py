import requests
import bs4
import json
from collections import deque

import asyncio
import aiohttp
import aiofiles

from urllib.parse import urljoin

import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# async def test(URL, max_pages, client):
#     visited = set()
#     to_visit = [URL]
#
#     while to_visit and len(visited) < max_pages:
#         url = to_visit.pop(0)
#         # if url in visited:
#         #     continue
#         try:
#             async with client.get(url) as response:
#                 soap = bs4.BeautifulSoup(await response.read(), 'lxml')
#                 logger.info(f"Visited: {url}")
#                 visited.add(url)
#
#                 for link in soap.find_all('a'):
#                     full_url = urljoin(url, link['href'])
#                     if full_url.startswith("http") and full_url not in visited:
#                         to_visit.append(full_url)
#         except Exception as error:
#             logger.error(error)
#             continue
#
#     logger.info(f"The visited reached to 10")
#     logger.info(f"Visited elements: {visited}")
#
# async def executer(URL):
#     async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(5.5)) as client:
#         task = test(URL, max_pages=10, client=client)
#         return await asyncio.gather(task)
#
# async def main():
#     res1 = asyncio.create_task(executer("https://www.google.com/"))
#     await res1



def test(URL, max_pages=10):
    visited = set()
    to_visit = deque([URL])
    json_storage = list()

    while to_visit and len(visited) < max_pages:
        url = to_visit.popleft()
        # if url in visited:
        #     continue
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200 and 'text/html' in response.headers.get("Content-Type", ''):
                soap = bs4.BeautifulSoup(response.text, 'lxml')
                logger.info(f"Visited: {url}")
                visited.add(url)

                for link in soap.find_all('a'):
                    full_url = urljoin(url, link['href'])
                    if full_url.startswith("http") and full_url not in visited:
                        json_storage.append({'external-url': url, 'internal-url_text': link.get_text(strip=True), 'internal-url': full_url})
                        to_visit.append(full_url)
        except Exception as error:
            logger.error(error)
            continue
    logger.info(f"The visited reached to 10")
    logger.info(f"Visited elements: {visited}")
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(json_storage, file, indent=3, ensure_ascii=False)
    with open("data.json", "r", encoding="utf-8") as file:
        new_data = json.load(file)
        logger.info(f"Json: {new_data}")




if __name__ == "__main__":
    # asyncio.run(main())
    test("https://www.google.com/")


