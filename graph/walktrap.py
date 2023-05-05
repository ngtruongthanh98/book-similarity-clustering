import json
import networkx as nx
import community
from cdlib import algorithms, evaluation

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

partition = algorithms.walktrap(G)

ave = evaluation.avg_embeddedness(G, partition)
print("🚀 ~ file: surprise_community_detection.py:24 ~ ave:", ave)
