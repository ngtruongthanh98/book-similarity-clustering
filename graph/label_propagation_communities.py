import pickle
import networkx as nx
import community
import matplotlib.pyplot as plt

filename = 'preprocessed_reduce'
G = pickle.load(open(f'{filename}.pickle', 'rb'))

# Run the Louvain algorithm
partition = nx.community.label_propagation_communities(G)

# plot the graph with nodes colored by their community membership
pos = nx.spring_layout(G)
colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'w', 'orange', 'purple']
for i, community in enumerate(partition):
    nx.draw_networkx_nodes(G, pos, nodelist=list(
        community), node_color=colors[i % len(colors)], node_size=30)
nx.draw_networkx_edges(G, pos=pos)
plt.show()
