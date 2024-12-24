'''
LAN Party with networkx
'''
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()


with open('input.txt','r') as f:
    lista = [line.strip('\n').split('-') for line in f]
    
    
for line in lista:
    left, right = line
    G.add_edge(left, right)    
        
#Plot
#fig = plt.figure()
#nx.draw(G, with_labels=True, node_size=5, font_size=3)
#plt.show()

# Find the cliques: subsets of connected elements
clusters = list(nx.find_cliques_recursive(G))
# Get the largest one
print(clusters)
clusters.sort(key=len)
clusters[-1].sort()

print(",".join(clusters[-1]))