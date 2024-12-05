from tqdm import tqdm
from functools import cmp_to_key

path = r"./5.txt"
with open(path, "r") as f:
    data =  [line.strip('\n') for line in f.readlines() ] 

# get rules and manuals
rules = []
manuals = []
for line in data:
    if '|' in line:
        left, right = list(map(int, line.split('|')))
        rules.append([left, right])
    elif ',' in line:
        manual = list(map(int, line.split(',')))
        manuals.append(manual)

# define comparing function
def compare(manual, left, right):
    if manual.index(left)<manual.index(right):
        return True
    else: 
        return False    

# for part 2, custom sorting funct
def sort_by_rules(left, right):
    # right order
    if [left, right] in rules:
        return -1
    # wrong order
    elif [right, left] in rules:
        return 1
    else:
        return 0

    
# Go through each manual and use the valid rules
valid = []
invalid = [] # for part 2

for manual in tqdm(manuals):
    # here we save bool for manual
    passed = [] 
    
    for rule in rules:
        left, right = rule
        # If number of rule are not present, ignore
        if left in manual and right in manual:
            passed.append(compare(manual, left, right)) 
        else:
            pass     
    # After comparing all rules, 
    # manual is valid is all rules were passed
    if all(passed):
        valid.append(manual)
    else:
        invalid.append(manual)
        
sol = 0
for manual in valid:
    sol += manual[len(manual)//2]
print(f'Solution part 1: {sol}\n')

sol2 = 0
for manual in invalid:
    newmanual = sorted(manual, key=cmp_to_key(sort_by_rules))
    print(f'Conversion: {manual} -> {newmanual}')
    sol2 += newmanual[len(newmanual)//2]
print(f'Solution part 2: {sol2}\n')
