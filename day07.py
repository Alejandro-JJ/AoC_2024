'''
Day 7 : operations
'''
from itertools import product
from tqdm import tqdm 

# Parse data
path = r"./7.txt"
with open(path, "r") as f:
    data =  [line.strip('\n') for line in f.readlines() ] 
lhs = []
rhs = []
for line in data:
    left = int(line.split(': ')[0])
    right = list(map(int,line.split(': ')[1].split(' ')))
    lhs.append(left)
    rhs.append(right)

def GenerateOperators(n):
    ops = list(product(['*', '+'], repeat=n))
    return ops

def CalculateEquation(nums, ops):
    sol = nums[0]
    for i in range(0,len(ops)):
        if ops[i]=='*':
            sol *= nums[i+1]
        else: # sum
            sol += nums[i+1]
    return sol

def GenerateOperators2(n):
    ops = list(product(['*', '+', '||'], repeat=n))
    return ops

def CalculateEquation2(nums, ops):
    sol = nums[0]
    for i in range(0,len(ops)):
        if ops[i]=='*':
            sol *= nums[i+1]
            
        elif ops[i]=='||': # concatenate
            leftchunk = sol * 10**(len(str(nums[i+1])))
            sol = leftchunk+nums[i+1]
            
        else: # sum
            sol += nums[i+1]
    return sol


# Loop
SOL = 0
for result, nums in tqdm(zip(lhs, rhs)):
    valid = False
    # Generate possible operations vectors
    ops_list = GenerateOperators2(len(nums)-1)
    # Loop through the combinations
    for ops in ops_list:
        candidate = CalculateEquation2(nums, ops)
        if candidate==result:
            #print(f'{result} = {candidate}')
            valid=True
            break
    if valid==True:
        SOL+=result
print(f'Valid solutions: {SOL}')