from flask import Flask, jsonify
import requests
import json

data = requests.get('https://api.github.com/users')
res = data.text
json_data = json.loads(res)

# print(json_data)

my_list = []
my_list2 = []
for elem in json_data:
    new_data = {}
    new_data['id'] = elem['id']
    new_data['login'] = elem['login']
    my_list.append(new_data)
    my_list2.append({'id': elem['id'], 'login': elem['login']})


for i in my_list2:
    print(i)

