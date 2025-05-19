import Lesson_21, write_div
import random
if __name__ == '__main__':
    for _ in range(0,1000):
        num = random.randint(0,1000)
        res = lesson_21.div_number(num)
        write_div.import_files('test.txtxt', str(res))

