import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Draw the nodes
pos = nx.spring_layout(G)  # Compute the layout of the graph
nx.draw_networkx_nodes(G, pos, node_color='r', node_size=500)

# Draw the edges
nx.draw_networkx_edges(G, pos, width=2)

# Show the plot
plt.show()
