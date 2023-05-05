import json
import networkx as nx
import community

# Load JSON data into a Python dictionary
with open('./graph/preprocessed.json', 'r') as f:
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

part = community.best_partition(G)
print("🚀 ~ file: louvain.py:24 ~ part:", part)
mod = community.modularity(part, G)
print("🚀 ~ file: louvain.py:25 ~ mod:", mod)
