import json
from collections import deque

data = {
    "name": 'Ruslan',
    "age": 17,
    "is_student": "Да",
}

# with open("data.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=3, ensure_ascii=False)

# with open("data.json", "r", encoding='utf-8') as file:
#     new_data = json.load(file)
#     print(type(new_data))
#     print(new_data)

a = deque(["https://www.google.com/"])
print(a.popleft())