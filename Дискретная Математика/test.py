import networkx as nx

#---directed graph---
G = nx.DiGraph(directed=True)

# add nodes
G.add_node("Singapore")
G.add_node("San Francisco")
G.add_node("Tokyo")
G.add_nodes_from(["Riga", "Copenhagen"])

# add edges
G.add_edge("Singapore","San Francisco")
G.add_edge("San Francisco","Tokyo")
G.add_edges_from(
    [
        ("Riga","Copenhagen"),
        ("Copenhagen","Singapore"),
        ("Singapore","Tokyo"),
        ("Riga","San Francisco"),
        ("San Francisco","Singapore"),
    ]
)
# set layout
pos = nx.circular_layout(G)

# draw graph
nx.draw(G, pos, with_labels = True)

# draw edge labels
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={
        ("Singapore","Tokyo"): '2 flights daily',
        ("San Francisco","Singapore"): '5 flights daily',
    },
    font_color='red'
)