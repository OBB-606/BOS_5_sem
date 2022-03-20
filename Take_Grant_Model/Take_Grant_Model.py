import csv

# 1 - r
# 2 - w
# 3 - t
# 4 - g
import matplotlib.pyplot as plt
import networkx as nx


def post():
    # command post
    temp_list = []
    with open('post.csv', 'r') as csv_r:
        reader = csv.reader(csv_r)
        for i in reader:
            temp_list.append(i)
    data = open('post.csv', "r")
    graph = nx.DiGraph()
    nx.parse_adjlist(data, delimiter=',', create_using=graph, nodetype=str)

    graph['s1']['o2']['weight'] = 1
    graph['s2']['o2']['weight'] = 2
    # graph.add_edge('o1', 'o3', weight=1)
    print("------------- command post ----------------")
    print("Изначальная структура: ")
    print(f"s1->o2 = 'r'\n s2->o2 = 'w'\n\n")
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.06')
    plt.show()
    #################################
    graph.add_edge('s1', 's2', weight=1)
    graph.add_edge('s2', 's1', weight=1.2)
    print("Добавленные ребра: ")
    print(f"s1->s2 = 'r'\n s2->s1 = 'w'\n\n")
    pos = nx.spring_layout(graph)
    # edge_labels = nx.get_edge_attributes(graph, 'weight')
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in graph.edges(data=True)])
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.1')
    plt.show()


def spy():
    #######***************----------- command spy #######***************-----------
    data = open('spy.csv', "r")
    graph = nx.DiGraph()
    nx.parse_adjlist(data, delimiter=',', create_using=graph, nodetype=str)

    graph['s1']['s2']['weight'] = 1
    graph['s2']['o1']['weight'] = 1
    # graph.add_edge('o1', 'o3', weight=1)

    print("------------- command spy ----------------")
    print("Изначальная структура: ")
    print(f"s1->s2 = 'r'\n s2->o1 = 'r'\n\n")

    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.06')
    plt.show()
    #################################
    graph.add_edge('s1', 'o1', weight=1)
    graph.add_edge('o1', 's1', weight=1.2)
    print("Добавленные ребра: ")
    print(f"s1->o1 = 'r'\n o1->s1 = 'w'\n\n")
    pos = nx.spring_layout(graph)
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in graph.edges(data=True)])
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.1')
    plt.show()


def find():
    #######***************----------- command find #######***************-----------

    data = open('spy.csv', "r")
    graph = nx.DiGraph()
    nx.parse_adjlist(data, delimiter=',', create_using=graph, nodetype=str)

    graph['s1']['s2']['weight'] = 2
    graph['s2']['o1']['weight'] = 2
    print("------------- command find ----------------")
    print("Изначальная структура: ")
    print(f"s1->s2 = 'w'\n s2->o1 = 'w'\n\n")
    # graph.add_edge('o1', 'o3', weight=1)
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.06')
    plt.show()
    #################################
    graph.add_edge('s1', 'o1', weight=1)
    graph.add_edge('o1', 's1', weight=2.1)
    print("Добавленные ребра: ")
    print(f"s1->o1 = 'w'\n o1->s1 = 'r'\n\n")
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')

    # edge_labels=dict([((u,v,),d['weight'])
    #              for u,v,d in graph.edges(data=True)])
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.1')
    plt.show()


def pass_():
    #######***************----------- command pass #######***************-----------

    data = open('pass.csv', "r")
    graph = nx.DiGraph()
    nx.parse_adjlist(data, delimiter=',', create_using=graph, nodetype=str)

    graph['s1']['o1']['weight'] = 2
    graph['s1']['o2']['weight'] = 1
    print("------------- command pass ----------------")
    print("Изначальная структура: ")
    print(f"s1->o1 = 'w'\n s1->o2 = 'r'\n\n")
    # graph.add_edge('o1', 'o3', weight=1)
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.06')
    plt.show()
    #################################
    graph.add_edge('o1', 'o2', weight=1)
    graph.add_edge('o2', 'o1', weight=1.2)
    print("Добавленные ребра: ")
    print(f"o1->o2 = 'r'\n o2->o1 = 'w'\n\n")
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')

    # edge_labels=dict([((u,v,),d['weight'])
    #              for u,v,d in graph.edges(data=True)])
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.1')
    plt.show()


