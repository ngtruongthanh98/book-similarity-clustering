import json
import networkx as nx
import pickle

# Load JSON data into a Python dictionary
file_name = 'preprocessed_reduce'
with open(f'./{file_name}.json', 'r') as f:
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

pickle.dump(G, open(f'{file_name}.pickle', 'wb'))
