from collections import deque

a = deque()
a.append('first')
a.append('second')
print(a)
# a.popleft()
# print(a)

for i in a:
    print(i)

b = [1,2,3,3]
print(deque(b))