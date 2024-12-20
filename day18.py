'''
Day 18: Maze with falling bites
'''

import numpy as np
import matplotlib.pyplot as plt
from heapq import heapify, heappop, heappush
from time import time
from tqdm import tqdm

start = time()
with open('input.txt') as f:
    bites = [list(map(int,[s for s in  line.strip('\n').split(',')])) for line in f.readlines()]
H, W = 71, 71 # 70, 70    


def CanWeGetOut(bit_idx): 
    # Make maze and fill up to certain value
    maze = np.zeros((H, W))
    
    for bit in bites[:bit_idx]:
        x, y = bit
        maze[y,x]=1
    
    # BFS to get out of maze
    end = (H-1, W-1)
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    queue = [(0, 0, 0)] # <- steps, y, x
    heapify(queue)
    visited = set((0,0,0))

    foundExit = False
    
    while queue:
        #print(f'length of queue {len(queue)}')
        steps, y, x = heappop(queue)
        # New possible states
        for direction in directions:
            dy, dx = direction
            ny, nx = y+dy, x+dx
            newsteps = steps+1
            if (ny, nx)==end:
                #print(f'Found solution with {newsteps} steps')
                foundExit = True
                break
            
            # Only conitnue iteration if we are inside bounds and not in wall
            if 0<=ny<H and 0<=nx<W and maze[ny, nx]==0:
                # Ignore if we visited it before
                if (ny, nx) in visited:
                    continue
                visited.add((ny,x))
                
                # Store new state in queue
                heappush(queue, (newsteps, ny, nx))
            else:
                continue
    return foundExit


for bit_idx in tqdm(range(0, len(bites))):
    if CanWeGetOut(bit_idx):
        pass
    else:
        print(f'Way blocked by {bites[bit_idx-1]}')
        break
    
    
print(f'Runtime {time()-start} seconds')