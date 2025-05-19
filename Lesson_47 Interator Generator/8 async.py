import asyncio
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# async def factorial(name, n):
#     start_time = time.time()
#     factorial = 1
#     for i in range(1, n + 1):
#         # logger.info(f"{name} doing:  {factorial} * {i} = {factorial * i}")
#         factorial *= i
#         await asyncio.sleep(0)
#     logger.info(f" {name} Завершился за {time.time() - start_time}")
#
#
# async def fibonachi(name, num):
#     start_time = time.time()
#     res = []
#     start = 0
#     next = 1
#     for _ in range(num):
#         res.append(start)
#         start, next = next, start + next
#         # logger.info(f"{name} doing: {res}")
#         await asyncio.sleep(0 )
#     logger.info(f" {name} Завершился за {time.time() - start_time}")
#
#
# async def main():
#     start = time.time()
#     f1 = asyncio.create_task(factorial('factorial', 100000))
#     f2 = asyncio.create_task(fibonachi('fibonachi', 100000))
#     await f1
#     await f2
#     logger.info(f" Общее время выполнения: {time.time() - start}")


# def factorial2(name, n):
#     start_time = time.time()
#     factorial = 1
#     for i in range(1, n + 1):
#         # logger.info(f"{name} doing:  {factorial} * {i} = {factorial * i}")
#         factorial *= i
#     logger.info(f" {name} Завершился за {time.time() - start_time}")
#
#
# def fibonachi2(name, num):
#     start_time = time.time()
#     res = []
#     start = 0
#     next = 1
#     for _ in range(num):
#         res.append(start)
#         start, next = next, start + next
#         # logger.info(f"{name} doing: {res}")
#     logger.info(f" {name} Завершился за {time.time() - start_time}")
#
#
# def main2():
#     start = time.time()
#     factorial2('factorial', 10000)
#     fibonachi2('fibonachi', 100000)
#     logger.info(f" Общее время выполнения: {time.time() - start}")


async def task1():
    logger.info("Start task1")
    counter = 0
    while True:
        counter += 1
        print("Запущен while")
        if counter == 10:
            break
        await asyncio.sleep(0.2)
    logger.info("Stop task1")


async def task2(num):
    logger.info("Start task1")

    res = 1
    counter = 0
    while True:
        res = num ** 2
        logger.info("res =", res)
        if counter == 10:
            break
        counter += 1
        await asyncio.sleep(0.2)
    logger.info("Stop task1")


async def main():
    f1 = asyncio.create_task(task1())
    f2 = asyncio.create_task(task2(100000))
    await f1
    await f2


if __name__ == "__main__":
    asyncio.run(main())
