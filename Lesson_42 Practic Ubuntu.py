import os
import multiprocessing

def func(num1, num2):
    print(f'Hello, my parent is {__name__}, his pid: {os.getpid()}')
    print(f'My name is {func.__name__}, my pid: {os.getppid()}. My_res = {num1 * num2}')

    return num1**num2

pros = multiprocessing.Process(target=func, args=(2,2))

if __name__ == '__main__':
    pros.start()
    print(pros.pid, pros.name)
    pros.join()