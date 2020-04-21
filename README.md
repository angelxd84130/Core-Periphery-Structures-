# Core-periphery structure analysis and visualization

1. Python packages used: matplotlib, pandas, cpalgorithm, networkx

2. Motivation: Project idea 2.2.3, It is important to maintain a who-trusts-whom network for block-chain based technologies such as bitcoins.
Core-periphery structures might help in detection of anomalies in transactions, or observe network-level transaction trends in crypto-currencies.

3. Further reading: Core Periphery Structures in Weighted Graphs Using Greedy Growth - Sardana et al. 
http://ieeexplore.ieee.org/document/7817029/

   Finding multiple core-periphery pairs in networks - Kojaku et al 
https://arxiv.org/abs/1702.06903

   A Graph Modification Approach for Finding Core–Periphery Structures in Protein Interaction Networks - Bruckner et al. 
https://link.springer.com/chapter/10.1007/978-3-662-44753-6_25

4. Dataset sourse: http://snap.stanford.edu/data/

5. Changes to the dataset: We modify the dataset format from integer to variable for the first two columns in order to fit in the requirement of generating a graph using networkx.

6. In order to install the packages all succuessfully, the user has to install a c++ complier before pip install operation. Otherwise, the required packages are not allowed to be installed into your environment.
