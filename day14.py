'''
Day 14: Robots in the bathroom
'''
import numpy as np
import matplotlib.pyplot as plt
import re

pattern = r'-?\d+'
with open('input.txt', 'r') as f:
    robots = [list(map(int, re.findall(pattern,line))) for line in f.readlines()]
#print(robots)
# Map shape
H, W = 103, 101

def move(x, y, vx, vy):
    # Moves robot one step
    # Returns new x, y
    new_x = x+vx
    new_y = y+vy
    # Wrap  : this might be problem if some robot makes huge steps
    if new_x>=W:
        new_x = new_x%W
    if new_x<0:
        new_x = new_x + W 
    if new_y>=H:
        new_y = new_y%H
    if new_y<0: # -2
        new_y = new_y + H 
    return new_x, new_y

t_max = 20000
trajectories = []
for robot in robots:
    x, y, vx, vy = robot
    robot_traj = [(x,y)]
    
    for time in range(t_max):
        x,y = move(x,y,vx,vy)
        robot_traj.append((x,y))
    trajectories.append(robot_traj)
    #print(f'{vx=}, {vy=}')
    #print(robot_traj)
#print(trajectories)
        

# Representation: only last stage
fig, ax = plt.subplots(1,1, figsize=(5,5))

for plot_time in range(0, t_max):
    mapa = np.zeros((H, W))
    for traj in trajectories:
        last_x, last_y = traj[plot_time]
        mapa[last_y, last_x] = mapa[last_y, last_x]+1
    ax.cla()
    ax.imshow(mapa) 
    ax.set_title(f'Timepoint {plot_time}')
    plt.draw()
    savename = r"C:\Users\Alejandro\Desktop\AoC\AoC_2024\EasterEgg"+ rf'\frame_{plot_time}.png'
    plt.savefig(savename)
    plt.ioff()

# Calculate quadrants
#Q1 = mapa[0:H//2, 0:W//2]
#Q2 = mapa[0:H//2, W//2+1:]
#Q3 = mapa[H//2+1:, 0:W//2]
#Q4 = mapa[H//2+1:, W//2+1:]

#print(f'Solution P1: {int(np.sum(Q1)*np.sum(Q2)*np.sum(Q3)*np.sum(Q4))}')