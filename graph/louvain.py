import json
import networkx as nx
import community
import matplotlib.pyplot as plt

# Load JSON data into a Python dictionary
with open('./preprocessed_reduce.json', 'r') as f:
    data = json.load(f)

# Convert the combined data to a list of edges
edges = []
for key, value in data.items():
    nodes = key.split('-')
    edge = (nodes[0], nodes[1], value)
    edges.append(edge)

# Create a graph and add the edges
G = nx.Graph()
G.add_weighted_edges_from(edges)

# Run the Louvain algorithm
partition = nx.community.louvain_communities(G)

# plot the graph with nodes colored by their community membership
pos = nx.spring_layout(G)
colors = ['r', 'g', 'b', 'y', 'c', 'm']
for i, community in enumerate(partition):
    nx.draw_networkx_nodes(G, pos, nodelist=list(
        community), node_color=colors[i % len(colors)], node_size=30)
nx.draw_networkx_edges(G, pos=pos)
plt.show()
