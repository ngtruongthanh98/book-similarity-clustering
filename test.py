import pandas as pd
import networkx as nx
import community
import matplotlib.pyplot as plt

# Read the dataset from a file and create a DataFrame
df = pd.read_csv('out.dimacs10-polbooks.txt', sep='\t', header=None,
                 names=['source', 'target'])

# Create a networkx graph from the DataFrame
G = nx.from_pandas_edgelist(df, 'source', 'target')

# Find the communities using Louvain algorithm
partition = community.best_partition(G)

# Visualize the graph
pos = nx.spring_layout(G)
cmap = plt.get_cmap('viridis')
nx.draw_networkx_nodes(G, pos, node_size=50,
                       node_color=list(partition.values()), cmap=cmap)
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()
