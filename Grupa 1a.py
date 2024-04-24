# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 07:54:03 2023

@author: SINISA
"""

import networkx as nx
#Generisanje praznog grafa
G = nx.Graph()

#Dodavanje čvorova i grana grafu G
G.add_nodes_from([1, 2, 3, 'TFZR'])
G.add_edges_from([(1, 2), (1, 3), (1, 'TFZR',{'ime':'Mihajlo'})])


G.add_nodes_from([4, 6, 7])
print("\nDodavanje tri nova čvora:\n", G.nodes, G.edges)

G.add_edges_from([(2, 4), (3, 6, {'prezime':'Pupin'}), (1, 7), ('TFZR', 4), ('TFZR', 6)])

print("\nPovezivanje dodatih čvorova i kreiranje novih grana:\n", G.nodes, G.edges)

print("\nLista susedstva za čvor TFZR sa atributima:\n", G['TFZR'])
print("\nStepen čvora TFZR:\n",G.degree['TFZR'])

A = nx.adjacency_matrix(G) #Vraća SciPy retku matricu

print("\nMatrica susedstva:\n", A)

print("\nNajkraći put:\n", nx.shortest_path(G, source = 3, target='TFZR'))

print("\nProsečna dužina putanje:\n", nx.average_shortest_path_length(G))

print("\nBroj čvorova:\n", G.number_of_nodes())
print("\nBroj grana:\n", G.number_of_edges())

w=list(nx.bfs_edges(G, 'TFZR'))
print("\nPretraga u širinu:\n",w)

pos = {
1:(6.5, 7),
2:(4.5, 6),
3:(10, 6.5),
4:(7, 5.5),
6:(8.5, 6),
7:(6, 6),
"TFZR":(9, 5),
}
   
nx.draw(G, pos = pos, with_labels = True, node_color="red", node_size=1000, font_color="black", font_size=16, font_family="Times New Roman")