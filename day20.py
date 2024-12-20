"""
Day 18: MAZE
"""
from tools import Text2Array
import numpy as np
import heapq
import matplotlib.pyplot as plt
from time import time
start = time()
plt.close('all')
with open('input.txt', 'r') as f:
    data = [[s for s in line.strip('\n')] for line in f.readlines()]
mydict = {'.':0, '#':1, 'S':2, 'E':3}
H, W = len(data), len(data[0])
# empty 0, wall 1, start 2, end 3

grid = Text2Array(data, mydict)
#plt.imshow(grid)
#plt.show()

#%
start_y, start_x = np.where(grid==2)[0][0], np.where(grid==2)[1][0]
end_y, end_x = np.where(grid==3)[0][0], np.where(grid==3)[1][0]
print(f'Start pos: {start_y, start_x}')
print(f'End pos: {end_y, end_x}')

directions = [(1,0), (-1,0), (0,1), (0,-1)]

# State will be (score, y, x, memory)
queue = []
heapq.heappush(queue, (0, start_y, start_x, [(start_y, start_x)]))


visited = {} # dictionary with scores at each (y, x, dir_y, dir_x)



while queue:
    #print(f'{len(queue)} elements in current queue')
    # get state
    score, pos_y, pos_x,memory = heapq.heappop(queue)
    # Try all four directions
    for direction in directions:
        dir_y, dir_x = direction
        # New potential position
        ny, nx = pos_y+dir_y, pos_x+dir_x
        
        # ignore this iteration if seen and is not the end
        if (ny, nx, dir_y, dir_x) in visited:
            continue 
        visited[(ny, nx, dir_y, dir_x)] = score
        
        # ignore this iteration if wall
        if grid[ny, nx]==1:
            continue
        
        # If reached end, save as a possible path
        if grid[ny, nx]==3:
            new_memory = memory.copy()
            new_memory.append((ny, nx))
            new_score=score+1
            print('Found solution!')
            break
        
        # if not, add to queue to continue
        else:
            new_memory = memory.copy()
            new_memory.append((ny,nx))
            new_score = score+1
            heapq.heappush(queue, (new_score, ny, nx, new_memory))
    
print(f'Total steps to solve maze: {new_score}')

'''
Now we have the path, and we can find the cheats
'''

cheats = {}

# For each point along the path
for i, pos in enumerate(new_memory):
    for dir in directions:
        # Look at immediate neighbor
        next_y, next_x = pos[0]+dir[0], pos[1]+dir[1]
        # Look at the element after
        nextnext_y, nextnext_x = pos[0]+2*dir[0], pos[1]+2*dir[1]
        
        #They both need to be inside grid
        if 0<=next_y<H and 0<=next_x<W and 0<=nextnext_y<H and 0<=nextnext_x<W:
        
            # They need to be wall and path
            if grid[next_y, next_x]==1 and (nextnext_y, nextnext_x) in new_memory:
                # The nextnext needs to be AFTER our current pos
                idx_now = new_memory.index((pos[0], pos[1]))
                idx_later = new_memory.index((nextnext_y, nextnext_x))
                if idx_later>idx_now:
                    # This is a valid cheat!!
                    jump = idx_later-idx_now-2
                    #print(f'Valid cheat at {pos} to {(nextnext_y, nextnext_x)} with jump {jump}')
                    #print(f'Initial idx: {idx_now}')
                    #print(f'After idx {idx_later}')
                    cheats[jump] = cheats.get(jump, 0) + 1
        

total = 0
for key in cheats.keys():
    if key>=100:
        total+=cheats[key]
print(f'Sol P1: {total}')
print(f'Runtime {time()-start} seconds')