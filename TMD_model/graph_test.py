import networkx as nx
import matplotlib.pyplot as plt

extend_dict: dict = {
    "t_1": ["t_2", "t_5", "t_3", "t_4"],
    "t_2": ["t_3", "t_4"],
    "t_3": ["t_4"],
    "t_4": ["t_5"],
    "t_5": []
}


graph = nx.Graph()
for i in extend_dict:
    graph.add_node(i)

for i in extend_dict:
    for j in extend_dict[i]:
        graph.add_edge(i, j)

options = {
    'node_color': 'blue',
    'node_size': 500,
    'arrowstyle': '-|>',
    'arrowsize': 12,
}
nx.draw_networkx(graph, arrows=True, **options)
plt.show()
















#########################################################################################################
#!!!_________________------  метки на ребрах и ориентированность__________-------------!!!!!!!!!!
#########################################################################################################


# import networkx as nx
# import numpy as np
# import matplotlib.pyplot as plt
# import pylab
#
# graph = nx.DiGraph()
#
# graph.add_edges_from([('A', 'B'),('C','D'),('graph','D')], weight=1)
# graph.add_edges_from([('D','A'),('D','E'),('B','D'),('D','E')], weight=2)
# graph.add_edges_from([('B','C'),('E','F')], weight=3)
# graph.add_edges_from([('C','F')], weight=4)
#
#
# val_map = {'A': 1.0,
#                    'D': 0.5714285714285714,
#                               'H': 0.0}
#
# values = [val_map.get(node, 0.45) for node in graph.nodes()]
# edge_labels=dict([((users,v,),d['weight'])
#                  for users,v,d in graph.edges(data=True)])
# red_edges = [('C','D'),('D','A')]
# edge_colors = ['black' if not edge in red_edges else 'red' for edge in graph.edges()]
#
# pos=nx.spring_layout(graph)
# nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_labels)
# nx.draw(graph,pos, node_color = values, node_size=800,edge_color=edge_colors,edge_cmap=plt.cm.Reds)
# plt.show()