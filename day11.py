'''
Day 11: Stones
'''
import numpy as np
from tqdm import tqdm
from time import time
start = time()

with open('11.txt', 'r') as f:
    initial = [int(s) for s in f.readline().strip('\n').split()]
#print(initial)

class Stone():
    # Lets include the possibility of removing all instances to save memory
    instances = []
    def __init__(self, number):
        self.number = number
        self.__class__.instances.append(self) # save ref
    
    def blink(self):
        # blinks and returns new stones
        if self.number==0:
            return [Stone(1)]
        elif len(str(self.number))%2==0:
            num_left =  int(str(self.number)[0:len(str(self.number))//2]) 
            num_right = int(str(self.number)[len(str(self.number))//2:])
            return [Stone(num_left), Stone(num_right)]
        else:
            return [Stone(self.number*2024)]

times = 75
current = initial

for t in tqdm(range(times)):
    #print(f'Blinking {t+1}th time...')
    new_stones= []
    for s in current:
        stone = Stone(s)
        daughters = stone.blink()
        for d in daughters:
            new_stones.append(d.number)
    print(f'After {t+1} blinks we have: {len(new_stones)} stones')

    current = new_stones
    for i,v in enumerate(Stone.instances):
        del v

print(f'Blinking took you {time(-start)} seconds')
print(f'\nFound {len(current)} stones after blinking {times} times')