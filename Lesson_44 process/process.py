# -*- coding: utf-8 -*-
import multiprocessing
import logging
import requests
import os
import time
logging.basicConfig(level=logging.DEBUG, filename='thread.log', filemode='w',
                    format='%(asctime)s %(levelname)s %(message)s')


# process_logger = logging.getLogger('process_log')
# process_logger.setLevel(logging.INFO)
# handler = logging.FileHandler(f"{__name__}.log", mode='w')
# formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
# handler.setFormatter(formatter)
# process_logger.addHandler(handler)
#
#
# time_logger = logging.getLogger('time_log')
# time_logger.setLevel(logging.INFO)
# handler2 = logging.FileHandler(f"{__name__}.log", mode='w')
# formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
# handler2.setFormatter(formatter2)
# time_logger.addHandler(handler2)

def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f'Функция {func.__name__} стартовала в {start}')
        res = func(*args, **kwargs)
        print(f'Функция {func.__name__} отработала за время {time.time() - start}')
        return res
    return wrapper


def cat_images(URL, result_path):

    response = requests.get(URL, timeout=(5,5))

    with open(result_path, 'wb') as path:
        path.write(response.content)

def run_cat_images(URL):
    # URL = "https://cataas.com/cat"
    if not os.path.exists('./temp'):
        os.mkdir('./temp')
    for i in range(10):
         cat_images(URL, f'temp/{i}.jpeg')

# run_cat_images("https://cataas.com/cat")

def run(num1, num2):
    return num1 * num2

@time_func
def pross(func, *args):
    process = []

    # for x in range(10):
    proc = multiprocessing.Process(target=func, args=args)
    proc.start()
    logging.debug(f'Start with pid {proc.pid}')
    process.append(proc)

    for p in process:
        p.join()
        logging.debug(f'End process {p.pid}')

if __name__ == '__main__':
    pross(run_cat_images, "https://cataas.com/cat")


