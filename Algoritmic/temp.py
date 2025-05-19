# def fire(n, c=1):
#     if c>n:
#         return
#     print(' '*(c-1)+'*'*(2*(n-c)+1))
#     fire(n, c+1)
#
# fire(5)

import string
# def fire(n, c=1):
#     print(c)
#     if c>len(n):
#         return
#     print([ch for ch in n])
#     fire(n, c+1)
#
# fire(string.digits)

def nuke(n):
    a = []
    for i in range(10):
        if (n>1):
            a.append(nuke(n-1))
            print("n", n)
        else:
            a.append(i)
            print("i", i)
    return a

nuke(10)