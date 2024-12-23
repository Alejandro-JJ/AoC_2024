'''
Day 23: LAN Party
'''
from collections import defaultdict
from itertools import combinations, permutations
from time import time
from tqdm import tqdm

start = time()
with open('input.txt', 'r') as f:
    data = [line.strip('\n').split('-') for line in f.readlines()]

Connections = defaultdict(set)

for entry in data:
    left, right = entry
    Connections[left].add(right)
    Connections[right].add(left)

VALID = []
# Check for each entry whether each combination is present in the list
for computer in tqdm(list(Connections.keys())):
    neighbors = list(Connections[computer])
    #print(neighbors)
    neighbors_combs = list(combinations(neighbors, 2))
    #print(neighbors_combs)
    # For each combination, both must be in original data
    for comb in neighbors_combs:
        left, right = comb
        if [left, right] in data or [right, left] in data:
            # It is a valid connection
            # We save it only if it was not seen before
            # We look for duplicates of all 9 possibilities
            triangle = [computer, left, right]
            threesomes = list(permutations(triangle, 3))
            #print(threesomes)
            if all (ts not in VALID for ts in threesomes):
                VALID.append((computer, left, right))



# How many of them contain a 't'
sol = 0
for threesome in VALID:
    a, b, c = threesome
    if a.startswith('t') or b.startswith('t') or c.startswith('t'):
        #print(threesome)
        sol+=1
print(f'Solution: {sol}')
print(f'Runtime {time()-start} seconds')