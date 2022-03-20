import csv

import matplotlib.pyplot as plt
import networkx as nx

temp_list = []
data = open('temp_csv.csv', "r")
with open('temp_csv.csv', 'r') as csv_r:
    reader = csv.reader(csv_r)
    for i in reader:
        temp_list.append(i)


graph = nx.DiGraph()
nx.parse_adjlist(data, delimiter=',', create_using=graph, nodetype=str)

graph['o1']['o2']['weight'] = 1
graph['o2']['o3']['weight'] = 1
# graph.add_edge('o1', 'o3', weight=1)
pos = nx.spring_layout(graph)

# node_labels = nx.get_node_attributes(graph, 'weight')
# nx.draw_networkx_labels(graph, pos, labels=node_labels)
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
nx.draw(graph, pos, with_labels=True, edge_cmap=plt.cm.Reds)
plt.show()
# for i in nx.generate_adjlist(graph, delimiter=','):
#     print(i)
# print(graph.nodes)

