import asyncio
import aiohttp
import aiofiles
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import logging
from collections import deque

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def request(session, URL):
    try:
        async with session.get(URL, timeout=10) as response:
            if response.status_code == 200 and 'text/html' in response.headers.get("Content-Type", ''):
                return await response.text()  # make_soap

    except Exception as error:
        logger.info(f"Error {error}")


# def make_soap(URL, content):
#     visited = set()
#     soap = bs4.BeautifulSoup(content, 'lxml')
#     for link in soap.find_all("a"):
#         full_url = urljoin(URL, link['href'])
#         title = link.get_text(strip=True)
#         logger.info(f"{title} - {full_url}")
#         visited.add(full_url)
#     return visited

async def make_soap(URL, content):
    visited = set()
    soap = bs4.BeautifulSoup(content.text, 'lxml')
    for link in soap.find_all("a"):
        full_url = urljoin(URL, link['href'])
        title = link.get_text(strip=True)
        logger.info(f"{title} - {full_url}")
        return await full_url, title


async def crawler(start_url, max_depth=3):
    to_visit = deque([start_url])
    json_storage = list()

    while to_visit and len(to_visit) < max_depth:
        url = to_visit.popleft()
        async with aiohttp.ClientSession() as session:
            response = request(session, start_url)
            return await make_soap(start_url, response)

async def main():
    res = asyncio.create_task(crawler('https://www.google.com/'))
    await res


if __name__ == "__main__":
    asyncio.run(main())