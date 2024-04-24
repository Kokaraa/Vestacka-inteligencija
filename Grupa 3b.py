# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 07:54:03 2023

@author: SINISA
"""

import networkx as nx

G = nx.Graph()

G.add_weighted_edges_from([(15, 5, 7), (15, 'SI', 31), (15, 'IT', 24),(5, 20, 62), (20, 10, 87),('SI', 'IT', 14), (5, 10, 45), ('IT', 10, 57)])

pos = nx.spiral_layout(G)
weight = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos= pos, with_labels = True, node_color = 'yellow', node_size = 750, font_color = 'red', font_size = 14, font_family = 'Arial')
nx.draw_networkx_edge_labels(G, pos, edge_labels = weight, font_size = 12)

print("\nČvorovi:\n", G.nodes)

print("\nGrane:\n", G.edges)

print("\nNajkraća putanja sa težinom:\n", nx.shortest_path(G, source='IT', target=5, weight='weight'))

print("\nNajkraća putanja bez težine:\n", nx.shortest_path(G, source='SI', target=5))

p = nx.shortest_path_length(G, source=5, target='IT', weight='weight')
print ("\nSuma težina:\n", p)