import networkx
import matplotlib.pyplot
import collections

# nodes = range(1, 10)
# # edges = [(7,2), (2,3), (7,4), (4,5), (7,3), (7,5), (1,7), (1,6), (6, 7), (1,5), (2,4), (6,3)]
# edges = [("Ruslan", "Karin"), ("Imanali", "Ruslan"), ("Imanali", "Idk"), ("Karim", "idk"), ("idk", "Ruslan"),  ("Imanali", "Karim")]
# G = networkx.Graph()
#
# # G.add_nodes_from(nodes)
# G.add_edges_from(edges)
# print(G.degree)
# print(G)
#
# networkx.draw(G, with_labels=True)
# matplotlib.pyplot.show()

Graph = networkx.Graph()



class Class_graph:

        def prepared_graph(self):
            Graph.add_node('Ruslan')
            Graph.add_node('Rustam')
            Graph.add_edge('Rustam', 'Ruslan')
            users = ['Karim', 'Bob', 'Lena', 'Imanali']
            Graph.add_nodes_from(users)
            Graph.add_edge('Karim', 'Ruslan')
            Graph.add_edge('Rustam', 'Lena')
            Graph.add_edge('Lena', 'Bob')
            Graph.add_edge('Bob', 'Imanali')
            return 'The Graph have prepared'

        def adding_graph(self, graph):
            i = 1
            while len(graph) < 5:
                print("degree", graph.degree)
                print("nodes", graph.nodes)
                print("")
                name = input(f"Кого вы хотите добавить в качестве ключевого графа({i}): ")
                name_for_note = input("Кого вы хотите добавить в качестве косвенного графа: ")
                Graph.add_node(name)
                Graph.add_node(name_for_note)
                Graph.add_edge(name, name_for_note)
                i += 1
            networkx.draw(graph, with_labels=True)
            matplotlib.pyplot.show()
            return graph


        def search_person(self, name, search):
            print("Ищем -", search)
            print("У нас -", name)
            if name == search:
                return True

        def line_search(self, name, search, graph):
            search_queue = collections.deque()
            search_queue += graph.neighbors(name)
            searched = []
            print(search_queue)
            while search_queue:
                person = search_queue.popleft()
                if not person in searched:
                    if self.search_person(person, search):
                        print(f'{person} was searched')
                        return True

                    else:
                        print(search_queue, 'Удалили -', person)
                        search_queue += graph.neighbors(person)
                        searched.append(person)

        def deep_recursion_search(self, graph, start, search, visited=None):
            if self.search_person(start, search):
                return f'{search} was searched!'
            elif visited is None:
                visited = set()
            visited.add(start)
            print(start)

            for neighbor in graph[start]:
                # print(neighbor)
                if neighbor not in visited:
                    a = self.deep_recursion_search(graph, neighbor, search, visited)
                    return a

        def show_friends(self, name):
            print("Это твои друзья: ", ''.join(Graph.neighbors(name)))



Flag = True
while Flag == True:
    a = Class_graph()
    print(a.prepared_graph())
    # print(a.adding_graph(Graph))
    # print(a.line_search(name=list(Graph.nodes)[0], search=input("Кого найти: "), graph=Graph))
    print(a.deep_recursion_search(Graph, list(Graph.nodes)[0], input("Кого найти: ")))
    # print(Class_graph().show_friends('Karim'))
    choice = input("Продолжать?(да/нет): ").lower()
    if choice == "нет":
        Flag = False

# my_list = {'2': 2, '1': 1}
# a = list(my_list.keys())[0]
# b = list(Graph.nodes)[0]
# print(type(a), type(b))