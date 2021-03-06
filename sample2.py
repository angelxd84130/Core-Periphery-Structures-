import networkx as nx
import pandas as pd
import cpalgorithm as cp

df = pd.read_csv('bitcoin_notime.csv', sep=',', names=['from', 'to', 'rate'])     #load data from dataset


G = nx.from_pandas_edgelist(df)

algorithm = cp.KM_config()
algorithm.detect(G)
c = algorithm.get_pair_id()
x = algorithm.get_coreness()

print(c)



# print('Name\tPairID\tCoreness')
# for key, value in sorted(c.items(), key=lambda x: x[1]):
#     print('%s\t%d\t%f' %(key, c[key], x[key]))
