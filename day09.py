'''
Day 9: Disk defragmentation
'''
import numpy as np
from tqdm import tqdm
from itertools import groupby
from time import time

START = time()

with open('./9.txt', 'r') as f:
    lines = [l.strip('\n') for l in f.readlines()]
data = [int(s) for s in ''.join(lines)]

# Create the real disk with empty spaces
# Empty spaces will be NaN
disk = []
file_id = 0
for pos, n in enumerate(data):
    # If the index is even, we have a file
    if pos%2==0:
        for _ in range(0,n):
            disk.append(file_id)
        file_id+=1

    # If the index in odd, we have space
    else:
        for _ in range(0,n):
            disk.append(-1)
 
print('Disk parse finished') 
#print(disk)
           
# Loop through the disk backwards
# and re-position elements
new_disk_1 = disk.copy()
for pos in range(len(new_disk_1)-1, -1, -1):
    # We encounter empty space
    if new_disk_1[pos]==-1:
        pass
    # We encounter a file
    else:
        # Look for firts available empty position
        newpos = new_disk_1.index(-1)
        # we move if the position is preceding our file
        if newpos<pos:
            file = new_disk_1[pos]
            new_disk_1[newpos]=file
            new_disk_1[pos]=-1

#print('Disk construction finished') 
#print(new_disk_1)
 
# cut disk to valid files:
cut_id = new_disk_1.index(-1)
cut_disk_1 = new_disk_1[0:cut_id]
#print(newdisk)
# Calculate solution value

sol = 0
for pos, file in enumerate(cut_disk_1):
    sol += (pos*file)
print(f'Solution part 1 : {sol}')


'''
For part 2, I need to construct a list of 
spaces and files first, with their lengths 
Do it using itertools.groupby

After having that, I can simply swap the tuples!
However, have to be careful adding smaller empty spaces if
the new file does not fill the gap completely
'''
file_length = [(key, len(list(group))) for key, group in groupby(disk)]
#print(file_length)

# Iterate backwards through list of tuples

# Starting position of search
i = len(file_length)-1

while True:
    file, length = file_length[i]
    #print(f'Considering {(file, length)}')

    # If we come to the back of the list, stop
    if i==0:
        break
    
    # If we encounter empty space, pass and start over
    elif file==-1:
        i-=1
        continue
    
    # We have a file
    else:
        foundplace = False
        # We move forward in the list 
        # looking for the first place where the file fits
        for j in range(0, i):
            file_cand, length_cand = file_length[j]
            #print(f'Candidato {file_cand, length_cand}')
            # We only continue if the candidate is empty file
            if file_cand==-1:
                # It fits:
                if length_cand==length:
                    #print(f'Switched {(file, length)} with fitting {(file_cand, length_cand)}')
                    file_length[i] = (file_cand, length_cand)
                    file_length[j] = (file, length)
                    foundplace=True
                    # I can continue next iteration in i-1
                    #i -=1
                    break
                    
                elif length_cand>length:
                    #print(f'Switched {(file, length)} with bigger {(file_cand, length_cand)}')
                    file_length[i] = (file_cand, length)
                    file_length[j] = (file, length)
                    # might have to change
                    file_length.insert(j+1, (-1, length_cand-length))
                    foundplace=True
                    # Do i need new indexing?
                    #i-=1
                    break
                
                else:
                    pass
                    #print(f'Did not find a fitting place for {(file, length)}')
    if foundplace==False:
        i-=1
        # can also be indented here               
                    
    #print(file_length)
    #print('\n')
    #print(f'Current {i=}')
    

# Calculate new sum
new_disk_2 = []
visual = ''

for file, length in file_length:
    for i in range(length):
        new_disk_2.append(file)
        symbol = str(file) if file!= -1 else '.'
        visual += symbol
#print(new_disk_2)
print(visual)

sol2 = 0
for pos, file in enumerate(new_disk_2):
    if file!=-1:
        sol2 += (pos*file)
print(f'Solution part 2 : {sol2}')

print(f'Total calculation time {(time()-START)/60} minutes')