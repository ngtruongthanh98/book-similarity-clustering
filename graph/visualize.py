import matplotlib.pyplot as plt
import pickle
import networkx as nx
import random

G = pickle.load(open(f'./graph/preprocessed_reduce_2.pickle', 'rb'))
partition = pickle.load(
    open(f'./graph/label_propagation_communities.pickle', 'rb'))

# Create a new empty graph
subgraph = nx.Graph()
sub_communities = []
node_samples = []
for community in partition:
    # Randomly select the number of elements to choose
    num_to_choose = random.randint(30, 45)
    # Choose a random sample of elements from the set
    community = list(community)
    node_sample = random.sample(community, min(num_to_choose, len(community)))
    sub_communities.append(set(node_sample))
    # Add the selected nodes and their edges to the subgraph
    subgraph.add_nodes_from(node_sample)
    subgraph.add_edges_from(G.subgraph(node_sample).edges())

# plot the graph with nodes colored by their community membership
pos = nx.spring_layout(subgraph)

# Define a list of random colors
colors = ["#"+''.join([random.choice('0123456789ABCDEF')
                      for j in range(6)]) for i in range(len(sub_communities))]

for i, community in enumerate(sub_communities):
    nx.draw_networkx_nodes(subgraph, pos, nodelist=list(
        community), node_color=colors[i % len(colors)], node_size=30)
nx.draw_networkx_edges(subgraph, pos=pos)
plt.show()
