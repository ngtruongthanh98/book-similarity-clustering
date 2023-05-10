from networkx.algorithms.community.quality import modularity
import random
import networkx as nx
import community
import matplotlib.pyplot as plt
import pickle
filename = 'preprocessed_reduce_4'
G = pickle.load(open(f'{filename}.pickle', 'rb'))

# print number of edges and nodes
print("Number of edges:", G.number_of_edges())
print("Number of nodes:", G.number_of_nodes())

# Run the Louvain algorithm
partition = nx.community.louvain_communities(G)


mod = modularity(G, partition)

print('Modularity of the best partition:', mod)

pickle.dump(partition, open(
    f'louvain.pickle', 'wb'))

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
