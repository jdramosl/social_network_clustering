import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

# Crear un grafo vacío
G = nx.Graph()

# Leer el archivo de aristas (edges) y agregar las conexiones al grafo
with open('12831.edges', 'r') as f_edges:
    for line in f_edges:
        source, target = line.strip().split()
        G.add_edge(source, target)

# Leer el archivo de características (feat) y agregar las características a los nodos
with open('12831.feat', 'r') as f_feat:
    for line in f_feat:
        node, *features = map(int, line.strip().split())
        G.add_node(node, features=features)

# Leer el archivo de características ego (egofeat) y agregarlas al nodo ego
with open('12831.egofeat', 'r') as f_egofeat:
    features = list(map(int, f_egofeat.readline().strip().split()))
    if G.has_node('ego'):
        G.nodes['ego']['features'] = features

# Leer el archivo de círculos (circles) y agregar las relaciones entre nodos a los grupos
with open('12831.circles', 'r') as f_circles:
    for line in f_circles:
        circle, *nodes = line.strip().split()
        for node in nodes:
            if G.has_node(node):
                G.nodes[node]['circle'] = circle

# Ahora tienes un grafo G con nodos, aristas y características asociadas. Puedes realizar análisis de grafos, aprendizaje automático u otras tareas según sea necesario.
degrees = [G.degree[node] for node in G.nodes()]
degrees
print("hi")
print(degrees)
cc = nx.clustering(G)
plt.hist(list(cc.values()),bins='auto')
plt.ylabel("Frequency")
plt.title("Figure 32: Social network clustering")
plt.xlabel("Clustering coefficient.")
bc = nx.betweenness_centrality(G)
dict(sorted(bc.items(), key= lambda kv: kv[1], reverse=True))

ac = nx.degree_assortativity_coefficient(G)
ac