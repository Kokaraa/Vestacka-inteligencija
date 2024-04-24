# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 07:54:03 2023

@author: SINISA
"""

import networkx as nx
#Generisanje praznog grafa
G = nx.Graph()

#Dodavanje čvorova i grana grafu G
G.add_nodes_from([5, 7, 9, 'Fakultet'])
G.add_edges_from([(5, 7), (5, 9), (5, 'Fakultet')])

G.add_nodes_from([4, 6])
print("\nDodavanje dva nova čvora:\n", G.nodes, G.edges)

G.add_edges_from([(4, 5, {'fakultet':'Tehnički'}), (4, 7, {'smer':'Informacione tehnologije'}), (6, 9, {'godina':'3'}), (6, 'Fakultet')])

print("\nPovezivanje dodatih čvorova i kreiranje novih grana:\n", G.nodes, G.edges)

for prom in G.neighbors('Fakultet'): print("\nLista susedstva za čvor Fakultet bez atributa:\n", prom)

print("\nLista susedstva:\n", G.adj) #Lista susedstva

print("\nStepen čvora Fakultet:\n",G.degree['Fakultet'])

A = nx.adjacency_matrix(G) #Vraća SciPy retku matricu

print("\nSimetrična matrica susedstva:\n", A.todense())

print("\nNajkraći put:\n", nx.shortest_path(G, source = 'Fakultet', target = 9 ))

print("\nNajkraća dužina putanje:\n", nx.shortest_path_length(G, source='Fakultet', target = 7))

print("\nBroj čvorova:\n", G.number_of_nodes())
print("\nBroj grana:\n", G.number_of_edges())

d=list(nx.dfs_edges(G, 'Fakultet'))
print("\nPretraga u dubinu:\n",d)

pos = nx.spring_layout(G) 

nx.draw(G, pos= pos, with_labels = True, node_color = 'green', node_size = 2000, font_color = 'white', font_size = 10, font_family = 'Verdana')