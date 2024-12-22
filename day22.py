'''
Day 22: 
'''
import numpy as np
import re
with open('input.txt', 'r') as f:
    seeds = [int(line.strip('\n')) for line in f.readlines()]

def mix(a, b):
    return a^b

def prune(a):
    return a%16777216

def next(sec):
    '''
       A: Calculate the result of multiplying the secret number by 64. 
        Then, mix this result into the secret number. Finally, prune the secret number.
        
        B: Calculate the result of dividing the secret number by 32. 
        Round the result down to the nearest integer. Then, mix this result into the secret number. 
        Finally, prune the secret number.
        
        C: Calculate the result of multiplying the secret number by 2048. 
        Then, mix this result into the secret number. Finally, prune the secret number.
    '''
    A = prune(mix(sec, sec*64))
    B = prune(mix(A, int(A/32)))
    C = prune(mix(B, B*2048))
    return C

result = 0
for seed in seeds:
    sec = seed
    for i in range(2000):
        sec = next(sec)
    result += sec
print(f'\nSolution : {result}')
