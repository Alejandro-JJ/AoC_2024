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
