import aiohttp
import asyncio
import aiofiles
from bs4 import BeautifulSoup
import json

async def fetch(URL):
    async with aiohttp.ClientSession() as session:  # Соединение с интернетом (соединение с сессией)
        async with session.get(URL) as request:  # Создает запрос, в данном случае get запрос. После получения запрос закроется, но не сессия
            if request.status == 200:
                return await request.text()

async def main(URL):
    tasks = [fetch(url) for url in URL]
    res = await asyncio.gather(*tasks)
    my_list = []
    for html in res:
        soap = BeautifulSoup(html, 'lxml')
        for link in soap.find_all('a'):
            my_list.append({link.get_text(): link['href']})
    async with aiofiles.open('file.json', 'w') as response:

        await response.write(str(my_list))        # Принимает только строку, не позволяет конвертировать в джосн. Необходимо исправить
            # print(link)

if __name__ == "__main__":
    asyncio.run(main(["https://example.com", "https://google.com"]))