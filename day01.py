path = r"C:\Users\Alejandro\Desktop\AoC\AoC_2024\input_01.txt"
with open(path, "r") as f:
    data = [l.split() for l in f.readlines()]
left = sorted([int(x[0]) for x in data])
right = sorted([int(x[1]) for x in data])

dist = 0
for n in range(0, len(left)):
    dist+=abs(left[n]-right[n])
print(f'distance: {dist}')

# Part 2, without sort
left = [int(x[0]) for x in data]
right = [int(x[1]) for x in data]
sim = 0
for n in left:
    reps = sum([s==n for s in right])
    sim += n*reps
print(f'similarity : {sim}')

