import threading
import logging
import time
import requests
import os
import random

logging.basicConfig(level=logging.DEBUG, filename='thread.log', filemode='w',
                    format='%(threadName)s %(asctime)s %(levelname)s %(message)s')


# def run(num1, num2):
#     return num1 * num2

def time_finc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'Функция {func.__name__} стартовала в {start}')
        res = func(*args, **kwargs)
        print(f'Функция {func.__name__} отработала за время {time.time() - start}')
        return res
    return wrapper

#
# def cat_images(URL, result_path):
#
#     response = requests.get(URL, timeout=(5,5))
#
#     with open(result_path, 'wb') as path:
#         path.write(response.content)
#
# def run_cat_images(URL):
#     # URL = "https://cataas.com/cat"
#     if not os.path.exists('./temp'):
#         os.mkdir('./temp')
#     for i in range(10):
#          cat_images(URL, f'temp/{i}.jpeg')
#
# @time_finc
# def run_thread(func, *args):
#     threads = []
#
#     t = threading.Thread(target=func, args=args)
#     t.start()
#     logging.debug(f'Start with pid {t.ident}')
#     threads.append(t)
#
#     for theard in threads:
#         theard.join()
#         logging.debug(f'End process {theard.ident}')
#
# run_thread(run_cat_images, "https://cataas.com/cat")


def highly_loaded_application():
    my_list = []
    for i in range(1, random.randint(100, 10000)):
        a = i / random.randint(1, 10000)
        my_list.append(a)
        # print(my_list)
    print(my_list)

# highly_loaded_application()

COUNT = 1
lock = threading.Lock()

def worker_1():
    global COUNT
    with lock:
        while COUNT < 1000:
            COUNT += 1
            logging.debug(f'Worker 1 increment COUNT {COUNT}')

def worker_2():
    global COUNT
    with lock:
        while COUNT > -1000:
            COUNT -= 1
            logging.debug(f'Worker 2 increment COUNT {COUNT}')


def thread1(func, *args):
    # threads = []

    # for i in range(10):
        t = threading.Thread(target=func, args=args)
        t.start()
        logging.debug('start')
        # threads.append(t)

    # for thr in threads:
        t.join()
        logging.debug('End thread')

if __name__ == '__main__':
    t1 = threading.Thread(target=worker_1)
    t2 = threading.Thread(target=worker_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

