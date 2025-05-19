import collections

Graph = {}
#
# Генеалогическоре древо Graph['Абильданова Сана'] = ['Абильданова Ардак', 'Абильданов Самат', 'Абильданов Рустам', 'Абильданов Еркен']
Graph['Абильданова Ардак'] = ['Дубовцев Руслан', 'Дильдабекова Оэлуна', 'Связь']
Graph['Абильданов Самат'] = []
Graph['Абильданов Рустам'] = ['Абильданова Эльдана']
Graph['Абильданов Еркен'] = []
Graph['Абильданова Эльдана'] = []

Graph['Связь'] = ['Дубовцев Георгиевич']

Graph['Дубовцев Георгиевич'] = ['Дубовцев Виктор', 'Дубовцев Слава']
Graph['Дубовцева Лидия'] = ['Дубовцев Виктор', 'Дубовцев Слава']
Graph['Дубовцев Виктор'] = ['Дубовцев Руслан', 'Дильдабекова Оэлуна', 'Связь2']
Graph['Дубовцев Виктор'] = ['Дубовцев Саша', 'Дубовцев Максим', 'Связь2']
Graph['Дубовцев Слава'] = ['Дубовцева Дана', 'Дубовцева Арьяна', 'Дубовцев Марк']
Graph['Дубовцев Руслан'] = []
Graph['Дильдабекова Оэлуна'] = []
Graph['Дубовцев Саша'] = []
Graph['Дубовцев Максим'] = []
Graph['Дубовцева Дана'] = []
Graph['Дубовцева Арьяна'] = []
Graph['Дубовцев Марк'] = []

Graph['Связь2'] = ['Бабушка Зоя']

Graph['Бабушка Зоя'] = ['Дубовцева Ира']
Graph['Дубовцева Ира'] = ['Дубовцев Саша', 'Дубовцев Максим']

print(Graph[list(Graph.keys())[0]])

Flag = True
while Flag == True:
    def adding_graph(graph):
        i = 1
        while len(graph) < 5:
            print(graph)
            name = input(f"Кого вы хотите добавить в качестве ключевого графа({i}): ")
            name_for_note = input("Кого вы хотите добавить в качестве косвенного графа: ").split(', ')
            if '' in name_for_note:
                name_for_note = []
            Graph[name] = name_for_note
            i += 1
        return graph


    def search_person(name, search):
        if name == search:
            return True


    def search(name, search):
        search_queue = collections.deque()
        search_queue += Graph[name]
        searched = []
        print(search_queue)
        while search_queue:
            person = search_queue.popleft()
            if not person in searched:
                if search_person(person, search):
                    print(f'{person} was searched')
                    return True

                else:
                    print(search_queue, 'Удалили -', person)
                    search_queue += Graph[person]
                    searched.append(person)

        return False

    print(adding_graph(Graph))
    print(search(list(Graph.keys())[0], input("Кого ищем?: ")))
    choice = input("Продолжать?(да/нет): ").lower()
    if choice == "нет":
        Flag = False


