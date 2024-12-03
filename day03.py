
'''
Day 3: Regular expressions
'''
import re
path = r"C:\Users\Alejandro\Desktop\AoC\AoC_2024\input_03.txt"
with open(path, "r") as f:
    data =  [l for l in f.readlines()] # is a single line

pattern1 = r'mul\(\d+,\d+\)'
sol = 0
for line in data:
    matches = re.findall(pattern1,line)
    for m in matches:
        l,r = m.strip('mul(').strip(')').split(',')
        sol+=int(l)*int(r)

print(f'Solution: {sol}')

# Second part. Approach is to delete data between don't() and do(),
# and then process the string

# DEBUGGED THIS FOR WAY TOO LONG: a don't() can cancel the END of the string
todel = r'don\'t\(\)(.*?)(do\(\)|$)' 

data2 = ''
for l in data:
    data2+=l.strip('\n')
#print(data2)
data3 = re.sub(todel, '', data2)
sol2 = 0
matches = re.findall(pattern1,data3)
for m in matches:
    l,r = m.strip('mul(').strip(')').split(',')
    sol2+=int(l)*int(r)
print(sol2)


