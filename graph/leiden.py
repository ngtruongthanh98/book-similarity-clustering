import random
import json
import networkx as nx
import community
from cdlib import algorithms, evaluation
import pickle
from networkx.algorithms.community.quality import modularity
import matplotlib.pyplot as plt

filename = 'preprocessed_reduce_4'
G = pickle.load(open(f'{filename}.pickle', 'rb'))

# print number of edges and nodes
print("Number of edges:", G.number_of_edges())
print("Number of nodes:", G.number_of_nodes())

partition = algorithms.leiden(G)

mod = modularity(G, partition.communities)


# plot the graph with nodes colored by their community membership
pos = nx.spring_layout(G)
# Define a list of random colors
colors = ["#"+''.join([random.choice('0123456789ABCDEF')
                      for j in range(6)]) for i in range(len(partition.communities))]
for i, community in enumerate(partition.communities):
    nx.draw_networkx_nodes(G, pos, nodelist=list(
        community), node_color=colors[i % len(colors)], node_size=30)

edge_subset = random.sample(G.edges(), 500)
nx.draw_networkx_edges(G, pos=pos)
plt.show()
