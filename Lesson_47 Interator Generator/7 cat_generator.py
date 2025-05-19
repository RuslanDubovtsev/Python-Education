import json
import logging
import time
import os
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def json_link(URL, image_url):
    res = requests.get(URL)
    json_res = res.json()
    answer = image_url

    return json_res[answer]
# print(json_link("https://random-d.uk/api/random"))


def get_image(url, result_path):
    response = requests.get(url, timeout=(5,5))
    with open(result_path, 'wb') as path:
            logger.info(f"Запись в файл (json)")
            path.write(response.content)
# for i in range(10):
#     get_image("https://random-d.uk/api/random", "temp/{}.jpeg")


def load_images():
    URL = yield
    PATH = "temp/{}.jpg"

    if URL != "https://cataas.com/cat?":
        res = requests.get(URL)
        json_res = res.json()
        print(json_res)
        link = input("image-key: ")
        while link not in json_res:
            link = input("image-key: ")
        URL = json_link(URL, link)

    if not os.path.exists('./temp'):
        os.mkdir('./temp')
    for i in range(10):
        get_image(URL, PATH.format(i))


def main_generator(output):
    next(output)
    link = input("What the link?\n")
    output.send(link)


def executer():
    try:
        main_generator(load_images())
    except StopIteration:
        print("StopIteration")


CAT = 'https://cataas.com/cat?'
DUCK = 'https://random-d.uk/api/random'
DOGS = 'https://dog.ceo/api/breeds/image/random'
FOX = 'https://randomfox.ca/floof/'

print(executer())
# print(json_link('https://random-d.uk/api/random'))
# print(requests.get(CAT).content)



# res = requests.get('https://random-d.uk/api/random')
# j = json.loads(res.text)
#
# print(j)
# print(requests.get(j['url']))
# print(requests.get(j['url']).content)

# load_images()

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# URL = "https://cataas.com/cat"
# URL_TEMP = "temp/{}.jpg"
#
# def req_img(url, temp, index=None):
#     if index is not None:
#         logger.info(f"[{index}] Старт загрузки...")
#
#     start = time.time()
#     try:
#         response = requests.get(url, timeout=(5, 5))
#         if response.status_code != 200:
#             logger.warning(f"[{index}] Ошибка: статус {response.status_code}")
#             return
#         with open(temp, 'wb') as file:
#             file.write(response.content)
#         if index is not None:
#             logger.info(f"[{index}] Готово за {round(time.time() - start, 2)} сек.")
#     except Exception as e:
#         logger.error(f"[{index}] Ошибка: {e}")
#
# def load_images_sequential():
#     logger.info("=== Последовательная загрузка ===")
#     start = time.time()
#     for i in range(10):
#         req_img(URL, URL_TEMP.format(i), i)
#     logger.info(f"[SEQUENTIAL] Done in {round(time.time() - start, 2)} сек.\n")
#
# def load_images_threading():
#     logger.info("=== Многопоточная загрузка ===")
#     start = time.time()
#     threads = []
#     for i in range(10):
#         thread = threading.Thread(target=req_img, args=(URL, URL_TEMP.format(i), i))
#         thread.start()
#         threads.append(thread)
#
#     for thread in threads:
#         thread.join()
#     logger.info(f"[THREADING] Done in {round(time.time() - start, 2)} сек.\n")
#
# def load_images_multiprocessing():
#     logger.info("=== Многопроцессная загрузка ===")
#     start = time.time()
#     procs = []
#     for i in range(10):
#         proc = multiprocessing.Process(target=req_img, args=(URL, URL_TEMP.format(i), i))
#         proc.start()
#         procs.append(proc)
#
#     for proc in procs:
#         proc.join()
#     logger.info(f"[MULTIPROCESSING] Done in {round(time.time() - start, 2)} сек.\n")
#
# if __name__ == '__main__':
#     if not os.path.exists('./temp'):
#         os.mkdir('./temp')
#
#
#     load_images_sequential()
#     load_images_threading()
#     load_images_multiprocessing()