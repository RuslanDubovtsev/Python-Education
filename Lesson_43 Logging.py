import logging
import random

# logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w',
#                     format='%(asctime)s %(levelname)s %(message)s')
#
# x = 5
# y = 0
# logging.info(f'start programm with {x} and {y}')
# try:
#     res = x/y
#     logging.info(f'Good resule {res}')
# except ZeroDivisionError as err:
#     logging.error(err)
def random_list():
    my_list = []
    for _ in range(0, 100):
        my_list.append(random.randint(0,100))
    my_list.append('oops')
    return my_list

print(random_list())

def log_check(my_list):
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w',
                        format='%(asctime)s %(levelname)s %(message)s')

    logging.info('Start program')

    for elem in my_list:
        try:
            res = elem / random.randint(0,100)
            logging.info(f'Result: {res}')
        except ZeroDivisionError as error:
            logging.error(error)
        except TypeError:
            logging.critical('Dividing a string by a integer')


print(log_check(random_list()))