import matplotlib.pyplot as plt
from tools import Text2Array
path = 'C:\\Users\\Alejandro\\Desktop\\AoC\\AoC_2024\\input_00.txt'
with open(path, 'r') as f:
    cosa = [[s for s in l.strip('\n')] for l in f.readlines()]
print(cosa)

# Custom dict
my_dic = {'.':0, '#':1}
from tools import  Text2Array
import matplotlib.pyplot as plt
A = Text2Array(cosa, my_dic)
print(A)
plt.imshow(A)
plt.show()