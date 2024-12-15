'''
Day 15: Warehouse robots
'''
import numpy as np
import matplotlib.pyplot as plt
from tools import Text2Array
from tqdm import tqdm
from matplotlib.colors import ListedColormap, BoundaryNorm


# PARSE MAP
with open('input.txt', 'r') as f:
    data = [line.strip('\n') for line in f.readlines()]

dict = {'.':0, '#':10, '@':1, 'O':4}
# empty 0, wall 10, me 1, box 4
mapa = Text2Array(data, dict)

# Custom colormap
cmap1 = ListedColormap(['black', 'lightgreen', 'goldenrod', 'slategray'])
norm1 = BoundaryNorm([-0.1, 0.1, 3.9, 5, 11], ncolors=4)

# PARSE MOVEMENT
with open('mvts.txt', 'r') as f:
    data = [[s for s in line.strip('\n')] for line in f.readlines()]

step_dict = {'<':(0,-1), '>': (0, 1), '^':(-1,0), 'v':(1,0)}

steps = [] # convert to single line of (dy, dx)
for line in data:
    for s in line:
        steps.append(step_dict[s])
print(f'Number of steps: {len(steps)}')
#############################################

def plot_and_save(mapa, t):
    savename = r"C:\Users\Alejandro\Desktop\AoC\AoC_2024\warehouse"+ rf'\frame_{t}.png'
    plt.imshow(mapa, interpolation='nearest', cmap=cmap1, norm=norm1)
    plt.savefig(savename)

pos_robot = np.where(mapa==1)[0][0], np.where(mapa==1)[1][0]

# Loop
for t, step in tqdm(enumerate(steps)):
    #print(f'I am at {pos_robot}')
    robot_y, robot_x = pos_robot
    dy, dx = step
    new_y = pos_robot[0]+dy  
    new_x = pos_robot[1]+dx
    #print(f'I will move dy={dy}, dx={dx}')
    
    # The new position is empty
    if mapa[new_y, new_x] == 0:
        mapa[new_y, new_x] = 1 # put robot
        mapa[robot_y, robot_x] = 0 # empty space behind him
        pos_robot = new_y, new_x
        plot_and_save(mapa, t)
        #print('The new posision is empty, I move\n')
        continue 
    
    # The new position is a wall
    if mapa[new_y, new_x] == 10:
        #print('I ran into a wall!\n')
        plot_and_save(mapa, t)
        continue
    
    # The new position is a box
    if mapa[new_y, new_x] == 4:
        #print('I encounter a box!')
        # I look for the next empty spot in the direction
        #print('Looking for next empty spot...')
        can_move = False
        c = 1
        while True:
            look_y, look_x = new_y+dy*c, new_x+dx*c
            #print(f'I see {mapa[look_y, look_x]}')
            if mapa[look_y, look_x]==10:
                #print('No spot found\n')
                break
            elif mapa[look_y, look_x]==4:
                #print('Box')
                c+=1
            else:
                #print(f'Found spot {look_y}, {look_x} and can move \n')
                can_move=True
                break
        
        if can_move:
            mapa[new_y, new_x] = 1 # put robot
            mapa[robot_y, robot_x] = 0 # empty space behind him
            mapa[look_y, look_x] = 4 # teleport box to the empty space
            pos_robot = new_y, new_x
        plot_and_save(mapa, t)
     
     
print('DONE!')           
plt.imshow(mapa)
plt.show()

# Result
sol = 0
boxes_y, boxes_x = np.where(mapa==4)
for y, x in zip(boxes_y, boxes_x):
    sol+=(100*y+x)
print(f'Solution P1: {sol}')