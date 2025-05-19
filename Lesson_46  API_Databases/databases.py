import sqlite3

def connection():
    connect = sqlite3.connect('database.db')
    return connect

def execute(statement, value=None):
    with connection() as connect:
        cursor = connect.cursor()
        cursor.execute(statement, value or [])
        return cursor

def create_table(name, statement: dict):
    data = [f"{key} {value}" for key, value in statement.items()]
    print("Create_table data:", data)
    return execute(f"""CREATE TABLE IF NOT EXISTS {name} ({','.join(data)})""")

def insert_table(name, statement: dict):
    placeholders = ','.join('?' * len(statement))
    columns_name = ','.join(statement.keys())
    columns_value = tuple(statement.values())
    return execute(f"""INSERT OR IGNORE INTO {name} ({columns_name}) VALUES ({placeholders})""", columns_value)

def select_table(name, criteria=None, order_by=None):
    criteria = criteria or {}
    query = f"""SELECT * FROM {name}"""

    if criteria:
        placeholders = [f'{column} = ?' for column in criteria.keys()]
        select_criteria = ' AND '.join(placeholders)
        query += f' WHERE {select_criteria}'

    if order_by:
        query += f' ORDER BY {order_by}'

    return execute(query, tuple(criteria.values()))

# def get_data(label, flag=True):
#     element = input(f"{label}: ")
#     while not element and flag:
#         element = input(f"{label}: ")
#     return element
#
# def get_insert_data(number):
#     my_list = []
#     for i in range(1, number + 1):
#         my_list.append({get_data("Ключ"): get_data("Значение")})
#     return my_list[0]

def get_user_input(label, flag=True):
    value = input(f"{label}: ") or None
    while flag and not value:
        value = input(f"{label}: ") or None
    return value

def get_new_bookmark_data():
    return {
        "name": get_user_input('name'),
        "age": get_user_input('age'),
        "job_title": get_user_input('job_title'),
    }

# print(get_insert_data(1))
# create = create_table('Test', {
#     'id': "INTEGER PRIMARY KEY AUTOINCREMENT",
#     'name': "TEXT",
#     'age': "INTEGER",
#     'job_title': "TEXT",
# })
# insert = insert_table('Test', get_new_bookmark_data())
# select = select_table('Test', {"id": 1, "title": "name"}).fetchall()
# print(select)