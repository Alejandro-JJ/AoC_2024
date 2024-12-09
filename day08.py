'''
Day 8: Antennas
'''
from collections import defaultdict
from itertools import combinations
import numpy as np
import matplotlib.pyplot as plt
from tools import ReadTextInput
# Load data
data, H, W = ReadTextInput('./8.txt')
print(f'Height: {H}, Width {W}')

# Create dictionary of positions
Antenna_Pos = defaultdict(list)

for row in range(0, H):
    for column in range(0, W):
        char =  data[row][column]
        if char != '.':
            Antenna_Pos[char].append((row, column))

def isInside(node):
    '''
    returns boolean, whether node is inside
    or outside the grid
    '''    
    if 0<=node[0]<H and 0<=node[1]<W:
        return True
    else:
        return False

def DrawNodes(pos1, pos2):
    '''
    Given two antennas at pos1 and pos2 (tuples)
    calculates the position of the two new possible
    nodes
    '''
    r1, c1 = pos1
    r2, c2 = pos2
    v1 = (r1-r2, c1-c2)
    v2 = (r2-r1, c2-c1)
    new1 = (r1+v1[0], c1+v1[1])
    new2 = (r2+v2[0], c2+v2[1])
    return new1, new2

def DrawNodes2(pos1, pos2):
    '''
    Given two antennas at pos1 and pos2 (tuples)
    calculates the position of all the new possible
    nodes and saves them in a list
    '''
    r1, c1 = pos1
    r2, c2 = pos2
    v1 = (r1-r2, c1-c2)
    v2 = (r2-r1, c2-c1)
    nodes = []
    # Generate nodes1
    escaped_1 = False
    scale_1 = 0
    while escaped_1==False:  
        new =  (r1+scale_1*v2[0], c1+scale_1*v2[1])
        if isInside(new):
            nodes.append(new)
            print(f'Added {new} as candidate')
            scale_1+=1
        else: 
            print(f'Node {new} escaped')
            escaped_1=True
        
    # Generate nodes2
    escaped_2 = False
    scale_2 = 0
    while escaped_2==False:  
        new =  (r2+scale_2*v1[0], c2+scale_2*v1[1])
        if isInside(new):
            nodes.append(new)
            print(f'Added {new} as candidate')
            scale_2+=1
        else: 
            print(f'Node {new} escaped')
            escaped_2=True
    
    return nodes




# Loop through all combinations
valid_nodes = set()
sol = 0

for type in Antenna_Pos.keys():
    for a1, a2 in list(combinations(Antenna_Pos[type], 2)):
        new1, new2 = DrawNodes(a1, a2)
        #print(f'Type {type}: {a1}, {a2} --> {new1}, {new2}')
        
        # Check that they fit into array
        if isInside(new1) and new1 not in valid_nodes:
            valid_nodes.add(new1)
            sol+=1
            
        if isInside(new2) and new2 not in valid_nodes:
            valid_nodes.add(new2)
            sol+=1
print(f'Part1. Valid nodes: {sol}')

# For part 2, I use a new node generating function
valid_nodes_2 = set()
sol_2 = 0

for type in Antenna_Pos.keys():
    for a1, a2 in list(combinations(Antenna_Pos[type], 2)):
        newnodes = DrawNodes2(a1, a2)
        #print(f'Type {type}: {a1}, {a2} --> {new1}, {new2}')
        for node in newnodes:
            if isInside(node) and node not in valid_nodes_2:
                valid_nodes_2.add(node)
                sol_2+=1
print(f'Part2. Valid nodes: {sol_2}')


# Visualization:
mapa = np.zeros((H, W))
for type in Antenna_Pos.keys():
    for ant in Antenna_Pos[type]:
        mapa[ant[0], ant[1]] = 1

for nod in valid_nodes_2:
    mapa[nod[0], nod[1]] = 2
    
plt.imshow(mapa, cmap='summer')
plt.show()