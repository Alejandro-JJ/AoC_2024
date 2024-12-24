'''
Day 24: Logical wires
'''
import re
from time import time
start = time()
with open('input.txt','r') as f:
    data = [line.strip('\n') for line in  f.readlines()]
d1 = data[:data.index('')]
d2 = data[data.index('')+1:]

# Known elements:
known = {}
for d in d1:
    name, value = d.split(': ')[0], int(d.split(': ')[1])
    known[name]=value

# Operations to do:
ops = []
for d in d2:
    a, b, c, d = d.replace(' -> ', ' ').split(' ')
    ops.append([a,b,c,d])

# Function to perform operation with first 3 elements
def calculate(left, op, right):
    if op=='AND': return left and right
    elif op=='OR': return left or right
    elif op=='XOR': return left^right
    else: raise Exception("wrong operation") 
    
# Loop while we have operations to do
i = 0
while len(ops)>0:
    #print(f'LENGTH : {len(ops)}')
    leftkey, op, rightkey, end = ops[i]
    
    # If both elements known, operate
    if leftkey in known.keys() and rightkey in known.keys():
        left = known[leftkey]
        right = known[rightkey]
        result = calculate(left, op, right)
        # And add it to known
        known[end] = result
        #print(f'Operation {leftkey, op, rightkey} -> {end} was done.')
        #print(f'Added {end, result} to dictionary')
        # Pop the current element from the list
        del ops[i]
        # And restart the seach from beginning
        i = 0
    
    # If both elements are not  in the known 
    else:
        # We continue to the next
        i += 1
#print(known)


# Get elements which start with z and sort them
Nzs = len([key for key in known.keys() if key.startswith('z')])

number = ''

for n in range(Nzs-1, -1, -1):
    key = 'z'+str(n).zfill(len(str(Nzs)))
    number+=str(known[key])
print(number)
print(int(number, 2))     
print(f'Runtime: {time()-start} seconds')       
    