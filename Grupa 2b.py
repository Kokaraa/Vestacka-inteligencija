# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:21:07 2023

@author: SINISA
"""

import networkx as nx

G = nx.Graph()

G.add_weighted_edges_from([(5, 7, 11), (5, 9, 13), (5, 'Fakultet', 25),(4, 5, 47), (4, 7, 20), (6, 9, 28), (6, 'Fakultet', 71)])

pos = nx.spring_layout(G) 
weight = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos= pos, with_labels = True, node_color = 'green', node_size = 2000, font_color = 'white', font_size = 10, font_family = 'Verdana')

nx.draw_networkx_edge_labels(G, pos, edge_labels = weight, font_size=11)

print("\nČvorovi:\n", G.nodes)

print("\nGrane:\n", G.edges)

print("\nNajkraća putanja sa težinom:\n", nx.shortest_path(G, source='Fakultet', target=5, weight='weight'))

print("\nNajkraća putanja bez težine:\n", nx.shortest_path(G, source='Fakultet', target=7))

p = nx.shortest_path_length(G, source='Fakultet', target=9, weight='weight')
print ("\nSuma težina:\n", p)