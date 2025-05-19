import requests
import json
from databases import select_table

class API:
    def __init__(self, info):
        self.info = info


    def form(self):
        return {
            'id': '',
            'name': '',
            'age': '',
            'job_title': '',

        }

    def transfer(self):
        json_list = []
        for elem in self.info:
            # print(elem[2])
            json_list.append({
            'id': elem[0],
            'name': elem[1],
            'age': elem[2],
            'job_title': elem[3],
            })
        return json_list



select = select_table('Test', ).fetchall()
a = API(select_table('Test', ).fetchall())
print(select)
print(a.transfer())