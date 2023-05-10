import matplotlib.pyplot as plt
import random
import networkx as nx
import community
import pickle

filename = 'preprocessed_reduce_3'
G = pickle.load(open(f'{filename}.pickle', 'rb'))


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
pickle.dump(communities, open(
    f'girvan_newman.pickle', 'wb'))

# plot the graph with nodes colored by their community membership
pos = nx.spring_layout(G)
# Define a list of random colors
colors = ["#"+''.join([random.choice('0123456789ABCDEF')
                      for j in range(6)]) for i in range(len(communities))]
for i, community in enumerate(communities):
    nx.draw_networkx_nodes(G, pos, nodelist=list(
        community), node_color=colors[i % len(colors)], node_size=30)
nx.draw_networkx_edges(G, pos=pos)
plt.show()
print('')
