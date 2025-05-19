from flask import Flask, jsonify
import requests
import json
# import json
#
# class Transducer:
#     def __init__(self, id, name, town):
#         self.id = id
#         self.name = name
#         self.town = town
#
#         self.my_dict = {
#             "id": id,
#             "shop": name,
#             "town": town
#         }
#
#     def conventer_to_json(self):
#         with open('dict.json', 'w') as file:
#             json.dump(self.my_dict, file, indent=4)
#         with open('dict.json', 'r') as file:
#             data = json.load(file)
#             return data
#
#     @staticmethod
#     def conventer_to_dict(my_json):
#         with open(my_json, 'r') as file:
#             data = json.load(file)
#             return type(data)
#
#
# # id = int(input("id: "))
# # name = input("name: ")
# # town = input("town: ")
# # print(Transducer(id, name, town).conventer_to_json())
# print(Transducer.conventer_to_dict("dict.json"))


# app = Flask(__name__)
#
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
#
# if __name__ == "__main__":
#     app.run(debug=True)

# ____________________GITHub_API_Flask_______________
resource = requests.get('https://api.github.com/users')
result = resource.text
data = json.loads(result)
app = Flask(__name__)


def search_login():
    my_list = []
    for elem in data:
        my_list.append({'id': elem['id'], 'name': elem['login']})
        # my_list.append({'name': elem['login']})

    return my_list

# print(search_login())

def choice_name(self):
    for i in self.search_login():
        print(i)
    choice = input("\nВыберите имя: ")
    while choice not in self.search_login():
        choice = input("\nВыберите имя: ")
    return choice

def get_url_name(name):
    new_url = requests.get(f'https://api.github.com/users/{name}')
    dict_data = json.loads(new_url.text)
    my_list = []
    # print(dict_data)
    data = {"name": dict_data['login'], "id": dict_data['html_url']}
    my_list.append(data)
    return my_list

@app.route('/')
def stars():
    return jsonify({'stars': search_login()})

@app.route('/<star_name>', methods=['GET'])
def detail_star(star_name):
    # print(star_name)
    star = list(filter(lambda s: s['name'] == star_name, search_login()))
    if len(star) == 0:
        return 'GitHub star is not found'
    return jsonify({'star': get_url_name(star[0]['name'])})  # star = [{'id': 1, 'name': 'mojombo'}]


# @app.route("/hello/api/<int:task_id>", methods=['GET'])
# def get_task(task_id):
#     task = list(filter(lambda t: t['id'] == task_id, tasks))
#     if len(task) == 0:
#         return "User is not find"
#     return jsonify({'task': task[0]})

if __name__ == "__main__":
    app.run(debug=True)