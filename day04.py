'''
Day 3: Sopa de letras
'''
import re
import numpy as np
import matplotlib.pyplot as plt

path = r"C:\Users\Alejandro\Desktop\AoC\AoC_2024\input_04.txt"
with open(path, "r") as f:
    soup =  [[s for s in line.strip('\n')] for line in f.readlines() ] # is a single line
width, height = len(soup[0]), len(soup)

# Go through every element and all 8 directions
# Save indices which are valid for later visualization
words = 0
indices = []
for i in range(0, height): #vertical
    for j in range(0, width): #horizontal
        # Go through all 8 directions
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                id_1 = (i, j)
                id_2 = (i+dy, j+dx)
                id_3 = (i+dy*2, j+dx*2)
                id_4 = (i+dy*3, j+dx*3)
                # Check that last element is inside soup
                if 0<=id_4[0]<height and 0<=id_4[1]<width:
                    # Get letters:
                    l1 = soup[id_1[0]][id_1[1]]
                    l2 = soup[id_2[0]][id_2[1]]
                    l3 = soup[id_3[0]][id_3[1]]
                    l4 = soup[id_4[0]][id_4[1]]
                    if (l1, l2, l3, l4)==('X', 'M', 'A', 'S'):
                        words+=1
                        indices.append([id_1,id_2,id_3,id_4])
print(f'Part 1: Found {words} solutions')

# Part 2 is even simpler
patterns = ['MMSS', 'SSMM', 'SMSM', 'MSMS']
words2 = 0
# We avoid edge elements
for i in range(1, height-1):
    for j in range(1, width-1):
        # We only evaluate if central char is "A"
        if soup[i][j]=='A':
            # take all surrounding four
            a,b,c,d = soup[i-1][j-1], soup[i-1][j+1], soup[i+1][j-1], soup[i+1][j+1]
            word = a+b+c+d
            if word in patterns:
                words2+=1

print(f'Part 2: Found {words2} solutions')
