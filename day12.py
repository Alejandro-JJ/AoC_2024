'''
Day 12: Garden walls
'''
with open('11.txt', 'r') as f:
    garden =[[s for s in line.strip('\n')] for line in f.readlines()]
H, W = len(garden), len(garden[0])

def neigh(row, col):
    n = []
    for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
        newrow, newcol = row+dr, col+dc
        if 0<=newrow<H and 0<=newcol<W:
            n.append(garden[newrow][newcol])
        else: 
            n.append('out')
    return n

# All info will be saved in a dictionary
# 'letter': [area, perim]
meas = {}
for r in range(0, H):
    for c in range(0, W):
        letter = garden[r][c]
        # Letter not seen before, create its entry
        if letter not in meas.keys():
            meas[letter] = [0,0]
        # Get neighbors and update current value
        old_area, old_perim = meas[letter]
        new_area = 1
        new_perim = len([n for n in neigh(r,c) if n!=letter])
        meas[letter] = [old_area+new_area, old_perim+new_perim]

print(meas)

price = 0
for letter in meas.keys():
    price += meas[letter][0]*meas[letter][1]
    
print(f'Solution part 1: {price}')

import numpy as np
import matplotlib.pyplot as plt
import pyclesperanto_prototype as cle
pixels = np.arange(1, len(meas.keys())+1)
pixvalue = list(zip(meas.keys(), pixels))
G = np.zeros((H,W))
print(pixvalue)
