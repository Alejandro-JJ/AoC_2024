'''
Day 5:
'''
import re
import numpy as np
import matplotlib.pyplot as plt

path = r"C:\Users\Alejandro\Desktop\AoC\AoC_2024\input_05.txt"
with open(path, "r") as f:
    data =  [[s for s in line.strip('\n')] for line in f.readlines() ]