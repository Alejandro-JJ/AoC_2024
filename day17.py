'''
Day 17: Computer
'''
import numpy as np
import re
from time import time

start= time()
with open('input.txt', 'r') as f:
    data = [line.strip('\n') for line in f.readlines()]
A = int(re.findall(r'\d+', data[0])[0])
B = int(re.findall(r'\d+', data[1])[0])
C = int(re.findall(r'\d+', data[2])[0])
PROG = list(map(int, data[4].split(' ')[1].split(',')))


def combo(input):
    if input in [0,1,2,3]:
        return input
    elif input==4:
        return A
    elif input==5:
        return B
    elif input==6:
        return C
    else:
        print(f'Not valid combo number: {input}')
OUTPUT = ''
pointer = 0
while pointer!=len(PROG):
    op = PROG[pointer]
    input = PROG[pointer+1]
    #print(f'Next: op {op} with input {input}')
    
    if op==0:
        # Division and overwrite A
        num = A
        den = 2**combo(input)
        A= int(np.floor(num/den))
        #print(f'OP_0 Division, assigned value {A=}')
        pointer+=2
        continue
    
    if op==1:
        # Bitwise XOR and overwrite B
        B = int(B^input)
        #print(f'OP_1 XOR, assigned value {B=}')
        pointer+=2
        continue
    
    if op==2:
        # Combo modulo 8 to B
        B = int(combo(input)%8)
        #print(f'OP_2 Combo%8, assigned value {B=}')
        pointer+=2
        continue
    
    if op==3:
        # Jump pointer
        if A==0:
            pointer+=2
        
        else:
            newpointer = input
            pointer = newpointer
            #print(f'OP_3 Jump, set {pointer=}')
        continue
    if op==4:
        # Witwise B and C, to B
        temp = B^C
        B = int(temp)
        #print(f'OP_4 XOR B and C, assigned {B=}')
        pointer+=2
        continue
    
    if op==5:
        # Output combo%8 to string
        out = combo(input)%8
        OUTPUT += (str(int(out))+',')
        #print(f'OP_5, added to output {str(out)},')
        pointer +=2
        continue
    
    if op==6:
        # Division and overwrite B
        num = A
        den = 2**combo(input)
        B = int(np.floor(num/den))
        #print(f'OP_6 Division, assigned value {B=}')
        pointer+=2
        continue
    
    if op==7:
        # Division and overwrite C
        num = A
        den = 2**combo(input)
        C = int(np.floor(num/den))
        #print(f'OP_6 Division, assigned value {C=}')
        pointer+=2
        continue
    
print(f'Done in {time()-start} seconds!')
print(str(OUTPUT)[:-1])