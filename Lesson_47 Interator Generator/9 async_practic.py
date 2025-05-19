import asyncio
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# async def print_num(name, limit):
#     for i in range(limit):
#         print(name, 2 ** i)
#         await asyncio.sleep(0.1)
#
#
# async def coroutine_1():
#     return await print_num('Worker1', 4)
#
#
# async def coroutine_2():
#     return await print_num('Worker2', 10)
#
#
# async def main():
#     # f1 = asyncio.create_task(coroutine_1())
#     # f2 = asyncio.create_task(coroutine_2())
#     # await f1
#     # await f2
#
#     await asyncio.gather(coroutine_1(), coroutine_2())


async def factorial(name, n):
    start_time = time.time()
    factorial = 1
    for i in range(1, n + 1):
        logger.info(f"{name} doing:  {factorial} * {i} = {factorial * i}")
        factorial *= i
        await asyncio.sleep(0.1)
    logger.info(f" {name} Завершился за {time.time() - start_time}")


async def logarithm(name, a, b):
    for i in range(1, b):
        # logger.info(i)
        if a ** i == b:
            logger.info(f"Done: log{a} {b} = {i}")
            break
        logger.info(f"log{a} {b} = {i}")
        await asyncio.sleep(0.1)


async def coroutine_1():
    return await factorial('factorial', 20)


async def coroutine_2():
    return await logarithm('fibonachi', 9, 205891132094649)


async def main():
    f1 = asyncio.create_task(coroutine_1())
    f2 = asyncio.create_task(coroutine_2())
    # await asyncio.gather(f1, f2)
    await f1
    await f2

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)