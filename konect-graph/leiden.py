import pandas as pd
import networkx as nx
import community
import matplotlib.pyplot as plt
from cdlib import algorithms

# Read the dataset from a file and create a DataFrame
df = pd.read_csv('out.dimacs10-polbooks.csv', header=None,
                 names=['source', 'target'])

edges = []
for index, row in df.iterrows():
    edge = (row['source'], row['target'])
    edges.append(edge)
# Create a networkx graph from the DataFrame
G = nx.Graph()
G.add_edges_from(edges)

# Find the communities using Louvain algorithm
partition = algorithms.leiden(G)

# Calculate the modularity of the best partition

partition_formatted = {}

for i, d in enumerate(partition.communities):
    for v in d:
        partition_formatted[v] = i

modularity = community.modularity(partition_formatted, G)

print('Modularity of the best partition:', modularity)

# plot the graph with nodes colored by their community membership
pos = nx.spring_layout(G)
colors = ['r', 'g', 'b', 'y', 'c', 'm']
for i, community in enumerate(partition.communities):
    nx.draw_networkx_nodes(G, pos, nodelist=list(
        community), node_color=colors[i % len(colors)], node_size=30)
nx.draw_networkx_edges(G, pos=pos)
plt.show()
