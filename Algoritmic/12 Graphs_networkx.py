import networkx
import collections
import os
#
graph = networkx.Graph()
# print(graph)
#
graph.add_node('Ruslan')
graph.add_node('Rustam')
graph.add_edge('Rustam', 'Ruslan')
users = ['Karim', 'Bob', 'Lena', 'Imanali']
graph.add_nodes_from(users)
graph.add_edge('Karim', 'Ruslan')
graph.add_edge('Rustam', 'Lena')
graph.add_edge('Lena', 'Bob')
graph.add_edge('Bob', 'Imanali')
# print(graph.edges)
# print(graph.nodes)
# print(graph.degree) # Выводит список nodes и количество edge (связей)
# print(graph.adj) # Выводит все в виде словаря
# # print(graph.neighbors('Ruslan'))
# # a = graph.neighbors('Rustam')
# # print(','.join(a))
# # print(graph)
# # print(graph['Ruslan'])
# # Graph = graph.nodes
def search_person(name, search):
    # print("\nИмя персонажа:", name)
    # print(f"Имя того, кого ищем: {search}\n")
    if name == search:
        return True

def dfs_recursive(graph, start, search, visited=None):
    if search_person(start, search):
        return True
    elif visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        #print(neighbor)
        if neighbor not in visited:
            a = dfs_recursive(graph, neighbor, search, visited)
            return a

print(dfs_recursive(graph, 'Ruslan', 'Bob'))

# print(os.name)