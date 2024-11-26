import numpy as np
import matplotlib.pyplot as plt

def Text2Array(lista, dic):
    '''
    Takes an nested list of symbols and creates
    an array, using the substitution dict provided
    '''
    rows, cols = len(lista), len(lista[0])
    A = np.zeros((rows, cols))
    for r in range(0, rows):
        for c in range(0, cols):
            # detect non-considered symbols
            if lista[r][c] not in dic.keys():
                print('Symbol not in dict')
            else:
                A[r,c] = dic[lista[r][c]]
    return A


