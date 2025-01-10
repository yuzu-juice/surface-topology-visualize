import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

n = 5
adj = [(i,j%n) for i in range(n) for j in range(i+1,n)]    #辺のリスト
g = nx.Graph(adj)
nx.draw_circular(g)     #頂点をサイクル上に並べてグラフを描画
#plt.savefig("compGraph.png")   #描画したやつを保存

g = nx.complete_bipartite_graph(3,3)
nx.draw_circular(g)
