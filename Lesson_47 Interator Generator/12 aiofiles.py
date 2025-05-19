import asyncio
import aiohttp
import aiofiles
import time
import requests
import os


def get_image(url, result_path):
    response = requests.get(url, timeout=(5,5))

    with open(result_path, 'wb') as path:
        path.write(response.content)



URL = "https://cataas.com/cat"

# PATH = f'cats/{i}.jpg'
CATS_WE_WANT = 10

async def get_cat(client, i):
    PATH = f'cats/{i}.jpg'
    async with client.get(URL) as response:
        print(response.status)
        result = await response.read()
        if not os.path.exists("./cats"):
            os.mkdir("./cats")
        async with aiofiles.open(PATH, 'wb') as response:
            await response.write(result)
        # await to_write(result, id)
        return result


# async def to_write(content, id):
#     PATH = f'cats/{id}.jpg'
#     if not os.path.exists("./cats"):
#         os.mkdir("./cats")
#     async with aiofiles.open(PATH, 'wb') as response:
#         await response.write(content)


async def get_all_cats():
    async with aiohttp.ClientSession(timeout=(aiohttp.ClientTimeout(5.5))) as client:
        tasks = [get_cat(client, i) for i in range(CATS_WE_WANT)]
        return await asyncio.gather(*tasks)


async def coroutine_for_cat1():
    print("coroutine_for_cat1")
    return await get_all_cats()


async def coroutine_for_cat2():
    print("coroutine_for_cat2")
    return await get_all_cats()


async def cat_main():
    res1 = asyncio.create_task(coroutine_for_cat1())
    # res2 = asyncio.create_task(coroutine_for_cat2())
    await res1
    # await res2

if __name__ == "__main__":
    asyncio.run(get_all_cats())