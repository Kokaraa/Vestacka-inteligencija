# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 07:54:03 2023

@author: SINISA
"""

import networkx as nx

G = nx.Graph()

G.add_nodes_from([15, 5, 'IT', 'SI'])
G.add_edges_from([(15, 5), (15, 'SI'), (15, 'IT')])

G.add_nodes_from([10, 20])
print("\nDodavanje dva nova čvora:\n", G.nodes, G.edges)

G.add_edges_from([(5, 20), (20, 10),('SI', 'IT', {'katedra':'Informacione tehnologije'}), (5, 10), ('IT', 10, {'predmet':'Sistemi veštačke inteligencije'})])

print("\nLista susedstva:\n", G.adj) #Lista susedstva

for prom in G.neighbors('SI'): print("\nLista susedstva za čvor SI bez atributa:\n", prom)

print("\nStepen čvora IT:\n",G.degree['IT'])

A = nx.adjacency_matrix(G) #Vraća SciPy retku matricu

print("\nMatrica susedstva:\n", A)

print("\nSvi najkraći putevi:\n", [p for p in nx.all_shortest_paths(G, source='IT', target = 5)])
   
print("\nNajkraća dužina putanje:\n", nx.shortest_path_length(G, source='SI', target=5))

print("\nProsečna dužina putanje:\n", nx.average_shortest_path_length(G))
print("\nBroj čvorova:\n", G.number_of_nodes())
print("\nBroj grana:\n", G.number_of_edges())

d=list(nx.dfs_edges(G, 15, 1))
print("\nPretraga u dubinu:\n",d)

pos = nx.spiral_layout(G)

nx.draw(G, pos= pos, with_labels = True, node_color = 'yellow', node_size = 750, font_color = 'red', font_size = 14, font_family = 'Arial')