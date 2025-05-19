import requests
import json
import os
import time
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import re
# s = globals()


# URL = 'https://swapi.dev/api/people/18/'
# res = requests.get(URL)
# # print(res.status_code)
# # print(res.text)
#
# data = json.loads(res.text)
# print(type(data))
# print(data['name'])
#
# with open('my_swapi.json', 'w') as file:
#     json.dump(data, file, indent=4) # преобразование словаря в текст
#
# with open('my_swapi.json', 'r') as file:
#     data = json.load(file)
#     print(data['name'])

# ________________Homework__________________
# URL = 'https://swapi.dev/api/people/3/'
# res = requests.get(URL)
# data = json.loads(res.text)
# with open('my_swapi.json', 'w') as file:
#     data['name'] = 'Руслан'
#     json.dump(data, file, indent=4)
#
# with open('my_swapi.json', 'r') as file:
#     data = json.load(file)
#     print(data)
#     print(data['homeworld'])
# __________________________________________

# app = Flask(__name__)
#
# @app.route('/google') b
# def Google():
#     URL_google = 'https://www.google.com/'
#     res = requests.get(URL_google)
#     return res.text
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# URL_youtube = ''
# URL_Facebook = ''




def get_image(url, result_path):
    response = requests.get(url, timeout=(5,5))

    with open(result_path, 'wb') as path:
        path.write(response.content)

URL = "https://cataas.com/cat"

PATH = "temo/{}.jpeg"

if not os.path.exists('./temp'):
    os.mkdir('./temp')
for i in range(10):
    get_image(URL, f'temp/{i}.jpg')



#
# URL = 'https://mignews.com/mobile'
#
# res = requests.get(URL)
# data = res.text
# print(type(data))
# soup = BeautifulSoup(data, 'lxml')
#
# a = soup.find_all('a', class_='dropdown-item')
#
#
#
# pars_dict = dict()
# for elem in a:
#     pars_dict[elem.text] = elem['href']
#
# print("Dict", pars_dict)
#
# for key, value in pars_dict.items():
#     print(key, ':', value)
#
# URL_Flask = pars_dict['\nЗнакомства\n']
# print("Dict2", URL_Flask)
# app = Flask(__name__)
# @app.route('/')
# def acquaintance():
#     result = requests.get(URL_Flask)
#     return result.text
#
# if __name__ == "__main__":
#     app.run(debug=True)
# __________________

# Sportsru_URL = "https://www.sports.ru/tribuna/"
# res = requests.get(Sportsru_URL)
# HTML_code = res.text
# soup = BeautifulSoup(HTML_code, 'lxml')
# news = soup.find_all("a", class_='h1 content-link')
# print(news)
#
# pars_dict = dict()
# for new in news:
#
#     pars_dict[new.text] = new['href']
#
# for key, value in pars_dict.items():
#     print(key, ":", value)
# url = pars_dict['Как клубам НХЛ везло с Могильным, Мессье, Капризовым: обмены драфт-пиков с историческими последствиями :']
# app = Flask(__name__)
# @app.route('/')
# def Flask():
#
#     res = requests.get(url)
#     return res.text
#
# if __name__ == "__main__":
#     app.run(debug=True)
#


# def video(url):
#     req = requests.get(url)
#     send = BeautifulSoup(req.text, "html.parser")
#     search = send.find_all("script")
#     key = '"videoId":"'
#     data = re.findall(key + r"([^*]{11})", str(search))
#
#     return data
#
#
# def lists(url):
#     req = requests.get(url)
#     send = BeautifulSoup(req.text, "html.parser")
#     search = send.find_all("script")
#     key = '"playlistId":"'
#     data = re.findall(key + r"([^*]{34})", str(search))
#
#     return data
#
#
# if __name__ == '__main__':
#
#     output = 'https://www.youtube.com/playlist?list=PLpYwltiByWUvGL4IP9lavL85uTuQ7R7My'
#     vid = video(output)
#     # print(vid)
#     vid = vid[::3]
#     vid = vid[:-1]
#     a = 0
#     for i in vid:
#         print(i)
#         a += 1
#         with open('test', 'w', encoding='utf-8') as file:
#             file.write(str('https://www.youtube.com/watch?v=' + i + '\n'))
#             print('https://www.youtube.com/watch?v=' + i)
#     print(a)

# app = Flask(__name__)
# #
# tasks = [
#     {
#         'id': 1,
#         'name': 'Ruslan',
#         'course':'Python',
#         'Test': True
#     },
#     {
#         'id': 2,
#         'name': 'Karim',
#         'course': 'Java',
#         'Test': True
#     },
#     {
#         'id': 3,
#         'name': 'Imanaly',
#         'course': 'Java',
#         'Test': True
#
#     }
# ]
#
# @app.route("/hello/api/", methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})
#
# @app.route("/hello/api/<int:task_id>", methods=['GET'])
# def get_task(task_id):
#     task = list(filter(lambda t: t['id'] == task_id, tasks))
#     if len(task) == 0:
#         return "User is not find"
#     return jsonify({'task': task[0]})
# # def task(task_id):
# #     for t in tasks:
# #         if t['id'] == task_id:
# #             return t
# if __name__ == "__main__":
#     app.run(debug=True)