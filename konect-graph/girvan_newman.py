import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import community

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


def girvan_newman_algorithm(G):
    # calculate initial betweenness centrality of all edges
    betweenness = nx.edge_betweenness_centrality(G)

    while len(G.edges()) > 0:
        # remove edge with highest betweenness centrality
        max_edge = max(betweenness, key=betweenness.get)
        G.remove_edge(*max_edge)

        # recalculate betweenness centrality of remaining edges
        betweenness = nx.edge_betweenness_centrality(G)

        # check if the graph has been split into disconnected components
        if nx.number_connected_components(G) > 1:
            # if so, return the list of communities
            communities = list(nx.connected_components(G))
            return communities

    # if no disconnected components are found, return the original graph as a single community
    return [set(G.nodes())]


# run the Girvan-Newman algorithm on a test graph
communities = girvan_newman_algorithm(G)

partition_formatted = {}

for i, d in enumerate(communities):
    for v in d:
        partition_formatted[v] = i

print("🚀 ~ file: louvain.py:24 ~ partition_formatted:", partition_formatted)
modularity = community.modularity(partition_formatted, G)

print('Modularity of the best partition:', modularity)

# plot the graph with nodes colored by their community membership
pos = nx.spring_layout(G)
colors = ['r', 'g', 'b', 'y', 'c', 'm']
for i, community in enumerate(communities):
    nx.draw_networkx_nodes(G, pos, nodelist=list(
        community), node_color=colors[i % len(colors)], node_size=30)
nx.draw_networkx_edges(G, pos=pos)
plt.show()
