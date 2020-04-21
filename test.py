import networkx as nx
import pandas as pd
import cpalgorithm as cp
import matplotlib.pyplot as plt


df = pd.read_csv('Using dataset.csv', sep=',')  # load data from dataset

G = nx.from_pandas_edgelist(df)
#M = nx.erdos_renyi_graph(80, 0.1)
L = nx.karate_club_graph()

algorithm = cp.KM_config()  # algorithm
algorithm.detect(L)
c = algorithm.get_pair_id()
x = algorithm.get_coreness()

nameString = "karate_club_KM_config"

file = open(nameString+".txt", "w")  # make the result as a txt file
file.write('Name\tPairID\tCoreness\n')

for key, value in sorted(c.items(), key=lambda x: x[1]):
    file.write('%s\t%d\t%f\n' %(key, c[key], x[key]))
file.close()

plt.figure(3, figsize=(8, 6))
cmap = plt.cm.get_cmap('Set1')
pos = nx.spring_layout(L)
node_colors = [cmap(c[d]) if x[d] ==1 else "white" for d in L.nodes()]
node_edge_colors = [cmap(c[d]) if x[d] ==0 else "black" for d in L.nodes()]
node_labels = [d for d in L.nodes()]

nodes = nx.draw_networkx_nodes(L, pos,  node_color=node_colors, linewidths=2)
nodes.set_edgecolor(node_edge_colors)
nx.draw_networkx_edges(L, pos)
nx.draw_networkx_labels(L, pos)

plt.gca().axis('off')
plt.title(nameString)  
plt.savefig(nameString+'.png')  # save the graph as a png file
