import networkx as nx
import community
from cdlib import algorithms, evaluation
import random
import matplotlib.pyplot as plt
import pickle

filename = 'preprocessed_reduce_3'
G = pickle.load(open(f'{filename}.pickle', 'rb'))

partition = algorithms.walktrap(G)

# plot the graph with nodes colored by their community membership
pos = nx.spring_layout(G)
# Define a list of random colors
colors = ["#"+''.join([random.choice('0123456789ABCDEF')
                      for j in range(6)]) for i in range(len(partition))]
for i, community in enumerate(partition):
    nx.draw_networkx_nodes(G, pos, nodelist=list(
        community), node_color=colors[i % len(colors)], node_size=30)

edge_subset = random.sample(G.edges(), 500)
nx.draw_networkx_edges(G, edgelist=edge_subset, pos=pos)
plt.show()
