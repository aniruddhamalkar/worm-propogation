import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G = nx.Graph()
G.add_edge(2, 3, weight=0.9)
G = nx.cubical_graph()
plt.subplot(121)
#<matplotlib.axes._subplots.AxesSubplot object at ...>
nx.draw(G)   # default spring_layout
plt.subplot(122)
#<matplotlib.axes._subplots.AxesSubplot object at ...>
nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b')
