import sys
import os

# print(sys.path[1])
# print(sys.path[0])
# При path[0]
# for dirname, dir, filename in os.walk(sys.path[0]):
#     for elem in filename:
#         if elem != 'new_text.txt':
#             if elem.endswith('.txt'):
#                 file = open(elem, 'r')
#                 buf = file.read()
#                 file.close()
#                 file = open('Test/new_text.txt', 'a')
#                 file.write(buf)
#                 file.close()
#
#         if elem.endswith('.py'):
#             filepy = open(elem, 'r')
#             filepy_text = filepy.read()
#             filepy.close()
#             print(filepy_text)


my_dir = sys.path[0]
path = input('Enter Directory: ')
my_path = os.path.join(my_dir, path)
abs_path = os.path.abspath(my_path)
print(abs_path)

count_files = 0
count_dirs = 0
size_of_catalog = 0
if os.path.exists(abs_path):
    for dirname, dir, file in os.walk(abs_path):
        if dir:
            print(dir)
            count_dirs += 1
        if file:
            for files in file:
                if os.path.exists(files):
                    print(files)
                    count_files += 1
                    size_of_catalog += os.path.getsize(files) / 1024
                    # print(size_of_catalog)
                else:
                    print("No")
else:
    print("Файл не существует")
print("Размер каталога (в Кб): ", size_of_catalog)
print("Количество подкаталогов: ", count_dirs)
print("Количество файлов: ", count_files)