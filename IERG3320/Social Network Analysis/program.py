# Cai Long Hua
# SID: 1155126875
# My class ID: 1

import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np
import networkx as nx
import pandas as pd
import csv

# read the sociomatrix.csv file, which is changed from Edges.csv. 
# More details, please see README.txt
df = pd.read_csv('sociomatrix.csv', header=None)
print("Sociomatrix:\n")
print(df,"\n")

# change sociomatrix to adjacency matrix (list)
print("Adjacency Matrix:\n")
ADJ_matrix = df.to_numpy()
print(ADJ_matrix, "\n")

# box list for storing edges from matrix
box = []

# judge that if there is existing edges between two nodes
# it means that if someone comments someone's blog
for a in range(len(ADJ_matrix)):
  for b in range(len(ADJ_matrix)):
    # 1 means that comment is happened
    if ADJ_matrix[a][b] == 1:
      box.append((a+1,b+1))
print("Relationship:\n")
print(box,"\n")

# set the size of figure and element
plt.figure(figsize=(8,6), frameon="True", num="This is graph G represent sociomatrix, please close the window then see the result values in CMD")

# create a direct graph
G_direct = nx.DiGraph()

# add nodes and edges from box
G_direct.add_edges_from(box)

# plot the G direct graph
nx.draw_networkx(G_direct, node_size = 400 ,node_color="blue")
plt.title("Direct graph G")
sn.set(style = "whitegrid")
plt.show()

# print out the result of in-degree, out-degree, closeness centrality and betweenness centrality
print("My class ID is 1, thus my node is also 1\n")
print("The value of the in-degree of the node 1: ", G_direct.in_degree(1))
print("The value of the out-degree of the node 1: ", G_direct.out_degree(1))
print("The value of the closeness centrality of the node 1: ", nx.closeness_centrality(G_direct)[1])
print("The value of the betweenness centrality of the node 1: ", nx.betweenness_centrality(G_direct)[1])