def take():
    #######***************----------- command take #######***************-----------

    data = open('take.csv', "r")
    graph = nx.DiGraph()
    nx.parse_adjlist(data, delimiter=',', create_using=graph, nodetype=str)

    graph['s1']['o1']['weight'] = 3
    graph['o1']['o2']['weight'] = 1
    print("------------- command take ----------------")
    print("Изначальная структура: ")
    print(f"s1->o1 = 't'\n o1->o2 = 'r'\n\n")
    # graph.add_edge('o1', 'o3', weight=1)
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.06')
    plt.show()
    #################################
    graph.add_edge('s1', 'o2', weight=1)
    print("Добавленные ребра: ")
    print(f"s1->o2 = 'r'\n\n")
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')

    # edge_labels=dict([((u,v,),d['weight'])
    #              for u,v,d in graph.edges(data=True)])
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.1')
    plt.show()


def grant():
    #######***************----------- command grant #######***************-----------

    data = open('grant.csv', "r")
    graph = nx.DiGraph()
    nx.parse_adjlist(data, delimiter=',', create_using=graph, nodetype=str)

    graph['s1']['o1']['weight'] = 4
    graph['s1']['o2']['weight'] = 1
    print("------------- command grant ----------------")
    print("Изначальная структура: ")
    print(f"s1->o1 = 'g'\n s1->o2 = 'r'\n\n")
    # graph.add_edge('o1', 'o3', weight=1)
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.06')
    plt.show()
    #################################
    graph.add_edge('o1', 'o2', weight=1)
    print("Добавленные ребра: ")
    print(f"o1->o2 = 'r'\n\n")
    pos = nx.spring_layout(graph)
    edge_labels = nx.get_edge_attributes(graph, 'weight')

    # edge_labels=dict([((u,v,),d['weight'])
    #              for u,v,d in graph.edges(data=True)])
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.1')
    plt.show()


def third():
    data = open('third.csv', "r")
    graph = nx.DiGraph()
    nx.parse_adjlist(data, delimiter=',', create_using=graph, nodetype=str)
    graph.add_edge('s2', 's1', weight=4)
    graph['s1']['s2']['weight'] = 4
    graph['s1']['o1']['weight'] = 3
    graph['o1']['o2']['weight'] = 3
    graph['o1']['s2']['weight'] = 3
    graph['o2']['o3']['weight'] = 3
    graph['o3']['o4']['weight'] = 3
    graph['o4']['s3']['weight'] = 3

    # print(f"s1->o1 = 'g'\n s1->o2 = 'r'\n\n")
    print("s1->s2 = 'g'")
    print("s1->o1 = 't'")
    print("s2->s1 = 'g'")
    print("o1->o2 = 't'")
    print("o1->s2 = 't'")
    print("o2->o3 = 't'")
    print("o3->o4 = 't'")
    print("o4->s3 = 't'")

    print("\n\ntg-подграф с типом 'G': s1 -- s2")
    print("Обнаружен мост между s1 и s3")
    nx.draw_circular(graph, with_labels=True, edge_cmap=plt.cm.Reds, connectionstyle='arc3, rad = 0.1')
    plt.show()
    #################################


def __main__():
    while True:
        l = [1, 2, 3]
        question = int(input("de_ure(1)de_facto(2): "))
        if question not in l:
            break
        else:
            if question == 2:
                command = int(input("write number de_facto rule: "))
                match command:
                    case 1:
                        post()
                    case 2:
                        spy()
                    case 3:
                        find()
                    case 4:
                        pass_()
            if question == 1:
                command = int(input("write number de_ure rule"))
                match command:
                    case 1:
                        take()
                    case 2:
                        grant()
            if question == 3:
                third()


if __name__ == __main__():
    __main__()

# import matplotlib.pyplot as plt
# import networkx as nx
#
# G = nx.DiGraph()
#
# G.add_edges_from([('A', 'B'), ('C', 'D'), ('graph', 'D')], weight=1)
# G.add_edges_from([('D', 'A'), ('D', 'E'), ('B', 'D'), ('D', 'E')], weight=2)
# G.add_edges_from([('B', 'C'), ('E', 'F')], weight=3)
# G.add_edges_from([('C', 'F')], weight=4)
#
# val_map = {'A': 1.0, 'D': 0.5714285714285714,
#            'H': 0.0}
#
# values = [val_map.get(node, 0.45) for node in G.nodes()]
# edge_labels = dict([((users, v,), d['weight'])
#                     for users, v, d in G.edges(data=True)])
# red_edges = [('C', 'D'), ('D', 'A')]
# edge_colors = ['black' if not edge in red_edges else 'red' for edge in G.edges()]
#
# pos = nx.spring_layout(G)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# nx.draw(G, pos, node_color=values, node_size=800, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
# plt.show()
