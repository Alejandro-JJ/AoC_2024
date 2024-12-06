from tools import  Text2Array
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from time import time

path = r"./6.txt"
with open(path, "r") as f:
    data =  [line.strip('\n') for line in f.readlines() ] 
mydict = {'.':0, '#':1, '^':3} # character is 3
mapa = Text2Array(data, mydict)
H, W = np.shape(mapa) # 10, 10, we need -1 

def rot90(dir):
    '''
    Takes the current direction as a tuple
    and returns the new rotated 90 degrees to the right
    '''
    rotdict = {(-1,0): (0,1), (0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0)}
    return rotdict[dir]
    
currpos = (np.where(mapa==3)[0][0], np.where(mapa==3)[1][0])
currdir = (-1,0) # starts upwards
visited = [currpos]

while True:
    # Calculate next potential position
    newpos = (currpos[0]+currdir[0], currpos[1]+currdir[1])
    
    # If we exit the map, break loop
    if not 0<=newpos[0]<H or not 0<=newpos[1]<W:
        break
    
    # If the position is occupied, rotate 90 and restart loop
    elif mapa[newpos[0], newpos[1]]==1:
        currdir = rot90(currdir)
        continue
    
    # If none of the above conditions are fulfilled, we can take a step
    else:
        currpos = newpos
        # save if not visited yet
        if currpos not in visited:
            visited.append(currpos)
            
print(f'Size of the map: {H,W}')
print(f'Number of visited positions: {len(visited)}')

'''
For part 2, I would create a loop where I place an obstacle (1)
and run the simulation again. In this case however, we need to 
check for loops. You can do that saving a state vector (pos, dir)
If you ever come to the same position with the same direction, 
you are stuck in a loop 

OPTIMIZED ROUTINE: only check obstacle positions 
which would interfere with the original path!!

Optimization idea: don't move step by step, but directly 
teleport to the next encountered obstacle in the path!

'''
# Part 2
obstaclepos = list(zip(np.where(mapa==0)[0], np.where(mapa==0)[1]))
print(f'There are {len(obstaclepos)} potential obstacles')
validobstacles = [i for i in obstaclepos if i in visited]
print(f'There are {len(validobstacles)} valid obstacles')

def EvaluateMap(mapa):
    '''
    Takes a map and returns:
        'Loop' if stuck in a loop
        'Open' if the guard escapes
    
    We keep track of an "state" tuple
    which contains (pos,dir)
    If this state has been visited before, is a loop
    '''
    currpos = (np.where(mapa==3)[0][0], np.where(mapa==3)[1][0])
    currdir = (-1,0) # starts upwards
    visited_states = [(currpos, currdir)]

    while True:
        # Calculate next potential position
        newpos = (currpos[0]+currdir[0], currpos[1]+currdir[1])
        
        # If we exit the map, break loop
        if not 0<=newpos[0]<H or not 0<=newpos[1]<W:
            return 'Open'
        
        # if we have been in this state before, break the loop
        elif (newpos, currdir) in visited_states:
            return 'Loop'
        
        # If the position is occupied, rotate 90 and restart loop
        elif mapa[newpos[0], newpos[1]]==1:
            currdir = rot90(currdir)
            continue
        
        # If none of the above conditions are fulfilled, we can take a step
        else:
            currpos = newpos
            #print(f'Moved to: {currpos}')
            # and save this state
            visited_states.append((currpos, currdir))

start = time()
LOOPS = 0
for obs in tqdm(validobstacles):
    #print(f'Testing obstacle in pos {obs[0]}, {obs[1]}')
    newmapa = mapa.copy()
    newmapa[obs[0],obs[1]] = 1
    #print(EvaluateMap(newmapa))
    if EvaluateMap(newmapa)=='Loop':
        LOOPS+=1
print(f'Loops found: {LOOPS}')
print(f'Time required: {(time()-start)/60} minutes')
