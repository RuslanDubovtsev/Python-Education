import asyncio
import aiohttp
import requests
import time

def fetch(url):
    response = requests.get(url)
    return response.status_code

def main():
    urls = ['https://httpbin.org/delay/1'] * 10
    start = time.time()
    for url in urls:
        print(fetch(url))
    print(f'{time.time() - start}')


URL = ['https://cataas.com/cat', 'https://httpbin.org/delay/1', 'https://cataas.com/cat?', 'https://random-d.uk/api/random',
       'https://dog.ceo/api/breeds/image/random', 'https://randomfox.ca/floof/','https://cataas.com/cat', 'https://httpbin.org/delay/1',
       'https://cataas.com/cat?', 'https://random-d.uk/api/random', 'https://dog.ceo/api/breeds/image/random', 'https://randomfox.ca/floof/', ]

async def async_fetch(session, url):
    async with session.get(url) as res:
        print(res.status)
        return res.status


async def async_main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [async_fetch(session, url) for url in URL]
        await asyncio.gather(*tasks)
    print(time.time() - start)


# URL = "https://cataas.com/cat"


# async def get_url(client):
#     async with client.get() as response:
#         print(response.status)
#         result = await response.read()
#         return result
#
#
# async def get_all_urls():
#     async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
#         tasks = get_url(client)
#         return await asyncio.gather(tasks)


# async def main_url():
#     res = asyncio.run(get_all_urls())
#     print(res)

if __name__ == "__main__":
    res = asyncio.run(async_main())
    print(res)


