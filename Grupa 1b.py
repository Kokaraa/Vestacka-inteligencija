# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:48:39 2023

@author: SINISA
"""

import networkx as nx

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 'TFZR'])

G.add_weighted_edges_from([(1, 2, 68), (1, 3, 5), (1, 'TFZR', 15), (2, 4, 7), (3, 6, 8), (1, 7, 20), ('TFZR', 4, 28), ('TFZR', 6, 37)])

pos = {
1:(6.5, 7),
2:(4.5, 6),
3:(10, 6.5),
4:(7, 5.5),
6:(8.5, 6),
7:(6, 6),
"TFZR":(9, 5),
}

weight = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos = pos, with_labels = True, node_color="red", node_size=1000, font_color="black", font_size=16, font_family="Times New Roman")

nx.draw_networkx_edge_labels(G, pos, edge_labels = weight, font_size=13)

print("\nČvorovi:\n", G.nodes)

print("\nGrane:\n", G.edges)

print("\nNajkraća putanja sa težinom:\n", nx.shortest_path(G, source='TFZR', target=2, weight='weight'))

print("\nNajkraća putanja bez težine:\n", nx.shortest_path(G, source='TFZR', target=2))

p = nx.shortest_path_length(G, source='TFZR', target=3, weight='weight')
print ("\nSuma težina:\n", p)