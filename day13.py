'''
Day 13: Claw machine
'''
import numpy as np
import re

with open('input.txt', 'r') as f:
    data = [p.strip('\n') for p in f.readlines() if len(p)>1] # avoid empty lines

patX = r'X\+\d+' # have to be stripped later
patY = r'Y\+\d+'
patsolX = r'X\=\d+'
patsolY = r'Y\=\d+'

problems = []
for i in range(0,len(data), 3):
    # Button A
    xa = int(re.findall(patX, data[i])[0].strip('X+'))
    ya = int(re.findall(patY, data[i])[0].strip('Y+'))
    # Button B
    xb = int(re.findall(patX, data[i+1])[0].strip('X+'))
    yb = int(re.findall(patY, data[i+1])[0].strip('Y+'))
    # Prize
    xp = 10000000000000+int(re.findall(patsolX, data[i+2])[0].strip('X='))
    yp = 10000000000000+int(re.findall(patsolY, data[i+2])[0].strip('Y='))
    problems.append([xa, ya, xb, yb, xp,yp])

def solve(xa, ya, xb, yb, xp, yp):
    # Solves the system of two equations
    determinant = (xa*yb-ya*xb)
    if determinant!=0:
        na = (xp*yb - yp*xb)/determinant
        nb = (xa*yp - ya*xp)/determinant
        # Even if solvable, we need int amount of moves
        if int(na)==na and int(nb)==nb:
            return na, nb
        else:
            return None
    else:
        return None

sols = []
p1 = 0
for problem in problems:
    xa, ya, xb, yb, xp,yp = problem
    sol = solve(xa,ya,xb,yb,xp,yp)
    sols.append(sol)
    if sol!=None:
        p1 += (3*sol[0]+sol[1])
    
print(f'Solution P1: {int(p1)}')