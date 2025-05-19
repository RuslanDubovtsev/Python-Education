import asyncio
import aiohttp
import aiofiles
import time
import requests
import os

def reader():
    with open('file.txt', 'r') as file:
        print("Start")
        file.read()
        print("End")


def main():
    reader()
    reader()


async def async_reader():
    print("Start")
    async with aiofiles.open('file.txt', 'r') as file:
        await file.read()
    print("End")


async def cor_1():
    print("Start")
    return await async_reader()

async def cor_2():
    return await async_reader()

async def cor_3():
    return await async_reader()

async def cor_4():
    return await async_reader()


async def async_main():
    await asyncio.gather(cor_1(), cor_2(), cor_3(), cor_4())






if __name__ == "__main__":
    asyncio.run(async_main())