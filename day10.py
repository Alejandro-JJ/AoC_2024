'''
Day 10: Hiking trails
'''
import numpy as np
from collections import deque
from time import time
start_time = time()

with open('./10.txt', 'r') as f:
    data = [[s for s in line.strip('\n')] for line in f.readlines()]
H, W = len(data), len(data[0])

mapa = np.zeros((H,W))
for r in range(0,H):
    for c in range(0,W):
        # Include this line to work with examples
        if data[r][c]!= '.':
            mapa[r,c] = int(data[r][c])
        else:
            mapa[r,c] = -3 # unreachable

# Starting points for the hikes
starts = list(zip(*np.where(mapa==0)))
#print(f'Starting points : {starts}')

def isInMap(pos):
    '''
    says if a tuple (row, col) is 
    inside the map
    '''
    row, col = pos
    if 0<=row<H and 0<=col<W:
        return True
    else:
        return False

def findNeigh(pos):
    '''
    calculates all possible four neighbors
    and return the valid ones with are in
    '''
    row, col = pos
    n1 = (row+1, col)
    n2 = (row-1, col)
    n3 = (row, col+1)
    n4 = (row, col-1)
    valid = []
    for n in [n1,n2,n3,n4]:
        if isInMap(n):
            valid.append(n)
    return valid


def hike(start):
    possible_paths = []
    queue = deque([start])
    visited = set()
    #print(f'Current queue: {queue=}')
    
    # as long as there are elements to be explored
    while queue:
        curr_pos = queue.popleft()
        #print(f'Current position {curr_pos=}')
        neighbours = findNeigh(curr_pos)
        # we have several neighbours
        for neigh in neighbours:
            # if we have seen the position, pass
            # for part 2, we dont avoid positions previously visited
            
            #if neigh in visited:
            #    pass
            #else:
            # If we can move there, move
            if mapa[neigh[0], neigh[1]] == mapa[curr_pos[0], curr_pos[1]]+1:
                
                # if we found a nine, found a destination
                if mapa[neigh[0], neigh[1]] == 9:
                    #print(f'Found a destination in {neigh}')
                    possible_paths.append(neigh)
                    visited.add(neigh)
                # If not a nine, continue path
                else:
                    #print(f'Took a step from {curr_pos} to {neigh}')
                    visited.add(neigh)
                    queue.append(neigh)
            
            # If it has another value, pass
            else:
                pass
    #print(f'Possible paths: {len(possible_paths)}')
    #print(f'Unique paths: {len(set(possible_paths))}')
    return len(possible_paths), len(set(possible_paths))

score = 0
rating = 0
for start in starts:
    possible, unique = hike(start)
    score += unique
    rating += possible

print(f'Part 1: {score}')
print(f'Part 2: {rating}')
                
print(f'Total runtime: {(time()-start_time)} seconds')