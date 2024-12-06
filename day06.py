from tools import  Text2Array
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

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
'''


""" # Video generation
savepath = "C:\\Users\\Alejandro\\Desktop\\AoC\\day6video\\"
fig, ax = plt.subplots(1,1,figsize=(5,5))
ax.imshow(mapa, cmap='Set3')
ax.set_axis_off()
plt.tight_layout()
plt.savefig(savepath+'f_00000.png')

f = 1
for v in tqdm(visited):
    # Overwrite map
    mapa[v[0], v[1]]=3
    ax.cla()
    ax.imshow(mapa, cmap='Set3')
    ax.set_axis_off()
    plt.tight_layout()
    plt.savefig(savepath+'f_' + str(f).zfill(5) + '.png')
    f += 1
         """
